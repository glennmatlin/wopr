"""Tests for frozen per-game channel budgets."""

from __future__ import annotations

import threading
import time
from concurrent.futures import ThreadPoolExecutor

import pytest

from nuclear_war_concordia import call_budget_cost
from nuclear_war_concordia.call_budget import (
    ChannelCallBudget,
    ChannelRequestBudgetExceeded,
)
from nuclear_war_contest.admissibility import classify_failure
from nuclear_war_contest.failure_receipt_validation import validate_failure_receipt
from nuclear_war_contest.manifest_types import StudyRequestBudget
from nuclear_war_contest.runner_budget import (
    ChannelCapExceeded,
    enforce_channel_caps,
)
from nuclear_war_contest.runner_cost import initial_cost_state


def _result(c2_calls: int, press_calls: int) -> dict[str, object]:
    return {
        "channel_metrics": {
            "c2": {"call_count": c2_calls},
            "press": {"call_count": press_calls},
        }
    }


def test_channel_caps_accept_boundary_counts() -> None:
    budget = StudyRequestBudget(2048, 160)

    enforce_channel_caps(_result(2048, 160), budget)


@pytest.mark.parametrize(
    ("c2_calls", "press_calls", "channel"),
    [(2049, 0, "c2"), (0, 161, "press")],
)
def test_channel_caps_fail_closed(
    c2_calls: int, press_calls: int, channel: str
) -> None:
    with pytest.raises(ChannelCapExceeded, match=f"{channel} channel cap exceeded"):
        enforce_channel_caps(
            _result(c2_calls, press_calls), StudyRequestBudget(2048, 160)
        )


def test_channel_caps_require_metrics() -> None:
    with pytest.raises(ValueError, match="Channel metrics"):
        enforce_channel_caps({}, StudyRequestBudget(2048, 160))


def test_channel_caps_reject_boolean_counts() -> None:
    with pytest.raises(ValueError, match="call_count"):
        enforce_channel_caps(
            _result(True, 0),
            StudyRequestBudget(2048, 160),  # type: ignore[arg-type]
        )


def test_channel_cap_failure_is_tier_c() -> None:
    try:
        enforce_channel_caps(_result(2049, 0), StudyRequestBudget(2048, 160))
    except ChannelCapExceeded as error:
        failure = classify_failure(error)
    else:
        raise AssertionError("expected channel cap failure")

    assert failure["tier"] == "C"
    assert failure["reasons"] == ["channel_cap_exceeded"]


def test_failure_receipt_surfaces_partial_transport_retries() -> None:
    error = ChannelRequestBudgetExceeded("c2", 3, 2, "provider-attempts")
    error.partial_metrics = {
        "c2": {
            "call_count": 1,
            "provider_attempt_count": 3,
            "transport_retry_count": 2,
        },
        "press": {
            "call_count": 0,
            "provider_attempt_count": 0,
            "transport_retry_count": 0,
        },
    }

    failure = classify_failure(error)

    assert failure["transport_retry_count"] == 2

    failure["transport_retry_count"] = 1
    with pytest.raises(ValueError, match="transport retries"):
        validate_failure_receipt(failure)


def test_failure_receipt_marks_a_call_blocked_before_provider_dispatch() -> None:
    error = ChannelRequestBudgetExceeded("c2", 1, 0, "provider-attempts")
    error.partial_metrics = {
        "c2": {
            "call_count": 1,
            "provider_attempt_count": 0,
            "transport_retry_count": 0,
        },
        "press": {
            "call_count": 0,
            "provider_attempt_count": 0,
            "transport_retry_count": 0,
        },
    }

    failure = classify_failure(error)
    assert failure["blocked_before_dispatch"] is True
    validate_failure_receipt(failure)
    failure.pop("blocked_before_dispatch")
    with pytest.raises(ValueError, match="attempts"):
        validate_failure_receipt(failure)


def test_failure_receipt_rejects_two_blocked_channels() -> None:
    error = ChannelRequestBudgetExceeded("c2", 1, 0, "provider-attempts")
    error.partial_metrics = {
        "c2": {
            "call_count": 1,
            "provider_attempt_count": 0,
            "transport_retry_count": 0,
        },
        "press": {
            "call_count": 1,
            "provider_attempt_count": 0,
            "transport_retry_count": 0,
        },
    }

    with pytest.raises(ValueError, match="blocked-before-dispatch"):
        validate_failure_receipt(classify_failure(error))


def test_failure_receipt_rejects_invalid_costs() -> None:
    error = ChannelRequestBudgetExceeded("c2", 1, 0, "provider-attempts")
    error.partial_metrics = {
        "c2": {
            "call_count": 1,
            "provider_attempt_count": 0,
            "transport_retry_count": 0,
        },
        "press": {
            "call_count": 0,
            "provider_attempt_count": 0,
            "transport_retry_count": 0,
        },
        "actual_cost_usd": -0.01,
    }

    with pytest.raises(ValueError, match="actual_cost_usd"):
        validate_failure_receipt(classify_failure(error))


def test_request_counter_rejects_before_dispatch() -> None:
    budget = ChannelCallBudget(1, 1)
    guard = budget.guard("c2")
    guard()

    with pytest.raises(ChannelRequestBudgetExceeded):
        guard()

    assert budget.c2_calls == 1


def test_study_cost_cap_is_shared_across_attempt_budgets() -> None:
    state: dict[str, float] = {}
    first = ChannelCallBudget(
        1,
        0,
        max_cost_usd=1.0,
        max_cost_per_request_usd=0.6,
        shared_cost_state=state,
    )
    first.active_channel = "c2"
    first.reserve_transport("c2")

    second = ChannelCallBudget(
        1,
        0,
        max_cost_usd=1.0,
        max_cost_per_request_usd=0.6,
        shared_cost_state=state,
    )
    second.active_channel = "c2"
    with pytest.raises(ChannelRequestBudgetExceeded, match="cost cap exceeded"):
        second.reserve_transport("c2")

    assert state["reserved_cost_usd"] == pytest.approx(0.6)


@pytest.mark.parametrize("invalid_cost", [-0.1, float("nan"), float("inf")])
def test_actual_cost_rejects_invalid_provider_values_before_mutation(
    invalid_cost: float,
) -> None:
    state: dict[str, float] = {}
    budget = ChannelCallBudget(1, 0, shared_cost_state=state)

    with pytest.raises(ValueError, match="actual cost"):
        budget.record_actual_cost(invalid_cost)

    assert budget.actual_cost_usd == 0.0
    assert state == {}


def test_initial_cost_state_uses_latest_study_totals() -> None:
    records = {
        "a": {
            "budget_metrics": {
                "study_reserved_cost_usd": 0.6,
                "study_actual_cost_usd": 0.4,
            }
        },
        "b": {
            "budget_metrics": {
                "study_reserved_cost_usd": 1.2,
                "study_actual_cost_usd": 0.8,
            }
        },
    }

    assert initial_cost_state(records) == {
        "reserved_cost_usd": pytest.approx(1.2),
        "actual_cost_usd": pytest.approx(0.8),
    }


@pytest.mark.parametrize("invalid_cost", [float("nan"), float("inf")])
def test_initial_cost_state_ignores_nonfinite_totals(invalid_cost: float) -> None:
    records = {
        "bad": {
            "budget_metrics": {
                "study_reserved_cost_usd": invalid_cost,
                "study_actual_cost_usd": invalid_cost,
            }
        },
        "good": {
            "budget_metrics": {
                "study_reserved_cost_usd": 0.4,
                "study_actual_cost_usd": 0.2,
            }
        },
    }

    assert initial_cost_state(records) == {
        "reserved_cost_usd": pytest.approx(0.4),
        "actual_cost_usd": pytest.approx(0.2),
    }


def test_observed_cost_cap_is_shared_and_preserves_partial_metrics() -> None:
    state: dict[str, float] = {}
    first = ChannelCallBudget(1, 0, max_cost_usd=1.0, shared_cost_state=state)
    first.active_channel = "c2"
    first.record_actual_cost(0.8)
    second = ChannelCallBudget(1, 0, max_cost_usd=1.0, shared_cost_state=state)
    second.active_channel = "c2"

    with pytest.raises(
        ChannelRequestBudgetExceeded, match="cost cap exceeded"
    ) as caught:
        second.record_actual_cost(0.3)

    assert caught.value.partial_metrics is not None
    assert state["actual_cost_usd"] == pytest.approx(1.1)


def test_shared_actual_cost_is_thread_safe(monkeypatch: pytest.MonkeyPatch) -> None:
    state: dict[str, float] = {}
    ready = threading.Barrier(8)
    original_study_cost = call_budget_cost.study_cost

    def delayed_study_cost(budget: object, field: str) -> float:
        value = original_study_cost(budget, field)
        time.sleep(0.002)
        return value

    monkeypatch.setattr(call_budget_cost, "study_cost", delayed_study_cost)

    def record_cost(_: int) -> None:
        budget = ChannelCallBudget(1, 0, shared_cost_state=state)
        budget.active_channel = "c2"
        ready.wait(timeout=5)
        budget.record_actual_cost(0.01)

    with ThreadPoolExecutor(max_workers=8) as executor:
        list(executor.map(record_cost, range(8)))

    assert state["actual_cost_usd"] == pytest.approx(0.08)
