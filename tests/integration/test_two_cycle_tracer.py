"""Fresh-process deterministic two-cycle episode tracer test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from tests.unit.two_cycle_test_support import stage_episode

from nuclear_war_contest.date_world.identity import canonical_hash

EXECUTOR_REVISION = "0" * 40
CONTEST_PATH = Path(__file__).parents[2] / "docs" / "contest"
STATIC_RECEIPT_PATH = CONTEST_PATH / "US_TWO_CYCLE_RECEIPT.json"
STATIC_EXECUTOR_REVISION = "67e8ec51281466aacb7b907c1c6212dde817e7c0"
STATIC_FIXTURE_HASH = "2a7d484d4096e598cee64cbf30c60344c3cca57a7f9cf52f384e6b0ce8f94e66"
STATIC_RUN_HASH = "83a143f8712d9b6d012b6dde2f03940062f63b961ad68ccf5bb3b3ae25660597"
STATIC_RECEIPT_HASH = "7e5dbd8216d9ea9abc55cc457ceae3df44e3ee4192459012a5459944bddfe6ee"


def test_two_cycle_tracer_passes_and_replays_in_fresh_process(
    tmp_path: Path,
) -> None:
    fixture_path = stage_episode(tmp_path)
    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.situation_room.episode_tracer",
            str(fixture_path),
            EXECUTOR_REVISION,
        ],
        check=True,
        capture_output=True,
        cwd=fixture_path.parents[1],
        text=True,
    )
    receipt = json.loads(process.stdout)

    assert receipt["status"] == "passed"
    assert receipt["executor_revision"] == EXECUTOR_REVISION
    assert receipt["replay_matched"] is True
    assert receipt["run"]["cycle_count"] == 2
    assert receipt["source_register_hash"] == (
        "73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f"
    )
    assert receipt["charter_hash"] == (
        "fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2"
    )
    assert receipt["date_profile_hash"] == (
        "64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477"
    )
    assert receipt["upstream_receipt_hashes"] == {
        "cycle1": "7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186",
        "bridge": "cf78c92190e8b2739923c0977a0af316b332643b563d0ad4818b13048c726ec4",
        "date": "4a582d72b6d8ff753c3e06adea4d36aef3c3b39b5284e4050ce9ed35e39815e3",
    }
    receipt_hash = receipt.pop("receipt_hash")
    assert receipt_hash == canonical_hash(receipt)


def test_two_cycle_tracer_writes_canonical_receipt(tmp_path: Path) -> None:
    fixture_path = stage_episode(tmp_path)
    output_path = tmp_path / "US_TWO_CYCLE_RECEIPT.json"
    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.situation_room.episode_tracer",
            str(fixture_path),
            EXECUTOR_REVISION,
            str(output_path),
        ],
        check=True,
        capture_output=True,
        cwd=fixture_path.parents[1],
        text=True,
    )

    assert process.stdout == ""
    receipt = json.loads(output_path.read_text(encoding="utf-8"))
    receipt_hash = receipt.pop("receipt_hash")
    assert receipt_hash == canonical_hash(receipt)


def test_retained_two_cycle_receipt_has_exact_identity() -> None:
    receipt = json.loads(STATIC_RECEIPT_PATH.read_text(encoding="utf-8"))

    assert receipt["status"] == "passed"
    assert receipt["executor_revision"] == STATIC_EXECUTOR_REVISION
    assert receipt["fixture_hash"] == STATIC_FIXTURE_HASH
    assert receipt["run_hash"] == STATIC_RUN_HASH
    assert receipt["replay_matched"] is True
    assert receipt["receipt_hash"] == STATIC_RECEIPT_HASH
    assert receipt["run"]["cycle_count"] == 2
    assert receipt["receipt_hash"] == canonical_hash(
        {key: value for key, value in receipt.items() if key != "receipt_hash"}
    )
