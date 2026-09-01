"""Hash and content validation for screening sidecar artifacts."""

from __future__ import annotations

import hashlib
from pathlib import Path

from nuclear_war_env.llm_model_scorecard_catalog import load_catalog_rows

from .screening_budget_validation import validate_screening_budget
from .screening_types import ScreeningManifest


def validate_screening_artifacts(root: Path, manifest: ScreeningManifest) -> None:
    catalog = _check_hash(
        root, manifest.catalog_path, manifest.catalog_sha256, "catalog"
    )
    _check_hash(
        root,
        manifest.final_candidate_path,
        manifest.final_candidate_sha256,
        "final candidate",
    )
    budget = _check_hash(root, manifest.budget_path, manifest.budget_sha256, "budget")
    validate_screening_budget(budget, manifest)
    rows = load_catalog_rows(catalog)
    if [row.model_id for row in rows] != [
        model.provider_model for model in manifest.models
    ]:
        raise ValueError("Screening catalog model order does not match manifest")
    for row, model in zip(rows, manifest.models, strict=True):
        if (row.input_price, row.output_price) != (
            model.input_usd_per_million,
            model.output_usd_per_million,
        ):
            raise ValueError("Screening catalog rates do not match manifest")


def _check_hash(root: Path, relative: str, expected: str, label: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or len(expected) != 64:
        raise ValueError(f"Screening {label} path or hash is invalid")
    resolved = root / path
    actual = hashlib.sha256(resolved.read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError(f"Screening {label} hash does not match")
    return resolved


__all__ = ["validate_screening_artifacts"]
