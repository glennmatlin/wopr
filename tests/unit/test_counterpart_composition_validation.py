"""Counterpart Room composition failure-boundary tests."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

import pytest
from tests.unit.two_cycle_fixture_values import ARTIFACT_NAMES

from nuclear_war_contest.date_world.identity import canonical_hash
from nuclear_war_contest.situation_room import load_counterpart_composition_fixture

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"
FIXTURE = CONTEST / "COUNTERPART_ROOM_COMPOSITION_FIXTURE.development.json"
ARTIFACTS = (
    *ARTIFACT_NAMES.values(),
    "US_TWO_CYCLE_FIXTURE.development.json",
    "US_TWO_CYCLE_RECEIPT.json",
    "HIMALDESH_ROOM_RECEIPT.json",
    "OLVANA_ROOM_RECEIPT.json",
)


def _stage(tmp_path: Path) -> Path:
    for name in ARTIFACTS:
        shutil.copyfile(CONTEST / name, tmp_path / name)
    path = tmp_path / FIXTURE.name
    shutil.copyfile(FIXTURE, path)
    return path


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


@pytest.mark.parametrize(
    ("artifact_key", "label"),
    [
        ("himaldesh_room_receipt", "Himaldesh Room"),
        ("olvana_room_receipt", "Olvana Room"),
    ],
)
def test_old_counterpart_fixtures_are_rejected_as_room_provenance(
    tmp_path: Path, artifact_key: str, label: str
) -> None:
    path = _stage(tmp_path)
    legacy_name = "US_CYCLE1_FIXTURE.development.json"
    shutil.copyfile(CONTEST / legacy_name, tmp_path / legacy_name)
    payload = _load(path)
    legacy = _load(tmp_path / legacy_name)
    payload["artifact_paths"][artifact_key] = legacy_name
    payload["artifact_hashes"][artifact_key] = canonical_hash(legacy)
    _write(path, payload)

    with pytest.raises(ValueError, match=f"exact {label} receipt"):
        load_counterpart_composition_fixture(path)


def test_changed_room_output_fails_before_us_execution(tmp_path: Path) -> None:
    path = _stage(tmp_path)
    receipt_path = tmp_path / "HIMALDESH_ROOM_RECEIPT.json"
    receipt = _load(receipt_path)
    receipt["run"]["output"]["content"]["decision_clock_hours"] = 19
    receipt.pop("receipt_hash")
    receipt["receipt_hash"] = canonical_hash(receipt)
    _write(receipt_path, receipt)
    payload = _load(path)
    payload["artifact_hashes"]["himaldesh_room_receipt"] = canonical_hash(receipt)
    payload["upstream_receipt_hashes"]["himaldesh"] = receipt["receipt_hash"]
    _write(path, payload)

    with pytest.raises(ValueError, match="exact Himaldesh Room receipt"):
        load_counterpart_composition_fixture(path)


def test_causal_binding_mismatch_fails_before_us_execution(tmp_path: Path) -> None:
    path = _stage(tmp_path)
    payload = _load(path)
    payload["output_bindings"][0]["us_cycle1_input_ids"] = ["USC1_INPUT_COMMON_001"]
    _write(path, payload)

    with pytest.raises(ValueError, match="counterpart output binding"):
        load_counterpart_composition_fixture(path)
