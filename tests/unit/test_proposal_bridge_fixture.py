"""Strict proposal bridge fixture loading tests."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from tests.unit.proposal_bridge_test_support import (
    CYCLE_RECEIPT_PATH,
    PROFILE_PATH,
    copied_payload,
    write_payload,
)

from nuclear_war_contest.date_world.profile import load_profile
from nuclear_war_contest.situation_room import load_proposal_bridge_fixture


def test_fixture_binds_exact_d68_and_d64_identities(tmp_path: Path) -> None:
    profile = load_profile(PROFILE_PATH)
    fixture = load_proposal_bridge_fixture(
        write_payload(tmp_path / "bridge.json"), CYCLE_RECEIPT_PATH, profile
    )

    assert fixture.fixture_id == "US_PROPOSAL_BRIDGE.development.test"
    assert fixture.cycle_receipt_hash == (
        "7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186"
    )
    assert fixture.date_profile_hash == profile.content_hash
    assert len(fixture.content_hash) == 64


def test_fixture_rejects_unknown_top_level_field(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["unexpected"] = True

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_proposal_bridge_fixture(
            write_payload(tmp_path / "bridge.json", payload),
            CYCLE_RECEIPT_PATH,
            load_profile(PROFILE_PATH),
        )


def test_fixture_rejects_jointly_modified_d68_receipt(tmp_path: Path) -> None:
    receipt = json.loads(CYCLE_RECEIPT_PATH.read_text(encoding="utf-8"))
    receipt["run_hash"] = "f" * 64
    receipt_path = tmp_path / "modified-receipt.json"
    receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

    with pytest.raises(ValueError, match="identity_mismatch"):
        load_proposal_bridge_fixture(
            write_payload(tmp_path / "bridge.json"),
            receipt_path,
            load_profile(PROFILE_PATH),
        )


def test_fixture_rejects_dependency_that_requires_reordering(tmp_path: Path) -> None:
    payload = copied_payload()
    effects = payload["proposals"][0]["effects"]
    effects[0]["dependency_effect_ids"] = [effects[1]["effect_id"]]

    with pytest.raises(ValueError, match="dependency_order"):
        load_proposal_bridge_fixture(
            write_payload(tmp_path / "bridge.json", payload),
            CYCLE_RECEIPT_PATH,
            load_profile(PROFILE_PATH),
        )


def test_fixture_rejects_clarification_that_rewrites_existing_policy(
    tmp_path: Path,
) -> None:
    payload = copied_payload()
    clarification = payload["clarifications"][0]
    clarification["requested_field_ids"] = ["intended_effect"]
    clarification["resolved_fields"] = {"intended_effect": "rewritten policy"}

    with pytest.raises(ValueError, match="invalid_clarification"):
        load_proposal_bridge_fixture(
            write_payload(tmp_path / "bridge.json", payload),
            CYCLE_RECEIPT_PATH,
            load_profile(PROFILE_PATH),
        )


def test_fixture_rejects_unmarked_missing_effect_field(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["proposals"][0]["effects"][0]["unresolved_field_ids"] = []

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_proposal_bridge_fixture(
            write_payload(tmp_path / "bridge.json", payload),
            CYCLE_RECEIPT_PATH,
            load_profile(PROFILE_PATH),
        )


def test_fixture_rejects_claimed_excon_evidence(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["consequence_proposals"][0]["evidence_status"] = "model_evidence"

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_proposal_bridge_fixture(
            write_payload(tmp_path / "bridge.json", payload),
            CYCLE_RECEIPT_PATH,
            load_profile(PROFILE_PATH),
        )


def test_fixture_rejects_room_identity_as_excon_adjudicator(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["consequence_proposals"][0]["adjudicator_id"] = "SEAT_PRESIDENT"

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_proposal_bridge_fixture(
            write_payload(tmp_path / "bridge.json", payload),
            CYCLE_RECEIPT_PATH,
            load_profile(PROFILE_PATH),
        )


def test_fixture_requires_attributable_source_component(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["proposals"][0]["source_component_ids"] = []

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_proposal_bridge_fixture(
            write_payload(tmp_path / "bridge.json", payload),
            CYCLE_RECEIPT_PATH,
            load_profile(PROFILE_PATH),
        )
