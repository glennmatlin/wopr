"""Decision routing and output projection for counterpart Room traces."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .counterpart_artifacts import CounterpartCharter
from .counterpart_compiled_models import CompiledCounterpartCharter
from .counterpart_room_decision_models import CounterpartDecision
from .counterpart_room_decision_routing import (
    decision_failure,
    route_failures,
    route_view,
)
from .counterpart_room_decision_semantics import output_projection_is_valid
from .counterpart_room_fixture import CounterpartRoomFixture


def _confirmation_result(
    item: dict[str, Any] | None,
    confirmation_id: str,
    compiled: CompiledCounterpartCharter,
    route: dict[str, Any],
    record: dict[str, Any],
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    spec = compiled.confirmation(confirmation_id)
    valid = item is not None and (
        item["status"] == "confirmed"
        and tuple(item["confirmer_seat_ids"]) == spec.confirmer_seat_ids
        and item["confirmed_record_id"] == record["product_id"]
    )
    if valid:
        return deepcopy(item), None
    reason = "missing_confirmation" if item is None else "invalid_confirmation"
    failure = decision_failure(
        confirmation_id,
        reason,
        route["eligible_forum_group_id"],
        spec.failure_effect,
    )
    return deepcopy(item), failure


def _confirmations(
    compiled: CompiledCounterpartCharter,
    payload: dict[str, Any],
    route: dict[str, Any],
    record: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    provided = {item["confirmation_id"]: item for item in payload["confirmations"]}
    retained: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for confirmation_id in route["required_confirmation_ids"]:
        item, failure = _confirmation_result(
            provided.get(confirmation_id), confirmation_id, compiled, route, record
        )
        if item is not None:
            retained.append(item)
        if failure is not None:
            failures.append(failure)
    return retained, failures


def _project_output(
    actor_id: str,
    payload: dict[str, Any],
    record: dict[str, Any],
    failure_effect: str,
) -> tuple[dict[str, Any] | None, dict[str, Any] | None, list[dict[str, Any]]]:
    projection = payload["output_projection"]
    if not output_projection_is_valid(actor_id, projection, record):
        failure = decision_failure(
            projection["projection_id"],
            "output_mismatch",
            record["group_id"],
            failure_effect,
        )
        return None, None, [failure]
    return deepcopy(projection), deepcopy(projection["output"]), []


def _finish_decision(
    charter: CounterpartCharter,
    compiled: CompiledCounterpartCharter,
    fixture: CounterpartRoomFixture,
    route: dict[str, Any],
    record: dict[str, Any],
) -> CounterpartDecision:
    payload = fixture.payload()
    failures = route_failures(charter.actor_id, record, payload["action_class"], route)
    confirmations, confirmation_failures = _confirmations(
        compiled, payload, route, record
    )
    failures.extend(confirmation_failures)
    projection, output, output_failures = _project_output(
        charter.actor_id, payload, record, route["failure_effect"]
    )
    failures.extend(output_failures)
    if failures:
        projection = None
        output = None
    return CounterpartDecision(
        route, record, confirmations, projection, output, failures, not failures
    )


def resolve_counterpart_decision(
    charter: CounterpartCharter,
    compiled: CompiledCounterpartCharter,
    fixture: CounterpartRoomFixture,
    attempts: list[dict[str, Any]],
    product_failures: list[dict[str, Any]],
) -> CounterpartDecision:
    action = fixture.payload()["action_class"]
    route = route_view(compiled, action)
    accepted = {
        item["group_id"]: item for item in attempts if item["status"] == "accepted"
    }
    record = accepted.get(route["eligible_forum_group_id"])
    if product_failures or record is None:
        return CounterpartDecision(None, record, [], None, None, [], False)
    return _finish_decision(charter, compiled, fixture, route, record)
