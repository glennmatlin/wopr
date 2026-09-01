"""Fail-closed loading for the offline three-model screening packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .screening_artifacts import validate_screening_artifacts
from .screening_builder import build_screening_manifest
from .screening_controls import validate_screening_manifest
from .screening_types import ScreeningManifest

_TOP_LEVEL = {
    "schema_version",
    "manifest_id",
    "selection_status",
    "full_design_model_selection",
    "source_revision",
    "catalog_path",
    "catalog_sha256",
    "budget_path",
    "budget_sha256",
    "final_candidate_path",
    "final_candidate_sha256",
    "screening_seeds",
    "study_seeds",
    "screening",
    "provider",
    "owner_total_cap_usd",
    "approval_status",
    "network_calls",
    "credentials_read",
    "models",
}
_SCREENING_FIELDS = {
    "mode",
    "players",
    "max_turns",
    "temperature",
    "max_tokens",
    "reasoning_enabled",
    "stream",
    "output_retries",
    "transport_retry_margin",
}
_PROVIDER_FIELDS = {"name", "base_url", "api_key_env"}


def load_screening_manifest_file(path: Path) -> ScreeningManifest:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return load_screening_manifest(payload, base_dir=path.parent)


def load_screening_manifest(
    payload: Any, *, base_dir: Path | None = None
) -> ScreeningManifest:
    _validate_shape(payload)
    screening = _section(payload["screening"], _SCREENING_FIELDS, "screening")
    provider = _section(payload["provider"], _PROVIDER_FIELDS, "provider")
    manifest = build_screening_manifest(payload, screening, provider)
    if len(manifest.screening_seeds) != 3 or len(manifest.study_seeds) != 5:
        raise ValueError("Screening and study seed counts are invalid")
    if set(manifest.screening_seeds) & set(manifest.study_seeds):
        raise ValueError("Screening and study seeds must be disjoint")
    validate_screening_artifacts(base_dir or Path.cwd(), manifest)
    validate_screening_manifest(manifest)
    return manifest


def _validate_shape(payload: Any) -> None:
    if not isinstance(payload, dict) or set(payload) != _TOP_LEVEL:
        raise ValueError("Screening manifest fields are invalid")
    if payload["schema_version"] != 1:
        raise ValueError("Screening manifest schema_version is invalid")


def _section(value: Any, fields: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"Screening {label} fields are invalid")
    return value


__all__ = ["load_screening_manifest", "load_screening_manifest_file"]
