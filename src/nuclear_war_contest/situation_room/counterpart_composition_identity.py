"""Exact upstream identities for counterpart Room composition."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

EXPECTED_IDENTITIES = {
    "d70": {
        "receipt_hash": (
            "7e5dbd8216d9ea9abc55cc457ceae3df44e3ee4192459012a5459944bddfe6ee"
        ),
        "fixture_hash": (
            "2a7d484d4096e598cee64cbf30c60344c3cca57a7f9cf52f384e6b0ce8f94e66"
        ),
        "run_hash": "83a143f8712d9b6d012b6dde2f03940062f63b961ad68ccf5bb3b3ae25660597",
    },
    "himaldesh": {
        "receipt_hash": (
            "98a006d17fe23c40d80ec6804da45a192106363d8b03fc7b096ce79d3cbfefc9"
        ),
        "fixture_hash": (
            "d6f9eb6a546cdf5d6d512511eef8c46c4da0d2c9175e28c7c080ce5d385b406c"
        ),
        "run_hash": "4a1c917aa4e45bbd009bb1fe008ceb932997716c60b759b5160944327714a38b",
        "actor_id": "ACTOR_HIMALDESH",
    },
    "olvana": {
        "receipt_hash": (
            "5586513c594acd6d4acab97978b2624c2917a6a8d49bb81be55818b3c433d547"
        ),
        "fixture_hash": (
            "a922444f415f0b592e5a657f2940524b6f01276c85a3280cb60782f5e8fc1a4b"
        ),
        "run_hash": "c6d212f7ed80ab77c2241920ec574d8577d7746a8e68f8ccef852bd3ad392a3a",
        "actor_id": "ACTOR_OLVANA",
    },
}
LABELS = {
    "d70": "D70",
    "himaldesh": "Himaldesh Room",
    "olvana": "Olvana Room",
}


def validate_exact_composition_receipt(key: str, payload: dict[str, Any]) -> None:
    expected = EXPECTED_IDENTITIES[key]
    retained = payload.get("receipt_hash")
    without_self_hash = {
        name: value for name, value in payload.items() if name != "receipt_hash"
    }
    observed = {
        "receipt_hash": retained,
        "fixture_hash": payload.get("fixture_hash"),
        "run_hash": payload.get("run_hash"),
    }
    if "actor_id" in expected:
        observed["actor_id"] = payload.get("actor_id")
    valid = (
        observed == expected
        and retained == canonical_hash(without_self_hash)
        and payload.get("status") == "passed"
        and payload.get("replay_matched") is True
    )
    if not valid:
        raise ValueError(f"identity_mismatch: exact {LABELS[key]} receipt is invalid")


__all__ = ["EXPECTED_IDENTITIES", "validate_exact_composition_receipt"]
