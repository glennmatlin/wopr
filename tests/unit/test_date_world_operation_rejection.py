"""Atomic DATE operation-rejection tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from nuclear_war_contest.date_world import (
    admit_transition,
    initialize_run,
    instantiate_patch,
    load_profile,
)

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)


def _fixture(operation: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    event = {
        "template_id": "FIXTURE_REJECTION_EVENT",
        "event_kind": "tracer_fixture",
        "episode_hour": 5,
        "causal_parent_ids": ["OBS_WX_RIDGE_FORECAST_01"],
        "source": "tracer_fixture",
        "affected_entity_ids": ["HIM_RECAPTURE_GROUP"],
        "audience_ids": ["US_ACTIVE_SEATS"],
        "evidence_ids": ["SYNTHETIC_AUTHORING_DEFAULT"],
        "assumptions": ["bounded no-model tracer fixture"],
        "uncertainty": {"confidence": "confirmed"},
        "content": "A deliberately tested fixture transition occurs.",
        "patch_template_id": "PATCH_FIXTURE_REJECTION",
    }
    patch = {
        "template_id": "PATCH_FIXTURE_REJECTION",
        "effective_hour": 5,
        "causal_parent_ids": ["FIXTURE_REJECTION_EVENT"],
        "operations": [operation],
    }
    return event, patch


@pytest.mark.parametrize(
    ("operation", "reason_code"),
    [
        (
            {
                "operation": "set_force_package_readiness",
                "force_package_id": "HIM_RECAPTURE_GROUP",
                "expected": "ready",
                "value": "delayed",
            },
            "failed_precondition",
        ),
        (
            {
                "operation": "set_force_package_readiness",
                "force_package_id": "PACKAGE_UNEARNED",
                "expected": "prepared",
                "value": "ready",
            },
            "unknown_reference",
        ),
        (
            {
                "operation": "set_affordance_state",
                "affordance_id": "AFF_UNEARNED",
                "expected": "available",
                "value": "restricted",
            },
            "unknown_reference",
        ),
        (
            {
                "operation": "set_force_package_readiness",
                "force_package_id": "HIM_RECAPTURE_GROUP",
                "expected": "prepared",
                "value": "ready",
                "path": "actors.USA.capabilities",
            },
            "forbidden_write",
        ),
        (
            {
                "operation": "set_capability",
                "actor_id": "USA",
                "capability_id": "CAPABILITY_UNEARNED",
                "value": "available",
            },
            "undeclared_operation",
        ),
        (
            {
                "operation": "set_force_package_readiness",
                "force_package_id": "HIM_RECAPTURE_GROUP",
                "expected": "prepared",
                "value": "instant_victory",
            },
            "invalid_value",
        ),
        (
            {
                "operation": "set_force_package_readiness",
                "force_package_id": "HIM_RECAPTURE_GROUP",
                "expected": None,
                "value": "ready",
            },
            "invalid_value",
        ),
    ],
)
def test_invalid_operation_rejects_the_whole_transition(
    operation: dict[str, Any], reason_code: str
) -> None:
    profile = load_profile(PROFILE_PATH)
    forecast = admit_transition(
        profile,
        initialize_run(profile, "rejection-run"),
        profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
    ).run
    event, template = _fixture(operation)
    result = admit_transition(
        profile, forecast, event, instantiate_patch(forecast, template)
    )

    assert result.receipt.accepted is False
    assert result.receipt.reason_codes == (reason_code,)
    assert result.run.current_core() == forecast.current_core()
    assert result.run.ledger() == forecast.ledger()
    assert len(result.run.receipts()) == len(forecast.receipts()) + 1
