"""Exact binding tests for the accepted U.S. Charter candidate."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json
from nuclear_war_contest.situation_room import load_source_register, load_us_charter

ROOT = Path(__file__).parents[2]
SOURCE_PATH = ROOT / "docs/contest/US_SOURCE_REGISTER.candidate.json"
CHARTER_PATH = ROOT / "docs/contest/US_CHARTER.candidate.json"
RATIFICATION_PATH = ROOT / "docs/contest/US_CHARTER_RATIFICATION.json"


def test_ratification_binds_exact_accepted_candidate() -> None:
    source = load_source_register(SOURCE_PATH)
    charter = load_us_charter(CHARTER_PATH, source)
    receipt = load_strict_json(RATIFICATION_PATH)

    assert isinstance(receipt, dict)
    assert receipt["status"] == "ratified"
    assert receipt["decision_id"] == "D67"
    assert receipt["candidate_commit"] == (
        "623612166aa65bb0c2f14a79ea6993cd02221f8d"
    )
    assert receipt["source_register_id"] == source.register_id
    assert receipt["source_register_hash"] == source.content_hash
    assert receipt["charter_id"] == charter.charter_id
    assert receipt["charter_hash"] == charter.content_hash
    assert canonical_hash(receipt) == (
        "0b831d55ba60dd458e44b0e63d714a82eaf05b508a32694f96181caba0b5ad13"
    )
