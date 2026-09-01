"""Strict envelope validation for counterpart Room fixtures."""

from __future__ import annotations

from typing import Any

from .validation import (
    fail,
    reject_officeholder_fields,
    require_records,
    require_text,
    require_text_list,
)

FIXTURE_FIELDS = {
    "schema_version",
    "fixture_id",
    "fixture_version",
    "status",
    "actor_id",
    "ratification_id",
    "ratification_hash",
    "source_register_hash",
    "charter_hash",
    "action_class",
    "watch_inputs",
    "group_products",
    "confirmations",
    "output_projection",
}
INPUT_FIELDS = {"input_id", "information_class_id", "sender_id", "content"}
PRODUCT_FIELDS = {"product_id", "group_id", "product_schema_id", "content"}
CONFIRMATION_FIELDS = {
    "confirmation_id",
    "confirmer_seat_ids",
    "confirmed_record_id",
    "status",
}
PROJECTION_FIELDS = {
    "projection_id",
    "projection_owner",
    "mapping_type",
    "source_decision_record_id",
    "output",
}


def _require_content(record: dict[str, Any], label: str) -> None:
    if not isinstance(record.get("content"), dict):
        fail("invalid_envelope", f"{label} content must be an object")


def _validate_header(payload: dict[str, Any]) -> None:
    reject_officeholder_fields(payload)
    if set(payload) != FIXTURE_FIELDS:
        fail("invalid_envelope", "counterpart Room fixture fields are invalid")
    fixed = {
        "schema_version": "counterpart-room-fixture.v0.1",
        "status": "development_fixture_non_evidence",
    }
    if any(payload.get(field) != value for field, value in fixed.items()):
        fail("invalid_envelope", "counterpart Room fixture fixed fields are invalid")
    for field in FIXTURE_FIELDS - {
        "watch_inputs",
        "group_products",
        "confirmations",
        "output_projection",
    }:
        require_text(payload.get(field), f"counterpart Room fixture {field}")


def _validate_input(item: dict[str, Any]) -> None:
    if set(item) != INPUT_FIELDS:
        fail("invalid_envelope", "counterpart Watch input fields are invalid")
    for field in INPUT_FIELDS - {"content"}:
        require_text(item[field], f"counterpart Watch input {field}")
    _require_content(item, "counterpart Watch input")


def _validate_product(item: dict[str, Any]) -> None:
    if set(item) != PRODUCT_FIELDS:
        fail("invalid_envelope", "counterpart product fields are invalid")
    for field in PRODUCT_FIELDS - {"content"}:
        require_text(item[field], f"counterpart product {field}")
    _require_content(item, "counterpart product")


def _validate_confirmation(item: dict[str, Any]) -> None:
    if set(item) != CONFIRMATION_FIELDS:
        fail("invalid_envelope", "counterpart confirmation fields are invalid")
    for field in CONFIRMATION_FIELDS - {"confirmer_seat_ids"}:
        require_text(item[field], f"counterpart confirmation {field}")
    require_text_list(item["confirmer_seat_ids"], "counterpart confirmation seats")


def _validate_projection(projection: object) -> None:
    if not isinstance(projection, dict) or set(projection) != PROJECTION_FIELDS:
        fail("invalid_envelope", "counterpart output projection is invalid")
    for field in PROJECTION_FIELDS - {"output"}:
        require_text(projection[field], f"counterpart projection {field}")
    output = projection["output"]
    if not isinstance(output, dict) or set(output) != {"output_id", "content"}:
        fail("invalid_envelope", "counterpart projected output is invalid")
    require_text(output["output_id"], "counterpart output identity")
    _require_content(output, "counterpart projected output")


def validate_counterpart_room_fixture_shape(payload: dict[str, Any]) -> None:
    _validate_header(payload)
    inputs = require_records(payload, "watch_inputs")
    products = require_records(payload, "group_products")
    confirmations = require_records(payload, "confirmations")
    if not inputs or not products:
        fail("invalid_envelope", "counterpart Room fixture is incomplete")
    for item in inputs:
        _validate_input(item)
    for item in products:
        _validate_product(item)
    for item in confirmations:
        _validate_confirmation(item)
    _validate_projection(payload.get("output_projection"))


__all__ = ["validate_counterpart_room_fixture_shape"]
