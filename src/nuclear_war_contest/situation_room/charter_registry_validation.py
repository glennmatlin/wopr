"""Institution-registry validation for U.S. Room Charters."""

from __future__ import annotations

from typing import Any, cast

from .validation import fail, require_text, require_text_list

REGISTRY_FIELDS = {"seats", "services"}
SEAT_FIELDS = {
    "seat_id",
    "office_class",
    "first_slice_disposition",
    "adviser_status",
    "mandate",
    "supported_contributions",
    "prohibited_actions",
    "information_entitlement_ids",
    "group_ids",
    "activation_predicate_ids",
    "decision_route_roles",
    "persona_posture_ids",
    "represented_role_ids",
    "fact_ids",
    "inference_ids",
}
SERVICE_FIELDS = {
    "service_id",
    "purpose",
    "responsibilities",
    "prohibited_actions",
    "activation_predicate_ids",
    "fact_ids",
    "inference_ids",
}
DISPOSITIONS = {"active", "triggered", "unavailable_without_mandate"}
ADVISER_STATUSES = {
    "voting_principal",
    "non_voting_adviser",
    "non_voting_invitee",
}


def _records(value: object, label: str) -> list[dict[str, Any]]:
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        fail("invalid_envelope", f"{label} must be a record list")
    return cast(list[dict[str, Any]], value)


def _validate_seat(seat: dict[str, Any]) -> None:
    if set(seat) != SEAT_FIELDS:
        fail("invalid_envelope", "seat fields are invalid")
    for field in ("seat_id", "office_class", "mandate"):
        require_text(seat[field], f"seat {field}")
    if seat["first_slice_disposition"] not in DISPOSITIONS:
        fail("invalid_envelope", "seat disposition is invalid")
    if seat["adviser_status"] not in ADVISER_STATUSES:
        fail("invalid_adviser_status", "seat adviser status is invalid")
    list_fields = SEAT_FIELDS - {
        "seat_id",
        "office_class",
        "first_slice_disposition",
        "adviser_status",
        "mandate",
    }
    for field in list_fields:
        require_text_list(seat[field], f"seat {field}")
    if not seat["activation_predicate_ids"]:
        fail("activation_error", "seat has no activation predicate")


def _validate_service(service: dict[str, Any]) -> None:
    if set(service) != SERVICE_FIELDS:
        fail("invalid_envelope", "service fields are invalid")
    for field in ("service_id", "purpose"):
        require_text(service[field], f"service {field}")
    for field in SERVICE_FIELDS - {"service_id", "purpose"}:
        require_text_list(service[field], f"service {field}")
    if not service["activation_predicate_ids"]:
        fail("activation_error", "service has no activation predicate")


def validate_registry(payload: dict[str, Any]) -> tuple[list[dict[str, Any]], ...]:
    registry = payload.get("institution_registry")
    if not isinstance(registry, dict) or set(registry) != REGISTRY_FIELDS:
        fail("invalid_envelope", "institution registry fields are invalid")
    seats = _records(registry["seats"], "seats")
    services = _records(registry["services"], "services")
    if not seats or not services:
        fail("invalid_envelope", "institution registry is incomplete")
    for seat in seats:
        _validate_seat(seat)
    for service in services:
        _validate_service(service)
    return seats, services


__all__ = ["validate_registry"]
