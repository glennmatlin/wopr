"""Typed group and product reference validation."""

from __future__ import annotations

from typing import Any

from .charter_reference_validation import require_subset
from .validation import fail


def validate_graph_references(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    for group in records["groups"]:
        require_subset(
            group["ordered_eligible_member_ids"],
            ids["seats"],
            "unknown_reference",
            "group members",
        )
        require_subset(
            group["input_entitlement_ids"],
            ids["information_classes"],
            "unknown_reference",
            "group inputs",
        )
        require_subset(
            group["dependency_group_ids"],
            ids["groups"],
            "unknown_reference",
            "group dependencies",
        )
        require_subset(
            group["shared_seat_barrier_ids"],
            ids["seats"],
            "unknown_reference",
            "group barriers",
        )
        if group["activation_predicate_id"] not in ids["activation_predicates"]:
            fail("unknown_reference", "group activation has an unknown reference")
        if group["product_schema_id"] not in ids["product_schemas"]:
            fail("unknown_reference", "group product has an unknown reference")
    for product in records["product_schemas"]:
        require_subset(
            product["producing_group_ids"],
            ids["groups"],
            "unknown_reference",
            "product groups",
        )


__all__ = ["validate_graph_references"]
