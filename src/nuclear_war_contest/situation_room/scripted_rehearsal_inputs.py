"""Seat-bound delivery bytes for scripted Room calls."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .cycle_fixture import UsCycleFixture


def initial_content_catalog(fixture: UsCycleFixture) -> dict[str, dict[str, Any]]:
    return {
        item["input_id"]: deepcopy(item["content"])
        for item in fixture.payload()["watch_inputs"]
    }


def add_product_content(
    catalog: dict[str, dict[str, Any]], product: dict[str, Any]
) -> None:
    catalog[product["product_id"]] = deepcopy(product)


def authorized_delivery_bytes(
    group: dict[str, Any],
    seat_id: str,
    deliveries: list[dict[str, Any]],
    catalog: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], ...]:
    allowed = set(group["input_entitlement_ids"])
    return tuple(
        {
            "delivery": deepcopy(item),
            "content": deepcopy(catalog[item["artifact_id"]]),
        }
        for item in deliveries
        if item["recipient_seat_id"] == seat_id
        and item["information_class_id"] in allowed
    )


__all__ = [
    "add_product_content",
    "authorized_delivery_bytes",
    "initial_content_catalog",
]
