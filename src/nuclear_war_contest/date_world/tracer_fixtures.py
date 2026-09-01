"""Bounded fixtures for the no-model DATE transition tracer."""

from __future__ import annotations

from typing import Any


def fixture_event(
    case_id: str,
    *,
    hour: int,
    patch_id: str | None = None,
    parents: list[str] | None = None,
    affected_ids: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "template_id": f"FIXTURE_{case_id}",
        "event_kind": "tracer_fixture",
        "episode_hour": hour,
        "causal_parent_ids": parents or ["OBS_WX_RIDGE_FORECAST_01"],
        "source": "tracer_fixture",
        "affected_entity_ids": affected_ids or ["HIM_RECAPTURE_GROUP"],
        "audience_ids": ["US_ACTIVE_SEATS"],
        "evidence_ids": ["SYNTHETIC_AUTHORING_DEFAULT"],
        "assumptions": ["bounded no-model tracer fixture"],
        "uncertainty": {"confidence": "confirmed"},
        "content": f"The tracer exercises {case_id.lower()}.",
        "patch_template_id": patch_id,
    }


def operation_patch(event: dict[str, Any], operation: dict[str, Any]) -> dict[str, Any]:
    return operations_patch(event, [operation])


def operations_patch(
    event: dict[str, Any], operations: list[dict[str, Any]]
) -> dict[str, Any]:
    patch_id = event["patch_template_id"]
    return {
        "template_id": patch_id,
        "effective_hour": event["episode_hour"],
        "causal_parent_ids": [event["template_id"]],
        "operations": operations,
    }


def readiness_fixture(value: str) -> tuple[dict[str, Any], dict[str, Any]]:
    case_id = f"HIM_READINESS_{value.upper()}"
    patch_id = f"PATCH_FIXTURE_{case_id}"
    event = fixture_event(case_id, hour=5, patch_id=patch_id)
    operation = {
        "operation": "set_force_package_readiness",
        "force_package_id": "HIM_RECAPTURE_GROUP",
        "expected": "prepared",
        "value": value,
    }
    return event, operation_patch(event, operation)


__all__ = [
    "fixture_event",
    "operation_patch",
    "operations_patch",
    "readiness_fixture",
]
