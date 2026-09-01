"""Execution helper for proposal bridge tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from tests.unit.proposal_bridge_fixture_values import (
    CYCLE_RECEIPT_PATH,
    PROFILE_PATH,
)
from tests.unit.proposal_bridge_test_support import write_payload

from nuclear_war_contest.date_world.profile import load_profile
from nuclear_war_contest.situation_room import (
    load_proposal_bridge_fixture,
    run_no_model_proposal_bridge,
)


def run_payload(
    tmp_path: Path, payload: dict[str, Any] | None = None
) -> dict[str, Any]:
    profile = load_profile(PROFILE_PATH)
    fixture = load_proposal_bridge_fixture(
        write_payload(tmp_path / "bridge.json", payload), CYCLE_RECEIPT_PATH, profile
    )
    return run_no_model_proposal_bridge(profile, fixture).receipt()


__all__ = ["run_payload"]
