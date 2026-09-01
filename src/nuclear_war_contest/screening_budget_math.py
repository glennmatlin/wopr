"""Deterministic arithmetic for the screening spend bound."""

from __future__ import annotations

from decimal import Decimal
from typing import Any

from .preflight_scalars import rate
from .screening_types import ScreeningManifest

_MODEL_BOUND_FIELDS = {
    "provider_model",
    "input_usd_per_million",
    "output_usd_per_million",
    "cost_usd",
}


def expected_bound(assumptions: dict[str, Any], model_count: int) -> dict[str, int]:
    retry_multiplier = (1 + assumptions["output_retries"]) * (
        1 + assumptions["transport_retry_margin"]
    )
    attempts = (
        model_count
        * assumptions["seeds_per_model"]
        * assumptions["calls_per_game"]
        * retry_multiplier
    )
    return {
        "models": model_count,
        "seeds_per_model": assumptions["seeds_per_model"],
        "calls_per_game": assumptions["calls_per_game"],
        "retry_multiplier": retry_multiplier,
        "provider_request_attempts": attempts,
        "input_tokens": attempts * assumptions["input_tokens_per_request"],
        "output_tokens": attempts * assumptions["output_tokens_per_request"],
    }


def validate_model_bounds(
    value: Any,
    upper_value: Any,
    manifest: ScreeningManifest,
    bound: dict[str, int],
) -> None:
    if not isinstance(value, list) or len(value) != len(manifest.models):
        raise ValueError("Screening model bounds are invalid")
    attempts = bound["provider_request_attempts"] // len(manifest.models)
    total = Decimal("0")
    for item, model in zip(value, manifest.models, strict=True):
        if not isinstance(item, dict) or set(item) != _MODEL_BOUND_FIELDS:
            raise ValueError("Screening model bound fields are invalid")
        if item["provider_model"] != model.provider_model:
            raise ValueError("Screening model bound ids do not match")
        expected = _cost(
            item,
            model.input_usd_per_million,
            model.output_usd_per_million,
            attempts,
        )
        if _decimal_rate(item["cost_usd"], "model cost") != expected:
            raise ValueError("Screening model cost does not recompute")
        total += expected
    upper = _decimal_rate(upper_value, "upper bound")
    if upper != total:
        raise ValueError("Screening budget upper bound does not recompute")
    if upper > Decimal(str(manifest.owner_total_cap_usd)):
        raise ValueError("Screening budget upper bound exceeds owner cap")


def _cost(
    item: dict[str, Any], input_rate: float, output_rate: float, attempts: int
) -> Decimal:
    if _decimal_rate(item["input_usd_per_million"], "input rate") != _decimal_rate(
        input_rate, "manifest input rate"
    ):
        raise ValueError("Screening budget input rate does not match manifest")
    if _decimal_rate(item["output_usd_per_million"], "output rate") != _decimal_rate(
        output_rate, "manifest output rate"
    ):
        raise ValueError("Screening budget output rate does not match manifest")
    value = (
        Decimal(attempts * 8192) * _decimal_rate(input_rate, "input rate")
        + Decimal(attempts * 512) * _decimal_rate(output_rate, "output rate")
    ) / Decimal(1_000_000)
    return value.quantize(Decimal("0.000001"))


def _decimal_rate(value: Any, field: str) -> Decimal:
    return Decimal(str(rate(value, field)))


__all__ = ["expected_bound", "validate_model_bounds"]
