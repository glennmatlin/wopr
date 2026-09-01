"""Fail-closed, no-network model selection preflight for the contest study."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .preflight_budget import enforce_channel_caps
from .preflight_measurement import validate_fixture_measurement
from .preflight_receipt import build_preflight_receipt, candidate_manifest_hash
from .preflight_scalars import nonnegative_int, positive_int, rate, seeds, text
from .preflight_types import CandidateManifest
from .preflight_validation import (
    load_models,
    validate_manifest,
)

_TOP_LEVEL = {
    "schema_version",
    "manifest_id",
    "source_revision",
    "offline_fixture_measurement",
    "preflight_seeds",
    "study_seeds",
    "study_design",
    "retry_policy",
    "request_budget",
    "offline_fixture",
    "models",
}


def load_candidate_manifest(
    payload: Any, *, base_dir: Path | None = None
) -> CandidateManifest:
    if not isinstance(payload, dict) or set(payload) != _TOP_LEVEL:
        raise ValueError("Candidate manifest fields are invalid")
    if payload["schema_version"] != 1:
        raise ValueError("Candidate manifest schema_version is invalid")
    design = _section(
        payload["study_design"],
        "study_design",
        {"condition_count", "seeds_per_condition"},
    )
    retry = _section(
        payload["retry_policy"],
        "retry_policy",
        {"output_retries", "transport_retry_margin"},
    )
    budget = _section(
        payload["request_budget"],
        "request_budget",
        {"max_tokens", "input_tokens_bound", "proposed_max_cost_usd"},
    )
    fixture = _section(
        payload["offline_fixture"],
        "offline_fixture",
        {
            "observed_c2_calls_per_game",
            "observed_press_calls_per_game",
            "max_c2_calls_per_game",
            "max_press_calls_per_game",
        },
    )
    measurement = _section(
        payload["offline_fixture_measurement"],
        "offline_fixture_measurement",
        {"path", "source_manifest_hash", "artifact_sha256"},
    )
    manifest = CandidateManifest(
        manifest_id=text(payload["manifest_id"], "manifest_id"),
        source_revision=text(payload["source_revision"], "source_revision"),
        fixture_measurement_path=text(measurement["path"], "measurement path"),
        fixture_measurement_manifest_hash=text(
            measurement["source_manifest_hash"], "measurement source hash"
        ),
        fixture_measurement_artifact_hash=text(
            measurement["artifact_sha256"], "measurement artifact hash"
        ),
        preflight_seeds=seeds(payload["preflight_seeds"], "preflight_seeds"),
        study_seeds=seeds(payload["study_seeds"], "study_seeds"),
        condition_count=positive_int(design["condition_count"], "condition_count"),
        seeds_per_condition=positive_int(
            design["seeds_per_condition"], "seeds_per_condition"
        ),
        output_retries=nonnegative_int(retry["output_retries"], "output_retries"),
        transport_retry_margin=nonnegative_int(
            retry["transport_retry_margin"], "transport_retry_margin"
        ),
        max_tokens=positive_int(budget["max_tokens"], "max_tokens"),
        input_tokens_bound=positive_int(
            budget["input_tokens_bound"], "input_tokens_bound"
        ),
        proposed_max_cost_usd=rate(
            budget["proposed_max_cost_usd"], "proposed_max_cost_usd"
        ),
        observed_c2_calls_per_game=positive_int(
            fixture["observed_c2_calls_per_game"], "observed_c2_calls_per_game"
        ),
        observed_press_calls_per_game=nonnegative_int(
            fixture["observed_press_calls_per_game"],
            "observed_press_calls_per_game",
        ),
        max_c2_calls_per_game=positive_int(
            fixture["max_c2_calls_per_game"], "max_c2_calls_per_game"
        ),
        max_press_calls_per_game=nonnegative_int(
            fixture["max_press_calls_per_game"], "max_press_calls_per_game"
        ),
        models=load_models(payload["models"]),
    )
    validate_manifest(manifest)
    validate_fixture_measurement(manifest, base_dir=base_dir)
    return manifest


def _section(value: Any, field: str, fields: set[str]) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"Candidate {field} fields are invalid")
    return value


__all__ = [
    "build_preflight_receipt",
    "candidate_manifest_hash",
    "enforce_channel_caps",
    "load_candidate_manifest",
]
