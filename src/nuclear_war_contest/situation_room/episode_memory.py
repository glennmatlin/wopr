"""Deterministic per-seat delivery history across two cycles."""

from __future__ import annotations

from typing import Any


def build_seat_memory(
    cycle1: dict[str, Any], cycle2: dict[str, Any]
) -> dict[str, dict[str, list[str]]]:
    active = cycle1["active_seat_ids"]
    if cycle2["active_seat_ids"] != active:
        raise ValueError("seat_identity_mismatch")
    return {
        seat_id: {
            "cycle_1_delivery_ids": _deliveries(cycle1, seat_id),
            "cycle_2_delivery_ids": _deliveries(cycle2, seat_id),
        }
        for seat_id in active
    }


def _deliveries(receipt: dict[str, Any], seat_id: str) -> list[str]:
    return [
        item["delivery_id"]
        for item in receipt["deliveries"]
        if item["recipient_seat_id"] == seat_id
    ]


__all__ = ["build_seat_memory"]
