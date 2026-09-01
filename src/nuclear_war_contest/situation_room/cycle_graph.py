"""Outcome-aware execution of the active U.S. group graph."""

from __future__ import annotations

from typing import Any

from .charter import UsCharter
from .compiled_models import CompiledUsCharter
from .cycle_fixture import UsCycleFixture
from .cycle_products import collect_product_attempt
from .cycle_schedule import next_execution_wave


def execute_product_graph(
    charter: UsCharter,
    compiled: CompiledUsCharter,
    fixture: UsCycleFixture,
) -> tuple[list[list[str]], list[dict[str, Any]], list[dict[str, Any]]]:
    payload = charter.payload()
    groups = {item["group_id"]: item for item in payload["groups"]}
    schemas = {item["product_schema_id"]: item for item in payload["product_schemas"]}
    products = {item["group_id"]: item for item in fixture.payload()["group_products"]}
    remaining = tuple(compiled.active_group_ids())
    completed: set[str] = set()
    schedule: list[list[str]] = []
    attempts: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    while remaining:
        wave = next_execution_wave(compiled, remaining, frozenset(completed))
        if not wave:
            break
        schedule.append(list(wave))
        for group_id in wave:
            group = groups[group_id]
            attempt, failure = collect_product_attempt(
                group_id,
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
        remaining = tuple(group_id for group_id in remaining if group_id not in wave)
    failures.extend(_blocked_failure(group_id) for group_id in remaining)
    return schedule, attempts, failures


def _blocked_failure(group_id: str) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{group_id}",
        "reason_code": "blocked_dependency",
        "group_id": group_id,
    }


__all__ = ["execute_product_graph"]
