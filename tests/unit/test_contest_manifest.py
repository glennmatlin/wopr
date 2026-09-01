"""Tests for contest manifest and paired-analysis contracts."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest

from nuclear_war_contest.analysis import build_paired_analysis
from nuclear_war_contest.config_builder import build_concordia_payload
from nuclear_war_contest.manifest import (
    load_study_manifest,
    manifest_hash,
    manifest_payload,
)


def _manifest_payload() -> dict[str, object]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


def test_manifest_enumerates_frozen_factorial_cells() -> None:
    manifest = load_study_manifest(_manifest_payload())

    assert len(manifest.cells) == 8
    assert "request_budget" not in manifest_payload(manifest)
    assert len({cell.cell_id for cell in manifest.cells}) == 8
    assert manifest_hash(manifest) == manifest_hash(manifest)
    payload = build_concordia_payload(manifest, manifest.cells[0])
    assert payload["press"] == {"mode": "none", "enabled": False}
    assert payload["seats"]["player_0"]["authority"]["archetype"] == "sole_authority"


def test_manifest_round_trips_frozen_request_budget() -> None:
    payload = _manifest_payload()
    payload["request_budget"] = {
        "max_c2_calls_per_game": 2048,
        "max_press_calls_per_game": 160,
        "input_tokens_bound": 8192,
        "max_output_tokens": 512,
        "max_cost_usd": 600.0,
        "max_cost_per_request_usd": 0.00152064,
        "transport_retry_margin": 2,
    }
    payload["preflight_receipt_hash"] = "a" * 64
    payload["preflight_approval_status"] = "approved"

    manifest = load_study_manifest(payload)

    assert manifest.request_budget is not None
    assert manifest.request_budget.max_c2_calls_per_game == 2048
    assert manifest.request_budget.max_output_tokens == 512
    assert manifest_payload(manifest) == payload


def test_manifest_rejects_malformed_request_budget() -> None:
    payload = _manifest_payload()
    payload["request_budget"] = {"max_c2_calls_per_game": 2048}

    with pytest.raises(ValueError, match="request_budget"):
        load_study_manifest(payload)

    payload["request_budget"] = None
    with pytest.raises(ValueError, match="request_budget"):
        load_study_manifest(payload)


def test_manifest_rejects_missing_factorial_cell() -> None:
    payload = _manifest_payload()
    payload["conditions"] = payload["conditions"][:-1]  # type: ignore[index]

    with pytest.raises(ValueError, match="all four communication-authority cells"):
        load_study_manifest(payload)


def test_manifest_rejects_literal_client_credentials() -> None:
    payload = _manifest_payload()
    payload["models"][0]["client"] = {"api_key": "literal-secret"}  # type: ignore[index]

    with pytest.raises(ValueError, match="client fields"):
        load_study_manifest(payload)


def test_analysis_keeps_seed_pairs_and_fixed_factors_separate() -> None:
    manifest = load_study_manifest(_manifest_payload())
    rows: list[dict[str, object]] = []
    for cell in manifest.cells:
        condition = next(
            item
            for item in manifest.conditions
            if item.condition_id == cell.condition_id
        )
        value = 1 if condition.communication == "full_press" else 0
        rows.append(
            {
                "condition_id": cell.condition_id,
                "model_id": cell.model_id,
                "seed": cell.seed,
                "communication": condition.communication,
                "authority": condition.authority,
                "admissibility": {"tier": "A"},
                "measures": {
                    "ordinary_escalation": {
                        "count": value,
                        "total_yield": value,
                        "first_turn": 1 if value else None,
                        "targets": [],
                    },
                    "forced_retaliation": {
                        "targeted_count": 0,
                        "executed_count": 0,
                        "total_yield": 0,
                        "targets": [],
                    },
                    "population_loss": 0,
                    "eliminations": 0,
                    "winner": None,
                    "surviving_factions": ["player_0"],
                    "turns": 2,
                    "censored": True,
                    "authority": {
                        "deliberation_count": 1,
                        "disagreement_count": 0,
                        "threshold_failure_count": 0,
                        "executive_match_count": 1,
                        "executive_override_count": 0,
                    },
                },
            }
        )

    analysis = build_paired_analysis(deepcopy(rows))

    assert len(analysis["primary"]["pairs"]) == 4
    assert len(analysis["exploratory"]["pairs"]) == 10
    assert {item["fixed_factor"] for item in analysis["primary"]["summary"]} == {
        "sole_authority",
        "no_press",
    }
