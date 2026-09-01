"""Fresh-process counterpart Room composition tracer tests."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from nuclear_war_contest.date_world.identity import canonical_hash
from nuclear_war_contest.situation_room.counterpart_composition_tracer import (
    run_counterpart_composition_tracer,
)

ROOT = Path(__file__).parents[2]
FIXTURE = ROOT / "docs/contest/COUNTERPART_ROOM_COMPOSITION_FIXTURE.development.json"
RECEIPT = ROOT / "docs/contest/COUNTERPART_ROOM_COMPOSITION_RECEIPT.json"
EXECUTOR_REVISION = "0" * 40
RETAINED_EXECUTOR = "ace150092f513b11d57c75cca92b52bbc8aca652"


def test_composition_tracer_binds_both_rooms_and_exact_d70() -> None:
    receipt = run_counterpart_composition_tracer(FIXTURE, EXECUTOR_REVISION)

    assert receipt["status"] == "passed"
    assert receipt["executor_revision"] == EXECUTOR_REVISION
    assert receipt["upstream_receipt_hashes"] == {
        "d70": "7e5dbd8216d9ea9abc55cc457ceae3df44e3ee4192459012a5459944bddfe6ee",
        "himaldesh": "98a006d17fe23c40d80ec6804da45a192106363d8b03fc7b096ce79d3cbfefc9",
        "olvana": "5586513c594acd6d4acab97978b2624c2917a6a8d49bb81be55818b3c433d547",
    }
    assert receipt["us_two_cycle_run_hash"] == (
        "83a143f8712d9b6d012b6dde2f03940062f63b961ad68ccf5bb3b3ae25660597"
    )
    assert [item["actor_id"] for item in receipt["counterpart_identities"]] == [
        "ACTOR_HIMALDESH",
        "ACTOR_OLVANA",
    ]
    assert receipt["replay_matched"] is True


def test_composition_tracer_replays_in_fresh_process() -> None:
    expected = run_counterpart_composition_tracer(FIXTURE, EXECUTOR_REVISION)
    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.situation_room.counterpart_composition_tracer",
            str(FIXTURE),
            EXECUTOR_REVISION,
        ],
        check=True,
        capture_output=True,
        cwd=ROOT,
        text=True,
    )

    assert process.stderr == ""
    assert json.loads(process.stdout) == expected


def test_composition_tracer_rejects_invalid_executor_revision() -> None:
    with pytest.raises(ValueError, match="executor revision is invalid"):
        run_counterpart_composition_tracer(FIXTURE, "not-a-revision")


def test_retained_composition_receipt_reproduces_exactly() -> None:
    retained = json.loads(RECEIPT.read_text(encoding="utf-8"))
    without_self_hash = {
        key: value for key, value in retained.items() if key != "receipt_hash"
    }

    assert retained["receipt_hash"] == canonical_hash(without_self_hash)
    assert retained == run_counterpart_composition_tracer(FIXTURE, RETAINED_EXECUTOR)
