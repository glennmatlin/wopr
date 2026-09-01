"""Room Instrument study variant: three Organizational Presets."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest

from nuclear_war_agents.faction_aggregation import aggregate_council
from nuclear_war_agents.faction_types import SubordinateVote
from nuclear_war_contest.analysis import build_paired_analysis
from nuclear_war_contest.manifest import load_study_manifest
from nuclear_war_contest.preflight import load_candidate_manifest
from nuclear_war_contest.preflight_study_binding import validate_study_binding
from nuclear_war_contest.runner import run_matched_study

_PRESETS = (
    "full_press_presidential_staff",
    "full_press_equal_council",
    "full_press_chair_weighted_council",
)


def _dry_run_payload() -> dict[str, object]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


def _room_instrument_payload() -> dict[str, object]:
    payload = _dry_run_payload()
    payload["study_variant"] = "room_instrument"
    payload["protocol_revision"] = "draft-0.2"
    payload["conditions"] = [
        {
            "condition_id": "full_press_presidential_staff",
            "communication": "full_press",
            "authority": "sole_authority",
            "authority_parameters": {"deference": 0.0},
            "press_passes": 1,
        },
        {
            "condition_id": "full_press_equal_council",
            "communication": "full_press",
            "authority": "council",
            "authority_parameters": {
                "threshold": 0.6666666667,
                "weights": {
                    "executive": 1.0,
                    "strategic_advisor": 1.0,
                    "risk_advisor": 1.0,
                },
            },
            "press_passes": 1,
        },
        {
            "condition_id": "full_press_chair_weighted_council",
            "communication": "full_press",
            "authority": "council",
            "authority_parameters": {
                "threshold": 0.6666666667,
                "weights": {
                    "executive": 2.0,
                    "strategic_advisor": 1.0,
                    "risk_advisor": 1.0,
                },
            },
            "press_passes": 1,
        },
    ]
    return payload


def test_room_instrument_manifest_loads_three_presets() -> None:
    manifest = load_study_manifest(_room_instrument_payload())

    assert manifest.study_variant == "room_instrument"
    assert [condition.condition_id for condition in manifest.conditions] == list(
        _PRESETS
    )
    assert len(manifest.cells) == 6


def test_room_instrument_manifest_rejects_missing_preset() -> None:
    payload = _room_instrument_payload()
    payload["conditions"] = payload["conditions"][:2]  # type: ignore[index]

    with pytest.raises(ValueError, match="room_instrument"):
        load_study_manifest(payload)


def test_room_instrument_manifest_rejects_weight_drift() -> None:
    payload = _room_instrument_payload()
    weighted = next(
        item
        for item in payload["conditions"]  # type: ignore[union-attr]
        if item["condition_id"] == "full_press_chair_weighted_council"  # type: ignore[index]
    )
    weighted["authority_parameters"]["weights"]["executive"] = 3.0  # type: ignore[index]

    with pytest.raises(ValueError, match="predeclared treatment"):
        load_study_manifest(payload)


def test_room_instrument_analysis_pairs_presets_not_factorial() -> None:
    rows = []
    for seed in (51, 52):
        for condition_id, authority, value in (
            ("full_press_presidential_staff", "sole_authority", 1),
            ("full_press_equal_council", "council", 2),
            ("full_press_chair_weighted_council", "council", 3),
        ):
            rows.append(
                {
                    "condition_id": condition_id,
                    "model_id": "offline_first_legal",
                    "seed": seed,
                    "communication": "full_press",
                    "authority": authority,
                    "admissibility": {"tier": "A"},
                    "measures": {
                        "ordinary_escalation": {
                            "count": value,
                            "total_yield": value,
                            "first_turn": 1,
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

    assert {pair["contrast"] for pair in analysis["primary"]["pairs"]} == {
        "equal_council_minus_staff",
        "chair_weighted_minus_staff",
    }
    assert "authority.disagreement_count" in analysis["primary"]["pairs"][0]["deltas"]
    assert (
        "authority.executive_override_count"
        in analysis["primary"]["pairs"][0]["deltas"]
    )
    assert len(analysis["primary"]["pairs"]) == 4
    assert all(
        pair["contrast"] != "factorial_interaction"
        for pair in analysis["exploratory"]["pairs"]
    )


def test_checked_in_room_instrument_manifest_binds_the_pair_candidate() -> None:
    path = (
        Path(__file__).parents[2]
        / "docs"
        / "contest"
        / "STUDY_MANIFEST.room_instrument.candidate.json"
    )
    candidate_path = (
        path.parent / "MODEL_MANIFEST.deepseek_flash_gpt_oss_20b.candidate.json"
    )
    manifest = load_study_manifest(json.loads(path.read_text(encoding="utf-8")))
    candidate = load_candidate_manifest(
        json.loads(candidate_path.read_text(encoding="utf-8")),
        base_dir=candidate_path.parent,
    )
    validate_study_binding(manifest, candidate)

    assert manifest.study_variant == "room_instrument"
    assert list(manifest.seeds) == [51, 52, 53]
    assert len(manifest.cells) == 18
    assert manifest.preflight_approval_status == "pending_owner"


def test_checked_in_room_instrument_demo_binds_one_candidate_model() -> None:
    path = (
        Path(__file__).parents[2]
        / "docs"
        / "contest"
        / "STUDY_MANIFEST.room_instrument_demo.candidate.json"
    )
    candidate_path = (
        path.parent / "MODEL_MANIFEST.deepseek_flash_gpt_oss_20b.candidate.json"
    )
    manifest = load_study_manifest(json.loads(path.read_text(encoding="utf-8")))
    candidate = load_candidate_manifest(
        json.loads(candidate_path.read_text(encoding="utf-8")),
        base_dir=candidate_path.parent,
    )

    validate_study_binding(manifest, candidate)


def test_room_instrument_smoke_binds_one_candidate_model() -> None:
    path = (
        Path(__file__).parents[2]
        / "docs"
        / "contest"
        / "STUDY_MANIFEST.room_instrument_smoke.candidate.json"
    )
    candidate_path = (
        path.parent / "MODEL_MANIFEST.deepseek_flash_gpt_oss_20b.candidate.json"
    )
    manifest = load_study_manifest(json.loads(path.read_text(encoding="utf-8")))
    candidate = load_candidate_manifest(
        json.loads(candidate_path.read_text(encoding="utf-8")),
        base_dir=candidate_path.parent,
    )

    validate_study_binding(manifest, candidate)


def test_equal_council_two_votes_bind() -> None:
    path = (
        Path(__file__).parents[2]
        / "docs"
        / "contest"
        / "STUDY_MANIFEST.room_instrument.candidate.json"
    )
    manifest = load_study_manifest(json.loads(path.read_text(encoding="utf-8")))
    condition = next(
        item
        for item in manifest.conditions
        if item.condition_id == "full_press_equal_council"
    )
    votes = [
        SubordinateVote("executive", "hold"),
        SubordinateVote("strategic_advisor", "release"),
        SubordinateVote("risk_advisor", "release"),
    ]

    selected, rule = aggregate_council(
        votes,
        weights=condition.authority_parameters["weights"],
        threshold=condition.authority_parameters["threshold"],
    )

    assert selected == "release"
    assert rule == "weighted_majority"


def test_offline_room_instrument_runner_reports_preset_pairs(tmp_path: Path) -> None:
    manifest = load_study_manifest(_room_instrument_payload())
    summary = run_matched_study(manifest, tmp_path)

    assert len(summary["attempts"]) == 6
    assert len(summary["analysis"]["primary"]["pairs"]) == 4
    assert all(
        pair["contrast"] != "factorial_interaction"
        for pair in summary["analysis"]["exploratory"]["pairs"]
    )
