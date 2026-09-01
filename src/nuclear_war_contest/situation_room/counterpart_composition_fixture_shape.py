"""Strict envelope checks for counterpart Room composition fixtures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

ARTIFACT_KEYS = frozenset(
    {
        "two_cycle_fixture",
        "two_cycle_receipt",
        "himaldesh_room_receipt",
        "olvana_room_receipt",
    }
)
RECEIPT_KEYS = frozenset({"d70", "himaldesh", "olvana"})
FIELDS = frozenset(
    {
        "schema_version",
        "fixture_id",
        "fixture_version",
        "status",
        "artifact_paths",
        "artifact_hashes",
        "upstream_receipt_hashes",
        "output_bindings",
    }
)
BINDING_FIELDS = frozenset(
    {
        "actor_id",
        "receipt_key",
        "mapping_owner",
        "mapping_type",
        "projection_id",
        "source_decision_record_id",
        "output_id",
        "output_hash",
        "us_cycle1_input_ids",
    }
)


def _is_hash(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _text_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and len(value) == len(set(value))
        and all(isinstance(item, str) and item for item in value)
    )


def _validate_header(payload: dict[str, Any]) -> None:
    if set(payload) != FIELDS:
        raise ValueError("invalid_envelope: composition fixture fields are invalid")
    fixed = {
        "schema_version": "counterpart-room-composition-fixture.v0.1",
        "status": "development_fixture_non_evidence",
    }
    if any(payload.get(key) != value for key, value in fixed.items()):
        raise ValueError("invalid_envelope: composition fixed fields are invalid")
    for field in ("fixture_id", "fixture_version"):
        if not isinstance(payload.get(field), str) or not payload[field]:
            raise ValueError("invalid_envelope: composition identity is invalid")


def _validate_artifacts(payload: dict[str, Any]) -> None:
    paths = payload.get("artifact_paths")
    hashes = payload.get("artifact_hashes")
    receipts = payload.get("upstream_receipt_hashes")
    if not isinstance(paths, dict) or set(paths) != ARTIFACT_KEYS:
        raise ValueError("invalid_envelope: composition artifact paths are invalid")
    if not isinstance(hashes, dict) or set(hashes) != ARTIFACT_KEYS:
        raise ValueError("invalid_envelope: composition artifact hashes are invalid")
    if not isinstance(receipts, dict) or set(receipts) != RECEIPT_KEYS:
        raise ValueError("invalid_envelope: composition receipt hashes are invalid")
    if any(
        not isinstance(value, str) or not value or Path(value).name != value
        for value in paths.values()
    ):
        raise ValueError("invalid_path: composition artifact path escapes its root")
    if any(not _is_hash(value) for value in [*hashes.values(), *receipts.values()]):
        raise ValueError("invalid_envelope: composition hash is invalid")


def _validate_binding(item: object) -> None:
    if not isinstance(item, dict) or set(item) != BINDING_FIELDS:
        raise ValueError("invalid_envelope: composition binding fields are invalid")
    text_fields = BINDING_FIELDS - {"us_cycle1_input_ids"}
    if any(
        not isinstance(item[field], str) or not item[field] for field in text_fields
    ):
        raise ValueError("invalid_envelope: composition binding is invalid")
    if not _is_hash(item["output_hash"]) or not _text_list(item["us_cycle1_input_ids"]):
        raise ValueError("invalid_envelope: composition binding values are invalid")


def validate_counterpart_composition_fixture_shape(payload: dict[str, Any]) -> None:
    _validate_header(payload)
    _validate_artifacts(payload)
    bindings = payload.get("output_bindings")
    if not isinstance(bindings, list) or len(bindings) != 2:
        raise ValueError("invalid_envelope: composition bindings are invalid")
    for item in bindings:
        _validate_binding(item)


__all__ = ["ARTIFACT_KEYS", "validate_counterpart_composition_fixture_shape"]
