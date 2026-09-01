"""Shared strict-validation primitives for Situation Room artifacts."""

from __future__ import annotations

from datetime import date
from typing import Any, NoReturn, cast

FORBIDDEN_OFFICEHOLDER_FIELDS = {
    "current_officeholder",
    "current_officeholder_name",
    "officeholder",
    "person_name",
}


def fail(reason_code: str, detail: str) -> NoReturn:
    raise ValueError(f"{reason_code}: {detail}")


def reject_officeholder_fields(value: Any) -> None:
    if isinstance(value, dict):
        if FORBIDDEN_OFFICEHOLDER_FIELDS & set(value):
            fail(
                "forbidden_officeholder_field", "artifact names a current officeholder"
            )
        for item in value.values():
            reject_officeholder_fields(item)
    elif isinstance(value, list):
        for item in value:
            reject_officeholder_fields(item)


def require_text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        fail("invalid_envelope", f"{label} must be non-empty text")
    return cast(str, value)


def require_text_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item for item in value
    ):
        fail("invalid_envelope", f"{label} must be a text list")
    if len(value) != len(set(value)):
        fail("duplicate_id", f"{label} repeats an identity")
    return cast(list[str], value)


def require_date(value: object, label: str, optional: bool = False) -> None:
    if value is None and optional:
        return
    text = require_text(value, label)
    try:
        date.fromisoformat(text)
    except ValueError:
        fail("invalid_envelope", f"{label} is not an ISO date")


def require_records(payload: dict[str, Any], field: str) -> list[dict[str, Any]]:
    value = payload.get(field)
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        fail("invalid_envelope", f"{field} must be a record list")
    return cast(list[dict[str, Any]], value)


__all__ = [
    "fail",
    "reject_officeholder_fields",
    "require_date",
    "require_records",
    "require_text",
    "require_text_list",
]
