"""Validation for the retained, no-provider fixture measurement artifact."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from nuclear_war_env.integer_validation import is_strict_int

from .preflight_types import CandidateManifest

_FIELDS = {
    "schema_version",
    "producer_command",
    "source_manifest_path",
    "source_manifest_hash",
    "backend",
    "conditions",
    "max_turns",
    "member_count",
    "measurements",
    "observed_max_member_calls",
    "observed_max_full_press_messages",
    "status",
}
_ROW_FIELDS = {"seed", "turns", "deliberations", "member_calls", "full_press_messages"}
_CONDITIONS = (
    "no_press_sole_authority",
    "full_press_sole_authority",
    "no_press_council",
    "full_press_council",
)


def validate_fixture_measurement(
    manifest: CandidateManifest, *, base_dir: Path | None = None
) -> None:
    root = base_dir or Path(__file__).resolve().parents[2] / "docs" / "contest"
    path = Path(manifest.fixture_measurement_path)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("Measurement path must be relative to the contest packet")
    artifact_path = root / path
    _validate_hash(artifact_path, manifest.fixture_measurement_artifact_hash)
    artifact = _read_object(artifact_path, "measurement artifact")
    _validate_artifact(artifact, manifest)
    source_name = artifact["source_manifest_path"]
    if not isinstance(source_name, str) or not source_name:
        raise ValueError("Measurement source path is invalid")
    source_path = artifact_path.parent / source_name
    if Path(source_name).is_absolute() or ".." in Path(source_name).parts:
        raise ValueError("Measurement source path must be relative")
    _validate_hash(source_path, manifest.fixture_measurement_manifest_hash)
    source = _read_object(source_path, "measurement source manifest")
    _validate_source(source, artifact, manifest.preflight_seeds)


def _validate_artifact(artifact: dict[str, Any], manifest: CandidateManifest) -> None:
    if set(artifact) != _FIELDS or artifact["schema_version"] != 1:
        raise ValueError("Measurement artifact fields are invalid")
    if artifact["backend"] != "concordia_first_legal":
        raise ValueError("Measurement backend is invalid")
    if artifact["conditions"] != list(_CONDITIONS):
        raise ValueError("Measurement conditions are invalid")
    if artifact["max_turns"] != 40 or artifact["member_count"] != 3:
        raise ValueError("Measurement run bounds are invalid")
    if artifact["status"] != "offline_planning_input_not_study_result":
        raise ValueError("Measurement status is invalid")
    rows = artifact["measurements"]
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("Measurement rows are invalid")
    for row in rows:
        _validate_row(row, artifact["member_count"], artifact["max_turns"])
    row_seeds = [row["seed"] for row in rows]
    if len(rows) != len(manifest.preflight_seeds) or set(row_seeds) != set(
        manifest.preflight_seeds
    ):
        raise ValueError("Measurement seeds do not match preflight seeds")
    if artifact["observed_max_member_calls"] != max(
        row["member_calls"] for row in rows
    ):
        raise ValueError("Measurement member-call maximum is invalid")
    if artifact["observed_max_full_press_messages"] != max(
        row["full_press_messages"] for row in rows
    ):
        raise ValueError("Measurement press maximum is invalid")
    if artifact["observed_max_member_calls"] != manifest.observed_c2_calls_per_game:
        raise ValueError("Candidate C2 observation does not match measurement")
    if (
        artifact["observed_max_full_press_messages"]
        != manifest.observed_press_calls_per_game
    ):
        raise ValueError("Candidate press observation does not match measurement")
    if artifact["source_manifest_hash"] != manifest.fixture_measurement_manifest_hash:
        raise ValueError("Measurement source hash does not match candidate")


def _validate_row(row: Any, member_count: int, max_turns: int) -> None:
    if not isinstance(row, dict) or set(row) != _ROW_FIELDS:
        raise ValueError("Measurement row fields are invalid")
    for field in _ROW_FIELDS:
        if not is_strict_int(row[field]) or row[field] < 0:
            raise ValueError(f"Measurement row {field} is invalid")
    if row["seed"] <= 0 or row["turns"] > max_turns:
        raise ValueError("Measurement row bounds are invalid")
    if row["member_calls"] != row["deliberations"] * member_count:
        raise ValueError("Measurement member-call count is invalid")


def _validate_source(
    source: dict[str, Any], artifact: dict[str, Any], seeds: tuple[int, ...]
) -> None:
    if source.get("schema_version") != 1:
        raise ValueError("Measurement source schema is invalid")
    if source.get("max_turns") != artifact["max_turns"]:
        raise ValueError("Measurement source max_turns does not match")
    if source.get("seeds") != list(seeds):
        raise ValueError("Measurement source seeds do not match")
    conditions = source.get("conditions")
    if (
        not isinstance(conditions, list)
        or not all(isinstance(item, dict) for item in conditions)
        or [item.get("condition_id") for item in conditions] != list(_CONDITIONS)
    ):
        raise ValueError("Measurement source conditions do not match")
    models = source.get("models")
    if not isinstance(models, list) or len(models) != 1:
        raise ValueError("Measurement source models are invalid")
    model = models[0]
    if not isinstance(model, dict) or model.get("backend") != "concordia_first_legal":
        raise ValueError("Measurement source backend is invalid")


def _read_object(path: Path, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Could not read {label}: {path}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{label} must be an object")
    return payload


def _validate_hash(path: Path, expected: str) -> None:
    if not path.is_file():
        raise ValueError(f"Measurement file is missing: {path}")
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError(f"Measurement hash mismatch: {path}")
