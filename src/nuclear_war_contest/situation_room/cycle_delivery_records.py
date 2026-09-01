"""Canonical delivery record construction."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash


def watch_delivery(item: dict[str, Any], seat_id: str) -> dict[str, Any]:
    return {
        "delivery_id": f"DELIVERY::{item['input_id']}::{seat_id}",
        "artifact_id": item["input_id"],
        "artifact_type": "watch_input",
        "input_id": item["input_id"],
        "information_class_id": item["information_class_id"],
        "sender_id": item["sender_id"],
        "recipient_seat_id": seat_id,
        "content_hash": canonical_hash(item["content"]),
        "causal_parent_ids": item["causal_parent_ids"],
    }


def product_delivery(
    product: dict[str, Any],
    information_class: str,
    sender_id: str,
    seat_id: str,
    parents: list[str],
) -> dict[str, Any]:
    product_id = product["product_id"]
    return {
        "delivery_id": f"DELIVERY::{product_id}::{seat_id}",
        "artifact_id": product_id,
        "artifact_type": "group_product",
        "product_id": product_id,
        "information_class_id": information_class,
        "sender_id": sender_id,
        "recipient_seat_id": seat_id,
        "content_hash": product["content_hash"],
        "causal_parent_ids": parents,
    }


__all__ = ["product_delivery", "watch_delivery"]
