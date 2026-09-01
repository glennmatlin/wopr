"""Exact binding tests for the accepted Counterpart Charter candidates."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"
RATIFICATION_PATH = CONTEST / "COUNTERPART_CHARTER_RATIFICATION.json"

EXPECTED = {
    "ACTOR_HIMALDESH": {
        "source": "6a2ad9ea06a462c3283ecdc8a14dccee0ffe9830f20bf961deddb830ed308f25",
        "charter": "c7184d1866913782fce5afea3edf1cc3a26942699973eb232e3bbee1782cb822",
    },
    "ACTOR_OLVANA": {
        "source": "932c12452ccb3373ccf4fc07c7d91f290d6812d1d8d1b227f49f0cf8eb4e06d5",
        "charter": "0aa48c3cb8e2980324b3db6d4c5426fb5ff67f746775728a0b00f38897fe389a",
    },
}


def test_ratification_binds_exact_accepted_candidates() -> None:
    receipt = load_strict_json(RATIFICATION_PATH)

    assert isinstance(receipt, dict)
    assert receipt["status"] == "ratified"
    assert receipt["decision_id"] == "D72"
    assert receipt["candidate_commit"] == ("8d65a6e05ed264193ddda3fbd5daea7bc1c88dee")
    bundles = {item["actor_id"]: item for item in receipt["actor_bundles"]}
    assert set(bundles) == set(EXPECTED)
    for actor_id, expected in EXPECTED.items():
        bundle = bundles[actor_id]
        prefix = "HIMALDESH" if actor_id == "ACTOR_HIMALDESH" else "OLVANA"
        source = load_strict_json(CONTEST / f"{prefix}_SOURCE_REGISTER.candidate.json")
        charter = load_strict_json(CONTEST / f"{prefix}_CHARTER.candidate.json")
        assert canonical_hash(source) == expected["source"]
        assert canonical_hash(charter) == expected["charter"]
        assert bundle["source_register_hash"] == expected["source"]
        assert bundle["charter_hash"] == expected["charter"]
    assert canonical_hash(receipt) == (
        "bbab62ea681f2e513407b926de5adfbfaeb8e73baf5fb86ea34808b9fa524384"
    )
