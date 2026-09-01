"""One complete scripted U.S. Room cycle."""

from __future__ import annotations

from typing import Any

from .charter import UsCharter
from .compiler import compile_us_charter
from .cycle_deliveries import materialize_product_deliveries, watch_deliveries
from .cycle_fixture import UsCycleFixture
from .cycle_products import collect_product_attempt
from .cycle_schedule import next_execution_wave
from .scripted_rehearsal_confirmations import rehearse_confirmations
from .scripted_rehearsal_context import CycleContext, CycleState
from .scripted_rehearsal_inputs import add_product_content, initial_content_catalog
from .scripted_rehearsal_models import CycleRehearsal, GroupRehearsal
from .scripted_rehearsal_runtime import SeatRuntime
from .scripted_rehearsal_wave import rehearse_wave


def rehearse_cycle(
    charter: UsCharter,
    fixture: UsCycleFixture,
    runtimes: dict[str, SeatRuntime],
    *,
    product_contracts: dict[str, dict[str, Any]] | None = None,
) -> CycleRehearsal:
    context = _cycle_context(charter, fixture, runtimes, product_contracts or {})
    state = _cycle_state(context)
    while state.remaining and _advance_wave(context, state):
        pass
    state.failures.extend(_blocked(group_id) for group_id in state.remaining)
    confirmations, confirmation_traces = _confirm(context, state)
    return CycleRehearsal(
        fixture.cycle_id,
        state.schedule,
        state.products,
        confirmations,
        state.portfolio_traces,
        state.group_traces,
        confirmation_traces,
        state.failures,
    )


def _cycle_context(
    charter: UsCharter,
    fixture: UsCycleFixture,
    runtimes: dict[str, SeatRuntime],
    product_contracts: dict[str, dict[str, Any]],
) -> CycleContext:
    compiled = compile_us_charter(charter)
    payload = charter.payload()
    groups = {item["group_id"]: item for item in payload["groups"]}
    schemas = {item["product_schema_id"]: item for item in payload["product_schemas"]}
    seats = {item["seat_id"]: item for item in payload["institution_registry"]["seats"]}
    return CycleContext(
        charter,
        fixture,
        compiled,
        groups,
        schemas,
        seats,
        runtimes,
        product_contracts,
    )


def _cycle_state(context: CycleContext) -> CycleState:
    initial = watch_deliveries(context.compiled, context.fixture)
    return CycleState(
        tuple(context.compiled.active_group_ids()),
        initial,
        initial,
        initial_content_catalog(context.fixture),
    )


def _advance_wave(context: CycleContext, state: CycleState) -> bool:
    wave = next_execution_wave(
        context.compiled, state.remaining, frozenset(state.completed)
    )
    if not wave:
        return False
    state.schedule.append(list(wave))
    outcomes = rehearse_wave(context, wave, state.deliveries, state.catalog)
    _collect_outcomes(context, state, wave, outcomes)
    state.attempts, state.deliveries = materialize_product_deliveries(
        context.charter,
        context.compiled,
        state.schedule,
        state.attempts,
        state.initial_deliveries,
    )
    state.remaining = tuple(item for item in state.remaining if item not in wave)
    return True


def _collect_outcomes(
    context: CycleContext,
    state: CycleState,
    wave: tuple[str, ...],
    outcomes: list[GroupRehearsal],
) -> None:
    for group_id, outcome in zip(wave, outcomes, strict=True):
        group = context.groups[group_id]
        state.portfolio_traces.extend(outcome.portfolio_traces)
        if outcome.group_trace is not None:
            state.group_traces.append(outcome.group_trace)
        state.failures.extend(outcome.failures)
        attempt, failure = collect_product_attempt(
            group_id,
            group,
            context.schemas[group["product_schema_id"]],
            context.compiled,
            outcome.product,
        )
        state.attempts.append(attempt)
        if failure is None and outcome.product is not None:
            state.completed.add(group_id)
            state.products.append(outcome.product)
            add_product_content(state.catalog, outcome.product)
        elif failure is not None:
            state.failures.append(failure)


def _confirm(
    context: CycleContext, state: CycleState
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if state.failures:
        return [], []
    confirmations, traces, failures = rehearse_confirmations(
        context.charter, context.fixture.payload(), state.products, context.runtimes
    )
    state.failures.extend(failures)
    return confirmations, traces


def _blocked(group_id: str) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{group_id}",
        "reason_code": "blocked_dependency",
        "group_id": group_id,
    }


__all__ = ["rehearse_cycle"]
