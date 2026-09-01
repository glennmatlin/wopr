"""Shared strict record validation for counterpart Room artifacts."""

from __future__ import annotations

from typing import Any

from .validation import fail, require_text, require_text_list


def validate_record(
    record: dict[str, Any],
    label: str,
    *,
    text_fields: set[str],
    list_fields: set[str],
    choice_fields: dict[str, set[str]] | None = None,
    boolean_fields: set[str] | None = None,
    integer_fields: set[str] | None = None,
) -> None:
    choices = choice_fields or {}
    booleans = boolean_fields or set()
    integers = integer_fields or set()
    expected = text_fields | list_fields | set(choices) | booleans | integers
    if set(record) != expected:
        fail("invalid_envelope", f"{label} fields are invalid")
    for field in text_fields:
        require_text(record[field], f"{label} {field}")
    for field in list_fields:
        require_text_list(record[field], f"{label} {field}")
    for field, allowed in choices.items():
        if record[field] not in allowed:
            fail("invalid_envelope", f"{label} {field} is unsupported")
    for field in booleans:
        if not isinstance(record[field], bool):
            fail("invalid_envelope", f"{label} {field} must be boolean")
    for field in integers:
        value = record[field]
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            fail("invalid_envelope", f"{label} {field} must be nonnegative")


__all__ = ["validate_record"]
