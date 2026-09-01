"""Institution-record validation for counterpart Room Charters."""

from __future__ import annotations

from typing import Any, cast

from .counterpart_record_validation import validate_record
from .validation import fail

SEAT_TEXT = {"seat_id", "office_class", "mandate"}
SEAT_LISTS = {
    "supported_contributions",
    "prohibited_actions",
    "information_entitlement_ids",
    "group_ids",
    "activation_predicate_ids",
    "decision_route_roles",
    "persona_posture_ids",
    "fact_ids",
    "inference_ids",
}
PARTICIPATION_CLASSES = {
    "formal_state_principal",
    "institutional_integrator",
    "nca_portfolio_adviser",
    "party_state_decider",
    "political_decider",
    "portfolio_adviser",
    "professional_adviser",
}
SERVICE_TEXT = {"service_id", "purpose"}
SERVICE_LISTS = {
    "responsibilities",
    "prohibited_actions",
    "activation_predicate_ids",
    "fact_ids",
    "inference_ids",
}


def _records(value: object, label: str) -> list[dict[str, Any]]:
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        fail("invalid_envelope", f"{label} must be a record list")
    return cast(list[dict[str, Any]], value)


def _validate_seat(seat: dict[str, Any]) -> None:
    validate_record(
        seat,
        "counterpart seat",
        text_fields=SEAT_TEXT,
        list_fields=SEAT_LISTS,
        choice_fields={
            "first_episode_disposition": {"active"},
            "participation_class": PARTICIPATION_CLASSES,
        },
    )
    if not seat["activation_predicate_ids"]:
        fail("activation_error", "counterpart seat has no activation predicate")


def _validate_service(service: dict[str, Any]) -> None:
    validate_record(
        service,
        "counterpart service",
        text_fields=SERVICE_TEXT,
        list_fields=SERVICE_LISTS,
    )
    if not service["activation_predicate_ids"]:
        fail("activation_error", "counterpart service has no activation predicate")


def validate_counterpart_registry(
    payload: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    registry = payload.get("institution_registry")
    if not isinstance(registry, dict) or set(registry) != {"seats", "services"}:
        fail("invalid_envelope", "counterpart institution registry is invalid")
    seats = _records(registry["seats"], "counterpart seats")
    services = _records(registry["services"], "counterpart services")
    if not seats or not services:
        fail("invalid_envelope", "counterpart institution registry is incomplete")
    for seat in seats:
        _validate_seat(seat)
    for service in services:
        _validate_service(service)
    return seats, services


__all__ = ["validate_counterpart_registry"]
