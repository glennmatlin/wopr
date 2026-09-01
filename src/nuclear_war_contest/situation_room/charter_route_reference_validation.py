"""Typed disclosure, confirmation, and route reference validation."""

from __future__ import annotations

from typing import Any

from .charter_reference_validation import require_subset
from .validation import fail


def _validate_permissions(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    addressable = ids["seats"] | ids["services"] | ids["groups"]
    for permission in records["disclosure_permissions"]:
        if permission["information_class_id"] not in ids["information_classes"]:
            fail("unknown_reference", "permission information class is unknown")
        require_subset(
            permission["sender_ids"],
            addressable,
            "unknown_reference",
            "permission senders",
        )
        require_subset(
            permission["recipient_ids"],
            addressable,
            "unknown_reference",
            "permission recipients",
        )


def _validate_confirmations(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    for confirmation in records["required_confirmations"]:
        if confirmation["requester_seat_id"] not in ids["seats"]:
            fail("unknown_reference", "confirmation requester is unknown")
        require_subset(
            confirmation["confirmer_seat_ids"],
            ids["seats"],
            "unknown_reference",
            "confirmation seats",
        )
        if (
            confirmation["applicability_predicate_id"]
            not in ids["activation_predicates"]
        ):
            fail("unknown_reference", "confirmation predicate is unknown")


def _validate_routes(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    action_classes = [route["action_class"] for route in records["decision_routes"]]
    if len(action_classes) != len(set(action_classes)):
        fail("incomplete_route", "decision route action class is ambiguous")
    scalar_refs = {
        "applicability_predicate_id": "activation_predicates",
        "owning_authority_seat_id": "seats",
        "eligible_forum_group_id": "groups",
        "final_decision_record_schema_id": "product_schemas",
    }
    for route in records["decision_routes"]:
        if any(
            route[field] not in ids[target] for field, target in scalar_refs.items()
        ):
            fail("unknown_reference", "decision route has an unknown reference")
        require_subset(
            route["consultation_group_ids"],
            ids["groups"],
            "unknown_reference",
            "route consultations",
        )
        require_subset(
            route["required_confirmation_ids"],
            ids["required_confirmations"],
            "unknown_reference",
            "route confirmations",
        )


def validate_route_references(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    _validate_permissions(records, ids)
    _validate_confirmations(records, ids)
    _validate_routes(records, ids)


__all__ = ["validate_route_references"]
