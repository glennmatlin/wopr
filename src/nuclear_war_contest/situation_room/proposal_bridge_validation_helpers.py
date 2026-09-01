"""Shared strict proposal bridge shape checks."""

from __future__ import annotations

from typing import Any


def require_record(value: Any, fields: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"invalid_envelope: {label} fields are invalid")
    return value


def require_text(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value:
        raise ValueError(f"invalid_envelope: {label} must be nonempty text")


def require_texts(item: dict[str, Any], fields: tuple[str, ...]) -> None:
    for field in fields:
        require_text(item[field], field)


def require_text_list(value: Any, label: str) -> None:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item for item in value
    ):
        raise ValueError(f"invalid_envelope: {label} must be a text list")
    if len(value) != len(set(value)):
        raise ValueError(f"duplicate_id: {label} contains duplicates")


__all__ = ["require_record", "require_text", "require_text_list", "require_texts"]
