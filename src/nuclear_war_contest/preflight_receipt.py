"""Receipt generation for the offline contest model preflight."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from .preflight_budget import build_budget
from .preflight_types import CandidateManifest, candidate_payload


def build_preflight_receipt(manifest: CandidateManifest) -> dict[str, Any]:
    budget = build_budget(manifest)
    if budget["upper_bound_usd"] > manifest.proposed_max_cost_usd:
        raise ValueError("Candidate proposed cost cap is below the envelope")
    return {
        "status": "pending_owner",
        "approval_status": "pending_owner",
        "manifest_id": manifest.manifest_id,
        "source_revision": manifest.source_revision,
        "offline_fixture_measurement": {
            "path": manifest.fixture_measurement_path,
            "source_manifest_hash": manifest.fixture_measurement_manifest_hash,
            "artifact_sha256": manifest.fixture_measurement_artifact_hash,
        },
        "candidate_manifest_hash": candidate_manifest_hash(manifest),
        "preflight_seeds": list(manifest.preflight_seeds),
        "study_seeds": list(manifest.study_seeds),
        "network_calls": 0,
        "credentials_read": False,
        "study": {
            "condition_count": manifest.condition_count,
            "seeds_per_condition": manifest.seeds_per_condition,
            "games": budget["study_games"],
        },
        "request_bound": budget,
        "cost_bound": {
            "upper_bound_usd": budget["upper_bound_usd"],
            "proposed_max_cost_usd": manifest.proposed_max_cost_usd,
        },
        "offline_fixture": {
            "observed_c2_calls_per_game": manifest.observed_c2_calls_per_game,
            "observed_press_calls_per_game": manifest.observed_press_calls_per_game,
            "operational_cap_c2_calls_per_game": manifest.max_c2_calls_per_game,
            "operational_cap_press_calls_per_game": manifest.max_press_calls_per_game,
        },
    }


def candidate_manifest_hash(manifest: CandidateManifest) -> str:
    encoded = json.dumps(
        candidate_payload(manifest), sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


__all__ = ["build_preflight_receipt", "candidate_manifest_hash"]
