"""DATE event and binding rejection tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from nuclear_war_contest.date_world import (
    DateProfile,
    DateRun,
    TransitionResult,
    admit_transition,
    initialize_run,
    instantiate_patch,
    load_profile,
)

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)


def _event(
    template_id: str,
    hour: int,
    patch_id: str | None = None,
    affected_id: str = "HIM_RECAPTURE_GROUP",
) -> dict[str, Any]:
    return {
        "template_id": template_id,
        "event_kind": "tracer_fixture",
        "episode_hour": hour,
        "causal_parent_ids": ["OBS_WX_RIDGE_FORECAST_01"],
        "source": "tracer_fixture",
        "affected_entity_ids": [affected_id],
        "audience_ids": ["US_ACTIVE_SEATS"],
        "evidence_ids": ["SYNTHETIC_AUTHORING_DEFAULT"],
        "assumptions": ["bounded no-model tracer fixture"],
        "uncertainty": {"confidence": "confirmed"},
        "content": "A bounded tracer fixture occurs.",
        "patch_template_id": patch_id,
    }


def _readiness_patch(event_id: str, value: str) -> dict[str, Any]:
    return {
        "template_id": f"PATCH_{event_id}",
        "effective_hour": 5,
        "causal_parent_ids": [event_id],
        "operations": [
            {
                "operation": "set_force_package_readiness",
                "force_package_id": "HIM_RECAPTURE_GROUP",
                "expected": "prepared",
                "value": value,
            }
        ],
    }


def _forecast(profile: DateProfile, run_id: str = "event-rejection-run") -> DateRun:
    return admit_transition(
        profile,
        initialize_run(profile, run_id),
        profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
    ).run


def _assert_rejected(
    result: TransitionResult, prior: DateRun, reason_code: str
) -> None:
    assert result.receipt.accepted is False
    assert result.receipt.reason_codes == (reason_code,)
    assert result.run.current_core() == prior.current_core()
    assert result.run.ledger() == prior.ledger()


@pytest.mark.parametrize(
    ("case", "reason_code"),
    [
        ("duplicate", "duplicate_id"),
        ("retroactive", "retroactive_time"),
        ("unknown_actor", "unknown_reference"),
        ("causal", "causal_mismatch"),
        ("authored_mismatch", "template_mismatch"),
        ("partial_patch", "partial_patch"),
    ],
)
def test_event_and_template_failures_are_retained(case: str, reason_code: str) -> None:
    profile = load_profile(PROFILE_PATH)
    prior = _forecast(profile)
    patch = None
    if case == "duplicate":
        event = profile.event_template("OBS_WX_RIDGE_FORECAST_01")
    elif case == "retroactive":
        event = _event("FIXTURE_RETROACTIVE", 0)
    elif case == "unknown_actor":
        event = _event("FIXTURE_UNKNOWN_ACTOR", 2, affected_id="ACTOR_UNEARNED")
    elif case == "causal":
        prior = initialize_run(profile, "causal-run")
        event = profile.event_template("WX_RIDGE_FRONT_01")
        patch = instantiate_patch(
            prior, profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01")
        )
    else:
        event = profile.event_template("WX_RIDGE_FRONT_01")
        patch_template = profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01")
        if case == "authored_mismatch":
            event["content"] = "Altered authored content."
        else:
            patch_template["operations"] = patch_template["operations"][:1]
        patch = instantiate_patch(prior, patch_template)

    _assert_rejected(admit_transition(profile, prior, event, patch), prior, reason_code)


def test_patch_bound_to_an_older_core_is_stale() -> None:
    profile = load_profile(PROFILE_PATH)
    fork = _forecast(profile, "stale-run")
    old_event = _event("FIXTURE_OLD_BINDING", 5, "PATCH_FIXTURE_OLD_BINDING")
    old_template = _readiness_patch("FIXTURE_OLD_BINDING", "ready")
    old_patch = instantiate_patch(fork, old_template)
    advance_event = _event("FIXTURE_ADVANCE", 5, "PATCH_FIXTURE_ADVANCE")
    advance_template = _readiness_patch("FIXTURE_ADVANCE", "delayed")
    advanced = admit_transition(
        profile,
        fork,
        advance_event,
        instantiate_patch(fork, advance_template),
    ).run

    _assert_rejected(
        admit_transition(profile, advanced, old_event, old_patch),
        advanced,
        "stale_core",
    )
