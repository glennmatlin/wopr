"""Graph-reference closure for counterpart Room Charters."""

from __future__ import annotations

from typing import Any

from .counterpart_charter_references import require_subset
from .validation import fail


def _validate_seats(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    for seat in records["seats"]:
        require_subset(seat["group_ids"], ids["groups"], "counterpart seat groups")
        require_subset(
            seat["information_entitlement_ids"],
            ids["information_classes"],
            "counterpart seat entitlements",
        )
        require_subset(
            seat["activation_predicate_ids"],
            ids["activation_predicates"],
            "counterpart seat activation",
        )
    for service in records["services"]:
        require_subset(
            service["activation_predicate_ids"],
            ids["activation_predicates"],
            "counterpart service activation",
        )


def _validate_group_references(
    group: dict[str, Any], members: set[str], ids: dict[str, set[str]]
) -> None:
    require_subset(list(members), ids["seats"], "counterpart group members")
    require_subset(
        group["input_entitlement_ids"],
        ids["information_classes"],
        "counterpart group inputs",
    )
    require_subset(
        group["dependency_group_ids"], ids["groups"], "counterpart dependencies"
    )
    require_subset(
        group["shared_seat_barrier_ids"], members, "counterpart seat barriers"
    )
    require_subset(
        [group["activation_predicate_id"]],
        ids["activation_predicates"],
        "group activation",
    )
    require_subset(
        [group["product_schema_id"]], ids["product_schemas"], "group product"
    )


def _validate_group_bindings(
    group: dict[str, Any],
    members: set[str],
    seats: dict[str, dict[str, Any]],
    products: dict[str, dict[str, Any]],
) -> None:
    group_id = group["group_id"]
    if any(group_id not in seats[seat_id]["group_ids"] for seat_id in members):
        fail("unknown_reference", f"group {group_id} has a one-way seat binding")
    if group_id not in products[group["product_schema_id"]]["producing_group_ids"]:
        fail("unknown_reference", f"group {group_id} has a one-way product binding")


def _validate_groups(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    seats = {seat["seat_id"]: seat for seat in records["seats"]}
    products = {item["product_schema_id"]: item for item in records["product_schemas"]}
    for group in records["groups"]:
        members = set(group["ordered_eligible_member_ids"])
        _validate_group_references(group, members, ids)
        _validate_group_bindings(group, members, seats, products)


def _validate_reverse_bindings(records: dict[str, list[dict[str, Any]]]) -> None:
    group_members = {
        group["group_id"]: set(group["ordered_eligible_member_ids"])
        for group in records["groups"]
    }
    for seat in records["seats"]:
        one_way = any(
            seat["seat_id"] not in group_members[group_id]
            for group_id in seat["group_ids"]
        )
        if one_way:
            fail("unknown_reference", f"seat {seat['seat_id']} has a one-way group")


def validate_counterpart_graph_references(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    _validate_seats(records, ids)
    _validate_groups(records, ids)
    _validate_reverse_bindings(records)
    for product in records["product_schemas"]:
        require_subset(
            product["producing_group_ids"], ids["groups"], "counterpart product groups"
        )


__all__ = ["validate_counterpart_graph_references"]
