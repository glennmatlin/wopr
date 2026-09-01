"""Deterministic no-model two-cycle episode execution tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from tests.unit.two_cycle_test_support import stage_episode

from nuclear_war_contest.situation_room import (
    load_two_cycle_fixture,
    run_no_model_two_cycle_episode,
)


def _receipt(tmp_path: Path) -> dict[str, Any]:
    fixture = load_two_cycle_fixture(stage_episode(tmp_path))
    return run_no_model_two_cycle_episode(fixture).receipt()


def test_episode_runs_two_cycles_through_ordered_world_barriers(
    tmp_path: Path,
) -> None:
    receipt = _receipt(tmp_path)

    assert receipt["status"] == "passed"
    assert receipt["phase_order"] == [
        "forecast",
        "cycle_1",
        "endogenous_consequence",
        "matched_weather",
        "matched_confirmation",
        "cycle_2",
        "final_adjudication",
        "final_consequence",
    ]
    assert receipt["cycle_1"]["run_hash"] == (
        "08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6"
    )
    assert receipt["bridge"]["run_hash"] == (
        "d43ad8544af90f8e44736133c11b6e8443275c901049ffb0800efd2e0978b996"
    )
    assert receipt["cycle_2"]["decision_supported"] is True


def test_episode_preserves_world_lineage_and_matched_weather(tmp_path: Path) -> None:
    receipt = _receipt(tmp_path)
    world = receipt["world"]

    assert world["ledger_template_ids"] == [
        "OBS_WX_RIDGE_FORECAST_01",
        "EXCON_CONSEQUENCE_PREPARATION_001",
        "WX_RIDGE_FRONT_01",
        "OBS_WX_RIDGE_CONFIRMED_01",
        "EXCON_CONSEQUENCE_NON_ACTION_002",
    ]
    assert world["core_version"] == 1
    assert world["outcomes"]["us_observation_state"] == "intermittent"
    assert world["outcomes"]["himaldesh_support_state"] == "restricted"
    assert world["replay_matched"] is True
    assert "EXCON_CONSEQUENCE_TRANSMISSION_001" not in world["ledger_template_ids"]
    blocked = [
        item
        for item in receipt["bridge"]["effect_results"]
        if item["status"] == "blocked"
    ]
    assert [item["effect_id"] for item in blocked] == [
        "EFFECT_TRANSMIT_INTELLIGENCE_001"
    ]


def test_weather_patch_is_atomic_and_bound_to_current_core(tmp_path: Path) -> None:
    world = _receipt(tmp_path)["world"]
    barrier = world["phase_receipts"]["matched_barrier"]

    assert barrier["patch_template_hash"] == (
        "a0e67568cf7fc355ff5126e77fc7be925e7d272b0521d3f82bac13e2cc0a0e6c"
    )
    assert barrier["weather"]["accepted"] is True
    assert barrier["weather"]["core_version_before"] == 0
    assert barrier["weather"]["core_version_after"] == 1
    assert barrier["confirmation"]["accepted"] is True
    assert barrier["confirmation"]["core_version_before"] == 1
    assert barrier["confirmation"]["core_version_after"] == 1


def test_cycle2_reassessment_binds_changed_state_and_conditions_policy(
    tmp_path: Path,
) -> None:
    receipt = _receipt(tmp_path)
    reassessment = receipt["cycle_2"]["reassessment"]

    assert reassessment["prior_decision_id"] == "USC1_PRODUCT_NSC_DECISION_001"
    assert reassessment["disposition"] == "condition"
    assert reassessment["changed_evidence_ids"] == [
        "EXCON_CONSEQUENCE_PREPARATION_001",
        "WX_RIDGE_FRONT_01",
        "OBS_WX_RIDGE_CONFIRMED_01",
    ]
    assert reassessment["core_hash"] == receipt["world"]["barrier_core_hash"]
    assert receipt["final_adjudication"]["status"] == "recorded_non_action"
    assert receipt["final_adjudication"]["world_receipt"]["accepted"] is True


def test_same_seats_retain_delivery_history_across_cycles(tmp_path: Path) -> None:
    receipt = _receipt(tmp_path)
    memory = receipt["seat_memory"]
    active = receipt["cycle_1"]["active_seat_ids"]

    assert list(memory) == active
    assert all(item["cycle_1_delivery_ids"] for item in memory.values())
    assert all(item["cycle_2_delivery_ids"] for item in memory.values())
    common = "USC2_INPUT_COMMON_WORLD_001"
    assert all(
        any(common in delivery_id for delivery_id in item["cycle_2_delivery_ids"])
        for item in memory.values()
    )
    final_recipients = {
        item["recipient_seat_id"] for item in receipt["final_consequence_deliveries"]
    }
    assert final_recipients == set(active)
