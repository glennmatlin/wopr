"""Fail-closed validation for source-bound counterpart Room Charters."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .charter_dependency_validation import reject_dependency_cycles
from .counterpart_charter_authority_validation import validate_counterpart_authority
from .counterpart_charter_graph_references import (
    validate_counterpart_graph_references,
)
from .counterpart_charter_graph_validation import validate_counterpart_graph_records
from .counterpart_charter_permission_validation import (
    validate_counterpart_permissions,
)
from .counterpart_charter_references import validate_counterpart_base_references
from .counterpart_charter_registry import validate_counterpart_registry
from .counterpart_charter_route_validation import validate_counterpart_route_records
from .validation import (
    fail,
    reject_officeholder_fields,
    require_records,
    require_text,
    require_text_list,
)

if TYPE_CHECKING:
    from .counterpart_artifacts import ActorSourceRegister

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
    "blocked_action_classes",
    "evidence_labels",
    "claim_boundary",
}
RECORD_FIELDS = CHARTER_FIELDS - {
    "schema_version",
    "charter_id",
    "charter_version",
    "status",
    "source_register_id",
    "source_register_hash",
    "actor_id",
    "objective_ids",
    "institution_registry",
    "claim_boundary",
}


def _validate_envelope(payload: dict[str, Any]) -> None:
    reject_officeholder_fields(payload)
    if set(payload) != CHARTER_FIELDS:
        fail("invalid_envelope", "counterpart Charter fields are invalid")
    if payload.get("schema_version") != "counterpart-room-charter.v0.1":
        fail("invalid_envelope", "counterpart Charter schema is unsupported")
    if payload.get("status") != "candidate":
        fail("invalid_envelope", "counterpart Charter status is invalid")
    for field in ("charter_id", "charter_version", "actor_id"):
        require_text(payload.get(field), f"counterpart Charter {field}")
    if not require_text_list(payload.get("objective_ids"), "counterpart objectives"):
        fail("invalid_envelope", "counterpart Charter requires objectives")
    boundary = require_text_list(
        payload.get("claim_boundary"), "counterpart claim boundary"
    )
    if not boundary:
        fail("invalid_envelope", "counterpart Charter requires a claim boundary")


def _validate_source_binding(
    payload: dict[str, Any], source_register: ActorSourceRegister
) -> None:
    if payload.get("actor_id") != source_register.actor_id:
        fail("unknown_reference", "counterpart actor does not match its source")
    if payload.get("source_register_id") != source_register.register_id:
        fail("unknown_reference", "counterpart source-register ID does not match")
    if payload.get("source_register_hash") != source_register.content_hash:
        fail("unknown_reference", "counterpart source-register hash does not match")


def _require_charter_records(payload: dict[str, Any]) -> None:
    validate_counterpart_registry(payload)
    for field in RECORD_FIELDS:
        records = require_records(payload, field)
        if not records:
            fail("invalid_envelope", f"counterpart Charter requires {field}")


def validate_counterpart_charter(
    payload: dict[str, Any], source_register: ActorSourceRegister
) -> None:
    _validate_envelope(payload)
    _validate_source_binding(payload, source_register)
    _require_charter_records(payload)
    validate_counterpart_graph_records(payload)
    validate_counterpart_route_records(payload)
    source = source_register.payload()
    records, ids = validate_counterpart_base_references(payload, source)
    validate_counterpart_graph_references(records, ids)
    validate_counterpart_permissions(payload, records, ids)
    validate_counterpart_authority(source, records, ids)
    reject_dependency_cycles(payload["groups"])


__all__ = ["validate_counterpart_charter"]
