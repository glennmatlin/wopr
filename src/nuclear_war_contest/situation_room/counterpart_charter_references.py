"""Identity and graph-reference validation for counterpart Charters."""

from __future__ import annotations

from typing import Any

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
    "blocked_action_classes": "blocked_action_class_id",
    "evidence_labels": "evidence_label_id",
}


def counterpart_records(payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    registry = payload["institution_registry"]
    return {
        "seats": registry["seats"],
        "services": registry["services"],
        **{
            field: payload[field]
            for field in IDENTITY_FIELDS
            if field not in {"seats", "services"}
        },
    }


def require_subset(values: list[str], expected: set[str], label: str) -> None:
    if not set(values) <= expected:
        fail("unknown_reference", f"{label} has an unknown reference")


def _validate_global_ids(
    payload: dict[str, Any],
    records: dict[str, list[dict[str, Any]]],
    source: dict[str, Any],
) -> None:
    identities = list(payload["objective_ids"])
    for field, identity_field in IDENTITY_FIELDS.items():
        identities.extend(record[identity_field] for record in records[field])
    for field, identity_field in (
        ("sources", "source_id"),
        ("facts", "fact_id"),
        ("inferences", "inference_id"),
        ("gaps", "gap_id"),
    ):
        identities.extend(record[identity_field] for record in source[field])
    if len(identities) != len(set(identities)):
        fail("duplicate_id", "counterpart bundle identity namespace repeats")


def _validate_evidence(
    records: dict[str, list[dict[str, Any]]], source: dict[str, Any]
) -> None:
    fact_ids = {record["fact_id"] for record in source["facts"]}
    inference_ids = {record["inference_id"] for record in source["inferences"]}
    evidence_ids = fact_ids | inference_ids
    for items in records.values():
        for item in items:
            if "fact_ids" in item:
                require_subset(item["fact_ids"], fact_ids, "counterpart fact IDs")
            if "inference_ids" in item:
                require_subset(
                    item["inference_ids"], inference_ids, "counterpart inference IDs"
                )
            if "persona_posture_ids" in item:
                require_subset(
                    item["persona_posture_ids"],
                    evidence_ids,
                    "counterpart persona posture IDs",
                )


def _validate_objectives(payload: dict[str, Any], source: dict[str, Any]) -> None:
    supported = {
        scope_id
        for inference in source["inferences"]
        for scope_id in inference["scope_ids"]
    }
    require_subset(payload["objective_ids"], supported, "counterpart objectives")


def validate_counterpart_base_references(
    payload: dict[str, Any], source: dict[str, Any]
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, set[str]]]:
    records = counterpart_records(payload)
    _validate_global_ids(payload, records, source)
    _validate_evidence(records, source)
    _validate_objectives(payload, source)
    ids = {
        field: {record[identity] for record in records[field]}
        for field, identity in IDENTITY_FIELDS.items()
    }
    return records, ids


__all__ = ["require_subset", "validate_counterpart_base_references"]
