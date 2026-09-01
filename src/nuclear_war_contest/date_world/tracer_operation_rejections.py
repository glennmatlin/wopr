"""Semantic-operation failures exercised by the DATE tracer."""

from __future__ import annotations

from typing import Any

from .models import DateRun
from .profile import DateProfile
from .tracer_fixtures import fixture_event, operation_patch, operations_patch


def _operation_case(
    profile: DateProfile,
    run: DateRun,
    case_id: str,
    operation: dict[str, Any],
) -> dict[str, str]:
    from .tracer_rejections import retain_rejection

    patch_id = f"PATCH_FIXTURE_{case_id}"
    event = fixture_event(case_id, hour=7, patch_id=patch_id)
    return retain_rejection(
        profile, run, case_id, event, operation_patch(event, operation)
    )


def _atomic_precondition_case(profile: DateProfile, run: DateRun) -> dict[str, str]:
    from .tracer_rejections import retain_rejection

    case_id = "FAILED_AFFORDANCE_PRECONDITION"
    event = fixture_event(case_id, hour=7, patch_id=f"PATCH_FIXTURE_{case_id}")
    operations = [
        {
            "operation": "set_affordance_state",
            "affordance_id": "AFF_US_RIDGE_ISR_WINDOW",
            "expected": "intermittent",
            "value": "restricted",
        },
        {
            "operation": "set_affordance_state",
            "affordance_id": "AFF_HIM_SOUTH_PASS_SUPPORT_WINDOW",
            "expected": "available",
            "value": "restricted",
        },
    ]
    return retain_rejection(
        profile, run, case_id, event, operations_patch(event, operations)
    )


def exercise_operation_rejections(
    profile: DateProfile, final: DateRun
) -> list[dict[str, str]]:
    cases = {
        "UNKNOWN_PACKAGE": {
            "operation": "set_force_package_readiness",
            "force_package_id": "PACKAGE_UNEARNED",
            "expected": "prepared",
            "value": "ready",
        },
        "UNKNOWN_AFFORDANCE": {
            "operation": "set_affordance_state",
            "affordance_id": "AFF_UNEARNED",
            "expected": "available",
            "value": "restricted",
        },
        "UNEARNED_CAPABILITY": {
            "operation": "set_capability",
            "actor_id": "USA",
            "capability_id": "CAPABILITY_UNEARNED",
            "value": "available",
        },
        "ARBITRARY_PATH": {
            "operation": "set_force_package_readiness",
            "force_package_id": "HIM_RECAPTURE_GROUP",
            "expected": "ready",
            "value": "delayed",
            "path": "actors.USA.capabilities",
        },
        "INVALID_VALUE": {
            "operation": "set_force_package_readiness",
            "force_package_id": "HIM_RECAPTURE_GROUP",
            "expected": "ready",
            "value": "instant_victory",
        },
    }
    operation_results = [
        _operation_case(profile, final, case_id, operation)
        for case_id, operation in cases.items()
    ]
    return [_atomic_precondition_case(profile, final), *operation_results]


__all__ = ["exercise_operation_rejections"]
