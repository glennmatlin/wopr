"""Construction helpers for the validated screening manifest."""

from __future__ import annotations

from typing import Any

from .preflight_scalars import nonnegative_int, positive_int, rate, seeds, text
from .screening_types import ScreeningManifest
from .screening_validation import load_screening_models


def build_screening_manifest(
    payload: dict[str, Any],
    screening: dict[str, Any],
    provider: dict[str, Any],
) -> ScreeningManifest:
    values = _identity_values(payload)
    values.update(_artifact_values(payload))
    values.update(_control_values(screening))
    values.update(_provider_values(payload, provider))
    values["models"] = load_screening_models(payload["models"], provider, screening)
    return ScreeningManifest(**values)


def _identity_values(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_id": text(payload["manifest_id"], "manifest_id"),
        "source_revision": text(payload["source_revision"], "source_revision"),
        "selection_status": text(payload["selection_status"], "selection_status"),
        "full_design_model_selection": text(
            payload["full_design_model_selection"], "full_design_model_selection"
        ),
        "screening_seeds": seeds(payload["screening_seeds"], "screening_seeds"),
        "study_seeds": seeds(payload["study_seeds"], "study_seeds"),
    }


def _artifact_values(payload: dict[str, Any]) -> dict[str, str]:
    return {
        "catalog_path": text(payload["catalog_path"], "catalog_path"),
        "catalog_sha256": text(payload["catalog_sha256"], "catalog_sha256"),
        "budget_path": text(payload["budget_path"], "budget_path"),
        "budget_sha256": text(payload["budget_sha256"], "budget_sha256"),
        "final_candidate_path": text(
            payload["final_candidate_path"], "final_candidate_path"
        ),
        "final_candidate_sha256": text(
            payload["final_candidate_sha256"], "final_candidate_sha256"
        ),
    }


def _control_values(screening: dict[str, Any]) -> dict[str, Any]:
    return {
        "mode": text(screening["mode"], "screening mode"),
        "players": positive_int(screening["players"], "players"),
        "max_turns": positive_int(screening["max_turns"], "max_turns"),
        "temperature": rate(screening["temperature"], "temperature"),
        "max_tokens": positive_int(screening["max_tokens"], "max_tokens"),
        "reasoning_enabled": _bool(screening["reasoning_enabled"], "reasoning_enabled"),
        "stream": _bool(screening["stream"], "stream"),
        "output_retries": nonnegative_int(
            screening["output_retries"], "output_retries"
        ),
        "transport_retry_margin": nonnegative_int(
            screening["transport_retry_margin"], "transport_retry_margin"
        ),
    }


def _provider_values(
    payload: dict[str, Any], provider: dict[str, Any]
) -> dict[str, Any]:
    return {
        "provider_name": text(provider["name"], "provider name"),
        "base_url": text(provider["base_url"], "provider base_url"),
        "api_key_env": text(provider["api_key_env"], "provider api_key_env"),
        "owner_total_cap_usd": rate(
            payload["owner_total_cap_usd"], "owner_total_cap_usd"
        ),
        "approval_status": text(payload["approval_status"], "approval_status"),
        "network_calls": nonnegative_int(payload["network_calls"], "network_calls"),
        "credentials_read": _bool(payload["credentials_read"], "credentials_read"),
    }


def _bool(value: Any, field: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"Screening {field} must be boolean")
    return value


__all__ = ["build_screening_manifest"]
