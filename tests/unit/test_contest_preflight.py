"""Tests for the non-billable contest model preflight packet."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from pathlib import Path
from typing import cast

import pytest

from nuclear_war_contest.preflight import (
    build_preflight_receipt,
    enforce_channel_caps,
    load_candidate_manifest,
)


def _candidate_payload() -> dict[str, object]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "MODEL_MANIFEST.candidate.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


def test_candidate_manifest_is_pending_owner_and_disjoint_from_study_seeds() -> None:
    manifest = load_candidate_manifest(_candidate_payload())

    assert set(manifest.preflight_seeds).isdisjoint(manifest.study_seeds)
    receipt = build_preflight_receipt(manifest)

    assert receipt["status"] == "pending_owner"
    assert receipt["network_calls"] == 0
    assert receipt["credentials_read"] is False
    assert receipt["study"]["games"] == 40
    assert receipt["request_bound"]["provider_request_attempts"] == 529920
    assert receipt["cost_bound"]["upper_bound_usd"] == pytest.approx(922.484736)
    assert receipt["offline_fixture"]["operational_cap_c2_calls_per_game"] == 2048
    assert receipt["offline_fixture"]["operational_cap_press_calls_per_game"] == 160
    checked_in = json.loads(
        (
            Path(__file__).parents[2]
            / "docs"
            / "contest"
            / "MODEL_PREFLIGHT_RECEIPT.json"
        ).read_text(encoding="utf-8")
    )
    assert checked_in == receipt
    measurement = json.loads(
        (
            Path(__file__).parents[2]
            / "docs"
            / "contest"
            / "M3_OFFLINE_FIXTURE_MEASUREMENTS.json"
        ).read_text(encoding="utf-8")
    )
    candidate_measurement = cast(
        dict[str, object], _candidate_payload()["offline_fixture_measurement"]
    )
    assert measurement["status"] == "offline_planning_input_not_study_result"
    assert measurement["observed_max_member_calls"] == 564
    assert [row["seed"] for row in measurement["measurements"]] == [91, 92, 93]
    assert (
        candidate_measurement["source_manifest_hash"]
        == measurement["source_manifest_hash"]
    )
    assert (
        receipt["offline_fixture_measurement"]["artifact_sha256"]
        == hashlib.sha256(
            (
                Path(__file__).parents[2]
                / "docs"
                / "contest"
                / "M3_OFFLINE_FIXTURE_MEASUREMENTS.json"
            ).read_bytes()
        ).hexdigest()
    )


def test_candidate_manifest_rejects_literal_credentials() -> None:
    payload = _candidate_payload()
    model = deepcopy(payload["models"][0])  # type: ignore[index]
    model["client"] = {"api_key": "literal-secret"}
    payload["models"][0] = model  # type: ignore[index]

    with pytest.raises(ValueError, match="client fields"):
        load_candidate_manifest(payload)


def test_candidate_manifest_rejects_preflight_seed_overlap() -> None:
    payload = _candidate_payload()
    payload["preflight_seeds"] = [51, 91, 92]  # type: ignore[index]

    with pytest.raises(ValueError, match="disjoint"):
        load_candidate_manifest(payload)


def test_candidate_manifest_binds_study_seed_count_to_design() -> None:
    payload = _candidate_payload()
    payload["study_seeds"] = [51]  # type: ignore[index]

    with pytest.raises(ValueError, match="seeds_per_condition"):
        load_candidate_manifest(payload)


def test_candidate_manifest_rejects_nonfactorial_condition_count() -> None:
    payload = _candidate_payload()
    payload["study_design"]["condition_count"] = 2  # type: ignore[index]

    with pytest.raises(ValueError, match="condition_count"):
        load_candidate_manifest(payload)


def test_candidate_manifest_rejects_model_override_environment() -> None:
    payload = _candidate_payload()
    payload["models"][0]["client"]["model_env"] = "WOPR_LLM_MODEL"  # type: ignore[index]

    with pytest.raises(ValueError, match="exact model"):
        load_candidate_manifest(payload)


def test_candidate_manifest_rejects_changed_role_prompt_hash() -> None:
    payload = _candidate_payload()
    payload["models"][0]["role_prompt_hashes"]["executive"] = "wrong"  # type: ignore[index]

    with pytest.raises(ValueError, match="role_prompt_hashes"):
        load_candidate_manifest(payload)


@pytest.mark.parametrize(
    "section",
    ["study_design", "retry_policy", "request_budget", "offline_fixture"],
)
def test_candidate_manifest_rejects_malformed_nested_sections(section: str) -> None:
    payload = _candidate_payload()
    payload[section] = []

    with pytest.raises(ValueError, match=section):
        load_candidate_manifest(payload)


def test_channel_caps_fail_closed_for_over_cap_observations() -> None:
    manifest = load_candidate_manifest(_candidate_payload())

    enforce_channel_caps(manifest, c2_calls=564, press_calls=60)
    with pytest.raises(ValueError, match="C2 channel cap"):
        enforce_channel_caps(manifest, c2_calls=2049, press_calls=0)
