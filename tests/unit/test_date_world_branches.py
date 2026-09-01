"""DATE tracer branch behavior tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world import (
    DateProfile,
    DateRun,
    admit_transition,
    initialize_run,
    instantiate_patch,
    load_profile,
    project_outcomes,
)

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)


def _readiness_templates(
    suffix: str, expected: str, value: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    event_id = f"FIXTURE_HIM_READINESS_{suffix}"
    patch_id = f"PATCH_FIXTURE_HIM_READINESS_{suffix}"
    event = {
        "template_id": event_id,
        "event_kind": "tracer_fixture",
        "episode_hour": 5,
        "causal_parent_ids": ["OBS_WX_RIDGE_FORECAST_01"],
        "source": "tracer_fixture",
        "affected_entity_ids": ["HIM_RECAPTURE_GROUP"],
        "audience_ids": ["US_ACTIVE_SEATS"],
        "evidence_ids": ["SYNTHETIC_AUTHORING_DEFAULT"],
        "assumptions": ["bounded no-model tracer fixture"],
        "uncertainty": {"confidence": "confirmed"},
        "content": f"The recapture group is {value}.",
        "patch_template_id": patch_id,
    }
    patch = {
        "template_id": patch_id,
        "effective_hour": 5,
        "causal_parent_ids": [event_id],
        "operations": [
            {
                "operation": "set_force_package_readiness",
                "force_package_id": "HIM_RECAPTURE_GROUP",
                "expected": expected,
                "value": value,
            }
        ],
    }
    return event, patch


def _admit_readiness_branch(profile: DateProfile, fork: DateRun, value: str) -> DateRun:
    event, patch_template = _readiness_templates(value.upper(), "prepared", value)
    patch = instantiate_patch(fork, patch_template)
    return admit_transition(profile, fork, event, patch).run


def test_matched_forks_retain_branch_state_through_same_weather_patch() -> None:
    profile = load_profile(PROFILE_PATH)
    fork = admit_transition(
        profile,
        initialize_run(profile, "matched-run"),
        profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
    ).run
    ready = _admit_readiness_branch(profile, fork, "ready")
    delayed = _admit_readiness_branch(profile, fork, "delayed")

    ready_patch = instantiate_patch(
        ready, profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01")
    )
    delayed_patch = instantiate_patch(
        delayed, profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01")
    )
    ready_final = admit_transition(
        profile,
        ready,
        profile.event_template("WX_RIDGE_FRONT_01"),
        ready_patch,
    ).run
    delayed_final = admit_transition(
        profile,
        delayed,
        profile.event_template("WX_RIDGE_FRONT_01"),
        delayed_patch,
    ).run

    assert ready_patch.template_hash == delayed_patch.template_hash
    assert ready_patch.patch_instance_id != delayed_patch.patch_instance_id
    assert ready_final.current_core()["core_version"] == 2
    assert delayed_final.current_core()["core_version"] == 2
    assert project_outcomes(ready_final.current_core())["us_observation_state"] == (
        "intermittent"
    )
    assert project_outcomes(delayed_final.current_core())["us_observation_state"] == (
        "intermittent"
    )
    assert ready_final.current_core()["force_packages"][2]["readiness"] == "ready"
    assert delayed_final.current_core()["force_packages"][2]["readiness"] == ("delayed")
    assert fork.current_core()["force_packages"][2]["readiness"] == "prepared"
