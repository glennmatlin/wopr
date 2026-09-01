"""Authority and information semantics for counterpart Charters."""

from __future__ import annotations

from typing import Any

from .counterpart_charter_references import require_subset
from .validation import fail

AUTHORITY_ROLES = {"civilian_decider", "military_decider", "party_state_decider"}


def _validate_route_references(route: dict[str, Any], ids: dict[str, set[str]]) -> None:
    require_subset(
        route["decision_authority_seat_ids"], ids["seats"], "route authorities"
    )
    require_subset(
        [route["applicability_predicate_id"]],
        ids["activation_predicates"],
        "route activation",
    )
    route_groups = [route["eligible_forum_group_id"], *route["consultation_group_ids"]]
    require_subset(route_groups, ids["groups"], "counterpart route groups")
    require_subset(
        route["required_confirmation_ids"],
        ids["required_confirmations"],
        "route confirmations",
    )
    require_subset(
        [route["final_decision_record_schema_id"]],
        ids["product_schemas"],
        "route product",
    )


def _validate_route_authority(
    route: dict[str, Any],
    seats: dict[str, dict[str, Any]],
    groups: dict[str, dict[str, Any]],
    products: dict[str, dict[str, Any]],
) -> None:
    route_id = route["route_id"]
    authorities = route["decision_authority_seat_ids"]
    forum_id = route["eligible_forum_group_id"]
    if not authorities or not set(authorities) <= set(
        groups[forum_id]["ordered_eligible_member_ids"]
    ):
        fail("incomplete_route", f"route {route_id} lacks its authority seats")
    if any(
        not set(seats[item]["decision_route_roles"]) & AUTHORITY_ROLES
        for item in authorities
    ):
        fail("inferred_delegation", f"route {route_id} invents authority")
    schema = products[route["final_decision_record_schema_id"]]
    if forum_id not in schema["producing_group_ids"]:
        fail("incomplete_route", f"route {route_id} cannot produce its record")
    if route["decision_rule"] == "single_named_decider" and len(authorities) != 1:
        fail("incomplete_route", f"route {route_id} has multiple single deciders")
    if route["decision_rule"] == "all_named_deciders_concur" and len(authorities) < 2:
        fail("incomplete_route", f"route {route_id} lacks joint deciders")


def _validate_route_confirmations(
    route: dict[str, Any], confirmations: dict[str, dict[str, Any]]
) -> None:
    for confirmation_id in route["required_confirmation_ids"]:
        applicable = confirmations[confirmation_id]["applicability_action_classes"]
        if route["action_class"] not in applicable:
            fail(
                "incomplete_route",
                f"route {route['route_id']} has an inapplicable confirmation",
            )


def _validate_confirmation(
    confirmation: dict[str, Any], ids: dict[str, set[str]], action_classes: set[str]
) -> None:
    seat_ids = confirmation["requester_seat_ids"] + confirmation["confirmer_seat_ids"]
    if not confirmation["requester_seat_ids"] or not confirmation["confirmer_seat_ids"]:
        fail("incomplete_route", "counterpart confirmation lacks a seat")
    require_subset(seat_ids, ids["seats"], "counterpart confirmation seats")
    require_subset(
        confirmation["applicability_action_classes"],
        action_classes,
        "confirmation actions",
    )


def _validate_routes(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    seats = {seat["seat_id"]: seat for seat in records["seats"]}
    groups = {group["group_id"]: group for group in records["groups"]}
    products = {item["product_schema_id"]: item for item in records["product_schemas"]}
    confirmations = {
        item["confirmation_id"]: item for item in records["required_confirmations"]
    }
    action_classes = {route["action_class"] for route in records["decision_routes"]}
    if len(action_classes) != len(records["decision_routes"]):
        fail("incomplete_route", "counterpart action class has multiple routes")
    for route in records["decision_routes"]:
        _validate_route_references(route, ids)
        _validate_route_authority(route, seats, groups, products)
        _validate_route_confirmations(route, confirmations)
    for confirmation in records["required_confirmations"]:
        _validate_confirmation(confirmation, ids, action_classes)


def validate_counterpart_authority(
    source: dict[str, Any],
    records: dict[str, list[dict[str, Any]]],
    ids: dict[str, set[str]],
) -> None:
    _validate_routes(records, ids)
    gap_ids = {gap["gap_id"] for gap in source["gaps"]}
    runnable = {route["action_class"] for route in records["decision_routes"]}
    for blocked in records["blocked_action_classes"]:
        if not blocked["gap_ids"]:
            fail("unknown_reference", "blocked counterpart action lacks a gap")
        require_subset(blocked["gap_ids"], gap_ids, "blocked counterpart gaps")
        if blocked["action_class"] in runnable:
            fail("incomplete_route", "counterpart action is both runnable and blocked")


__all__ = ["validate_counterpart_authority"]
