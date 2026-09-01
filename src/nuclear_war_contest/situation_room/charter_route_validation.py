"""Disclosure, confirmation, and decision-route validation."""

from __future__ import annotations

from typing import Any

from .validation import fail, require_text, require_text_list

PERMISSION_FIELDS = {
    "permission_id",
    "information_class_id",
    "sender_ids",
    "recipient_ids",
    "delivery_mode",
    "fact_ids",
    "inference_ids",
}
CONFIRMATION_FIELDS = {
    "confirmation_id",
    "description",
    "requester_seat_id",
    "confirmer_seat_ids",
    "applicability_predicate_id",
    "failure_effect",
    "fact_ids",
    "inference_ids",
}
ROUTE_FIELDS = {
    "route_id",
    "action_class",
    "applicability_predicate_id",
    "owning_authority_seat_id",
    "eligible_forum_group_id",
    "decision_rule",
    "presidential_attention_rule",
    "consultation_group_ids",
    "required_confirmation_ids",
    "final_decision_record_schema_id",
    "failure_effect",
    "fact_ids",
    "inference_ids",
}
DELIVERY_MODES = {"direct", "group_delivery", "logged_retrieval"}
DECISION_RULES = {"full_consensus_or_refer", "president_decides"}
ATTENTION_RULES = {"poll_separately", "required"}


def _validate_permission(record: dict[str, Any]) -> None:
    if set(record) != PERMISSION_FIELDS:
        fail("invalid_envelope", "disclosure-permission fields are invalid")
    for field in ("permission_id", "information_class_id"):
        require_text(record[field], f"permission {field}")
    if record["delivery_mode"] not in DELIVERY_MODES:
        fail("invalid_envelope", "permission delivery mode is invalid")
    for field in ("sender_ids", "recipient_ids", "fact_ids", "inference_ids"):
        require_text_list(record[field], f"permission {field}")


def _validate_confirmation(record: dict[str, Any]) -> None:
    if set(record) != CONFIRMATION_FIELDS:
        fail("invalid_envelope", "confirmation fields are invalid")
    text_fields = (
        "confirmation_id",
        "description",
        "requester_seat_id",
        "applicability_predicate_id",
        "failure_effect",
    )
    for field in text_fields:
        require_text(record[field], f"confirmation {field}")
    for field in ("confirmer_seat_ids", "fact_ids", "inference_ids"):
        require_text_list(record[field], f"confirmation {field}")


def _validate_route(record: dict[str, Any]) -> None:
    if set(record) != ROUTE_FIELDS:
        fail("invalid_envelope", "decision-route fields are invalid")
    text_fields = ROUTE_FIELDS - {
        "consultation_group_ids",
        "required_confirmation_ids",
        "fact_ids",
        "inference_ids",
        "decision_rule",
        "presidential_attention_rule",
    }
    for field in text_fields:
        require_text(record[field], f"decision route {field}")
    if record["decision_rule"] not in DECISION_RULES:
        fail("incomplete_route", "decision rule is unsupported")
    if record["presidential_attention_rule"] not in ATTENTION_RULES:
        fail("incomplete_route", "presidential-attention rule is unsupported")
    for field in (
        "consultation_group_ids",
        "required_confirmation_ids",
        "fact_ids",
        "inference_ids",
    ):
        require_text_list(record[field], f"decision route {field}")


def validate_route_records(payload: dict[str, Any]) -> None:
    for record in payload["disclosure_permissions"]:
        _validate_permission(record)
    for record in payload["required_confirmations"]:
        _validate_confirmation(record)
    for record in payload["decision_routes"]:
        _validate_route(record)


def validate_route_semantics(payload: dict[str, Any]) -> None:
    seats = {seat["seat_id"]: seat for seat in payload["institution_registry"]["seats"]}
    groups = {group["group_id"]: group for group in payload["groups"]}
    products = {
        product["product_schema_id"]: product for product in payload["product_schemas"]
    }
    information = {
        item["information_class_id"]: item for item in payload["information_classes"]
    }
    for seat in seats.values():
        entitlements = set(seat["information_entitlement_ids"])
        if any(
            information[item]["sensitivity"] == "world_ground_truth"
            for item in entitlements
        ):
            fail(
                "entitlement_leak",
                f"seat {seat['seat_id']} receives World ground truth",
            )
    for route in payload["decision_routes"]:
        owner = seats[route["owning_authority_seat_id"]]
        if "owning_authority" not in owner["decision_route_roles"]:
            fail("inferred_delegation", f"route {route['route_id']} invents authority")
        forum_id = route["eligible_forum_group_id"]
        schema = products[route["final_decision_record_schema_id"]]
        forum_has_owner = (
            owner["seat_id"] in groups[forum_id]["ordered_eligible_member_ids"]
        )
        forum_produces_record = forum_id in schema["producing_group_ids"]
        if not forum_has_owner or not forum_produces_record:
            fail(
                "incomplete_route",
                f"route {route['route_id']} cannot produce a decision",
            )


__all__ = ["validate_route_records", "validate_route_semantics"]
