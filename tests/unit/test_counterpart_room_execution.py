"""Deterministic counterpart Room trace tests."""

from __future__ import annotations

import json
from pathlib import Path

from nuclear_war_contest.situation_room import (
    load_actor_source_register,
    load_counterpart_charter,
    load_counterpart_room_fixture,
    replay_counterpart_room,
    run_no_model_counterpart_room,
)

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"
RATIFICATION = CONTEST / "COUNTERPART_CHARTER_RATIFICATION.json"
LEGACY = CONTEST / "US_CYCLE1_FIXTURE.development.json"


def _run(prefix: str):
    source = load_actor_source_register(
        CONTEST / f"{prefix}_SOURCE_REGISTER.candidate.json"
    )
    charter = load_counterpart_charter(
        CONTEST / f"{prefix}_CHARTER.candidate.json", source
    )
    fixture = load_counterpart_room_fixture(
        CONTEST / f"{prefix}_ROOM_FIXTURE.development.json",
        charter,
        RATIFICATION,
    )
    return charter, run_no_model_counterpart_room(charter, fixture)


def _legacy_output(actor_id: str) -> dict[str, object]:
    payload = json.loads(LEGACY.read_text(encoding="utf-8"))
    fixture = next(
        item for item in payload["counterpart_fixtures"] if item["actor_id"] == actor_id
    )
    return fixture["outputs"][0]


def test_himaldesh_trace_runs_two_lanes_into_joint_decision() -> None:
    charter, run = _run("HIMALDESH")
    receipt = run.receipt()

    assert receipt["status"] == "passed"
    assert len(receipt["active_seat_ids"]) == 11
    assert receipt["schedule"] == [
        [
            "HD_GROUP_PORTFOLIO_EXTERNAL",
            "HD_GROUP_PORTFOLIO_INTERIOR",
            "HD_GROUP_PORTFOLIO_FINANCE",
            "HD_GROUP_PORTFOLIO_INFORMATION",
            "HD_GROUP_PORTFOLIO_INFRASTRUCTURE",
            "HD_GROUP_PORTFOLIO_HUMANITARIAN",
            "HD_GROUP_COMMAND_CELL",
        ],
        ["HD_GROUP_CABINET_DRAFT"],
        ["HD_GROUP_CABINET_REVIEW"],
        ["HD_GROUP_JOINT_EXECUTIVE"],
    ]
    assert receipt["decision_route"]["decision_authority_seat_ids"] == [
        "HD_SEAT_PRIME_MINISTER",
        "HD_SEAT_PRESIDENT",
    ]
    assert len(receipt["confirmations"]) == 2
    assert receipt["output"] == _legacy_output("ACTOR_HIMALDESH")
    replayed = replay_counterpart_room(charter, run)
    assert replayed.content_hash == run.content_hash


def test_olvana_trace_serializes_nca_and_world_projection() -> None:
    charter, run = _run("OLVANA")
    receipt = run.receipt()

    assert receipt["status"] == "passed"
    assert len(receipt["active_seat_ids"]) == 9
    assert receipt["schedule"] == [
        ["OLV_GROUP_NCA_PORTFOLIOS"],
        ["OLV_GROUP_COMMAND_ASSESSMENT"],
        ["OLV_GROUP_SID_INTEGRATION"],
        ["OLV_GROUP_NCA_REVIEW"],
        ["OLV_GROUP_PARTY_DIRECTION"],
    ]
    assert receipt["decision_route"]["decision_authority_seat_ids"] == [
        "OLV_SEAT_GENERAL_SECRETARY"
    ]
    assert len(receipt["confirmations"]) == 3
    assert receipt["output_projection"]["projection_owner"] == "world_authored"
    assert receipt["output"] == _legacy_output("ACTOR_OLVANA")
    replayed = replay_counterpart_room(charter, run)
    assert replayed.receipt() == receipt
