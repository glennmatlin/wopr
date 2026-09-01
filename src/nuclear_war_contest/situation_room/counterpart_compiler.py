"""Deterministic compilation of validated counterpart Room Charters."""

from __future__ import annotations

from typing import Any

from .counterpart_artifacts import CounterpartCharter
from .counterpart_compiled_models import (
    CompiledCounterpartCharter,
    CompiledCounterpartConfirmation,
    CompiledCounterpartGroup,
    CompiledCounterpartRoute,
    CompiledCounterpartSeat,
)
from .counterpart_compiler_graph import (
    compile_active_groups,
    compile_active_seats,
    dependency_closure,
    shared_seat_barriers,
)


def _recipients(
    payload: dict[str, Any],
    seats: dict[str, CompiledCounterpartSeat],
    groups: dict[str, CompiledCounterpartGroup],
) -> dict[tuple[str, str], tuple[str, ...]]:
    scope_id = {
        "ACTOR_HIMALDESH": "HD_SCOPE_ALL_ACTIVE_SEATS",
        "ACTOR_OLVANA": "OLV_SCOPE_ALL_ACTIVE_SEATS",
    }[payload["actor_id"]]
    recipients_by_key: dict[tuple[str, str], set[str]] = {}
    for permission in payload["disclosure_permissions"]:
        recipients: set[str] = set()
        for recipient_id in permission["recipient_ids"]:
            if recipient_id == scope_id:
                recipients.update(seats)
            elif recipient_id in groups:
                recipients.update(seat.seat_id for seat in groups[recipient_id].members)
            elif recipient_id in seats:
                recipients.add(recipient_id)
        for sender_id in permission["sender_ids"]:
            key = (permission["information_class_id"], sender_id)
            recipients_by_key.setdefault(key, set()).update(recipients)
    return {
        key: tuple(sorted(recipients)) for key, recipients in recipients_by_key.items()
    }


def _routes(payload: dict[str, Any]) -> dict[str, CompiledCounterpartRoute]:
    return {
        item["action_class"]: CompiledCounterpartRoute(
            route_id=item["route_id"],
            action_class=item["action_class"],
            decision_authority_seat_ids=tuple(item["decision_authority_seat_ids"]),
            decision_rule=item["decision_rule"],
            eligible_forum_group_id=item["eligible_forum_group_id"],
            consultation_group_ids=tuple(item["consultation_group_ids"]),
            required_confirmation_ids=tuple(item["required_confirmation_ids"]),
            final_decision_record_schema_id=item["final_decision_record_schema_id"],
            failure_effect=item["failure_effect"],
        )
        for item in payload["decision_routes"]
    }


def _confirmations(
    payload: dict[str, Any],
) -> dict[str, CompiledCounterpartConfirmation]:
    return {
        item["confirmation_id"]: CompiledCounterpartConfirmation(
            confirmation_id=item["confirmation_id"],
            requester_seat_ids=tuple(item["requester_seat_ids"]),
            confirmer_seat_ids=tuple(item["confirmer_seat_ids"]),
            applicability_action_classes=tuple(item["applicability_action_classes"]),
            failure_effect=item["failure_effect"],
        )
        for item in payload["required_confirmations"]
    }


def compile_counterpart_charter(
    charter: CounterpartCharter,
) -> CompiledCounterpartCharter:
    payload = charter.payload()
    seats = compile_active_seats(payload)
    groups = compile_active_groups(payload, seats)
    blocked = {
        item["action_class"]: tuple(item["gap_ids"])
        for item in payload["blocked_action_classes"]
    }
    return CompiledCounterpartCharter(
        actor_id=charter.actor_id,
        source_register_hash=charter.source_register_hash,
        charter_hash=charter.content_hash,
        _seats=seats,
        _groups=groups,
        _dependencies=dependency_closure(groups),
        _barriers=shared_seat_barriers(groups),
        _recipients=_recipients(payload, seats, groups),
        _routes=_routes(payload),
        _confirmations=_confirmations(payload),
        _blocked_gaps=blocked,
    )


__all__ = ["compile_counterpart_charter"]
