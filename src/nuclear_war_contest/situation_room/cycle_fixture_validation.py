"""Strict no-model U.S. cycle fixture envelope validation."""

from __future__ import annotations

from typing import Any

from .charter import UsCharter

_FIXTURE_FIELDS = frozenset(
    {
        "schema_version",
        "fixture_id",
        "fixture_version",
        "status",
        "actor_id",
        "cycle_id",
        "ratification_id",
        "ratification_hash",
        "source_register_hash",
        "charter_hash",
        "action_class",
        "counterpart_fixtures",
        "watch_inputs",
        "group_products",
        "confirmations",
    }
)
_COUNTERPART_FIELDS = frozenset({"fixture_id", "actor_id", "status", "outputs"})
_OUTPUT_FIELDS = frozenset({"output_id", "content"})
_INPUT_FIELDS = frozenset(
    {
        "input_id",
        "information_class_id",
        "sender_id",
        "causal_parent_ids",
        "content",
    }
)
_PRODUCT_FIELDS = frozenset({"product_id", "group_id", "product_schema_id", "content"})
_CONFIRMATION_FIELDS = frozenset(
    {"confirmation_id", "confirmer_seat_ids", "confirmed_record_id", "status"}
)


def validate_cycle_fixture_shape(
    payload: dict[str, Any],
    charter: UsCharter,
    ratification: dict[str, Any],
    expected_cycle_id: str = "CYCLE_1",
) -> None:
    if set(payload) != _FIXTURE_FIELDS:
        raise ValueError("invalid_envelope: cycle fixture fields are invalid")
    charter_payload = charter.payload()
    fixed = {
        "schema_version": "us-cycle-fixture.v0.1",
        "status": "development_fixture_non_evidence",
        "actor_id": charter_payload["actor_id"],
        "cycle_id": expected_cycle_id,
        "ratification_id": ratification.get("ratification_id"),
    }
    if any(payload.get(key) != value for key, value in fixed.items()):
        raise ValueError("invalid_envelope: cycle fixture fixed fields are invalid")
    _require_nonempty_strings(
        payload, ("fixture_id", "fixture_version", "action_class")
    )
    for field in (
        "counterpart_fixtures",
        "watch_inputs",
        "group_products",
        "confirmations",
    ):
        if not isinstance(payload[field], list):
            raise ValueError(f"invalid_envelope: {field} must be a list")
    for item in payload["counterpart_fixtures"]:
        _require_record(item, _COUNTERPART_FIELDS, "counterpart fixture")
        _require_nonempty_strings(item, ("fixture_id", "actor_id", "status"))
        if not isinstance(item["outputs"], list) or not item["outputs"]:
            raise ValueError("invalid_envelope: counterpart outputs are invalid")
        for output in item["outputs"]:
            _require_record(output, _OUTPUT_FIELDS, "counterpart output")
            _require_nonempty_strings(output, ("output_id",))
            _require_content(output, "counterpart output")
    for item in payload["watch_inputs"]:
        _require_record(item, _INPUT_FIELDS, "Watch input")
        _require_nonempty_strings(
            item, ("input_id", "information_class_id", "sender_id")
        )
        if not isinstance(item["causal_parent_ids"], list) or not all(
            isinstance(value, str) and value for value in item["causal_parent_ids"]
        ):
            raise ValueError("invalid_envelope: Watch input parents are invalid")
        _require_content(item, "Watch input")
    for item in payload["group_products"]:
        _require_record(item, _PRODUCT_FIELDS, "group product")
        _require_nonempty_strings(item, ("product_id", "group_id", "product_schema_id"))
        _require_content(item, "group product")
    for item in payload["confirmations"]:
        _require_record(item, _CONFIRMATION_FIELDS, "confirmation")
        _require_nonempty_strings(
            item, ("confirmation_id", "confirmed_record_id", "status")
        )
        if not isinstance(item["confirmer_seat_ids"], list) or not all(
            isinstance(value, str) and value for value in item["confirmer_seat_ids"]
        ):
            raise ValueError("invalid_envelope: confirmation seats are invalid")


def _require_record(item: Any, fields: frozenset[str], label: str) -> None:
    if not isinstance(item, dict) or set(item) != fields:
        raise ValueError(f"invalid_envelope: {label} fields are invalid")


def _require_nonempty_strings(item: dict[str, Any], fields: tuple[str, ...]) -> None:
    if any(not isinstance(item[field], str) or not item[field] for field in fields):
        raise ValueError("invalid_envelope: cycle fixture string is invalid")


def _require_content(item: dict[str, Any], label: str) -> None:
    if not isinstance(item["content"], dict):
        raise ValueError(f"invalid_envelope: {label} content must be an object")


__all__ = ["validate_cycle_fixture_shape"]
