"""Deterministic no-model execution for one counterpart Room."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .counterpart_artifacts import CounterpartCharter
from .counterpart_compiled_models import CompiledCounterpartCharter
from .counterpart_compiler import compile_counterpart_charter
from .counterpart_room_decision import resolve_counterpart_decision
from .counterpart_room_decision_models import CounterpartDecision
from .counterpart_room_deliveries import (
    materialize_counterpart_deliveries,
    watch_deliveries,
)
from .counterpart_room_fixture import CounterpartRoomFixture
from .counterpart_room_graph import execute_counterpart_graph

RoomExecution = tuple[
    CompiledCounterpartCharter,
    list[list[str]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    CounterpartDecision | None,
]


@dataclass(frozen=True)
class CounterpartRoomRun:
    fixture_hash: str
    content_hash: str
    _receipt: dict[str, Any]
    _fixture: CounterpartRoomFixture

    def receipt(self) -> dict[str, Any]:
        return deepcopy(self._receipt)

    def fixture(self) -> CounterpartRoomFixture:
        return self._fixture


def _blocked_failure(action: str, gaps: tuple[str, ...]) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::BLOCKED::{action}",
        "reason_code": "blocked_action_class",
        "action_class": action,
        "gap_ids": list(gaps),
        "failure_effect": "no_external_state_change",
    }


def _execute_room(
    charter: CounterpartCharter, fixture: CounterpartRoomFixture
) -> RoomExecution:
    compiled = compile_counterpart_charter(charter)
    payload = fixture.payload()
    action = payload["action_class"]
    blocked_gaps = compiled.blocked_gap_ids(action)
    schedule: list[list[str]] = []
    attempts: list[dict[str, Any]] = []
    deliveries = watch_deliveries(compiled, fixture)
    failures = [_blocked_failure(action, blocked_gaps)] if blocked_gaps else []
    decision = None
    if not blocked_gaps:
        schedule, attempts, failures = execute_counterpart_graph(
            charter, compiled, fixture
        )
        attempts, deliveries = materialize_counterpart_deliveries(
            charter, compiled, schedule, attempts, deliveries
        )
        decision = resolve_counterpart_decision(
            charter, compiled, fixture, attempts, failures
        )
        failures.extend(decision.failures)
    return compiled, schedule, attempts, deliveries, failures, decision


def _identity_fields(
    charter: CounterpartCharter,
    fixture: CounterpartRoomFixture,
    compiled: CompiledCounterpartCharter,
    action: str,
) -> dict[str, Any]:
    return {
        "schema_version": "counterpart-room-run.v0.1",
        "evidence_status": "development_fixture_non_evidence",
        "actor_id": charter.actor_id,
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "ratification_hash": fixture.ratification_hash,
        "source_register_hash": charter.source_register_hash,
        "charter_hash": charter.content_hash,
        "action_class": action,
        "active_seat_ids": list(compiled.active_seat_ids()),
    }


def _decision_fields(decision: CounterpartDecision | None) -> dict[str, Any]:
    return {
        "decision_route": decision.route if decision else None,
        "decision_record": decision.record if decision else None,
        "confirmations": decision.confirmations if decision else [],
        "decision_supported": decision.supported if decision else False,
        "output_projection": decision.projection if decision else None,
        "output": decision.output if decision else None,
    }


def _run_receipt(
    charter: CounterpartCharter,
    fixture: CounterpartRoomFixture,
    execution: RoomExecution,
) -> dict[str, Any]:
    compiled, schedule, attempts, deliveries, failures, decision = execution
    receipt = _identity_fields(
        charter, fixture, compiled, fixture.payload()["action_class"]
    )
    receipt["status"] = "failed" if failures else "passed"
    receipt.update(
        {
            "deliveries": deliveries,
            "schedule": schedule,
            "group_attempts": attempts,
            "failures": failures,
            "world_effects_admitted": False,
        }
    )
    receipt.update(_decision_fields(decision))
    return receipt


def run_no_model_counterpart_room(
    charter: CounterpartCharter, fixture: CounterpartRoomFixture
) -> CounterpartRoomRun:
    receipt = _run_receipt(charter, fixture, _execute_room(charter, fixture))
    return CounterpartRoomRun(
        fixture_hash=fixture.content_hash,
        content_hash=canonical_hash(receipt),
        _receipt=deepcopy(receipt),
        _fixture=fixture,
    )


__all__ = ["CounterpartRoomRun", "run_no_model_counterpart_room"]
