"""Required seat confirmations for scripted Room rehearsal."""

from __future__ import annotations

from typing import Any

from .charter import UsCharter
from .free_output_models import SeatProductFailure
from .scripted_rehearsal_calls import confirmation_call
from .scripted_rehearsal_runtime import SeatRuntime
from .scripted_rehearsal_validation import confirmation_validator


def rehearse_confirmations(
    charter: UsCharter,
    cycle: dict[str, Any],
    products: list[dict[str, Any]],
    runtimes: dict[str, SeatRuntime],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    seats, specs, group_id, decision = _confirmation_inputs(charter, cycle, products)
    confirmations: list[dict[str, Any]] = []
    traces: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for expected in cycle["confirmations"]:
        spec = specs[expected["confirmation_id"]]
        confirmed = _rehearse_one(
            cycle["cycle_id"],
            group_id,
            expected,
            spec,
            decision,
            seats,
            runtimes,
            traces,
            failures,
        )
        if confirmed:
            confirmations.append(expected)
    return confirmations, traces, failures


def _confirmation_inputs(
    charter: UsCharter,
    cycle: dict[str, Any],
    products: list[dict[str, Any]],
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    str,
    dict[str, Any],
]:
    payload = charter.payload()
    seats = {item["seat_id"]: item for item in payload["institution_registry"]["seats"]}
    specs = {
        item["confirmation_id"]: item for item in payload["required_confirmations"]
    }
    group_id = _route(payload, cycle["action_class"])["eligible_forum_group_id"]
    decision = next(item for item in products if item["group_id"] == group_id)
    return seats, specs, group_id, decision


def _rehearse_one(
    cycle_id: str,
    group_id: str,
    expected: dict[str, Any],
    specification: dict[str, Any],
    decision: dict[str, Any],
    seats: dict[str, dict[str, Any]],
    runtimes: dict[str, SeatRuntime],
    traces: list[dict[str, Any]],
    failures: list[dict[str, Any]],
) -> bool:
    for seat_id in specification["confirmer_seat_ids"]:
        call = confirmation_call(
            cycle_id, group_id, seats[seat_id], specification, decision
        )
        validator = confirmation_validator(
            cycle_id, specification, seat_id, expected["confirmed_record_id"]
        )
        try:
            result = runtimes[seat_id].produce(call, validator)
        except SeatProductFailure as exc:
            traces.append(exc.snapshot)
            failures.append(_failure(expected["confirmation_id"], seat_id))
            return False
        traces.append(result.trace())
    return True


def _route(payload: dict[str, Any], action_class: str) -> dict[str, Any]:
    return next(
        item
        for item in payload["decision_routes"]
        if item["action_class"] == action_class
    )


def _failure(confirmation_id: str, seat_id: str) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{confirmation_id}::{seat_id}",
        "reason_code": "seat_confirmation_failure",
        "confirmation_id": confirmation_id,
        "seat_id": seat_id,
    }


__all__ = ["rehearse_confirmations"]
