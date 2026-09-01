"""Fail-closed validation for actor source registers."""

from __future__ import annotations

from typing import Any

from .source_validation import REGISTER_FIELDS, validate_source_register
from .validation import fail, reject_officeholder_fields, require_text

ACTOR_REGISTER_FIELDS = REGISTER_FIELDS | {"actor_id"}


def validate_actor_source_register(payload: dict[str, Any]) -> None:
    reject_officeholder_fields(payload)
    if set(payload) != ACTOR_REGISTER_FIELDS:
        fail("invalid_envelope", "actor source-register fields are invalid")
    if payload.get("schema_version") != "actor-source-register.v0.1":
        fail("invalid_envelope", "actor source-register schema is unsupported")
    require_text(payload.get("actor_id"), "actor source-register actor_id")
    compatible = {field: payload[field] for field in REGISTER_FIELDS}
    compatible["schema_version"] = "us-source-register.v0.1"
    validate_source_register(compatible)


__all__ = ["validate_actor_source_register"]
