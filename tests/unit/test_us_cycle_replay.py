"""Deterministic no-model U.S. cycle replay tests."""

from __future__ import annotations

from pathlib import Path

from tests.unit.us_cycle_test_support import loaded_cycle_fixture

from nuclear_war_contest.situation_room import (
    replay_us_cycle,
    run_no_model_us_cycle,
)


def test_cycle_replay_reconstructs_exact_receipt(tmp_path: Path) -> None:
    charter, fixture = loaded_cycle_fixture(tmp_path, complete=True)
    source = run_no_model_us_cycle(charter, fixture)

    replayed = replay_us_cycle(charter, source)

    assert replayed.content_hash == source.content_hash
    assert replayed.receipt() == source.receipt()
