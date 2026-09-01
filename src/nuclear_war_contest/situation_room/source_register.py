"""Source-register loading for the U.S. Room Charter."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

from .source_validation import validate_source_register


@dataclass(frozen=True)
class SourceRegister:
    """A source register bound to its canonical serialized identity."""

    register_id: str
    register_version: str
    content_hash: str
    _payload: dict[str, Any]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)


def load_source_register(path: Path) -> SourceRegister:
    try:
        payload = load_strict_json(path)
    except ValueError as error:
        raise ValueError(f"invalid_envelope: {error}") from error
    if not isinstance(payload, dict):
        raise ValueError("invalid_envelope: U.S. source register must be an object")
    validate_source_register(payload)
    register_id = payload.get("register_id")
    register_version = payload.get("register_version")
    if not isinstance(register_id, str) or not register_id:
        raise ValueError("U.S. source register register_id is invalid")
    if not isinstance(register_version, str) or not register_version:
        raise ValueError("U.S. source register register_version is invalid")
    return SourceRegister(
        register_id=register_id,
        register_version=register_version,
        content_hash=canonical_hash(payload),
        _payload=deepcopy(payload),
    )


__all__ = ["SourceRegister", "load_source_register"]
