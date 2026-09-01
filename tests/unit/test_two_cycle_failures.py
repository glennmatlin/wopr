"""Fail-closed two-cycle episode behavior tests."""

from __future__ import annotations

import json
from pathlib import Path

from tests.unit.two_cycle_test_support import (
    cycle2_payload,
    episode_payload,
    stage_episode,
)

from nuclear_war_contest.date_world.identity import canonical_hash
from nuclear_war_contest.situation_room import (
    load_two_cycle_fixture,
    run_no_model_two_cycle_episode,
)
from nuclear_war_contest.situation_room.episode_completion import classify_episode_end


def test_stale_cycle2_core_binding_is_an_abort(tmp_path: Path) -> None:
    path = stage_episode(tmp_path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    cycle2_path = tmp_path / payload["artifact_paths"]["cycle2_fixture"]
    cycle2 = cycle2_payload()
    cycle2["group_products"][-2]["content"]["reassessment"]["core_hash"] = "f" * 64
    cycle2["group_products"][-1]["content"]["reassessment"]["core_hash"] = "f" * 64
    cycle2_path.write_text(json.dumps(cycle2), encoding="utf-8")
    payload["artifact_hashes"]["cycle2_fixture"] = canonical_hash(cycle2)
    payload["cycle2_reassessment"]["core_hash"] = "f" * 64
    path.write_text(json.dumps(payload), encoding="utf-8")

    receipt = run_no_model_two_cycle_episode(load_two_cycle_fixture(path)).receipt()

    assert receipt["status"] == "aborted"
    assert receipt["failure"]["reason_code"] == "reassessment_mismatch"
    assert "final_consequence" not in receipt["phase_order"]


def test_retroactive_final_consequence_is_an_abort(tmp_path: Path) -> None:
    payload = episode_payload()
    payload["final_adjudication"]["world_event"]["episode_hour"] = 5
    receipt = run_no_model_two_cycle_episode(
        load_two_cycle_fixture(stage_episode(tmp_path, payload))
    ).receipt()

    assert receipt["status"] == "aborted"
    assert receipt["failure"]["reason_code"] == "retroactive_time"


def test_terminal_and_abort_are_not_interchangeable() -> None:
    open_core = {"terminal_state": "open"}
    terminal_core = {"terminal_state": "strategic_exchange"}

    assert classify_episode_end(open_core, cycle2_started=False, failed=True) == "abort"
    assert (
        classify_episode_end(terminal_core, cycle2_started=False, failed=False)
        == "substantive_terminal"
    )
    assert (
        classify_episode_end(open_core, cycle2_started=True, failed=False) == "normal"
    )
