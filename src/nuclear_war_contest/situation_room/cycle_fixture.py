"""No-model U.S. Cycle 1 development fixture loading."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

from .charter import UsCharter
from .cycle_fixture_references import validate_cycle_fixture_references
from .cycle_fixture_validation import validate_cycle_fixture_shape

_D67_RATIFICATION_HASH = (
    "0b831d55ba60dd458e44b0e63d714a82eaf05b508a32694f96181caba0b5ad13"
)


@dataclass(frozen=True)
class UsCycleFixture:
    fixture_id: str
    cycle_id: str
    ratification_hash: str
    content_hash: str
    _payload: dict[str, Any]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)


def load_us_cycle_fixture(
    path: Path,
    charter: UsCharter,
    ratification_path: Path,
    *,
    expected_cycle_id: str = "CYCLE_1",
    external_parent_ids: frozenset[str] = frozenset(),
) -> UsCycleFixture:
    payload = load_strict_json(path)
    ratification = load_strict_json(ratification_path)
    if not isinstance(payload, dict) or not isinstance(ratification, dict):
        raise ValueError("invalid_envelope: cycle artifacts must be objects")
    return load_us_cycle_fixture_payload(
        payload,
        charter,
        ratification,
        expected_cycle_id=expected_cycle_id,
        external_parent_ids=external_parent_ids,
    )


def load_us_cycle_fixture_payload(
    payload: dict[str, Any],
    charter: UsCharter,
    ratification: dict[str, Any],
    *,
    expected_cycle_id: str,
    external_parent_ids: frozenset[str] = frozenset(),
) -> UsCycleFixture:
    if expected_cycle_id not in {"CYCLE_1", "CYCLE_2"}:
        raise ValueError("invalid_envelope: expected cycle identity is invalid")
    validate_cycle_fixture_shape(payload, charter, ratification, expected_cycle_id)
    ratification_hash = canonical_hash(ratification)
    if ratification_hash != _D67_RATIFICATION_HASH:
        raise ValueError("identity_mismatch: D67 ratification identity is invalid")
    if payload.get("ratification_hash") != ratification_hash:
        raise ValueError("identity_mismatch: cycle ratification hash is invalid")
    if payload.get("source_register_hash") != charter.source_register_hash:
        detail = "cycle source register hash is not ratified"
        raise ValueError(f"identity_mismatch: {detail}")
    if payload.get("charter_hash") != charter.content_hash:
        raise ValueError("identity_mismatch: cycle Charter hash is not ratified")
    validate_cycle_fixture_references(payload, charter, external_parent_ids)
    return UsCycleFixture(
        fixture_id=payload["fixture_id"],
        cycle_id=payload["cycle_id"],
        ratification_hash=ratification_hash,
        content_hash=canonical_hash(payload),
        _payload=deepcopy(payload),
    )


__all__ = [
    "UsCycleFixture",
    "load_us_cycle_fixture",
    "load_us_cycle_fixture_payload",
]
