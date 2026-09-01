"""Fresh-process no-model U.S. Cycle 1 tracer test."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

from tests.unit.us_cycle_fixture_values import (
    CHARTER_PATH,
    RATIFICATION_HASH,
    RATIFICATION_PATH,
    SOURCE_PATH,
)
from tests.unit.us_cycle_test_support import loaded_cycle_fixture

from nuclear_war_contest.situation_room.cycle_tracer import run_cycle_tracer

EXECUTOR_REVISION = "0" * 40
STATIC_FIXTURE_PATH = SOURCE_PATH.parent / "US_CYCLE1_FIXTURE.development.json"
STATIC_FIXTURE_HASH = "ea7333ec4e7423ad628455d18638c6e0eefd9fdca3b0bd17f85d35fb2d2ac9fc"
STATIC_RECEIPT_PATH = SOURCE_PATH.parent / "US_CYCLE1_RECEIPT.json"
STATIC_EXECUTOR_REVISION = "6c06ed4a7e362cdee89ca15df7aff385aec0aaf8"
STATIC_RECEIPT_HASH = "7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186"


def _canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def test_no_model_cycle_passes_and_replays_in_a_fresh_process(
    tmp_path: Path,
) -> None:
    _, fixture = loaded_cycle_fixture(tmp_path, complete=True)
    fixture_path = tmp_path / "cycle-fixture.json"
    fixture_path.write_text(json.dumps(fixture.payload()), encoding="utf-8")

    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.situation_room.cycle_tracer",
            str(SOURCE_PATH),
            str(CHARTER_PATH),
            str(RATIFICATION_PATH),
            str(fixture_path),
            EXECUTOR_REVISION,
        ],
        check=True,
        capture_output=True,
        cwd=SOURCE_PATH.parents[3],
        text=True,
    )
    receipt = json.loads(process.stdout)

    assert receipt["status"] == "passed"
    assert receipt["executor_revision"] == EXECUTOR_REVISION
    assert receipt["ratification_hash"] == RATIFICATION_HASH
    assert receipt["fixture_hash"] == fixture.content_hash
    assert receipt["replay_matched"] is True
    assert receipt["run"]["decision_supported"] is True
    assert receipt["run"]["world_effects_admitted"] is False
    assert len(receipt["counterpart_fixtures"]) == 2
    receipt_hash = receipt.pop("receipt_hash")
    assert receipt_hash == _canonical_hash(receipt)


def test_retained_development_fixture_passes_and_replays() -> None:
    receipt = run_cycle_tracer(
        SOURCE_PATH,
        CHARTER_PATH,
        RATIFICATION_PATH,
        STATIC_FIXTURE_PATH,
        EXECUTOR_REVISION,
    )

    assert receipt["status"] == "passed"
    assert receipt["evidence_status"] == "development_fixture_non_evidence"
    assert receipt["fixture_hash"] == STATIC_FIXTURE_HASH
    assert receipt["replay_matched"] is True
    assert receipt["run"]["decision_supported"] is True
    assert receipt["run"]["world_effects_admitted"] is False


def test_fresh_process_can_retain_receipt(tmp_path: Path) -> None:
    receipt_path = tmp_path / "cycle-receipt.json"
    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.situation_room.cycle_tracer",
            str(SOURCE_PATH),
            str(CHARTER_PATH),
            str(RATIFICATION_PATH),
            str(STATIC_FIXTURE_PATH),
            EXECUTOR_REVISION,
            str(receipt_path),
        ],
        check=False,
        capture_output=True,
        cwd=SOURCE_PATH.parents[3],
        text=True,
    )

    assert process.returncode == 0
    assert process.stdout == ""
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert receipt["fixture_hash"] == STATIC_FIXTURE_HASH
    assert receipt["receipt_hash"] == _canonical_hash(
        {key: value for key, value in receipt.items() if key != "receipt_hash"}
    )


def test_retained_receipt_binds_exact_executor_and_fixture() -> None:
    receipt = json.loads(STATIC_RECEIPT_PATH.read_text(encoding="utf-8"))

    assert receipt["executor_revision"] == STATIC_EXECUTOR_REVISION
    assert receipt["fixture_hash"] == STATIC_FIXTURE_HASH
    assert receipt["ratification_hash"] == RATIFICATION_HASH
    assert receipt["replay_matched"] is True
    assert receipt["run"]["decision_supported"] is True
    assert receipt["run"]["world_effects_admitted"] is False
    assert receipt["receipt_hash"] == STATIC_RECEIPT_HASH
    assert receipt["receipt_hash"] == _canonical_hash(
        {key: value for key, value in receipt.items() if key != "receipt_hash"}
    )
