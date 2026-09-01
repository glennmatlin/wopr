"""Tests for the deterministic post-screen model-selection report."""

from __future__ import annotations

import json
from pathlib import Path

from nuclear_war_contest.screening_manifest import load_screening_manifest_file
from nuclear_war_contest.screening_selection import build_screening_selection

MANIFEST = (
    Path(__file__).parents[2] / "docs" / "contest" / "MODEL_SCREENING.candidate.json"
)


def test_selection_ranks_only_operational_metrics() -> None:
    manifest = load_screening_manifest_file(MANIFEST)
    rows = [
        _row(model.model_id, reprompts=index, retries=index, cost=0.1 + index)
        for index, model in enumerate(manifest.models)
        for _ in manifest.screening_seeds
    ]

    selection = build_screening_selection(manifest, rows)

    assert selection["selection_status"] == "ready"
    assert selection["all_three_eligible"] is True
    assert selection["ranked_model_ids"] == [
        manifest.models[0].model_id,
        manifest.models[1].model_id,
        manifest.models[2].model_id,
    ]
    assert selection["retained_model_ids"] == selection["ranked_model_ids"][:2]


def test_selection_excludes_tier_c_model() -> None:
    manifest = load_screening_manifest_file(MANIFEST)
    rows = [
        _row(model.model_id, reprompts=0, retries=0, cost=0.1)
        for model in manifest.models
        for _ in manifest.screening_seeds
    ]
    rows[1]["admissibility"]["tier"] = "C"

    selection = build_screening_selection(manifest, rows)

    excluded = selection["models"][0]
    assert excluded["eligible"] is False
    assert "tier_c_attempt" in excluded["reasons"]
    assert len(selection["eligible_model_ids"]) == 2
    assert selection["selection_status"] == "ready"


def test_selection_requires_operational_metrics() -> None:
    manifest = load_screening_manifest_file(MANIFEST)
    rows = [
        _row(model.model_id, reprompts=0, retries=0, cost=0.1)
        for model in manifest.models
        for _ in manifest.screening_seeds
    ]
    rows[0].pop("budget_metrics")
    rows[3].pop("budget_metrics")

    selection = build_screening_selection(manifest, rows)

    assert selection["selection_status"] == "insufficient"
    assert selection["models"][0]["eligible"] is False
    assert "missing_operational_metrics" in selection["models"][0]["reasons"]
    json.dumps(selection, allow_nan=False)


def test_selection_rejects_zero_provider_attempts() -> None:
    manifest = load_screening_manifest_file(MANIFEST)
    rows = [
        _row(model.model_id, reprompts=0, retries=0, cost=0.1)
        for model in manifest.models
        for _ in manifest.screening_seeds
    ]
    for row in rows[: len(manifest.screening_seeds)]:
        row["budget_metrics"]["c2"]["provider_attempt_count"] = 0
        row["budget_metrics"]["press"]["provider_attempt_count"] = 0

    selection = build_screening_selection(manifest, rows)

    assert selection["models"][0]["eligible"] is False
    assert "zero_provider_attempts" in selection["models"][0]["reasons"]


def _row(model_id: str, *, reprompts: int, retries: int, cost: float):
    return {
        "model_id": model_id,
        "status": "completed",
        "admissibility": {
            "tier": "A" if reprompts == 0 else "B",
            "fallback_count": 0,
            "output_reprompt_count": reprompts,
            "transport_retry_count": retries,
            "reasons": [],
        },
        "budget_metrics": {
            "c2": {"provider_attempt_count": 1},
            "press": {"provider_attempt_count": 1},
            "actual_cost_usd": cost,
        },
    }
