"""Open-content Policy Package boundary tests."""

from __future__ import annotations

import json
from pathlib import Path

from tests.unit.us_cycle_test_support import RATIFICATION_PATH, loaded_cycle_fixture

from nuclear_war_contest.situation_room import (
    load_us_cycle_fixture,
    run_no_model_us_cycle,
)


def test_missing_policy_domain_fails_closed_before_decision(tmp_path: Path) -> None:
    charter, complete = loaded_cycle_fixture(tmp_path, complete=True)
    payload = complete.payload()
    package = next(
        item for item in payload["group_products"] if item["group_id"] == "GROUP_PC"
    )
    package["content"]["domain_dispositions"].pop()
    fixture_path = tmp_path / "missing-domain.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    failures = {item["group_id"]: item for item in receipt["failures"]}
    assert receipt["status"] == "failed"
    assert failures["GROUP_PC"]["reason_code"] == "invalid_policy_package"
    assert failures["GROUP_NSC"]["reason_code"] == "blocked_dependency"
    assert receipt["decision_supported"] is False


def test_policy_package_preserves_open_additional_content(tmp_path: Path) -> None:
    charter, complete = loaded_cycle_fixture(tmp_path, complete=True)
    payload = complete.payload()
    package = next(
        item for item in payload["group_products"] if item["group_id"] == "GROUP_PC"
    )
    package["content"]["unanticipated_cross_domain_option"] = {
        "original_language": "Offer a reversible verification channel.",
        "conditions": ["partner consent", "reciprocal access"],
    }
    fixture_path = tmp_path / "open-content.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    assert receipt["status"] == "passed"
    assert (
        receipt["policy_package"]["content"]["unanticipated_cross_domain_option"]
        == package["content"]["unanticipated_cross_domain_option"]
    )


def test_malformed_domain_disposition_becomes_failure_receipt(tmp_path: Path) -> None:
    charter, complete = loaded_cycle_fixture(tmp_path, complete=True)
    payload = complete.payload()
    package = next(
        item for item in payload["group_products"] if item["group_id"] == "GROUP_PC"
    )
    package["content"]["domain_dispositions"][0]["responsible_seat_ids"] = [
        {"not": "a seat ID"}
    ]
    fixture_path = tmp_path / "malformed-domain.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    failures = {item["group_id"]: item for item in receipt["failures"]}
    assert receipt["status"] == "failed"
    assert failures["GROUP_PC"]["reason_code"] == "invalid_policy_package"
