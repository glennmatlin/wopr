"""Strict loading for counterpart Room composition fixtures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

from .counterpart_composition_bindings import validate_counterpart_output_bindings
from .counterpart_composition_fixture_shape import (
    ARTIFACT_KEYS,
    validate_counterpart_composition_fixture_shape,
)
from .counterpart_composition_identity import (
    EXPECTED_IDENTITIES,
    validate_exact_composition_receipt,
)
from .counterpart_composition_models import CounterpartCompositionFixture
from .episode_fixture import load_two_cycle_fixture


def _load_object(path: Path, label: str) -> dict[str, Any]:
    payload = load_strict_json(path)
    if not isinstance(payload, dict):
        raise ValueError(f"invalid_envelope: {label} must be an object")
    return payload


def _load_artifacts(
    root: Path, payload: dict[str, Any]
) -> tuple[dict[str, Path], dict[str, dict[str, Any]]]:
    paths = {key: root / payload["artifact_paths"][key] for key in ARTIFACT_KEYS}
    artifacts: dict[str, dict[str, Any]] = {}
    for key, path in paths.items():
        artifact = _load_object(path, f"composition artifact {key}")
        if canonical_hash(artifact) != payload["artifact_hashes"][key]:
            raise ValueError(f"identity_mismatch: composition artifact {key} changed")
        artifacts[key] = artifact
    return paths, artifacts


def load_counterpart_composition_fixture(
    path: Path,
) -> CounterpartCompositionFixture:
    payload = _load_object(path, "counterpart composition fixture")
    validate_counterpart_composition_fixture_shape(payload)
    paths, artifacts = _load_artifacts(path.parent, payload)
    receipts = {
        "d70": artifacts["two_cycle_receipt"],
        "himaldesh": artifacts["himaldesh_room_receipt"],
        "olvana": artifacts["olvana_room_receipt"],
    }
    for key, receipt in receipts.items():
        validate_exact_composition_receipt(key, receipt)
    expected_receipts = {
        key: value["receipt_hash"] for key, value in EXPECTED_IDENTITIES.items()
    }
    if payload["upstream_receipt_hashes"] != expected_receipts:
        raise ValueError("identity_mismatch: composition receipt manifest is invalid")
    two_cycle = load_two_cycle_fixture(paths["two_cycle_fixture"])
    if two_cycle.content_hash != EXPECTED_IDENTITIES["d70"]["fixture_hash"]:
        raise ValueError("identity_mismatch: exact D70 fixture is invalid")
    counterparts = validate_counterpart_output_bindings(payload, two_cycle, receipts)
    return CounterpartCompositionFixture(
        fixture_id=payload["fixture_id"],
        content_hash=canonical_hash(payload),
        two_cycle=two_cycle,
        _payload=payload,
        _receipts=receipts,
        _counterparts=counterparts,
    )


__all__ = ["load_counterpart_composition_fixture"]
