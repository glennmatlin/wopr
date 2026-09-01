"""Typed cross-reference validation for U.S. Room Charters."""

from __future__ import annotations

from typing import Any

from .source_register import SourceRegister
from .validation import fail

IDENTITY_FIELDS = {
    "seats": "seat_id",
    "services": "service_id",
    "groups": "group_id",
    "information_classes": "information_class_id",
    "disclosure_permissions": "permission_id",
    "activation_predicates": "activation_predicate_id",
    "decision_routes": "route_id",
    "required_confirmations": "confirmation_id",
    "product_schemas": "product_schema_id",
    "evidence_labels": "evidence_label_id",
}


def charter_records(payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    registry = payload["institution_registry"]
    return {
        "seats": registry["seats"],
        "services": registry["services"],
        **{field: payload[field] for field in IDENTITY_FIELDS if field not in registry},
    }


def require_subset(
    values: list[str], expected: set[str], reason_code: str, label: str
) -> None:
    if not set(values) <= expected:
        fail(reason_code, f"{label} has an unknown reference")


def _validate_global_ids(
    payload: dict[str, Any],
    records: dict[str, list[dict[str, Any]]],
    source: dict[str, Any],
) -> None:
    charter_ids = list(payload["objective_ids"])
    for field, items in records.items():
        identity_field = IDENTITY_FIELDS[field]
        charter_ids.extend(item[identity_field] for item in items)
    source_ids = [item["source_id"] for item in source["sources"]]
    source_ids.extend(item["fact_id"] for item in source["facts"])
    source_ids.extend(item["inference_id"] for item in source["inferences"])
    source_ids.extend(item["gap_id"] for item in source["gaps"])
    identities = charter_ids + source_ids
    if len(identities) != len(set(identities)):
        fail("duplicate_id", "Charter and source identity namespace repeats")


def _validate_evidence_bindings(
    records: dict[str, list[dict[str, Any]]], source: dict[str, Any]
) -> None:
    fact_ids = {item["fact_id"] for item in source["facts"]}
    inference_ids = {item["inference_id"] for item in source["inferences"]}
    for items in records.values():
        for item in items:
            if "fact_ids" in item:
                require_subset(item["fact_ids"], fact_ids, "unbound_fact", "fact IDs")
            if "inference_ids" in item:
                require_subset(
                    item["inference_ids"],
                    inference_ids,
                    "unbound_inference",
                    "inference IDs",
                )
            if "persona_posture_ids" in item:
                evidence_ids = fact_ids | inference_ids
                require_subset(
                    item["persona_posture_ids"],
                    evidence_ids,
                    "unknown_reference",
                    "persona posture IDs",
                )


def _validate_institution_refs(
    records: dict[str, list[dict[str, Any]]], ids: dict[str, set[str]]
) -> None:
    for seat in records["seats"]:
        require_subset(
            seat["group_ids"], ids["groups"], "unknown_reference", "seat groups"
        )
        require_subset(
            seat["information_entitlement_ids"],
            ids["information_classes"],
            "unknown_reference",
            "seat entitlements",
        )
        require_subset(
            seat["activation_predicate_ids"],
            ids["activation_predicates"],
            "unknown_reference",
            "seat activation",
        )
    for service in records["services"]:
        require_subset(
            service["activation_predicate_ids"],
            ids["activation_predicates"],
            "unknown_reference",
            "service activation",
        )


def validate_charter_base_references(
    payload: dict[str, Any], source_register: SourceRegister
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, set[str]]]:
    records = charter_records(payload)
    source = source_register.payload()
    _validate_global_ids(payload, records, source)
    _validate_evidence_bindings(records, source)
    ids = {
        field: {item[identity] for item in records[field]}
        for field, identity in IDENTITY_FIELDS.items()
    }
    _validate_institution_refs(records, ids)
    return records, ids


__all__ = ["require_subset", "validate_charter_base_references"]
