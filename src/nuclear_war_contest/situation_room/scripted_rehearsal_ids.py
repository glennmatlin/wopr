"""Stable logical-call identities for scripted Room rehearsal."""

from __future__ import annotations


def portfolio_call_id(cycle_id: str, group_id: str, seat_id: str) -> str:
    return f"{cycle_id}::{group_id}::{seat_id}::portfolio"


def group_product_call_id(cycle_id: str, group_id: str, seat_id: str) -> str:
    return f"{cycle_id}::{group_id}::{seat_id}::group_product"


def confirmation_call_id(cycle_id: str, confirmation_id: str, seat_id: str) -> str:
    return f"{cycle_id}::{confirmation_id}::{seat_id}::confirmation"


__all__ = [
    "confirmation_call_id",
    "group_product_call_id",
    "portfolio_call_id",
]
