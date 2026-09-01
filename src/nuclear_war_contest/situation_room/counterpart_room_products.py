"""Collection of authored no-model counterpart group products."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .counterpart_compiled_models import CompiledCounterpartCharter
from .counterpart_room_product_semantics import counterpart_product_is_valid


def _failure(group_id: str, reason_code: str, effect: str) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{group_id}",
        "reason_code": reason_code,
        "group_id": group_id,
        "failure_effect": effect,
    }


def _attempt_base(
    group: dict[str, Any], compiled: CompiledCounterpartCharter
) -> dict[str, Any]:
    group_id = group["group_id"]
    return {
        "attempt_id": f"ATTEMPT::{group_id}",
        "group_id": group_id,
        "product_schema_id": group["product_schema_id"],
        "member_seat_ids": [seat.seat_id for seat in compiled.group_members(group_id)],
    }


def _failed_attempt(
    base: dict[str, Any], product: dict[str, Any] | None, reason: str, effect: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    attempt = {**base, "status": "failed"}
    if product is None:
        attempt["product_id"] = None
    else:
        attempt["product"] = deepcopy(product)
    return attempt, _failure(base["group_id"], reason, effect)


def _product_content(
    actor_id: str,
    group: dict[str, Any],
    schema: dict[str, Any],
    compiled: CompiledCounterpartCharter,
    product: dict[str, Any],
) -> dict[str, Any] | None:
    content = product.get("content")
    if product.get("product_schema_id") != group["product_schema_id"]:
        return None
    if not isinstance(content, dict):
        return None
    if not set(schema["required_fields"]) <= set(content):
        return None
    if not counterpart_product_is_valid(actor_id, group["group_id"], content, compiled):
        return None
    return content


def collect_counterpart_product(
    actor_id: str,
    group: dict[str, Any],
    schema: dict[str, Any],
    compiled: CompiledCounterpartCharter,
    product: dict[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    base = _attempt_base(group, compiled)
    if product is None:
        return _failed_attempt(base, None, "missing_product", group["failure_effect"])
    content = _product_content(actor_id, group, schema, compiled, product)
    if content is None:
        return _failed_attempt(
            base, product, "invalid_product", group["failure_effect"]
        )
    return (
        {
            **base,
            "status": "accepted",
            "product_id": product["product_id"],
            "content": deepcopy(content),
            "content_hash": canonical_hash(content),
        },
        None,
    )


__all__ = ["collect_counterpart_product"]
