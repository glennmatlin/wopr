"""One model-bound group product in the scripted Room rehearsal."""

from __future__ import annotations

from typing import Any

from .free_output_models import SeatProductCall, SeatProductFailure
from .scripted_rehearsal_calls import group_call, portfolio_call
from .scripted_rehearsal_context import GroupContext
from .scripted_rehearsal_inputs import authorized_delivery_bytes
from .scripted_rehearsal_models import GroupRehearsal
from .scripted_rehearsal_validation import group_validator, portfolio_validator


def rehearse_group(
    context: GroupContext,
) -> GroupRehearsal:
    contributions, traces, failure = _collect_portfolios(context)
    if failure is not None:
        return _failed(context.group["group_id"], traces, failure)
    return _record_group_product(context, contributions, traces)


def _collect_portfolios(
    context: GroupContext,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], str | None]:
    contributions: list[dict[str, Any]] = []
    traces: list[dict[str, Any]] = []
    for member in context.compiled.group_members(context.group["group_id"]):
        try:
            product, trace = _produce_portfolio(context, member.seat_id)
        except SeatProductFailure as exc:
            traces.append(exc.snapshot)
            return contributions, traces, member.seat_id
        contributions.append(product)
        traces.append(trace)
    return contributions, traces, None


def _produce_portfolio(
    context: GroupContext, seat_id: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    group = context.group
    delivery_bytes = authorized_delivery_bytes(
        group, seat_id, context.deliveries, context.catalog
    )
    call = portfolio_call(
        context.cycle_id, group, context.seats[seat_id], delivery_bytes
    )
    result = context.runtimes[seat_id].produce(
        call, portfolio_validator(context.cycle_id, group["group_id"], seat_id)
    )
    return result.product(), result.trace()


def _record_group_product(
    context: GroupContext,
    contributions: list[dict[str, Any]],
    traces: list[dict[str, Any]],
) -> GroupRehearsal:
    group = context.group
    recorder_id = context.compiled.group_members(group["group_id"])[0].seat_id
    call = _group_product_call(context, recorder_id, contributions)
    try:
        result = context.runtimes[recorder_id].produce(
            call,
            group_validator(
                group, context.schema, context.compiled, context.product_contract
            ),
        )
    except SeatProductFailure as exc:
        return GroupRehearsal(
            group["group_id"],
            None,
            traces,
            exc.snapshot,
            [_failure(group["group_id"], recorder_id)],
        )
    return GroupRehearsal(
        group["group_id"], result.product(), traces, result.trace(), []
    )


def _group_product_call(
    context: GroupContext, recorder_id: str, contributions: list[dict[str, Any]]
) -> SeatProductCall:
    delivery_bytes = authorized_delivery_bytes(
        context.group, recorder_id, context.deliveries, context.catalog
    )
    return group_call(
        context.cycle_id,
        context.group,
        context.seats[recorder_id],
        delivery_bytes,
        tuple(contributions),
        context.schema,
        context.product_contract,
    )


def _failed(
    group_id: str, traces: list[dict[str, Any]], seat_id: str
) -> GroupRehearsal:
    return GroupRehearsal(group_id, None, traces, None, [_failure(group_id, seat_id)])


def _failure(group_id: str, seat_id: str) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{group_id}::{seat_id}",
        "reason_code": "seat_product_failure",
        "group_id": group_id,
        "seat_id": seat_id,
    }


__all__ = ["rehearse_group"]
