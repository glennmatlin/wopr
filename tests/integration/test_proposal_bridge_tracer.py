"""Fresh-process no-model proposal and consequence bridge test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from tests.unit.proposal_bridge_test_support import (
    CYCLE_RECEIPT_PATH,
    PROFILE_PATH,
    write_payload,
)

from nuclear_war_contest.date_world.identity import canonical_hash

EXECUTOR_REVISION = "0" * 40
STATIC_FIXTURE_PATH = (
    PROFILE_PATH.parent / "US_PROPOSAL_BRIDGE_FIXTURE.development.json"
)
STATIC_FIXTURE_HASH = "4b47bc86dad3226692146cc92b21f7b3da61a5919b87ce26924514d7f44ce465"
STATIC_RECEIPT_PATH = PROFILE_PATH.parent / "US_PROPOSAL_BRIDGE_RECEIPT.json"
STATIC_EXECUTOR_REVISION = "1b912ff693a84c5e1081fc76d1ed1f71e4f810aa"
STATIC_RUN_HASH = "d43ad8544af90f8e44736133c11b6e8443275c901049ffb0800efd2e0978b996"
STATIC_RECEIPT_HASH = "cf78c92190e8b2739923c0977a0af316b332643b563d0ad4818b13048c726ec4"


def test_bridge_passes_and_replays_in_fresh_process(tmp_path: Path) -> None:
    fixture_path = write_payload(tmp_path / "bridge.json")

    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.situation_room.proposal_bridge_tracer",
            str(PROFILE_PATH),
            str(CYCLE_RECEIPT_PATH),
            str(fixture_path),
            EXECUTOR_REVISION,
        ],
        check=True,
        capture_output=True,
        cwd=PROFILE_PATH.parents[3],
        text=True,
    )
    receipt = json.loads(process.stdout)

    assert receipt["status"] == "passed"
    assert receipt["executor_revision"] == EXECUTOR_REVISION
    assert receipt["replay_matched"] is True
    assert receipt["run"]["effect_summary"] == {
        "attempted": 2,
        "admitted": 1,
        "blocked": 1,
    }
    receipt_hash = receipt.pop("receipt_hash")
    assert receipt_hash == canonical_hash(receipt)


def test_fresh_process_can_retain_bridge_receipt(tmp_path: Path) -> None:
    fixture_path = write_payload(tmp_path / "bridge.json")
    output_path = tmp_path / "receipt.json"
    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.situation_room.proposal_bridge_tracer",
            str(PROFILE_PATH),
            str(CYCLE_RECEIPT_PATH),
            str(fixture_path),
            EXECUTOR_REVISION,
            str(output_path),
        ],
        check=False,
        capture_output=True,
        cwd=PROFILE_PATH.parents[3],
        text=True,
    )

    assert process.returncode == 0
    assert process.stdout == ""
    receipt = json.loads(output_path.read_text(encoding="utf-8"))
    assert receipt["receipt_hash"] == canonical_hash(
        {key: value for key, value in receipt.items() if key != "receipt_hash"}
    )


def test_retained_development_fixture_passes() -> None:
    from nuclear_war_contest.situation_room.proposal_bridge_tracer import (
        run_proposal_bridge_tracer,
    )

    receipt = run_proposal_bridge_tracer(
        PROFILE_PATH,
        CYCLE_RECEIPT_PATH,
        STATIC_FIXTURE_PATH,
        EXECUTOR_REVISION,
    )

    assert receipt["status"] == "passed"
    assert receipt["fixture_hash"] == STATIC_FIXTURE_HASH
    assert receipt["replay_matched"] is True
    assert receipt["run"]["effect_summary"]["admitted"] == 1
    assert receipt["run"]["effect_summary"]["blocked"] == 1


def test_retained_bridge_receipt_has_exact_identity() -> None:
    receipt = json.loads(STATIC_RECEIPT_PATH.read_text(encoding="utf-8"))

    assert receipt["status"] == "passed"
    assert receipt["executor_revision"] == STATIC_EXECUTOR_REVISION
    assert receipt["fixture_hash"] == STATIC_FIXTURE_HASH
    assert receipt["run_hash"] == STATIC_RUN_HASH
    assert receipt["receipt_hash"] == STATIC_RECEIPT_HASH
    assert receipt["replay_matched"] is True
    assert receipt["run"]["effect_summary"] == {
        "attempted": 2,
        "admitted": 1,
        "blocked": 1,
    }
    receipt_without_hash = {
        key: value for key, value in receipt.items() if key != "receipt_hash"
    }
    assert receipt["receipt_hash"] == canonical_hash(receipt_without_hash)
