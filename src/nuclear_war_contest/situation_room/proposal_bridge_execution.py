"""Deterministic no-model proposal and consequence bridge execution."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, core_hash
from nuclear_war_contest.date_world.profile import DateProfile
from nuclear_war_contest.date_world.transition import initialize_run

from .proposal_bridge_effects import execute_proposal_effects
from .proposal_bridge_models import ProposalBridgeFixture, ProposalBridgeRun


def run_no_model_proposal_bridge(
    profile: DateProfile, fixture: ProposalBridgeFixture
) -> ProposalBridgeRun:
    initial = initialize_run(profile, f"proposal-bridge::{fixture.fixture_id}")
    effect_results, world = execute_proposal_effects(profile, fixture, initial)
    payload = fixture.payload()
    cycle = fixture.cycle_receipt()
    admitted = [item for item in effect_results if item["status"] == "admitted"]
    blocked = [item for item in effect_results if item["status"] == "blocked"]
    initial_core = initial.current_core()
    final_core = world.current_core()
    receipt: dict[str, Any] = {
        "schema_version": "proposal-bridge-run.v0.1",
        "status": "passed",
        "evidence_status": "development_fixture_non_evidence",
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "cycle_receipt_hash": fixture.cycle_receipt_hash,
        "cycle_run_hash": cycle["run_hash"],
        "date_profile_hash": fixture.date_profile_hash,
        "policy_package": _artifact_identity(cycle["run"]["policy_package"]),
        "decision_record": _artifact_identity(cycle["run"]["decision_record"]),
        "proposals": payload["proposals"],
        "clarifications": payload["clarifications"],
        "effect_results": effect_results,
        "effect_summary": {
            "attempted": len(effect_results),
            "admitted": len(admitted),
            "blocked": len(blocked),
        },
        "world": {
            "run_id": world.run_id,
            "initial_core_hash": core_hash(initial_core),
            "final_core_hash": core_hash(final_core),
            "final_core": final_core,
            "core_unchanged": core_hash(initial_core) == core_hash(final_core),
            "ledger": list(world.ledger()),
            "validation_receipts": [asdict(item) for item in world.receipts()],
        },
        "claim_boundary": [
            "no_model_proposal_evidence",
            "no_creative_excon_evidence",
            "no_official_effect_authority_evidence",
            "no_counterpart_room_evidence",
            "no_date_episode_evidence",
            "no_comparative_result",
        ],
    }
    return ProposalBridgeRun(
        content_hash=canonical_hash(receipt),
        _receipt=receipt,
        _fixture=fixture,
    )


def _artifact_identity(artifact: dict[str, Any]) -> dict[str, str]:
    return {
        "artifact_id": artifact["product_id"],
        "content_hash": artifact["content_hash"],
    }


__all__ = ["ProposalBridgeRun", "run_no_model_proposal_bridge"]
