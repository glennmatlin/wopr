"""Charter-derived delivery records for counterpart Room traces."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .counterpart_artifacts import CounterpartCharter
from .counterpart_compiled_models import CompiledCounterpartCharter
from .counterpart_room_fixture import CounterpartRoomFixture


def watch_deliveries(
    compiled: CompiledCounterpartCharter, fixture: CounterpartRoomFixture
) -> list[dict[str, Any]]:
    deliveries: list[dict[str, Any]] = []
    for item in fixture.payload()["watch_inputs"]:
        recipients = set(
            compiled.recipients_for(item["information_class_id"], item["sender_id"])
        )
        for seat_id in compiled.active_seat_ids():
            if seat_id in recipients:
                deliveries.append(
                    {
                        "delivery_id": f"DELIVERY::{item['input_id']}::{seat_id}",
                        "artifact_id": item["input_id"],
                        "artifact_type": "watch_input",
                        "information_class_id": item["information_class_id"],
                        "sender_id": item["sender_id"],
                        "recipient_seat_id": seat_id,
                        "content_hash": canonical_hash(item["content"]),
                    }
                )
    return deliveries


def _information_class(charter: CounterpartCharter, group_id: str) -> str | None:
    classes = {
        item["information_class_id"]
        for item in charter.payload()["disclosure_permissions"]
        if group_id in item["sender_ids"]
    }
    if len(classes) > 1:
        raise ValueError("invalid_envelope: counterpart product class is ambiguous")
    return next(iter(classes), None)


def _authorized_inputs(
    compiled: CompiledCounterpartCharter,
    group_id: str,
    deliveries: tuple[dict[str, Any], ...],
) -> list[str]:
    group = compiled.group(group_id)
    members = {seat.seat_id for seat in group.members}
    classes = set(group.input_entitlement_ids)
    return list(
        dict.fromkeys(
            item["artifact_id"]
            for item in deliveries
            if item["recipient_seat_id"] in members
            and item["information_class_id"] in classes
        )
    )


def _product_deliveries(
    charter: CounterpartCharter,
    compiled: CompiledCounterpartCharter,
    attempt: dict[str, Any],
) -> list[dict[str, Any]]:
    group_id = attempt["group_id"]
    information_class = _information_class(charter, group_id)
    if information_class is None:
        return []
    recipients = set(compiled.recipients_for(information_class, group_id))
    return [
        {
            "delivery_id": f"DELIVERY::{attempt['product_id']}::{seat_id}",
            "artifact_id": attempt["product_id"],
            "artifact_type": "group_product",
            "information_class_id": information_class,
            "sender_id": group_id,
            "recipient_seat_id": seat_id,
            "content_hash": attempt["content_hash"],
        }
        for seat_id in compiled.active_seat_ids()
        if seat_id in recipients
    ]


def materialize_counterpart_deliveries(
    charter: CounterpartCharter,
    compiled: CompiledCounterpartCharter,
    schedule: list[list[str]],
    attempts: list[dict[str, Any]],
    initial: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    attempts = deepcopy(attempts)
    deliveries = deepcopy(initial)
    by_group = {item["group_id"]: item for item in attempts}
    for wave in schedule:
        available = tuple(deliveries)
        for group_id in wave:
            by_group[group_id]["authorized_input_ids"] = _authorized_inputs(
                compiled, group_id, available
            )
        for group_id in wave:
            attempt = by_group[group_id]
            if attempt["status"] == "accepted":
                deliveries.extend(_product_deliveries(charter, compiled, attempt))
    return attempts, deliveries


__all__ = ["materialize_counterpart_deliveries", "watch_deliveries"]
