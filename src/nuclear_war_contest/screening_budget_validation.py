"""Validate the frozen screening budget artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .screening_budget_math import expected_bound, validate_model_bounds
from .screening_types import ScreeningManifest

_ASSUMPTION_FIELDS = {
    "screening_mode",
    "seeds_per_model",
    "calls_per_game",
    "calls_source",
    "input_tokens_per_request",
    "output_tokens_per_request",
    "output_retries",
    "transport_retry_margin",
}
_BOUND_FIELDS = {
    "models",
    "seeds_per_model",
    "calls_per_game",
    "retry_multiplier",
    "provider_request_attempts",
    "input_tokens",
    "output_tokens",
}
_TOP_LEVEL_FIELDS = {
    "schema_version",
    "manifest_id",
    "status",
    "authorization_status",
    "network_calls",
    "credentials_read",
    "assumptions",
    "request_bound",
    "model_bounds",
    "upper_bound_usd",
    "owner_total_cap_usd",
    "note",
}


def validate_screening_budget(path: Path, manifest: ScreeningManifest) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or set(payload) != _TOP_LEVEL_FIELDS:
        raise ValueError("Screening budget must be an object")
    if payload["schema_version"] != 1:
        raise ValueError("Screening budget schema_version is invalid")
    _validate_authorization(payload, manifest)
    assumptions = _section(payload.get("assumptions"), _ASSUMPTION_FIELDS)
    bound = _section(payload.get("request_bound"), _BOUND_FIELDS)
    _validate_assumptions(assumptions)
    expected = expected_bound(assumptions, len(manifest.models))
    if not all(_strict_int(bound[key]) for key in _BOUND_FIELDS):
        raise ValueError("Screening request bound contains invalid integers")
    if bound != expected:
        raise ValueError("Screening request bound does not recompute")
    validate_model_bounds(
        payload.get("model_bounds"),
        payload.get("upper_bound_usd"),
        manifest,
        expected,
    )


def _validate_authorization(
    payload: dict[str, Any], manifest: ScreeningManifest
) -> None:
    if (
        payload.get("manifest_id") != manifest.manifest_id
        or payload.get("status") != "planning_only"
        or payload.get("authorization_status") != "pending_owner"
        or payload.get("network_calls") != 0
        or payload.get("credentials_read") is not False
        or payload.get("owner_total_cap_usd") != manifest.owner_total_cap_usd
    ):
        raise ValueError("Screening budget authorization fields are invalid")


def _validate_assumptions(assumptions: dict[str, Any]) -> None:
    numeric_fields = (
        "seeds_per_model",
        "calls_per_game",
        "input_tokens_per_request",
        "output_tokens_per_request",
        "output_retries",
        "transport_retry_margin",
    )
    if not all(_strict_int(assumptions[field]) for field in numeric_fields):
        raise ValueError("Screening budget assumptions contain invalid integers")
    expected = {
        "screening_mode": "press_light",
        "seeds_per_model": 3,
        "calls_per_game": 624,
        "calls_source": "observed_c2_564_plus_observed_press_60",
        "input_tokens_per_request": 8192,
        "output_tokens_per_request": 512,
        "output_retries": 1,
        "transport_retry_margin": 2,
    }
    if assumptions != expected:
        raise ValueError("Screening budget assumptions are not frozen")


def _section(value: Any, fields: set[str]) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError("Screening budget section fields are invalid")
    return value


def _strict_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


__all__ = ["validate_screening_budget"]
