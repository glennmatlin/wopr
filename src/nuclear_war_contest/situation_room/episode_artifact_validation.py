"""Artifact path and hash validation for two-cycle fixtures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

ARTIFACT_KEYS = frozenset(
    {
        "source_register",
        "charter",
        "ratification",
        "cycle1_fixture",
        "cycle1_receipt",
        "bridge_fixture",
        "bridge_receipt",
        "date_profile",
        "date_tracer_receipt",
        "cycle2_fixture",
    }
)


def validate_episode_artifacts(payload: dict[str, Any]) -> None:
    paths = payload.get("artifact_paths")
    hashes = payload.get("artifact_hashes")
    receipts = payload.get("upstream_receipt_hashes")
    if not isinstance(paths, dict) or set(paths) != ARTIFACT_KEYS:
        raise ValueError("invalid_envelope: artifact paths are invalid")
    if not isinstance(hashes, dict) or set(hashes) != ARTIFACT_KEYS:
        raise ValueError("invalid_envelope: artifact hashes are invalid")
    if not isinstance(receipts, dict) or set(receipts) != {"cycle1", "bridge", "date"}:
        raise ValueError("invalid_envelope: upstream receipt hashes are invalid")
    for key, value in paths.items():
        if not isinstance(value, str) or not value or Path(value).is_absolute():
            raise ValueError(f"invalid_path: artifact path {key} is invalid")
        if Path(value).name != value:
            raise ValueError(f"invalid_path: artifact path {key} escapes its root")
    values = [*hashes.values(), *receipts.values()]
    if any(not _is_hash(value) for value in values):
        raise ValueError("invalid_envelope: artifact hash is invalid")


def _is_hash(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


__all__ = ["ARTIFACT_KEYS", "validate_episode_artifacts"]
