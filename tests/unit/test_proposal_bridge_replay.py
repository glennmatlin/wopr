"""Deterministic proposal bridge replay tests."""

from __future__ import annotations

from pathlib import Path

from tests.unit.proposal_bridge_test_support import (
    CYCLE_RECEIPT_PATH,
    PROFILE_PATH,
    write_payload,
)

from nuclear_war_contest.date_world.profile import load_profile
from nuclear_war_contest.situation_room import (
    load_proposal_bridge_fixture,
    replay_proposal_bridge,
    run_no_model_proposal_bridge,
)


def test_replay_reproduces_run_and_world_ledger(tmp_path: Path) -> None:
    profile = load_profile(PROFILE_PATH)
    fixture = load_proposal_bridge_fixture(
        write_payload(tmp_path / "bridge.json"), CYCLE_RECEIPT_PATH, profile
    )
    source = run_no_model_proposal_bridge(profile, fixture)

    replayed = replay_proposal_bridge(profile, source)

    assert replayed.content_hash == source.content_hash
    assert replayed.receipt() == source.receipt()
