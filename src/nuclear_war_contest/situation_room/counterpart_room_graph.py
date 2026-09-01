"""Outcome-aware execution of a counterpart Room group graph."""

from __future__ import annotations

from typing import Any

from .counterpart_artifacts import CounterpartCharter
from .counterpart_compiled_models import CompiledCounterpartCharter
from .counterpart_room_fixture import CounterpartRoomFixture
from .counterpart_room_products import collect_counterpart_product
from .counterpart_room_schedule import next_counterpart_wave


def _execute_wave(
    charter: CounterpartCharter,
    compiled: CompiledCounterpartCharter,
    fixture: CounterpartRoomFixture,
    wave: tuple[str, ...],
    attempts: list[dict[str, Any]],
    failures: list[dict[str, Any]],
) -> set[str]:
    payload = charter.payload()
    groups = {item["group_id"]: item for item in payload["groups"]}
    schemas = {item["product_schema_id"]: item for item in payload["product_schemas"]}
    products = {item["group_id"]: item for item in fixture.payload()["group_products"]}
    completed: set[str] = set()
    for group_id in wave:
        group = groups[group_id]
        attempt, failure = collect_counterpart_product(
            charter.actor_id,
            group,
            schemas[group["product_schema_id"]],
            compiled,
            products.get(group_id),
        )
        attempts.append(attempt)
        if failure is None:
            completed.add(group_id)
        else:
            failures.append(failure)
    return completed


def _blocked_failure(
    group_id: str, compiled: CompiledCounterpartCharter
) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{group_id}",
        "reason_code": "blocked_dependency",
        "group_id": group_id,
        "failure_effect": compiled.group(group_id).failure_effect,
    }


def execute_counterpart_graph(
    charter: CounterpartCharter,
    compiled: CompiledCounterpartCharter,
    fixture: CounterpartRoomFixture,
) -> tuple[list[list[str]], list[dict[str, Any]], list[dict[str, Any]]]:
    remaining = tuple(compiled.active_group_ids())
    completed: set[str] = set()
    schedule: list[list[str]] = []
    attempts: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    while remaining:
        wave = next_counterpart_wave(compiled, remaining, frozenset(completed))
        if not wave:
            break
        schedule.append(list(wave))
        completed.update(
            _execute_wave(charter, compiled, fixture, wave, attempts, failures)
        )
        remaining = tuple(group_id for group_id in remaining if group_id not in wave)
    failures.extend(_blocked_failure(group_id, compiled) for group_id in remaining)
    return schedule, attempts, failures


__all__ = ["execute_counterpart_graph"]
