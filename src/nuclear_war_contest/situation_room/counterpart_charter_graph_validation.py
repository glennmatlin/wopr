"""Graph-record validation for counterpart Room Charters."""

from __future__ import annotations

from typing import Any

from .counterpart_record_validation import validate_record

GROUP_TEXT = {
    "group_id",
    "purpose",
    "activation_predicate_id",
    "product_schema_id",
    "failure_effect",
}
GROUP_LISTS = {
    "ordered_eligible_member_ids",
    "input_entitlement_ids",
    "dependency_group_ids",
    "shared_seat_barrier_ids",
    "fact_ids",
    "inference_ids",
}
INFORMATION_TEXT = {"information_class_id", "description"}
EVIDENCE_TEXT = {"evidence_label_id", "label", "description"}
PREDICATE_TEXT = {"activation_predicate_id", "description"}
PREDICATE_LISTS = {"condition_ids", "fact_ids", "inference_ids"}
PRODUCT_TEXT = {"product_schema_id", "product_type"}
PRODUCT_LISTS = {
    "producing_group_ids",
    "required_fields",
    "fact_ids",
    "inference_ids",
}


def _validate_group(group: dict[str, Any]) -> None:
    validate_record(
        group,
        "counterpart group",
        text_fields=GROUP_TEXT,
        list_fields=GROUP_LISTS,
        integer_fields={"collection_order"},
    )


def _validate_information(information: dict[str, Any]) -> None:
    validate_record(
        information,
        "counterpart information class",
        text_fields=INFORMATION_TEXT,
        list_fields={"fact_ids", "inference_ids"},
        choice_fields={
            "sensitivity": {
                "common",
                "group_product",
                "seat_private",
                "world_ground_truth",
            }
        },
    )


def _validate_predicate(predicate: dict[str, Any]) -> None:
    validate_record(
        predicate,
        "counterpart activation predicate",
        text_fields=PREDICATE_TEXT,
        list_fields=PREDICATE_LISTS,
        choice_fields={"predicate_type": {"always", "episode_relevance"}},
        boolean_fields={"first_episode_value"},
    )


def _validate_product(product: dict[str, Any]) -> None:
    validate_record(
        product,
        "counterpart product schema",
        text_fields=PRODUCT_TEXT,
        list_fields=PRODUCT_LISTS,
        boolean_fields={"preserves_dissent"},
    )


def _validate_evidence(evidence: dict[str, Any]) -> None:
    validate_record(
        evidence,
        "counterpart evidence label",
        text_fields=EVIDENCE_TEXT,
        list_fields=set(),
    )


def validate_counterpart_graph_records(payload: dict[str, Any]) -> None:
    for field, validator in (
        ("groups", _validate_group),
        ("information_classes", _validate_information),
        ("activation_predicates", _validate_predicate),
        ("product_schemas", _validate_product),
        ("evidence_labels", _validate_evidence),
    ):
        for record in payload[field]:
            validator(record)


__all__ = ["validate_counterpart_graph_records"]
