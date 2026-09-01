"""Group, activation, information, and product validation."""

from __future__ import annotations

from typing import Any

from .validation import fail, require_text, require_text_list

GROUP_FIELDS = {
    "group_id",
    "purpose",
    "ordered_eligible_member_ids",
    "active_member_rule",
    "input_entitlement_ids",
    "dependency_group_ids",
    "shared_seat_barrier_ids",
    "activation_predicate_id",
    "product_schema_id",
    "collection_order",
    "failure_effect",
    "fact_ids",
    "inference_ids",
}
INFORMATION_FIELDS = {
    "information_class_id",
    "description",
    "sensitivity",
    "fact_ids",
    "inference_ids",
}
PREDICATE_FIELDS = {
    "activation_predicate_id",
    "predicate_type",
    "condition_ids",
    "first_episode_value",
    "description",
    "fact_ids",
    "inference_ids",
}
PRODUCT_FIELDS = {
    "product_schema_id",
    "product_type",
    "producing_group_ids",
    "required_fields",
    "preserves_dissent",
    "fact_ids",
    "inference_ids",
}
EVIDENCE_FIELDS = {"evidence_label_id", "label", "description"}
ACTIVE_MEMBER_RULES = {"all_activated", "activated_voting_and_advisers"}
SENSITIVITIES = {
    "common",
    "group_product",
    "seat_private",
    "underlying_retrieval",
    "world_ground_truth",
}
PREDICATE_TYPES = {"always", "all_of", "any_of", "episode_relevance", "request"}


def _validate_group(record: dict[str, Any]) -> None:
    if set(record) != GROUP_FIELDS:
        fail("invalid_envelope", "group fields are invalid")
    for field in (
        "group_id",
        "purpose",
        "activation_predicate_id",
        "product_schema_id",
        "failure_effect",
    ):
        require_text(record[field], f"group {field}")
    if record["active_member_rule"] not in ACTIVE_MEMBER_RULES:
        fail("invalid_envelope", "group active-member rule is invalid")
    for field in (
        "ordered_eligible_member_ids",
        "input_entitlement_ids",
        "dependency_group_ids",
        "shared_seat_barrier_ids",
        "fact_ids",
        "inference_ids",
    ):
        require_text_list(record[field], f"group {field}")
    order = record["collection_order"]
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        fail("invalid_envelope", "group collection order is invalid")


def _validate_information(record: dict[str, Any]) -> None:
    if set(record) != INFORMATION_FIELDS:
        fail("invalid_envelope", "information-class fields are invalid")
    require_text(record["information_class_id"], "information-class identity")
    require_text(record["description"], "information-class description")
    if record["sensitivity"] not in SENSITIVITIES:
        fail("invalid_envelope", "information-class sensitivity is invalid")
    require_text_list(record["fact_ids"], "information-class fact IDs")
    require_text_list(record["inference_ids"], "information-class inference IDs")


def _validate_predicate(record: dict[str, Any]) -> None:
    if set(record) != PREDICATE_FIELDS:
        fail("invalid_envelope", "activation-predicate fields are invalid")
    require_text(record["activation_predicate_id"], "activation identity")
    require_text(record["description"], "activation description")
    if record["predicate_type"] not in PREDICATE_TYPES:
        fail("activation_error", "activation predicate type is invalid")
    if not isinstance(record["first_episode_value"], bool):
        fail("activation_error", "first-episode activation value is invalid")
    for field in ("condition_ids", "fact_ids", "inference_ids"):
        require_text_list(record[field], f"activation {field}")


def _validate_product(record: dict[str, Any]) -> None:
    if set(record) != PRODUCT_FIELDS:
        fail("invalid_envelope", "product-schema fields are invalid")
    for field in ("product_schema_id", "product_type"):
        require_text(record[field], f"product {field}")
    for field in (
        "producing_group_ids",
        "required_fields",
        "fact_ids",
        "inference_ids",
    ):
        require_text_list(record[field], f"product {field}")
    if not isinstance(record["preserves_dissent"], bool):
        fail("invalid_envelope", "product dissent flag is invalid")


def validate_graph_records(payload: dict[str, Any]) -> None:
    for record in payload["groups"]:
        _validate_group(record)
    for record in payload["information_classes"]:
        _validate_information(record)
    for record in payload["activation_predicates"]:
        _validate_predicate(record)
    for record in payload["product_schemas"]:
        _validate_product(record)
    for record in payload["evidence_labels"]:
        if set(record) != EVIDENCE_FIELDS:
            fail("invalid_envelope", "evidence-label fields are invalid")
        for field in EVIDENCE_FIELDS:
            require_text(record[field], f"evidence-label {field}")


__all__ = ["validate_graph_records"]
