"""Fresh-process deterministic counterpart Room tracer tests."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from nuclear_war_contest.date_world.identity import canonical_hash
from nuclear_war_contest.situation_room.counterpart_room_tracer import (
    run_counterpart_room_tracer,
)

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"
RATIFICATION = CONTEST / "COUNTERPART_CHARTER_RATIFICATION.json"
EXECUTOR_REVISION = "0" * 40
RATIFICATION_HASH = "bbab62ea681f2e513407b926de5adfbfaeb8e73baf5fb86ea34808b9fa524384"
ACTOR_IDENTITIES = {
    "HIMALDESH": (
        "6a2ad9ea06a462c3283ecdc8a14dccee0ffe9830f20bf961deddb830ed308f25",
        "c7184d1866913782fce5afea3edf1cc3a26942699973eb232e3bbee1782cb822",
    ),
    "OLVANA": (
        "932c12452ccb3373ccf4fc07c7d91f290d6812d1d8d1b227f49f0cf8eb4e06d5",
        "0aa48c3cb8e2980324b3db6d4c5426fb5ff67f746775728a0b00f38897fe389a",
    ),
}


def _paths(prefix: str) -> tuple[Path, Path, Path]:
    return (
        CONTEST / f"{prefix}_SOURCE_REGISTER.candidate.json",
        CONTEST / f"{prefix}_CHARTER.candidate.json",
        CONTEST / f"{prefix}_ROOM_FIXTURE.development.json",
    )


@pytest.mark.parametrize("prefix", ["HIMALDESH", "OLVANA"])
def test_counterpart_room_tracer_binds_exact_bundle(prefix: str) -> None:
    source_path, charter_path, fixture_path = _paths(prefix)

    receipt = run_counterpart_room_tracer(
        source_path,
        charter_path,
        RATIFICATION,
        fixture_path,
        EXECUTOR_REVISION,
    )

    source_hash, charter_hash = ACTOR_IDENTITIES[prefix]
    assert receipt["status"] == "passed"
    assert receipt["executor_revision"] == EXECUTOR_REVISION
    assert receipt["source_register_hash"] == source_hash
    assert receipt["charter_hash"] == charter_hash
    assert receipt["ratification_hash"] == RATIFICATION_HASH
    assert receipt["run_hash"] == canonical_hash(receipt["run"])
    assert receipt["replay_matched"] is True
    assert receipt["run"]["world_effects_admitted"] is False


def test_counterpart_room_tracer_replays_in_fresh_process() -> None:
    source_path, charter_path, fixture_path = _paths("OLVANA")
    expected = run_counterpart_room_tracer(
        source_path,
        charter_path,
        RATIFICATION,
        fixture_path,
        EXECUTOR_REVISION,
    )

    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.situation_room.counterpart_room_tracer",
            str(source_path),
            str(charter_path),
            str(RATIFICATION),
            str(fixture_path),
            EXECUTOR_REVISION,
        ],
        check=True,
        capture_output=True,
        cwd=ROOT,
        text=True,
    )

    assert process.stderr == ""
    assert json.loads(process.stdout) == expected


def test_counterpart_room_tracer_rejects_invalid_executor_revision() -> None:
    source_path, charter_path, fixture_path = _paths("HIMALDESH")

    with pytest.raises(ValueError, match="executor revision is invalid"):
        run_counterpart_room_tracer(
            source_path,
            charter_path,
            RATIFICATION,
            fixture_path,
            "not-a-revision",
        )
