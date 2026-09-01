"""Information-permission closure for counterpart Room Charters."""

from __future__ import annotations

from typing import Any

from .counterpart_charter_references import require_subset
from .validation import fail


def _scope_id(actor_id: str) -> str:
    scopes = {
        "ACTOR_HIMALDESH": "HD_SCOPE_ALL_ACTIVE_SEATS",
        "ACTOR_OLVANA": "OLV_SCOPE_ALL_ACTIVE_SEATS",
    }
    if actor_id not in scopes:
        fail("unknown_reference", "counterpart actor has no authorized scope identity")
    return scopes[actor_id]


def _recipient_seats(
    recipient_ids: list[str],
    scope_id: str,
    seats: dict[str, dict[str, Any]],
    groups: dict[str, dict[str, Any]],
) -> set[str]:
    resolved: set[str] = set()
    for recipient_id in recipient_ids:
        if recipient_id == scope_id:
            resolved.update(seats)
        elif recipient_id in groups:
            resolved.update(groups[recipient_id]["ordered_eligible_member_ids"])
        elif recipient_id in seats:
            resolved.add(recipient_id)
    return resolved


def _has_direct_entitlement(
    information_id: str,
    seat: dict[str, Any],
    groups: dict[str, dict[str, Any]],
) -> bool:
    if information_id in seat["information_entitlement_ids"]:
        return True
    return any(
        information_id in groups[group_id]["input_entitlement_ids"]
        for group_id in seat["group_ids"]
    )


def _reject_world_truth(
    seats: dict[str, dict[str, Any]], information: dict[str, dict[str, Any]]
) -> None:
    for seat in seats.values():
        if any(
            information[item]["sensitivity"] == "world_ground_truth"
            for item in seat["information_entitlement_ids"]
        ):
            fail("entitlement_leak", f"seat {seat['seat_id']} receives World truth")


def _validate_permission(
    permission: dict[str, Any],
    scope_id: str,
    seats: dict[str, dict[str, Any]],
    groups: dict[str, dict[str, Any]],
    ids: dict[str, set[str]],
) -> None:
    information_id = permission["information_class_id"]
    require_subset(
        [information_id], ids["information_classes"], "permission information"
    )
    require_subset(permission["sender_ids"], ids["services"] | ids["groups"], "senders")
    recipients = ids["seats"] | ids["groups"] | {scope_id}
    require_subset(permission["recipient_ids"], recipients, "counterpart recipients")
    resolved = _recipient_seats(permission["recipient_ids"], scope_id, seats, groups)
    exceeds_entitlement = permission["delivery_mode"] == "direct" and any(
        not _has_direct_entitlement(information_id, seats[seat_id], groups)
        for seat_id in resolved
    )
    if exceeds_entitlement:
        fail(
            "entitlement_leak",
            f"permission {permission['permission_id']} exceeds entitlement",
        )


def validate_counterpart_permissions(
    payload: dict[str, Any],
    records: dict[str, list[dict[str, Any]]],
    ids: dict[str, set[str]],
) -> None:
    scope_id = _scope_id(payload["actor_id"])
    seats = {seat["seat_id"]: seat for seat in records["seats"]}
    groups = {group["group_id"]: group for group in records["groups"]}
    information = {
        item["information_class_id"]: item for item in records["information_classes"]
    }
    _reject_world_truth(seats, information)
    for permission in records["disclosure_permissions"]:
        _validate_permission(permission, scope_id, seats, groups, ids)


__all__ = ["validate_counterpart_permissions"]
