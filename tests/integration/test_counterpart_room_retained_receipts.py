"""Exact retained counterpart Room receipt tests."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nuclear_war_contest.date_world.identity import canonical_hash
from nuclear_war_contest.situation_room.counterpart_room_tracer import (
    run_counterpart_room_tracer,
)

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"
RATIFICATION = CONTEST / "COUNTERPART_CHARTER_RATIFICATION.json"
EXECUTOR_REVISION = "b165acc206b374d87fcd0e3b9e1ba32c6b375d39"
EXPECTED = {
    "HIMALDESH": {
        "fixture_hash": (
            "d6f9eb6a546cdf5d6d512511eef8c46c4da0d2c9175e28c7c080ce5d385b406c"
        ),
        "run_hash": "4a1c917aa4e45bbd009bb1fe008ceb932997716c60b759b5160944327714a38b",
        "receipt_hash": (
            "98a006d17fe23c40d80ec6804da45a192106363d8b03fc7b096ce79d3cbfefc9"
        ),
        "output_hash": (
            "317c977a6656a4125e28e025323363a386dddcb394fe8bcf81e94f2f71d7aea2"
        ),
    },
    "OLVANA": {
        "fixture_hash": (
            "a922444f415f0b592e5a657f2940524b6f01276c85a3280cb60782f5e8fc1a4b"
        ),
        "run_hash": "c6d212f7ed80ab77c2241920ec574d8577d7746a8e68f8ccef852bd3ad392a3a",
        "receipt_hash": (
            "5586513c594acd6d4acab97978b2624c2917a6a8d49bb81be55818b3c433d547"
        ),
        "output_hash": (
            "c1362fc0bdab5b9f18dd70f7750911bb31d88004d360a8325115d28c20ff27fe"
        ),
    },
}


def _paths(prefix: str) -> tuple[Path, Path, Path, Path]:
    return (
        CONTEST / f"{prefix}_SOURCE_REGISTER.candidate.json",
        CONTEST / f"{prefix}_CHARTER.candidate.json",
        CONTEST / f"{prefix}_ROOM_FIXTURE.development.json",
        CONTEST / f"{prefix}_ROOM_RECEIPT.json",
    )


@pytest.mark.parametrize("prefix", ["HIMALDESH", "OLVANA"])
def test_retained_counterpart_receipt_reconstructs_exactly(prefix: str) -> None:
    source_path, charter_path, fixture_path, receipt_path = _paths(prefix)
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    expected = EXPECTED[prefix]

    assert receipt["executor_revision"] == EXECUTOR_REVISION
    assert receipt["fixture_hash"] == expected["fixture_hash"]
    assert receipt["run_hash"] == expected["run_hash"]
    assert receipt["receipt_hash"] == expected["receipt_hash"]
    assert canonical_hash(receipt["run"]["output"]) == expected["output_hash"]
    without_self_hash = {
        key: value for key, value in receipt.items() if key != "receipt_hash"
    }
    assert canonical_hash(without_self_hash) == receipt["receipt_hash"]
    assert receipt == run_counterpart_room_tracer(
        source_path,
        charter_path,
        RATIFICATION,
        fixture_path,
        EXECUTOR_REVISION,
    )
