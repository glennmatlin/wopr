"""Exact two-cycle episode replay test."""

from __future__ import annotations

from pathlib import Path

from tests.unit.two_cycle_test_support import stage_episode

from nuclear_war_contest.situation_room import (
    load_two_cycle_fixture,
    replay_two_cycle_episode,
    run_no_model_two_cycle_episode,
)


def test_replay_reproduces_episode_receipt(tmp_path: Path) -> None:
    fixture = load_two_cycle_fixture(stage_episode(tmp_path))
    source = run_no_model_two_cycle_episode(fixture)

    replayed = replay_two_cycle_episode(source)

    assert replayed.content_hash == source.content_hash
    assert replayed.receipt() == source.receipt()
