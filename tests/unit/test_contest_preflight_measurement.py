"""Tests for binding the offline fixture measurement artifact."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest

from nuclear_war_contest.preflight import load_candidate_manifest


def _candidate_payload() -> dict[str, object]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "MODEL_MANIFEST.candidate.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


def test_candidate_manifest_rejects_tampered_measurement_rows(tmp_path: Path) -> None:
    payload = _candidate_payload()
    contest_dir = Path(__file__).parents[2] / "docs" / "contest"
    source_name = "M3_OFFLINE_SOURCE_MANIFEST.json"
    shutil.copy2(contest_dir / source_name, tmp_path / source_name)
    measurement = json.loads(
        (contest_dir / "M3_OFFLINE_FIXTURE_MEASUREMENTS.json").read_text(
            encoding="utf-8"
        )
    )
    measurement["observed_max_member_calls"] = 563
    measurement_path = tmp_path / "measurement.json"
    measurement_path.write_text(json.dumps(measurement), encoding="utf-8")
    measurement_config = payload["offline_fixture_measurement"]
    assert isinstance(measurement_config, dict)
    measurement_config["path"] = "measurement.json"
    measurement_config["artifact_sha256"] = hashlib.sha256(
        measurement_path.read_bytes()
    ).hexdigest()

    with pytest.raises(ValueError, match="maximum"):
        load_candidate_manifest(payload, base_dir=tmp_path)


def test_candidate_manifest_rejects_duplicate_measurement_seed(
    tmp_path: Path,
) -> None:
    payload = _candidate_payload()
    contest_dir = Path(__file__).parents[2] / "docs" / "contest"
    source_name = "M3_OFFLINE_SOURCE_MANIFEST.json"
    shutil.copy2(contest_dir / source_name, tmp_path / source_name)
    measurement = json.loads(
        (contest_dir / "M3_OFFLINE_FIXTURE_MEASUREMENTS.json").read_text(
            encoding="utf-8"
        )
    )
    measurement["measurements"].append(dict(measurement["measurements"][0]))
    measurement_path = tmp_path / "measurement.json"
    measurement_path.write_text(json.dumps(measurement), encoding="utf-8")
    measurement_config = payload["offline_fixture_measurement"]
    assert isinstance(measurement_config, dict)
    measurement_config["path"] = "measurement.json"
    measurement_config["artifact_sha256"] = hashlib.sha256(
        measurement_path.read_bytes()
    ).hexdigest()

    with pytest.raises(ValueError, match="seeds"):
        load_candidate_manifest(payload, base_dir=tmp_path)


def test_candidate_manifest_rejects_malformed_measurement_seed(
    tmp_path: Path,
) -> None:
    payload = _candidate_payload()
    contest_dir = Path(__file__).parents[2] / "docs" / "contest"
    source_name = "M3_OFFLINE_SOURCE_MANIFEST.json"
    shutil.copy2(contest_dir / source_name, tmp_path / source_name)
    measurement = json.loads(
        (contest_dir / "M3_OFFLINE_FIXTURE_MEASUREMENTS.json").read_text(
            encoding="utf-8"
        )
    )
    measurement["measurements"][0]["seed"] = []
    measurement_path = tmp_path / "measurement.json"
    measurement_path.write_text(json.dumps(measurement), encoding="utf-8")
    measurement_config = payload["offline_fixture_measurement"]
    assert isinstance(measurement_config, dict)
    measurement_config["path"] = "measurement.json"
    measurement_config["artifact_sha256"] = hashlib.sha256(
        measurement_path.read_bytes()
    ).hexdigest()

    with pytest.raises(ValueError, match="row seed"):
        load_candidate_manifest(payload, base_dir=tmp_path)
