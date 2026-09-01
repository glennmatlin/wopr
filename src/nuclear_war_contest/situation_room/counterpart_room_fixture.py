"""Loading for source-bound deterministic counterpart Room fixtures."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

from .counterpart_artifacts import CounterpartCharter
from .counterpart_room_fixture_references import (
    validate_counterpart_room_fixture_references,
)
from .counterpart_room_fixture_shape import validate_counterpart_room_fixture_shape
from .validation import fail

D72_RATIFICATION_HASH = (
    "bbab62ea681f2e513407b926de5adfbfaeb8e73baf5fb86ea34808b9fa524384"
)


@dataclass(frozen=True)
class CounterpartRoomFixture:
    fixture_id: str
    actor_id: str
    ratification_hash: str
    content_hash: str
    _payload: dict[str, Any]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)


def _load_object(path: Path, label: str) -> dict[str, Any]:
    payload = load_strict_json(path)
    if not isinstance(payload, dict):
        fail("invalid_envelope", f"{label} must be an object")
    return payload


def _validate_ratification(
    payload: dict[str, Any],
    ratification: dict[str, Any],
    charter: CounterpartCharter,
) -> None:
    ratification_hash = canonical_hash(ratification)
    fixed = {
        "status": "ratified",
        "decision_id": "D72",
        "ratification_id": payload["ratification_id"],
    }
    if ratification_hash != D72_RATIFICATION_HASH or any(
        ratification.get(field) != value for field, value in fixed.items()
    ):
        fail("identity_mismatch", "counterpart ratification identity is invalid")
    bundles = {item["actor_id"]: item for item in ratification.get("actor_bundles", [])}
    bundle = bundles.get(charter.actor_id)
    if not isinstance(bundle, dict):
        fail("identity_mismatch", "counterpart actor is not ratified")
    expected = (charter.source_register_hash, charter.content_hash)
    observed = (bundle.get("source_register_hash"), bundle.get("charter_hash"))
    if observed != expected or payload["ratification_hash"] != ratification_hash:
        fail("identity_mismatch", "counterpart fixture is not ratified")


def load_counterpart_room_fixture(
    path: Path,
    charter: CounterpartCharter,
    ratification_path: Path,
) -> CounterpartRoomFixture:
    payload = _load_object(path, "counterpart Room fixture")
    ratification = _load_object(ratification_path, "counterpart ratification")
    validate_counterpart_room_fixture_shape(payload)
    if payload["actor_id"] != charter.actor_id:
        fail("identity_mismatch", "counterpart fixture actor is invalid")
    expected = (charter.source_register_hash, charter.content_hash)
    observed = (payload["source_register_hash"], payload["charter_hash"])
    if observed != expected:
        fail("identity_mismatch", "counterpart fixture bundle is invalid")
    _validate_ratification(payload, ratification, charter)
    validate_counterpart_room_fixture_references(payload, charter)
    return CounterpartRoomFixture(
        fixture_id=payload["fixture_id"],
        actor_id=payload["actor_id"],
        ratification_hash=payload["ratification_hash"],
        content_hash=canonical_hash(payload),
        _payload=deepcopy(payload),
    )


__all__ = ["CounterpartRoomFixture", "load_counterpart_room_fixture"]
