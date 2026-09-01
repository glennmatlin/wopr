"""Deterministic no-model U.S. Room cycle execution."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .charter import UsCharter
from .compiler import compile_us_charter
from .cycle_decision import resolve_cycle_decision
from .cycle_deliveries import (
    decision_deliveries,
    materialize_product_deliveries,
    watch_deliveries,
)
from .cycle_fixture import UsCycleFixture
from .cycle_graph import execute_product_graph


@dataclass(frozen=True)
class UsCycleRun:
    fixture_hash: str
    content_hash: str
    _receipt: dict[str, Any]
    _fixture: UsCycleFixture

    def receipt(self) -> dict[str, Any]:
        return deepcopy(self._receipt)

    def fixture(self) -> UsCycleFixture:
        return self._fixture


def run_no_model_us_cycle(charter: UsCharter, fixture: UsCycleFixture) -> UsCycleRun:
    compiled = compile_us_charter(charter)
    payload = fixture.payload()
    schedule, attempts, failures = execute_product_graph(charter, compiled, fixture)
    attempts, deliveries = materialize_product_deliveries(
        charter,
        compiled,
        schedule,
        attempts,
        watch_deliveries(compiled, fixture),
    )
    decision = resolve_cycle_decision(charter, fixture, attempts, failures)
    failures.extend(decision.failures)
    if decision.supported and decision.record is not None:
        deliveries.extend(
            decision_deliveries(
                compiled,
                decision.record,
                [item["confirmation_id"] for item in decision.confirmations],
            )
        )
    receipt: dict[str, Any] = {
        "schema_version": "us-cycle-run.v0.1",
        "status": "failed" if failures else "passed",
        "evidence_status": "development_fixture_non_evidence",
        "cycle_id": fixture.cycle_id,
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "ratification_hash": fixture.ratification_hash,
        "source_register_hash": payload["source_register_hash"],
        "charter_hash": charter.content_hash,
        "active_seat_ids": list(compiled.active_seat_ids()),
        "deliveries": deliveries,
        "schedule": schedule,
        "group_attempts": attempts,
        "policy_package": decision.policy_package,
        "decision_route": decision.route,
        "decision_record": decision.record,
        "confirmations": decision.confirmations,
        "decision_supported": decision.supported,
        "failures": failures,
        "world_effects_admitted": False,
    }
    return UsCycleRun(
        fixture_hash=fixture.content_hash,
        content_hash=canonical_hash(receipt),
        _receipt=deepcopy(receipt),
        _fixture=fixture,
    )


__all__ = ["UsCycleRun", "run_no_model_us_cycle"]
