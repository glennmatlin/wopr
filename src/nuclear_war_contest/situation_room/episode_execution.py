"""Deterministic no-model two-cycle U.S. episode execution."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, core_hash
from nuclear_war_contest.date_world.replay import replay_run

from .cycle_execution import run_no_model_us_cycle
from .episode_adjudication import admit_final_adjudication
from .episode_identity import BRIDGE_RUN_HASH, CYCLE1_RUN_HASH
from .episode_memory import build_seat_memory
from .episode_models import TwoCycleFixture, TwoCycleRun
from .episode_receipt import success_receipt
from .episode_world import (
    BarrierResult,
    admit_bridge_consequence,
    admit_matched_weather,
    initialize_episode_world,
)
from .proposal_bridge_execution import run_no_model_proposal_bridge


def run_no_model_two_cycle_episode(fixture: TwoCycleFixture) -> TwoCycleRun:
    phases: list[str] = []
    profile = fixture.profile()
    world, forecast_receipt = initialize_episode_world(
        profile, f"two-cycle::{fixture.fixture_id}"
    )
    phases.append("forecast")
    cycle1 = run_no_model_us_cycle(fixture.charter, fixture.cycle1_fixture())
    phases.append("cycle_1")
    if cycle1.content_hash != CYCLE1_RUN_HASH:
        return _abort(fixture, phases, "cycle1_identity_mismatch")
    bridge = run_no_model_proposal_bridge(profile, fixture.bridge_fixture())
    if bridge.content_hash != BRIDGE_RUN_HASH:
        return _abort(fixture, phases, "bridge_identity_mismatch")
    world, bridge_receipt = admit_bridge_consequence(profile, world, bridge.receipt())
    phases.append("endogenous_consequence")
    barrier = admit_matched_weather(profile, world)
    phases.extend(["matched_weather", "matched_confirmation"])
    cycle2 = run_no_model_us_cycle(fixture.charter, fixture.cycle2_fixture())
    phases.append("cycle_2")
    cycle2_receipt = cycle2.receipt()
    if not cycle2_receipt["decision_supported"]:
        return _abort(fixture, phases, "cycle2_decision_unsupported")
    if not _reassessment_matches(fixture, cycle1.receipt(), barrier):
        return _abort(fixture, phases, "reassessment_mismatch")
    try:
        memory = build_seat_memory(cycle1.receipt(), cycle2_receipt)
    except ValueError:
        return _abort(fixture, phases, "seat_identity_mismatch")
    phases.append("final_adjudication")
    world, adjudication, reason = admit_final_adjudication(
        profile,
        barrier.run,
        fixture.payload()["final_adjudication"],
        cycle2_receipt,
    )
    if reason is not None:
        return _abort(fixture, phases, reason)
    phases.append("final_consequence")
    replayed = replay_run(profile, world)
    replay_matched = (
        replayed.current_core() == world.current_core()
        and replayed.ledger() == world.ledger()
    )
    receipt = success_receipt(
        fixture,
        phases,
        cycle1.receipt(),
        cycle1.content_hash,
        bridge.receipt(),
        bridge.content_hash,
        cycle2_receipt,
        cycle2.content_hash,
        memory,
        adjudication,
        {
            "forecast": forecast_receipt,
            "endogenous_consequence": bridge_receipt,
            "matched_barrier": barrier.receipt,
        },
        barrier.core_hash,
        world,
        replay_matched,
    )
    return _run(fixture, receipt)


def _reassessment_matches(
    fixture: TwoCycleFixture, cycle1: dict[str, Any], barrier: BarrierResult
) -> bool:
    expected = fixture.payload()["cycle2_reassessment"]
    decision = cycle1["decision_record"]
    core = barrier.run.current_core()
    return (
        expected["prior_decision_id"] == decision["product_id"]
        and expected["prior_decision_hash"] == decision["content_hash"]
        and expected["core_version"] == core["core_version"]
        and expected["core_hash"] == core_hash(core)
        and expected["changed_evidence_ids"]
        == fixture.payload()["cycle2_external_parent_ids"]
    )


def _abort(
    fixture: TwoCycleFixture, phases: list[str], reason_code: str
) -> TwoCycleRun:
    return _run(
        fixture,
        {
            "schema_version": "us-two-cycle-run.v0.1",
            "status": "aborted",
            "evidence_status": "development_fixture_non_evidence",
            "fixture_id": fixture.fixture_id,
            "fixture_hash": fixture.content_hash,
            "phase_order": list(phases),
            "failure": {"reason_code": reason_code},
            "cycle_count": sum(item in phases for item in ("cycle_1", "cycle_2")),
        },
    )


def _run(fixture: TwoCycleFixture, receipt: dict[str, Any]) -> TwoCycleRun:
    return TwoCycleRun(canonical_hash(receipt), receipt, fixture)


__all__ = ["run_no_model_two_cycle_episode"]
