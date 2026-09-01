"""Typed values for the offline contest model preflight."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class CandidateModel:
    model_id: str
    model_family: str
    backend: str
    provider: str
    client: dict[str, Any]
    max_retries: int
    role_prompt_hashes: dict[str, str]
    input_usd_per_million: float
    output_usd_per_million: float


@dataclass(frozen=True)
class CandidateManifest:
    manifest_id: str
    source_revision: str
    fixture_measurement_path: str
    fixture_measurement_manifest_hash: str
    fixture_measurement_artifact_hash: str
    preflight_seeds: tuple[int, ...]
    study_seeds: tuple[int, ...]
    condition_count: int
    seeds_per_condition: int
    output_retries: int
    transport_retry_margin: int
    max_tokens: int
    input_tokens_bound: int
    proposed_max_cost_usd: float
    observed_c2_calls_per_game: int
    observed_press_calls_per_game: int
    max_c2_calls_per_game: int
    max_press_calls_per_game: int
    models: tuple[CandidateModel, ...]


def candidate_payload(manifest: CandidateManifest) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "manifest_id": manifest.manifest_id,
        "source_revision": manifest.source_revision,
        "offline_fixture_measurement": {
            "path": manifest.fixture_measurement_path,
            "source_manifest_hash": manifest.fixture_measurement_manifest_hash,
            "artifact_sha256": manifest.fixture_measurement_artifact_hash,
        },
        "preflight_seeds": list(manifest.preflight_seeds),
        "study_seeds": list(manifest.study_seeds),
        "study_design": {
            "condition_count": manifest.condition_count,
            "seeds_per_condition": manifest.seeds_per_condition,
        },
        "retry_policy": {
            "output_retries": manifest.output_retries,
            "transport_retry_margin": manifest.transport_retry_margin,
        },
        "request_budget": {
            "max_tokens": manifest.max_tokens,
            "input_tokens_bound": manifest.input_tokens_bound,
            "proposed_max_cost_usd": manifest.proposed_max_cost_usd,
        },
        "offline_fixture": {
            "observed_c2_calls_per_game": manifest.observed_c2_calls_per_game,
            "observed_press_calls_per_game": manifest.observed_press_calls_per_game,
            "max_c2_calls_per_game": manifest.max_c2_calls_per_game,
            "max_press_calls_per_game": manifest.max_press_calls_per_game,
        },
        "models": [model.__dict__ for model in manifest.models],
    }


__all__ = ["CandidateManifest", "CandidateModel", "candidate_payload"]
