"""Source-bound counterpart Room artifact loading."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

from .counterpart_charter_validation import validate_counterpart_charter
from .counterpart_source_validation import validate_actor_source_register


@dataclass(frozen=True)
class ActorSourceRegister:
    """An actor source register bound to its canonical serialized identity."""

    register_id: str
    register_version: str
    actor_id: str
    content_hash: str
    _payload: dict[str, Any]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)


@dataclass(frozen=True)
class CounterpartCharter:
    """A counterpart Charter bound to one actor source register."""

    charter_id: str
    charter_version: str
    actor_id: str
    source_register_hash: str
    content_hash: str
    _payload: dict[str, Any]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)


def _load_object(path: Path, label: str) -> dict[str, Any]:
    try:
        payload = load_strict_json(path)
    except ValueError as error:
        raise ValueError(f"invalid_envelope: {error}") from error
    if not isinstance(payload, dict):
        raise ValueError(f"invalid_envelope: {label} must be an object")
    return payload


def load_actor_source_register(path: Path) -> ActorSourceRegister:
    payload = _load_object(path, "actor source register")
    validate_actor_source_register(payload)
    return ActorSourceRegister(
        register_id=payload["register_id"],
        register_version=payload["register_version"],
        actor_id=payload["actor_id"],
        content_hash=canonical_hash(payload),
        _payload=deepcopy(payload),
    )


def load_counterpart_charter(
    path: Path, source_register: ActorSourceRegister
) -> CounterpartCharter:
    payload = _load_object(path, "counterpart Charter")
    validate_counterpart_charter(payload, source_register)
    return CounterpartCharter(
        charter_id=payload["charter_id"],
        charter_version=payload["charter_version"],
        actor_id=payload["actor_id"],
        source_register_hash=source_register.content_hash,
        content_hash=canonical_hash(payload),
        _payload=deepcopy(payload),
    )


__all__ = [
    "ActorSourceRegister",
    "CounterpartCharter",
    "load_actor_source_register",
    "load_counterpart_charter",
]
