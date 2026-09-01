"""Counterpart Room to D70 composition tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from nuclear_war_contest.situation_room import (
    load_counterpart_composition_fixture,
    replay_counterpart_composition,
    run_no_model_counterpart_composition,
)

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"
FIXTURE = CONTEST / "COUNTERPART_ROOM_COMPOSITION_FIXTURE.development.json"
D70_RECEIPT = CONTEST / "US_TWO_CYCLE_RECEIPT.json"


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_composition_uses_room_receipts_and_preserves_exact_d70_run() -> None:
    fixture = load_counterpart_composition_fixture(FIXTURE)
    run = run_no_model_counterpart_composition(fixture)
    receipt = run.receipt()
    d70 = _load(D70_RECEIPT)

    assert receipt["status"] == "passed"
    assert receipt["us_two_cycle"]["source_receipt_hash"] == d70["receipt_hash"]
    assert receipt["us_two_cycle"]["run_hash"] == d70["run_hash"]
    assert receipt["us_two_cycle"]["run"] == d70["run"]
    provenance = {item["actor_id"]: item for item in receipt["counterparts"]}
    assert set(provenance) == {"ACTOR_HIMALDESH", "ACTOR_OLVANA"}
    assert provenance["ACTOR_HIMALDESH"]["output_id"] == (
        "HIM_OUTPUT_SUPPORT_REQUEST_001"
    )
    assert provenance["ACTOR_OLVANA"]["output_id"] == ("OLV_OUTPUT_RIDGE_POSTURE_001")
    assert provenance["ACTOR_HIMALDESH"]["mapping_type"] == (
        "decision_record_output_components"
    )
    assert provenance["ACTOR_HIMALDESH"]["projection_id"] == (
        "HD_PROJECTION_SUPPORT_REQUEST_001"
    )
    assert provenance["ACTOR_OLVANA"]["mapping_type"] == "authored_world_projection"
    assert provenance["ACTOR_OLVANA"]["projection_id"] == (
        "OLV_PROJECTION_RIDGE_POSTURE_001"
    )
    assert provenance["ACTOR_HIMALDESH"]["us_cycle1_input_ids"] == [
        "USC1_INPUT_COMMON_001",
        "USC1_INPUT_STATE_PRIVATE_001",
        "USC1_INPUT_DEFENSE_PRIVATE_001",
        "USC1_INPUT_JUSTICE_PRIVATE_001",
        "USC1_INPUT_EOP_LEGAL_PRIVATE_001",
        "USC1_INPUT_CJCS_PRIVATE_001",
        "USC1_INPUT_THEATER_PRIVATE_001",
    ]
    assert provenance["ACTOR_OLVANA"]["us_cycle1_input_ids"] == [
        "USC1_INPUT_COMMON_001",
        "USC1_INPUT_DNI_PRIVATE_001",
        "USC1_INPUT_CIA_PRIVATE_001",
        "USC1_INPUT_TREASURY_PRIVATE_001",
        "USC1_INPUT_ENERGY_PRIVATE_001",
        "USC1_INPUT_CJCS_PRIVATE_001",
        "USC1_INPUT_THEATER_PRIVATE_001",
    ]
    rendered_provenance = json.dumps(receipt["counterparts"], sort_keys=True)
    assert "HIM_CYCLE1_REQUEST.development.v0_1" not in rendered_provenance
    assert "OLV_CYCLE1_POSTURE.development.v0_1" not in rendered_provenance
    assert receipt["migration_check"] == {
        "cycle1_fixture_hash": d70["cycle1_fixture_hash"],
        "status": "matched_not_final_provenance",
        "output_bytes_matched": True,
        "historical_counterpart_fixture_role": (
            "fixture_load_reference_validation_only"
        ),
        "us_execution_input_source": "cycle1_watch_inputs",
    }


def test_composition_replays_exactly() -> None:
    fixture = load_counterpart_composition_fixture(FIXTURE)
    run = run_no_model_counterpart_composition(fixture)

    replayed = replay_counterpart_composition(run)

    assert replayed.content_hash == run.content_hash
    assert replayed.receipt() == run.receipt()
