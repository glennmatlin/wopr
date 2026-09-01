"""Nested proposal bridge fixture shape validation."""

from __future__ import annotations

from typing import Any

from .proposal_bridge_validation_helpers import (
    require_text,
    require_text_list,
    require_texts,
)

CLARIFIABLE_FIELDS = {
    "intended_effect",
    "means_or_resources",
    "object_or_audience",
    "timing",
    "conditions",
}


def validate_proposal(item: dict[str, Any]) -> None:
    require_texts(
        item,
        (
            "proposal_id",
            "proposal_version",
            "actor_id",
            "original_language",
            "source_policy_package_id",
            "institutional_decision_record_id",
        ),
    )
    require_text_list(item["source_component_ids"], "proposal components")
    if not item["source_component_ids"]:
        raise ValueError("invalid_envelope: proposal component is required")
    if not isinstance(item["effects"], list) or not item["effects"]:
        raise ValueError("invalid_envelope: proposal effects are invalid")
    if not isinstance(item["open_content"], dict):
        raise ValueError("invalid_envelope: proposal open content is invalid")


def validate_effect(item: dict[str, Any]) -> None:
    require_texts(item, ("effect_id", "original_language", "consequence_proposal_id"))
    for field in (
        "source_component_ids",
        "dependency_effect_ids",
        "unresolved_field_ids",
        "capability_record_ids",
    ):
        require_text_list(item[field], field)
    if not item["source_component_ids"]:
        raise ValueError("invalid_envelope: effect component is required")
    if not set(item["unresolved_field_ids"]) <= CLARIFIABLE_FIELDS:
        raise ValueError("invalid_envelope: unresolved effect field is invalid")
    unresolved = set(item["unresolved_field_ids"])
    if any(
        (item[field] is None) != (field in unresolved) for field in CLARIFIABLE_FIELDS
    ):
        raise ValueError("invalid_envelope: missing effect field is not marked")
    for field in ("intended_effect", "timing"):
        if item[field] is not None:
            require_text(item[field], field)
    for field in ("means_or_resources", "object_or_audience", "conditions"):
        if item[field] is not None:
            require_text_list(item[field], field)
    authority = item["authority_record_id"]
    if authority is not None:
        require_text(authority, "authority_record_id")
    if not isinstance(item["open_content"], dict):
        raise ValueError("invalid_envelope: effect open content is invalid")


def validate_clarification(item: dict[str, Any]) -> None:
    require_texts(
        item,
        (
            "clarification_id",
            "proposal_id",
            "effect_id",
            "original_effect_hash",
            "status",
            "question",
            "response",
        ),
    )
    if item["status"] not in {"resolved", "unresolved"}:
        raise ValueError("invalid_envelope: clarification status is invalid")
    require_text_list(item["requested_field_ids"], "requested clarification fields")
    if not set(item["requested_field_ids"]) <= CLARIFIABLE_FIELDS:
        raise ValueError("invalid_envelope: clarification field is invalid")
    if not isinstance(item["resolved_fields"], dict):
        raise ValueError("invalid_envelope: resolved fields must be an object")


def validate_authority(item: dict[str, Any]) -> None:
    require_texts(item, tuple(item))
    if item["status"] not in {"authorized", "not_authorized"}:
        raise ValueError("invalid_envelope: effect authority status is invalid")
    if item["evidence_status"] != "development_fixture_non_evidence":
        raise ValueError("invalid_envelope: effect authority evidence is invalid")


def validate_capability(item: dict[str, Any]) -> None:
    require_texts(
        item,
        (
            "capability_record_id",
            "effect_id",
            "predicate_type",
            "entity_id",
            "actor_id",
            "evidence_status",
        ),
    )
    if item["predicate_type"] not in {
        "activity_owned_by",
        "affordance_controlled_by",
        "affordance_state_is",
        "force_package_owned_by",
    }:
        raise ValueError("invalid_envelope: capability predicate is invalid")
    expected = item["expected_value"]
    if expected is not None:
        require_text(expected, "expected_value")
    if item["evidence_status"] != "development_fixture_non_evidence":
        raise ValueError("invalid_envelope: capability evidence is invalid")


__all__ = [
    "CLARIFIABLE_FIELDS",
    "validate_authority",
    "validate_capability",
    "validate_clarification",
    "validate_effect",
    "validate_proposal",
]
