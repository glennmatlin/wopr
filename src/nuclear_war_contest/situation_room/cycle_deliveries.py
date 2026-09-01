"""Charter-derived input and product delivery records."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .charter import UsCharter
from .compiled_models import CompiledUsCharter
from .cycle_delivery_records import product_delivery, watch_delivery
from .cycle_fixture import UsCycleFixture


def watch_deliveries(
    compiled: CompiledUsCharter, fixture: UsCycleFixture
) -> list[dict[str, Any]]:
    deliveries: list[dict[str, Any]] = []
    for item in fixture.payload()["watch_inputs"]:
        entitled = set(
            compiled.recipients_for(item["information_class_id"], item["sender_id"])
        )
        for seat_id in compiled.active_seat_ids():
            if seat_id in entitled:
                deliveries.append(watch_delivery(item, seat_id))
    return deliveries


def materialize_product_deliveries(
    charter: UsCharter,
    compiled: CompiledUsCharter,
    schedule: list[list[str]],
    attempts: list[dict[str, Any]],
    initial: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    attempts = deepcopy(attempts)
    deliveries = deepcopy(initial)
    by_group = {item["group_id"]: item for item in attempts}
    groups = {item["group_id"]: item for item in charter.payload()["groups"]}
    for wave in schedule:
        available = tuple(deliveries)
        for group_id in wave:
            attempt = by_group[group_id]
            attempt["authorized_input_ids"] = _authorized_inputs(
                groups[group_id], compiled, available
            )
        for group_id in wave:
            attempt = by_group[group_id]
            if attempt["status"] == "accepted":
                deliveries.extend(_product_deliveries(charter, compiled, attempt))
    return attempts, deliveries


def decision_deliveries(
    compiled: CompiledUsCharter,
    record: dict[str, Any],
    confirmation_ids: list[str],
) -> list[dict[str, Any]]:
    recipients = set(
        compiled.recipients_for("INFO_DECISION_RECORD", "SERVICE_EXECUTIVE_SECRETARY")
    )
    return [
        product_delivery(
            record,
            "INFO_DECISION_RECORD",
            "SERVICE_EXECUTIVE_SECRETARY",
            seat_id,
            confirmation_ids,
        )
        for seat_id in compiled.active_seat_ids()
        if seat_id in recipients
    ]


def _authorized_inputs(
    group: dict[str, Any],
    compiled: CompiledUsCharter,
    deliveries: tuple[dict[str, Any], ...],
) -> list[str]:
    members = {seat.seat_id for seat in compiled.group_members(group["group_id"])}
    classes = set(group["input_entitlement_ids"])
    return list(
        dict.fromkeys(
            item["artifact_id"]
            for item in deliveries
            if item["recipient_seat_id"] in members
            and item["information_class_id"] in classes
        )
    )


def _product_deliveries(
    charter: UsCharter,
    compiled: CompiledUsCharter,
    attempt: dict[str, Any],
) -> list[dict[str, Any]]:
    group_id = attempt["group_id"]
    information_class = _product_information_class(charter, group_id)
    if information_class is None:
        return []
    recipients = set(compiled.recipients_for(information_class, group_id))
    active_groups = set(compiled.active_group_ids())
    for group in charter.payload()["groups"]:
        if (
            group["group_id"] in active_groups
            and group_id in group["dependency_group_ids"]
            and information_class in group["input_entitlement_ids"]
        ):
            recipients.update(
                seat.seat_id for seat in compiled.group_members(group["group_id"])
            )
    return [
        product_delivery(
            attempt,
            information_class,
            group_id,
            seat_id,
            attempt["authorized_input_ids"],
        )
        for seat_id in compiled.active_seat_ids()
        if seat_id in recipients
    ]


def _product_information_class(charter: UsCharter, group_id: str) -> str | None:
    classes = {
        item["information_class_id"]
        for item in charter.payload()["disclosure_permissions"]
        if group_id in item["sender_ids"]
    }
    if len(classes) > 1:
        raise ValueError("invalid_envelope: product information class is ambiguous")
    return next(iter(classes), None)


__all__ = ["decision_deliveries", "materialize_product_deliveries", "watch_deliveries"]
