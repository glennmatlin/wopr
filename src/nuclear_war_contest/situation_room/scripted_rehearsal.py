"""Complete offline model-bound U.S. Room rehearsal."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .compiler import compile_us_charter
from .episode_execution import run_no_model_two_cycle_episode
from .episode_models import TwoCycleFixture
from .scripted_rehearsal_cycle import rehearse_cycle
from .scripted_rehearsal_materialization import materialize_rehearsed_fixture
from .scripted_rehearsal_models import CycleRehearsal, ScriptedRehearsalRun
from .scripted_rehearsal_runtime import (
    ClientFactory,
    build_seat_runtimes,
    default_client_factory,
)
from .scripted_rehearsal_scripts import build_scripted_responses


def run_scripted_two_cycle_rehearsal(
    fixture: TwoCycleFixture,
    *,
    client_factory: ClientFactory | None = None,
) -> ScriptedRehearsalRun:
    responses = build_scripted_responses(fixture)
    factory = default_client_factory if client_factory is None else client_factory
    runtimes = build_seat_runtimes(fixture.charter, responses, factory)
    cycle1 = rehearse_cycle(fixture.charter, fixture.cycle1_fixture(), runtimes)
    if cycle1.failures:
        return _failed_run(fixture, cycle1, None)
    cycle2 = rehearse_cycle(fixture.charter, fixture.cycle2_fixture(), runtimes)
    if cycle2.failures or not _exact_fixture_outputs(fixture, cycle1, cycle2):
        return _failed_run(fixture, cycle1, cycle2)
    materialized = materialize_rehearsed_fixture(fixture, cycle1, cycle2)
    episode = run_no_model_two_cycle_episode(materialized)
    receipt = _receipt(fixture, cycle1, cycle2, episode.receipt(), episode.content_hash)
    return ScriptedRehearsalRun(canonical_hash(receipt), receipt, materialized)


def _exact_fixture_outputs(
    fixture: TwoCycleFixture,
    cycle1: CycleRehearsal,
    cycle2: CycleRehearsal,
) -> bool:
    expected1 = fixture.cycle1_fixture().payload()
    expected2 = fixture.cycle2_fixture().payload()
    return (
        cycle1.products == expected1["group_products"]
        and cycle1.confirmations == expected1["confirmations"]
        and cycle2.products == expected2["group_products"]
        and cycle2.confirmations == expected2["confirmations"]
    )


def _receipt(
    fixture: TwoCycleFixture,
    cycle1: CycleRehearsal,
    cycle2: CycleRehearsal,
    episode: dict[str, Any] | None,
    episode_hash: str | None,
) -> dict[str, Any]:
    portfolio, groups, confirmations = _call_traces(cycle1, cycle2)
    failures = cycle1.failures + cycle2.failures
    receipt = _receipt_identity(fixture, failures, episode)
    receipt.update(
        {
            "cycle_schedules": {
                cycle1.cycle_id: cycle1.schedule,
                cycle2.cycle_id: cycle2.schedule,
            },
            "portfolio_product_calls": portfolio,
            "group_product_calls": groups,
            "confirmation_calls": confirmations,
            "group_product_call_count": len(groups),
            "confirmation_call_count": len(confirmations),
            "failures": failures,
            "episode_run_hash": episode_hash,
            "episode": episode,
        }
    )
    return receipt


def _receipt_identity(
    fixture: TwoCycleFixture,
    failures: list[dict[str, Any]],
    episode: dict[str, Any] | None,
) -> dict[str, Any]:
    return {
        "schema_version": "scripted-room-rehearsal.v0.1",
        "status": "failed" if failures or episode is None else "passed",
        "evidence_status": "scripted_rehearsal_non_evidence",
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "charter_hash": fixture.charter.content_hash,
        "active_seat_ids": list(compile_us_charter(fixture.charter).active_seat_ids()),
    }


def _call_traces(
    cycle1: CycleRehearsal, cycle2: CycleRehearsal
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    return (
        cycle1.portfolio_traces + cycle2.portfolio_traces,
        cycle1.group_traces + cycle2.group_traces,
        cycle1.confirmation_traces + cycle2.confirmation_traces,
    )


def _failed_run(
    fixture: TwoCycleFixture,
    cycle1: CycleRehearsal,
    cycle2: CycleRehearsal | None,
) -> ScriptedRehearsalRun:
    selected = cycle2 or CycleRehearsal("CYCLE_2", [], [], [], [], [], [], [])
    receipt = _receipt(fixture, cycle1, selected, None, None)
    if not receipt["failures"]:
        receipt["failures"] = [
            {"reason_code": "scripted_outputs_do_not_match_retained_fixture"}
        ]
    return ScriptedRehearsalRun(canonical_hash(receipt), receipt, fixture)


__all__ = ["ScriptedRehearsalRun", "run_scripted_two_cycle_rehearsal"]
