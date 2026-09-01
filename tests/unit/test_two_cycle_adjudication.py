"""Strict final-adjudication boundary tests for the two-cycle fixture."""

from __future__ import annotations

from pathlib import Path

import pytest
from tests.unit.two_cycle_test_support import episode_payload, stage_episode

from nuclear_war_contest.situation_room import load_two_cycle_fixture


def test_final_event_must_be_an_excon_consequence(tmp_path: Path) -> None:
    payload = episode_payload()
    payload["final_adjudication"]["world_event"]["event_kind"] = "room_decision"

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_two_cycle_fixture(stage_episode(tmp_path, payload))


def test_final_adjudication_must_bind_the_cycle2_decision(tmp_path: Path) -> None:
    payload = episode_payload()
    payload["final_adjudication"]["decision_record_id"] = (
        "USC2_PRODUCT_POLICY_PACKAGE_001"
    )

    with pytest.raises(ValueError, match="causal_mismatch"):
        load_two_cycle_fixture(stage_episode(tmp_path, payload))


def test_final_consequence_requires_world_causal_parents(tmp_path: Path) -> None:
    payload = episode_payload()
    payload["final_adjudication"]["world_event"]["causal_parent_ids"] = []

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_two_cycle_fixture(stage_episode(tmp_path, payload))
