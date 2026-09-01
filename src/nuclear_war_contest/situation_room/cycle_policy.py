"""Integrated U.S. Policy Package completeness checks."""

from __future__ import annotations

from typing import Any

from .compiled_models import CompiledUsCharter

_ORDERED_DOMAIN_IDS = (
    "diplomacy_private_channels",
    "intelligence_collection_sharing",
    "defense_support_posture",
    "economic_financial_measures",
    "public_communication",
    "contingency_reassessment",
)
_DOMAIN_IDS = frozenset(_ORDERED_DOMAIN_IDS)
_ORDERED_DISPOSITIONS = (
    "immediate_action",
    "conditional_action",
    "no_action",
    "not_applicable",
)
_DISPOSITIONS = frozenset(_ORDERED_DISPOSITIONS)
_ORDERED_FIELDS = (
    "domain_id",
    "responsible_seat_ids",
    "deciding_forum_group_id",
    "reason",
    "disposition",
)
_FIELDS = frozenset(_ORDERED_FIELDS)


def policy_package_is_complete(
    content: dict[str, Any], compiled: CompiledUsCharter
) -> bool:
    dispositions = content.get("domain_dispositions")
    if not isinstance(dispositions, list) or len(dispositions) != len(_DOMAIN_IDS):
        return False
    active_seats = set(compiled.active_seat_ids())
    active_groups = set(compiled.active_group_ids())
    found: set[str] = set()
    for item in dispositions:
        if not isinstance(item, dict) or not _FIELDS <= set(item):
            return False
        domain_id = item["domain_id"]
        seats = item["responsible_seat_ids"]
        forum_id = item["deciding_forum_group_id"]
        reason = item["reason"]
        disposition = item["disposition"]
        if (
            not isinstance(domain_id, str)
            or domain_id not in _DOMAIN_IDS
            or domain_id in found
            or not isinstance(seats, list)
            or not seats
            or not all(isinstance(seat_id, str) and seat_id for seat_id in seats)
            or len(seats) != len(set(seats))
            or not set(seats) <= active_seats
            or not isinstance(forum_id, str)
            or forum_id not in active_groups
            or not isinstance(reason, str)
            or not reason
            or not isinstance(disposition, str)
            or disposition not in _DISPOSITIONS
        ):
            return False
        found.add(domain_id)
    return found == _DOMAIN_IDS


def policy_package_domain_dispositions_schema() -> dict[str, Any]:
    return {
        "type": "array",
        "minItems": len(_ORDERED_DOMAIN_IDS),
        "maxItems": len(_ORDERED_DOMAIN_IDS),
        "required_domain_ids": list(_ORDERED_DOMAIN_IDS),
        "items": _domain_disposition_item_schema(),
    }


def _domain_disposition_item_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "required": list(_ORDERED_FIELDS),
        "properties": {
            "domain_id": {"type": "string", "enum": list(_ORDERED_DOMAIN_IDS)},
            "responsible_seat_ids": {
                "type": "array",
                "minItems": 1,
                "uniqueItems": True,
                "items": {"type": "string"},
            },
            "deciding_forum_group_id": {"type": "string"},
            "reason": {"type": "string", "minLength": 1},
            "disposition": {
                "type": "string",
                "enum": list(_ORDERED_DISPOSITIONS),
            },
        },
    }


__all__ = [
    "policy_package_domain_dispositions_schema",
    "policy_package_is_complete",
]
