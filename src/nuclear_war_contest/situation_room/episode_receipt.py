"""Successful two-cycle episode receipt construction."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from nuclear_war_contest.date_world.identity import core_hash
from nuclear_war_contest.date_world.models import DateRun
from nuclear_war_contest.date_world.projections import project_outcomes

from .episode_adjudication import final_consequence_deliveries
from .episode_models import TwoCycleFixture


def success_receipt(
    fixture: TwoCycleFixture,
    phases: list[str],
    cycle1: dict[str, Any],
    cycle1_hash: str,
    bridge: dict[str, Any],
    bridge_hash: str,
    cycle2: dict[str, Any],
    cycle2_hash: str,
    memory: dict[str, Any],
    adjudication: dict[str, Any],
    world_receipts: dict[str, Any],
    barrier_core_hash: str,
    world: DateRun,
    replay_matched: bool,
) -> dict[str, Any]:
    return {
        "schema_version": "us-two-cycle-run.v0.1",
        "status": "passed",
        "evidence_status": "development_fixture_non_evidence",
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "cycle_count": 2,
        "phase_order": list(phases),
        "cycle_1": {"run_hash": cycle1_hash, **cycle1},
        "bridge": {
            "run_hash": bridge_hash,
            "effect_summary": bridge["effect_summary"],
            "effect_results": bridge["effect_results"],
        },
        "cycle_2": {
            "run_hash": cycle2_hash,
            **cycle2,
            "reassessment": fixture.payload()["cycle2_reassessment"],
        },
        "seat_memory": memory,
        "final_adjudication": adjudication,
        "final_consequence_deliveries": final_consequence_deliveries(
            adjudication, cycle2["active_seat_ids"]
        ),
        "world": {
            "run_id": world.run_id,
            "barrier_core_hash": barrier_core_hash,
            "final_core_hash": core_hash(world.current_core()),
            "core_version": world.current_core()["core_version"],
            "ledger_template_ids": [item["template_id"] for item in world.ledger()],
            "ledger": list(world.ledger()),
            "validation_receipts": [asdict(item) for item in world.receipts()],
            "outcomes": project_outcomes(world.current_core()),
            "phase_receipts": world_receipts,
            "replay_matched": replay_matched,
        },
        "claim_boundary": [
            "no_model_behavior_evidence",
            "no_creative_excon_evidence",
            "no_counterpart_room_evidence",
            "no_matched_us_condition_evidence",
            "no_date_evaluation_evidence",
        ],
    }


__all__ = ["success_receipt"]
