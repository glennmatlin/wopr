"""Route views and failures for counterpart Room decisions."""

from __future__ import annotations

from typing import Any

from .counterpart_compiled_models import CompiledCounterpartCharter
from .counterpart_room_decision_semantics import decision_record_is_valid


def decision_failure(
    identity: str, reason: str, group_id: str, effect: str
) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{identity}",
        "reason_code": reason,
        "group_id": group_id,
        "failure_effect": effect,
    }


def route_view(compiled: CompiledCounterpartCharter, action: str) -> dict[str, Any]:
    route = compiled.route_for(action)
    return {
        "route_id": route.route_id,
        "action_class": route.action_class,
        "decision_authority_seat_ids": list(route.decision_authority_seat_ids),
        "decision_rule": route.decision_rule,
        "eligible_forum_group_id": route.eligible_forum_group_id,
        "consultation_group_ids": list(route.consultation_group_ids),
        "required_confirmation_ids": list(route.required_confirmation_ids),
        "final_decision_record_schema_id": route.final_decision_record_schema_id,
        "failure_effect": route.failure_effect,
    }


def route_failures(
    actor_id: str, record: dict[str, Any], action: str, route: dict[str, Any]
) -> list[dict[str, Any]]:
    if decision_record_is_valid(actor_id, record, action):
        return []
    return [
        decision_failure(
            route["route_id"],
            "route_mismatch",
            record["group_id"],
            route["failure_effect"],
        )
    ]


__all__ = ["decision_failure", "route_failures", "route_view"]
