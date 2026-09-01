"""Fail-closed counterpart Room execution tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from tests.unit.counterpart_room_test_support import (
    mutated_room_run,
    room_product,
)


def test_missing_dissent_disposition_blocks_himaldesh_joint_decision(
    tmp_path: Path,
) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        review = room_product(payload, "HD_GROUP_CABINET_REVIEW")
        review["content"]["dissent_dispositions"] = []

    receipt = mutated_room_run("HIMALDESH", tmp_path, mutate)
    failures = {item["group_id"]: item for item in receipt["failures"]}

    assert receipt["status"] == "failed"
    assert failures["HD_GROUP_CABINET_REVIEW"]["reason_code"] == "invalid_product"
    assert failures["HD_GROUP_JOINT_EXECUTIVE"]["reason_code"] == ("blocked_dependency")
    assert receipt["output"] is None


def test_olvana_portfolio_reordering_blocks_sid_and_party_direction(
    tmp_path: Path,
) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        positions = room_product(payload, "OLV_GROUP_NCA_PORTFOLIOS")["content"][
            "ordered_positions"
        ]
        positions[0], positions[1] = positions[1], positions[0]

    receipt = mutated_room_run("OLVANA", tmp_path, mutate)
    failures = {item["group_id"]: item for item in receipt["failures"]}

    assert failures["OLV_GROUP_NCA_PORTFOLIOS"]["reason_code"] == "invalid_product"
    assert failures["OLV_GROUP_PARTY_DIRECTION"]["reason_code"] == (
        "blocked_dependency"
    )
    assert receipt["output"] is None


@pytest.mark.parametrize(
    ("prefix", "action_class", "gap_id"),
    [
        (
            "HIMALDESH",
            "direct_conventional_force_employment_without_operational_command",
            "HD_GAP_OPERATIONAL_COMMANDER",
        ),
        (
            "OLVANA",
            "strategic_or_nuclear_readiness_signaling_or_use",
            "OLV_GAP_NUCLEAR_DECISION_PATH",
        ),
        (
            "OLVANA",
            "setup_authored_limited_nuclear_coercion_debate",
            "OLV_GAP_LIMITED_USE_SOURCE_DRIFT",
        ),
        (
            "OLVANA",
            "politburo_collective_vote_or_consensus",
            "OLV_GAP_PSC_COMPOSITION",
        ),
    ],
)
def test_blocked_action_classes_retain_exact_gap(
    tmp_path: Path, prefix: str, action_class: str, gap_id: str
) -> None:
    receipt = mutated_room_run(
        prefix, tmp_path, lambda payload: payload.update({"action_class": action_class})
    )

    assert receipt["status"] == "failed"
    assert receipt["schedule"] == []
    assert receipt["failures"][0]["gap_ids"] == [gap_id]
    assert receipt["output"] is None
