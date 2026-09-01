"""U.S. Room Charter loading."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

from .charter_validation import validate_charter
from .source_register import SourceRegister


@dataclass(frozen=True)
class UsCharter:
    """A U.S. Charter bound to its source snapshot and canonical identity."""

    charter_id: str
    charter_version: str
    source_register_hash: str
    content_hash: str
    _payload: dict[str, Any]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)


def load_us_charter(path: Path, source_register: SourceRegister) -> UsCharter:
    try:
        payload = load_strict_json(path)
    except ValueError as error:
        raise ValueError(f"invalid_envelope: {error}") from error
    if not isinstance(payload, dict):
        raise ValueError("invalid_envelope: U.S. Charter must be an object")
    validate_charter(payload, source_register)
    charter_id = payload.get("charter_id")
    charter_version = payload.get("charter_version")
    if not isinstance(charter_id, str) or not charter_id:
        raise ValueError("invalid_envelope: Charter charter_id is invalid")
    if not isinstance(charter_version, str) or not charter_version:
        raise ValueError("invalid_envelope: Charter charter_version is invalid")
    return UsCharter(
        charter_id=charter_id,
        charter_version=charter_version,
        source_register_hash=source_register.content_hash,
        content_hash=canonical_hash(payload),
        _payload=deepcopy(payload),
    )


__all__ = ["UsCharter", "load_us_charter"]
