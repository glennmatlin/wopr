"""Strict two-cycle episode fixture loading tests."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from tests.unit.two_cycle_test_support import episode_payload, stage_episode

from nuclear_war_contest.date_world.identity import canonical_hash
from nuclear_war_contest.situation_room import load_two_cycle_fixture
from nuclear_war_contest.situation_room.cycle_fixture import load_us_cycle_fixture

CONTEST_PATH = Path(__file__).parents[2] / "docs" / "contest"


def test_fixture_binds_exact_upstream_and_cycle2_identity(tmp_path: Path) -> None:
    fixture = load_two_cycle_fixture(stage_episode(tmp_path))

    assert fixture.fixture_id == "US_TWO_CYCLE_EPISODE.development.test"
    assert fixture.cycle1_fixture().cycle_id == "CYCLE_1"
    assert fixture.cycle2_fixture().cycle_id == "CYCLE_2"
    assert fixture.profile().content_hash == (
        "64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477"
    )
    assert len(fixture.content_hash) == 64


def test_retained_fixture_has_exact_reviewed_identity() -> None:
    fixture = load_two_cycle_fixture(
        CONTEST_PATH / "US_TWO_CYCLE_FIXTURE.development.json"
    )

    assert fixture.fixture_id == "US_TWO_CYCLE_EPISODE.development.v0_1"
    assert fixture.content_hash == (
        "2a7d484d4096e598cee64cbf30c60344c3cca57a7f9cf52f384e6b0ce8f94e66"
    )
    assert fixture.cycle2_fixture().content_hash == (
        "dc99ac7a92e2402451973041325f670c0bb626058068a221f695ee4cd0d9119f"
    )


def test_cycle1_loader_remains_closed_to_cycle2_fixture() -> None:
    episode = load_two_cycle_fixture(
        CONTEST_PATH / "US_TWO_CYCLE_FIXTURE.development.json"
    )

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_us_cycle_fixture(
            CONTEST_PATH / "US_CYCLE2_FIXTURE.development.json",
            episode.charter,
            CONTEST_PATH / "US_CHARTER_RATIFICATION.json",
        )


def test_fixture_rejects_unknown_top_level_field(tmp_path: Path) -> None:
    payload = episode_payload()
    payload["unexpected"] = True

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_two_cycle_fixture(stage_episode(tmp_path, payload))


def test_fixture_rejects_path_escape(tmp_path: Path) -> None:
    payload = episode_payload()
    payload["artifact_paths"]["charter"] = "../US_CHARTER.candidate.json"

    with pytest.raises(ValueError, match="invalid_path"):
        load_two_cycle_fixture(stage_episode(tmp_path, payload))


def test_fixture_rejects_jointly_modified_d69_receipt(tmp_path: Path) -> None:
    path = stage_episode(tmp_path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    receipt_path = tmp_path / payload["artifact_paths"]["bridge_receipt"]
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    receipt["run_hash"] = "f" * 64
    receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
    payload["artifact_hashes"]["bridge_receipt"] = canonical_hash(receipt)
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="identity_mismatch"):
        load_two_cycle_fixture(path)


def test_fixture_rejects_cycle2_parent_outside_episode_world(tmp_path: Path) -> None:
    payload = episode_payload()
    payload["cycle2_external_parent_ids"].remove("EXCON_CONSEQUENCE_PREPARATION_001")

    with pytest.raises(ValueError, match="unknown_reference"):
        load_two_cycle_fixture(stage_episode(tmp_path, payload))


def test_fixture_rejects_room_identity_as_final_adjudicator(tmp_path: Path) -> None:
    payload = episode_payload()
    payload["final_adjudication"]["adjudicator_id"] = "SEAT_PRESIDENT"

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_two_cycle_fixture(stage_episode(tmp_path, payload))


def test_fixture_rejects_non_text_world_parent_without_raw_type_error(
    tmp_path: Path,
) -> None:
    payload = episode_payload()
    payload["cycle2_external_parent_ids"][0] = {"invalid": "parent"}

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_two_cycle_fixture(stage_episode(tmp_path, payload))


def test_fixture_rejects_cycle2_group_graph_change(tmp_path: Path) -> None:
    path = stage_episode(tmp_path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    cycle2_path = tmp_path / payload["artifact_paths"]["cycle2_fixture"]
    cycle2 = json.loads(cycle2_path.read_text(encoding="utf-8"))
    cycle2["group_products"] = cycle2["group_products"][1:]
    cycle2_path.write_text(json.dumps(cycle2), encoding="utf-8")
    payload["artifact_hashes"]["cycle2_fixture"] = canonical_hash(cycle2)
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="identity_mismatch"):
        load_two_cycle_fixture(path)
