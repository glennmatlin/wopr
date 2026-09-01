"""No-model group product collection and validation."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .compiled_models import CompiledUsCharter
from .cycle_policy import policy_package_is_complete


def collect_product_attempt(
    group_id: str,
    group: dict[str, Any],
    schema: dict[str, Any],
    compiled: CompiledUsCharter,
    product: dict[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    schema_id = group["product_schema_id"]
    base = {
        "attempt_id": f"ATTEMPT::{group_id}",
        "group_id": group_id,
        "product_schema_id": schema_id,
        "member_seat_ids": [seat.seat_id for seat in compiled.group_members(group_id)],
    }
    if product is None:
        return {**base, "status": "failed", "product_id": None}, _failure(
            group_id, "missing_product"
        )
    content = product.get("content")
    if product.get("product_schema_id") != schema_id or not isinstance(content, dict):
        attempt = {**base, "status": "failed", "product": deepcopy(product)}
        return attempt, _failure(group_id, "invalid_product")
    if not set(schema["required_fields"]) <= set(content):
        attempt = {**base, "status": "failed", "product": deepcopy(product)}
        return attempt, _failure(group_id, "invalid_product")
    if group_id == "GROUP_PC" and not policy_package_is_complete(content, compiled):
        attempt = {**base, "status": "failed", "product": deepcopy(product)}
        return attempt, _failure(group_id, "invalid_policy_package")
    attempt = {
        **base,
        "status": "accepted",
        "product_id": product["product_id"],
        "content": deepcopy(content),
        "content_hash": canonical_hash(content),
    }
    return attempt, None


def _failure(group_id: str, reason_code: str) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{group_id}",
        "reason_code": reason_code,
        "group_id": group_id,
    }


__all__ = ["collect_product_attempt"]
