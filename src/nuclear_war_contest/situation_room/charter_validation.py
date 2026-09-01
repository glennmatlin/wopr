"""Fail-closed validation for U.S. Room Charter candidates."""

from __future__ import annotations

from typing import Any

from .charter_consistency_validation import validate_charter_consistency
from .charter_dependency_validation import reject_dependency_cycles
from .charter_graph_reference_validation import validate_graph_references
from .charter_graph_validation import validate_graph_records
from .charter_reference_validation import validate_charter_base_references
from .charter_registry_validation import validate_registry
from .charter_route_reference_validation import validate_route_references
from .charter_route_validation import validate_route_records, validate_route_semantics
from .source_register import SourceRegister
from .validation import (
    fail,
    reject_officeholder_fields,
    require_records,
    require_text,
    require_text_list,
)

CHARTER_FIELDS = {
    "schema_version",
    "charter_id",
    "charter_version",
    "status",
    "source_register_id",
    "source_register_hash",
    "actor_id",
    "objective_ids",
    "institution_registry",
    "groups",
    "information_classes",
    "disclosure_permissions",
    "activation_predicates",
    "decision_routes",
    "required_confirmations",
    "product_schemas",
    "evidence_labels",
}
RECORD_FIELDS = (
    "groups",
    "information_classes",
    "disclosure_permissions",
    "activation_predicates",
    "decision_routes",
    "required_confirmations",
    "product_schemas",
    "evidence_labels",
)


def validate_charter(payload: dict[str, Any], source_register: SourceRegister) -> None:
    reject_officeholder_fields(payload)
    if set(payload) != CHARTER_FIELDS:
        fail("invalid_envelope", "Charter fields are invalid")
    if payload.get("schema_version") != "us-room-charter.v0.1":
        fail("invalid_envelope", "Charter schema is unsupported")
    if payload.get("status") != "candidate":
        fail("invalid_envelope", "Charter status is invalid")
    for field in ("charter_id", "charter_version", "actor_id"):
        require_text(payload.get(field), f"Charter {field}")
    objectives = require_text_list(payload.get("objective_ids"), "Charter objectives")
    if not objectives:
        fail("invalid_envelope", "Charter requires actor objectives")
    if payload.get("source_register_id") != source_register.register_id:
        fail("unknown_reference", "Charter source-register ID does not match")
    if payload.get("source_register_hash") != source_register.content_hash:
        fail("unknown_reference", "Charter source-register hash does not match")
    validate_registry(payload)
    for field in RECORD_FIELDS:
        require_records(payload, field)
    required_nonempty = (
        "groups",
        "information_classes",
        "activation_predicates",
        "decision_routes",
        "product_schemas",
        "evidence_labels",
    )
    if any(not payload[field] for field in required_nonempty):
        fail("invalid_envelope", "Charter registry is incomplete")
    validate_graph_records(payload)
    validate_route_records(payload)
    records, identities = validate_charter_base_references(payload, source_register)
    validate_graph_references(records, identities)
    validate_route_references(records, identities)
    validate_charter_consistency(payload, source_register)
    reject_dependency_cycles(payload["groups"])
    validate_route_semantics(payload)


__all__ = ["validate_charter"]
