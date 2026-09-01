"""Strict no-model U.S. Cycle 1 fixture loading tests."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from tests.unit.us_cycle_fixture_values import development_counterparts

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json
from nuclear_war_contest.situation_room import (
    load_source_register,
    load_us_charter,
    load_us_cycle_fixture,
)

ROOT = Path(__file__).parents[2]
SOURCE_PATH = ROOT / "docs/contest/US_SOURCE_REGISTER.candidate.json"
CHARTER_PATH = ROOT / "docs/contest/US_CHARTER.candidate.json"
RATIFICATION_PATH = ROOT / "docs/contest/US_CHARTER_RATIFICATION.json"
RATIFICATION_HASH = "0b831d55ba60dd458e44b0e63d714a82eaf05b508a32694f96181caba0b5ad13"


def _fixture_payload(source_hash: str, charter_hash: str) -> dict[str, object]:
    return {
        "schema_version": "us-cycle-fixture.v0.1",
        "fixture_id": "US_CYCLE1_NO_MODEL.test",
        "fixture_version": "0.1.0",
        "status": "development_fixture_non_evidence",
        "actor_id": "ACTOR_UNITED_STATES",
        "cycle_id": "CYCLE_1",
        "ratification_id": "US_PUBLIC_2026Q3.ratification.D67",
        "ratification_hash": RATIFICATION_HASH,
        "source_register_hash": source_hash,
        "charter_hash": charter_hash,
        "action_class": "presidential_policy_direction",
        "counterpart_fixtures": development_counterparts(),
        "watch_inputs": [],
        "group_products": [],
        "confirmations": [],
    }


def _write_fixture(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_fixture_loads_with_the_ratified_charter_identity(tmp_path: Path) -> None:
    source = load_source_register(SOURCE_PATH)
    charter = load_us_charter(CHARTER_PATH, source)
    fixture_path = tmp_path / "cycle.json"
    _write_fixture(
        fixture_path, _fixture_payload(source.content_hash, charter.content_hash)
    )

    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)

    assert fixture.fixture_id == "US_CYCLE1_NO_MODEL.test"
    assert fixture.cycle_id == "CYCLE_1"
    assert fixture.ratification_hash == RATIFICATION_HASH
    assert len(fixture.content_hash) == 64
    assert fixture.payload()["charter_hash"] == charter.content_hash


@pytest.mark.parametrize(
    "identity_field",
    ["ratification_hash", "source_register_hash", "charter_hash"],
)
def test_fixture_rejects_identity_mismatch(tmp_path: Path, identity_field: str) -> None:
    source = load_source_register(SOURCE_PATH)
    charter = load_us_charter(CHARTER_PATH, source)
    payload = _fixture_payload(source.content_hash, charter.content_hash)
    payload[identity_field] = "f" * 64
    fixture_path = tmp_path / "cycle.json"
    _write_fixture(fixture_path, payload)

    with pytest.raises(ValueError, match="identity_mismatch"):
        load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)


def test_fixture_rejects_unknown_top_level_field(tmp_path: Path) -> None:
    source = load_source_register(SOURCE_PATH)
    charter = load_us_charter(CHARTER_PATH, source)
    payload = _fixture_payload(source.content_hash, charter.content_hash)
    payload["unexpected"] = True
    fixture_path = tmp_path / "cycle.json"
    _write_fixture(fixture_path, payload)

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)


def test_fixture_rejects_jointly_modified_ratification(tmp_path: Path) -> None:
    source = load_source_register(SOURCE_PATH)
    charter = load_us_charter(CHARTER_PATH, source)
    ratification = load_strict_json(RATIFICATION_PATH)
    assert isinstance(ratification, dict)
    ratification["charter_hash"] = "f" * 64
    ratification_path = tmp_path / "modified-ratification.json"
    ratification_path.write_text(json.dumps(ratification), encoding="utf-8")
    payload = _fixture_payload(source.content_hash, charter.content_hash)
    payload["ratification_hash"] = canonical_hash(ratification)
    fixture_path = tmp_path / "cycle.json"
    _write_fixture(fixture_path, payload)

    with pytest.raises(ValueError, match="identity_mismatch"):
        load_us_cycle_fixture(fixture_path, charter, ratification_path)
