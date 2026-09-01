"""Fail-closed counterpart decision and output tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from tests.unit.counterpart_room_test_support import mutated_room_run, room_product


def test_missing_confirmation_blocks_output_locally(tmp_path: Path) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        payload["confirmations"] = payload["confirmations"][1:]

    receipt = mutated_room_run("HIMALDESH", tmp_path, mutate)
    failure = next(
        item
        for item in receipt["failures"]
        if item["reason_code"] == "missing_confirmation"
    )

    assert receipt["status"] == "failed"
    assert failure["failure_effect"] == "block_named_defense_component"
    assert receipt["output"] is None


def test_route_mismatch_retains_local_failure_effect(tmp_path: Path) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        decision = room_product(payload, "HD_GROUP_JOINT_EXECUTIVE")
        decision["content"]["prime_minister_position"]["position"] = "withhold"

    receipt = mutated_room_run("HIMALDESH", tmp_path, mutate)
    failure = receipt["failures"][-1]

    assert failure["reason_code"] == "route_mismatch"
    assert failure["failure_effect"] == "no_external_state_change"
    assert receipt["output"] is None


def test_changed_olvana_projection_bytes_fail_closed(tmp_path: Path) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        payload["output_projection"]["output"]["content"]["occupation_status"] = (
            "changed"
        )

    receipt = mutated_room_run("OLVANA", tmp_path, mutate)
    failure = receipt["failures"][-1]

    assert receipt["status"] == "failed"
    assert failure["reason_code"] == "output_mismatch"
    assert failure["failure_effect"] == "no_supported_posture_change"
    assert receipt["output"] is None
