"""Strict JSON parsing for free-output Room products."""

from __future__ import annotations

import json
from typing import Any


def parse_product(raw_response: str) -> dict[str, Any]:
    product = json.loads(
        raw_response,
        object_pairs_hook=_reject_duplicate_keys,
        parse_constant=_reject_constant,
    )
    if not isinstance(product, dict):
        raise ValueError("Free-output Room product must be a JSON object")
    return product


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    product: dict[str, Any] = {}
    for key, value in pairs:
        if key in product:
            raise ValueError(f"Duplicate JSON key: {key}")
        product[key] = value
    return product


def _reject_constant(value: str) -> None:
    raise ValueError(f"Non-finite JSON value: {value}")


__all__ = ["parse_product"]
