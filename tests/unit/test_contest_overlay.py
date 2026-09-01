"""Neutral-staff Overlay is Demo-only chair text."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nuclear_war_contest.config_builder import build_concordia_payload
from nuclear_war_contest.manifest import load_study_manifest
from nuclear_war_contest.overlay_packs import overlay_pack_hash
from nuclear_war_contest.runner import run_matched_study


def _room_instrument_payload() -> dict[str, object]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["study_variant"] = "room_instrument"
    payload["protocol_revision"] = "draft-0.2"
    payload["conditions"] = [
        {
            "condition_id": "full_press_presidential_staff",
            "communication": "full_press",
            "authority": "sole_authority",
            "authority_parameters": {"deference": 0.0},
            "press_passes": 1,
        },
        {
            "condition_id": "full_press_equal_council",
            "communication": "full_press",
            "authority": "council",
            "authority_parameters": {
                "threshold": 0.6666666667,
                "weights": {
                    "executive": 1.0,
                    "strategic_advisor": 1.0,
                    "risk_advisor": 1.0,
                },
            },
            "press_passes": 1,
        },
        {
            "condition_id": "full_press_chair_weighted_council",
            "communication": "full_press",
            "authority": "council",
            "authority_parameters": {
                "threshold": 0.6666666667,
                "weights": {
                    "executive": 2.0,
                    "strategic_advisor": 1.0,
                    "risk_advisor": 1.0,
                },
            },
            "press_passes": 1,
        },
    ]
    return payload


def test_sounding_payload_keeps_structure_only_chair_titles() -> None:
    manifest = load_study_manifest(_room_instrument_payload())
    payload = build_concordia_payload(manifest, manifest.cells[0])
    members = payload["seats"]["player_0"]["authority"]["members"]

    assert payload["seats"]["player_0"]["identity"]["role"] == (
        "cautious nuclear commander"
    )
    assert [member["identity"]["role"] for member in members] == [
        "executive decision authority",
        "strategic advisor",
        "risk advisor",
    ]


def test_neutral_staff_overlay_uses_chair_operations_dissent_titles() -> None:
    payload = _room_instrument_payload()
    payload["overlay"] = "neutral_staff"
    payload["overlay_pack_hash"] = overlay_pack_hash()
    payload["conditions"] = [
        condition
        for condition in payload["conditions"]  # type: ignore[union-attr]
        if condition["condition_id"] == "full_press_equal_council"  # type: ignore[index]
    ]
    payload["study_variant"] = "room_instrument_demo"
    payload["seeds"] = [51]
    manifest = load_study_manifest(payload)
    seats = build_concordia_payload(manifest, manifest.cells[0])["seats"]
    members = seats["player_0"]["authority"]["members"]

    assert seats["player_0"]["identity"]["name"] == "Room 0"
    assert seats["player_0"]["identity"]["role"] == "room"
    assert [member["member_id"] for member in members] == [
        "executive",
        "strategic_advisor",
        "risk_advisor",
    ]
    assert [member["identity"]["role"] for member in members] == [
        "chair",
        "operations",
        "dissent",
    ]
    assert members[0]["identity"]["name"] == "Room 0 Chair"
    assert "nuclear commander" not in seats["player_1"]["identity"]["role"]


def test_checked_in_demo_manifest_is_one_overlaid_cell() -> None:
    path = (
        Path(__file__).parents[2]
        / "docs"
        / "contest"
        / "STUDY_MANIFEST.room_instrument_demo.candidate.json"
    )
    manifest = load_study_manifest(json.loads(path.read_text(encoding="utf-8")))
    payload = build_concordia_payload(manifest, manifest.cells[0])

    assert manifest.study_variant == "room_instrument_demo"
    assert manifest.overlay == "neutral_staff"
    assert len(manifest.cells) == 1
    assert payload["seats"]["player_0"]["authority"]["members"][2]["identity"][
        "role"
    ] == "dissent"
    assert manifest.overlay_pack_hash == overlay_pack_hash()


def test_demo_manifest_rejects_wrong_overlay_pack_hash() -> None:
    path = (
        Path(__file__).parents[2]
        / "docs"
        / "contest"
        / "STUDY_MANIFEST.room_instrument_demo.candidate.json"
    )
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["overlay_pack_hash"] = "0" * 64

    with pytest.raises(ValueError, match="overlay_pack_hash"):
        load_study_manifest(payload)


def test_demo_attempt_records_overlay_pack_hash(tmp_path: Path) -> None:
    payload = _room_instrument_payload()
    payload["overlay"] = "neutral_staff"
    payload["overlay_pack_hash"] = overlay_pack_hash()
    payload["study_variant"] = "room_instrument_demo"
    payload["seeds"] = [51]
    payload["conditions"] = [
        condition
        for condition in payload["conditions"]  # type: ignore[union-attr]
        if condition["condition_id"] == "full_press_equal_council"  # type: ignore[index]
    ]
    summary = run_matched_study(load_study_manifest(payload), tmp_path)
    row = summary["attempts"][0]

    assert row["overlay"] == "neutral_staff"
    assert row["overlay_pack_hash"] == overlay_pack_hash()


def test_sounding_attempt_omits_overlay_pack_hash(tmp_path: Path) -> None:
    summary = run_matched_study(
        load_study_manifest(_room_instrument_payload()), tmp_path
    )

    assert {row["overlay"] for row in summary["attempts"]} == {"off"}
    assert all("overlay_pack_hash" not in row for row in summary["attempts"])
