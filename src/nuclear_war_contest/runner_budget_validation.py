"""Derived and cumulative channel-budget validation."""

from __future__ import annotations

import math
from typing import Any

from nuclear_war_concordia.channel_metrics import build_channel_metrics
from nuclear_war_env.integer_validation import is_strict_int


def validate_channel_metrics(result: dict[str, Any]) -> None:
    metrics = derived_metrics(result)
    if metrics is None:
        raise ValueError("Validated artifacts are required for channel metrics")
    summary = result.get("summary")
    stored = summary.get("channel_metrics") if isinstance(summary, dict) else None
    validate_stored_metrics(stored, metrics)


def validate_budget_metrics(
    result: dict[str, Any], initial_metrics: dict[str, Any] | None = None
) -> None:
    summary = result.get("summary")
    budget = summary.get("budget_metrics") if isinstance(summary, dict) else None
    if not isinstance(budget, dict):
        raise ValueError("Authoritative budget metrics are missing")
    derived = derived_metrics(result)
    if derived is None:
        raise ValueError("Validated artifacts are required for budget metrics")
    for channel in ("c2", "press"):
        _validate_channel_budget(budget, derived, initial_metrics, channel)
    _validate_costs(budget)


def derived_metrics(result: dict[str, Any]) -> dict[str, Any] | None:
    trace_artifact = result.get("trace_artifact")
    c2_artifact = result.get("c2_artifact")
    if not isinstance(trace_artifact, dict) or not isinstance(c2_artifact, dict):
        return None
    traces = trace_artifact.get("traces")
    deliberations = c2_artifact.get("deliberations")
    press_artifact = result.get("press_artifact")
    press = (
        press_artifact.get("messages", []) if isinstance(press_artifact, dict) else []
    )
    if not isinstance(traces, list) or not isinstance(deliberations, list):
        return None
    return build_channel_metrics(traces, c2_artifact, press)


def _validate_channel_budget(
    budget: dict[str, Any],
    derived: dict[str, Any],
    initial: dict[str, Any] | None,
    channel: str,
) -> None:
    observed = budget.get(channel)
    expected = derived[channel]
    if not isinstance(observed, dict):
        raise ValueError(f"Budget metrics are missing {channel}")
    logical_calls = _count(observed, "call_count", channel)
    attempts = _count(observed, "provider_attempt_count", channel)
    previous_calls = _prior_count(initial, channel, "call_count")
    previous_attempts = _prior_count(initial, channel, "provider_attempt_count")
    previous_retries = _prior_count(initial, channel, "transport_retry_count")
    current_retries = expected.get("recoverable_provider_retry_count", 0)
    current_calls = expected["call_count"] - current_retries
    if not is_strict_int(current_retries) or current_calls < 0:
        raise ValueError(f"Budget {channel} derived calls are invalid")
    if logical_calls != previous_calls + current_calls:
        raise ValueError(f"Budget {channel} logical calls are invalid")
    if attempts != previous_attempts + expected["call_count"]:
        raise ValueError(f"Budget {channel} provider attempts are invalid")
    retries = observed.get("transport_retry_count")
    if retries != previous_retries + current_retries:
        raise ValueError(f"Budget {channel} transport retries are invalid")
    if logical_calls > attempts:
        raise ValueError(f"Budget {channel} logical calls exceed attempts")


def _validate_costs(budget: dict[str, Any]) -> None:
    for field in (
        "reserved_cost_usd",
        "actual_cost_usd",
        "study_reserved_cost_usd",
        "study_actual_cost_usd",
    ):
        value = budget.get(field)
        if (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or not math.isfinite(float(value))
            or value < 0
        ):
            raise ValueError(f"Budget metric {field} is invalid")
    if budget["study_reserved_cost_usd"] < budget["reserved_cost_usd"]:
        raise ValueError("Study reserved cost is below the attempt cost")
    if budget["study_actual_cost_usd"] < budget["actual_cost_usd"]:
        raise ValueError("Study actual cost is below the attempt cost")


def _count(values: dict[str, Any], field: str, channel: str) -> int:
    value = values.get(field)
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"Budget {channel} {field} is invalid")
    return value


def _prior_count(metrics: dict[str, Any] | None, channel: str, field: str) -> int:
    if metrics is None:
        return 0
    values = metrics.get(channel)
    if not isinstance(values, dict):
        raise ValueError(f"Prior budget metrics are missing {channel}")
    value = values.get(field)
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"Prior budget {channel} {field} is invalid")
    return value


def validate_stored_metrics(stored: Any, derived: dict[str, Any]) -> None:
    if not isinstance(stored, dict):
        raise ValueError("Stored channel metrics are missing")
    if stored != derived:
        raise ValueError("Stored channel metrics do not match validated traces")


__all__ = [
    "derived_metrics",
    "validate_budget_metrics",
    "validate_channel_metrics",
    "validate_stored_metrics",
]
