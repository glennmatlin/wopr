"""Reference closure for counterpart Room fixtures."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from .counterpart_artifacts import CounterpartCharter
from .counterpart_compiler import compile_counterpart_charter
from .validation import fail


def _require_unique(items: Iterable[dict[str, Any]], field: str) -> None:
    values = [item[field] for item in items]
    if len(values) != len(set(values)):
        fail("duplicate_id", f"counterpart fixture repeats {field}")


def _validate_inputs(payload: dict[str, Any], charter_payload: dict[str, Any]) -> None:
    permissions = {
        (item["information_class_id"], sender_id)
        for item in charter_payload["disclosure_permissions"]
        for sender_id in item["sender_ids"]
    }
    for item in payload["watch_inputs"]:
        key = (item["information_class_id"], item["sender_id"])
        if key not in permissions:
            fail("unknown_reference", "counterpart Watch input lacks permission")


def _validate_products(
    payload: dict[str, Any], charter_payload: dict[str, Any]
) -> None:
    groups = {item["group_id"]: item for item in charter_payload["groups"]}
    for item in payload["group_products"]:
        group = groups.get(item["group_id"])
        if group is None or item["product_schema_id"] != group["product_schema_id"]:
            fail("unknown_reference", "counterpart product has an unknown binding")


def _validate_confirmations(
    payload: dict[str, Any], charter_payload: dict[str, Any]
) -> None:
    specs = {
        item["confirmation_id"]: item
        for item in charter_payload["required_confirmations"]
    }
    product_ids = {item["product_id"] for item in payload["group_products"]}
    for item in payload["confirmations"]:
        spec = specs.get(item["confirmation_id"])
        if spec is None or not set(item["confirmer_seat_ids"]) <= set(
            spec["confirmer_seat_ids"]
        ):
            fail("unknown_reference", "counterpart confirmation binding is invalid")
        if item["confirmed_record_id"] not in product_ids:
            fail("unknown_reference", "counterpart confirmed record is unknown")


def _validate_action(payload: dict[str, Any], charter_payload: dict[str, Any]) -> None:
    runnable = {item["action_class"] for item in charter_payload["decision_routes"]}
    blocked = {
        item["action_class"] for item in charter_payload["blocked_action_classes"]
    }
    if payload["action_class"] not in runnable | blocked:
        fail("unknown_reference", "counterpart fixture action is unknown")


def _expected_projection(actor_id: str) -> tuple[str, str, str]:
    return {
        "ACTOR_HIMALDESH": (
            "room_decision",
            "decision_record_output_components",
            "HIM_OUTPUT_SUPPORT_REQUEST_001",
        ),
        "ACTOR_OLVANA": (
            "world_authored",
            "authored_world_projection",
            "OLV_OUTPUT_RIDGE_POSTURE_001",
        ),
    }[actor_id]


def _validate_output(payload: dict[str, Any]) -> None:
    product_ids = {item["product_id"] for item in payload["group_products"]}
    projection = payload["output_projection"]
    if projection["source_decision_record_id"] not in product_ids:
        fail("unknown_reference", "counterpart projection source is unknown")
    observed = (
        projection["projection_owner"],
        projection["mapping_type"],
        projection["output"]["output_id"],
    )
    if observed != _expected_projection(payload["actor_id"]):
        fail("output_mismatch", "counterpart output projection identity is invalid")


def validate_counterpart_room_fixture_references(
    payload: dict[str, Any], charter: CounterpartCharter
) -> None:
    charter_payload = charter.payload()
    _require_unique(payload["watch_inputs"], "input_id")
    _require_unique(payload["group_products"], "product_id")
    _require_unique(payload["group_products"], "group_id")
    _require_unique(payload["confirmations"], "confirmation_id")
    _validate_inputs(payload, charter_payload)
    _validate_products(payload, charter_payload)
    _validate_confirmations(payload, charter_payload)
    _validate_action(payload, charter_payload)
    _validate_output(payload)
    compiled = compile_counterpart_charter(charter)
    for item in payload["watch_inputs"]:
        if not compiled.recipients_for(item["information_class_id"], item["sender_id"]):
            fail("entitlement_leak", "counterpart Watch input has no recipient")


__all__ = ["validate_counterpart_room_fixture_references"]
