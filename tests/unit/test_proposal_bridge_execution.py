"""No-model proposal bridge execution tests."""

from __future__ import annotations

from pathlib import Path

from tests.unit.proposal_bridge_run_support import run_payload
from tests.unit.proposal_bridge_test_support import (
    copied_payload,
)

from nuclear_war_contest.date_world.identity import canonical_hash


def test_compound_proposal_admits_valid_effect_and_retains_blocked_effect(
    tmp_path: Path,
) -> None:
    original = copied_payload()["proposals"][0]["original_language"]

    receipt = run_payload(tmp_path)

    by_id = {item["effect_id"]: item for item in receipt["effect_results"]}
    admitted = by_id["EFFECT_PREPARE_INTELLIGENCE_001"]
    blocked = by_id["EFFECT_TRANSMIT_INTELLIGENCE_001"]
    assert receipt["status"] == "passed"
    assert receipt["proposals"][0]["original_language"] == original
    assert receipt["proposals"][0]["open_content"]["format"].startswith("open")
    assert admitted["status"] == "admitted"
    assert admitted["original_effect"]["timing"] is None
    assert admitted["resolved_effect"]["timing"] == (
        "before the hour-four disposition clock"
    )
    assert admitted["clarification"]["status"] == "resolved"
    assert admitted["world_receipt"]["accepted"] is True
    assert blocked["status"] == "blocked"
    assert blocked["reason_codes"] == ["unresolved_clarification"]
    assert receipt["world"]["core_unchanged"] is True
    assert len(receipt["world"]["ledger"]) == 1


def test_missing_authority_blocks_effect_and_only_proven_descendant(
    tmp_path: Path,
) -> None:
    payload = copied_payload()
    effect = payload["proposals"][0]["effects"][0]
    effect["authority_record_id"] = None
    payload["clarifications"][0]["original_effect_hash"] = canonical_hash(effect)

    receipt = run_payload(tmp_path, payload)

    first, second = receipt["effect_results"]
    assert first["reason_codes"] == ["missing_effect_authority"]
    assert second["reason_codes"] == ["blocked_dependency"]
    assert receipt["world"]["ledger"] == []


def test_false_typed_capability_blocks_world_admission(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["capability_records"][0]["actor_id"] = "HIM"

    receipt = run_payload(tmp_path, payload)

    assert receipt["effect_results"][0]["reason_codes"] == ["missing_capability"]
    assert receipt["world"]["ledger"] == []


def test_novel_open_content_is_not_an_admission_failure(tmp_path: Path) -> None:
    payload = copied_payload()
    proposal = payload["proposals"][0]
    proposal["original_language"] = "Use an unprecedented reversible liaison method."
    proposal["open_content"] = {"unanticipated_policy_shape": ["alpha", "beta"]}
    payload["consequence_proposals"][0]["content"] = (
        "An unforeseen but state-bounded preparation consequence occurs."
    )

    receipt = run_payload(tmp_path, payload)

    assert receipt["effect_results"][0]["status"] == "admitted"
