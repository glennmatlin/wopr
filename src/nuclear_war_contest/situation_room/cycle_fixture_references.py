"""No-model U.S. cycle fixture identity and reference validation."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from .charter import UsCharter
from .compiler import compile_us_charter


def validate_cycle_fixture_references(
    payload: dict[str, Any],
    charter: UsCharter,
    external_parent_ids: frozenset[str] = frozenset(),
) -> None:
    charter_payload = charter.payload()
    outputs = [
        output
        for fixture in payload["counterpart_fixtures"]
        for output in fixture["outputs"]
    ]
    _require_unique(payload["counterpart_fixtures"], "fixture_id")
    _require_unique(outputs, "output_id")
    _require_unique(payload["watch_inputs"], "input_id")
    _require_unique(payload["group_products"], "product_id")
    _require_unique(payload["group_products"], "group_id")
    _require_unique(payload["confirmations"], "confirmation_id")
    actor_ids = {item["actor_id"] for item in payload["counterpart_fixtures"]}
    if actor_ids != {"ACTOR_HIMALDESH", "ACTOR_OLVANA"}:
        raise ValueError("unknown_reference: counterpart actor set is invalid")
    if any(
        item["status"] != "development_fixture_non_evidence"
        for item in payload["counterpart_fixtures"]
    ):
        raise ValueError("invalid_envelope: counterpart fixture status is invalid")
    output_ids = {item["output_id"] for item in outputs}
    information_ids = {
        item["information_class_id"] for item in charter_payload["information_classes"]
    }
    permission_keys = {
        (item["information_class_id"], sender_id)
        for item in charter_payload["disclosure_permissions"]
        for sender_id in item["sender_ids"]
    }
    for item in payload["watch_inputs"]:
        if item["information_class_id"] not in information_ids:
            raise ValueError("unknown_reference: Watch information class is unknown")
        permission_key = (item["information_class_id"], item["sender_id"])
        if permission_key not in permission_keys:
            raise ValueError("unknown_reference: Watch permission is unknown")
        if not set(item["causal_parent_ids"]) <= (output_ids | external_parent_ids):
            raise ValueError("unknown_reference: Watch causal parent is unknown")
    active_group_ids = set(compile_us_charter(charter).active_group_ids())
    schema_ids = {
        item["product_schema_id"] for item in charter_payload["product_schemas"]
    }
    for item in payload["group_products"]:
        if item["group_id"] not in active_group_ids:
            raise ValueError("unknown_reference: product group is not active")
        if item["product_schema_id"] not in schema_ids:
            raise ValueError("unknown_reference: product schema is unknown")
    product_ids = {item["product_id"] for item in payload["group_products"]}
    confirmation_ids = {
        item["confirmation_id"] for item in charter_payload["required_confirmations"]
    }
    seat_ids = {
        item["seat_id"] for item in charter_payload["institution_registry"]["seats"]
    }
    for item in payload["confirmations"]:
        if item["confirmation_id"] not in confirmation_ids:
            raise ValueError("unknown_reference: confirmation is unknown")
        if not set(item["confirmer_seat_ids"]) <= seat_ids:
            raise ValueError("unknown_reference: confirmation seat is unknown")
        if item["confirmed_record_id"] not in product_ids:
            raise ValueError("unknown_reference: confirmed record is unknown")
    route_classes = {
        item["action_class"] for item in charter_payload["decision_routes"]
    }
    if payload["action_class"] not in route_classes:
        raise ValueError("unknown_reference: action class is unknown")


def _require_unique(items: Iterable[dict[str, Any]], field: str) -> None:
    values = [item[field] for item in items]
    if len(values) != len(set(values)):
        raise ValueError(f"duplicate_id: duplicate cycle fixture {field}")


__all__ = ["validate_cycle_fixture_references"]
