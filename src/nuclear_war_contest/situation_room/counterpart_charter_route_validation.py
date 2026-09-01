"""Permission and authority-record validation for counterpart Charters."""

from __future__ import annotations

from typing import Any

from .counterpart_record_validation import validate_record


def _validate_permission(permission: dict[str, Any]) -> None:
    validate_record(
        permission,
        "counterpart disclosure permission",
        text_fields={"permission_id", "information_class_id"},
        list_fields={"sender_ids", "recipient_ids", "fact_ids", "inference_ids"},
        choice_fields={"delivery_mode": {"direct", "group_delivery"}},
    )


def _validate_confirmation(confirmation: dict[str, Any]) -> None:
    validate_record(
        confirmation,
        "counterpart confirmation",
        text_fields={"confirmation_id", "description", "failure_effect"},
        list_fields={
            "requester_seat_ids",
            "confirmer_seat_ids",
            "applicability_action_classes",
            "fact_ids",
            "inference_ids",
        },
    )


def _validate_route(route: dict[str, Any]) -> None:
    validate_record(
        route,
        "counterpart decision route",
        text_fields={
            "route_id",
            "action_class",
            "applicability_predicate_id",
            "eligible_forum_group_id",
            "final_decision_record_schema_id",
            "failure_effect",
        },
        list_fields={
            "decision_authority_seat_ids",
            "consultation_group_ids",
            "required_confirmation_ids",
            "fact_ids",
            "inference_ids",
        },
        choice_fields={
            "decision_rule": {"all_named_deciders_concur", "single_named_decider"}
        },
    )


def _validate_blocked(blocked: dict[str, Any]) -> None:
    validate_record(
        blocked,
        "counterpart blocked action class",
        text_fields={
            "blocked_action_class_id",
            "action_class",
            "reason",
            "failure_effect",
        },
        list_fields={"gap_ids"},
    )


def validate_counterpart_route_records(payload: dict[str, Any]) -> None:
    for field, validator in (
        ("disclosure_permissions", _validate_permission),
        ("required_confirmations", _validate_confirmation),
        ("decision_routes", _validate_route),
        ("blocked_action_classes", _validate_blocked),
    ):
        for record in payload[field]:
            validator(record)


__all__ = ["validate_counterpart_route_records"]
