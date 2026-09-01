"""Cross-record semantic consistency for U.S. Room Charters."""

from __future__ import annotations

from typing import Any

from .source_register import SourceRegister
from .validation import fail


def _validate_objectives(
    payload: dict[str, Any], source_register: SourceRegister
) -> None:
    supported_scopes = {
        scope_id
        for inference in source_register.payload()["inferences"]
        for scope_id in inference["scope_ids"]
    }
    if not set(payload["objective_ids"]) <= supported_scopes:
        fail("unknown_reference", "Charter objective is not source-bound")


def _validate_membership(payload: dict[str, Any]) -> None:
    seats = payload["institution_registry"]["seats"]
    groups = payload["groups"]
    for seat in seats:
        expected_groups = {
            group["group_id"]
            for group in groups
            if seat["seat_id"] in group["ordered_eligible_member_ids"]
        }
        if set(seat["group_ids"]) != expected_groups:
            fail("invalid_envelope", "seat and group membership disagree")


def _validate_shared_seat_barriers(payload: dict[str, Any]) -> None:
    seats = {
        seat["seat_id"]: seat for seat in payload["institution_registry"]["seats"]
    }
    for group in payload["groups"]:
        expected = {
            seat_id
            for seat_id in group["ordered_eligible_member_ids"]
            if len(seats[seat_id]["group_ids"]) > 1
        }
        if set(group["shared_seat_barrier_ids"]) != expected:
            fail("invalid_envelope", "group shared-seat barriers are inconsistent")


def _recipient_seat_ids(
    recipient_id: str,
    seats: dict[str, dict[str, Any]],
    groups: dict[str, dict[str, Any]],
) -> list[str]:
    if recipient_id in seats:
        return [recipient_id]
    if recipient_id in groups:
        return groups[recipient_id]["ordered_eligible_member_ids"]
    return []


def _validate_permission_entitlements(payload: dict[str, Any]) -> None:
    seats = {
        seat["seat_id"]: seat for seat in payload["institution_registry"]["seats"]
    }
    groups = {group["group_id"]: group for group in payload["groups"]}
    for permission in payload["disclosure_permissions"]:
        information_id = permission["information_class_id"]
        for recipient_id in permission["recipient_ids"]:
            for seat_id in _recipient_seat_ids(recipient_id, seats, groups):
                if information_id not in seats[seat_id]["information_entitlement_ids"]:
                    detail = (
                        f"permission {permission['permission_id']} exceeds "
                        "seat entitlement"
                    )
                    fail(
                        "entitlement_leak",
                        detail,
                    )


def validate_charter_consistency(
    payload: dict[str, Any], source_register: SourceRegister
) -> None:
    _validate_objectives(payload, source_register)
    _validate_membership(payload)
    _validate_shared_seat_barriers(payload)
    _validate_permission_entitlements(payload)


__all__ = ["validate_charter_consistency"]
