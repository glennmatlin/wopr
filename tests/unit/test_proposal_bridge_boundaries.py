"""Proposal bridge authority and World boundary tests."""

from __future__ import annotations

from pathlib import Path

from tests.unit.proposal_bridge_effect_support import resolved_second_effect_payload
from tests.unit.proposal_bridge_run_support import run_payload
from tests.unit.proposal_bridge_test_support import copied_payload


def test_policy_route_owner_does_not_replace_explicit_effect_authority(
    tmp_path: Path,
) -> None:
    payload = copied_payload()
    payload["effect_authority_records"][0]["authorizing_seat_id"] = "SEAT_CIA_DIRECTOR"

    receipt = run_payload(tmp_path, payload)

    assert receipt["effect_results"][0]["reason_codes"] == ["invalid_effect_authority"]


def test_us_proposal_cannot_claim_counterpart_core_capability(tmp_path: Path) -> None:
    payload = copied_payload()
    capability = payload["capability_records"][0]
    capability.update(
        {
            "predicate_type": "force_package_owned_by",
            "entity_id": "HIM_RECAPTURE_GROUP",
            "actor_id": "HIM",
        }
    )
    consequence = payload["consequence_proposals"][0]
    consequence["core_read"]["entity_ids"] = ["HIM_RECAPTURE_GROUP"]
    consequence["affected_entity_ids"] = ["HIM_RECAPTURE_GROUP"]

    receipt = run_payload(tmp_path, payload)

    assert receipt["effect_results"][0]["reason_codes"] == ["missing_capability"]


def test_consequence_must_disclose_capability_entity_in_core_read(
    tmp_path: Path,
) -> None:
    payload = copied_payload()
    payload["consequence_proposals"][0]["core_read"]["entity_ids"] = []

    receipt = run_payload(tmp_path, payload)

    assert receipt["effect_results"][0]["reason_codes"] == ["causal_mismatch"]
    assert receipt["world"]["ledger"] == []


def test_represented_room_decision_is_not_excon_consequence(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["consequence_proposals"][0]["represented_room_decision_actor_ids"] = ["HIM"]

    receipt = run_payload(tmp_path, payload)

    assert receipt["effect_results"][0]["reason_codes"] == ["represented_room_decision"]
    assert receipt["world"]["ledger"] == []


def test_stale_core_read_blocks_consequence_before_transition(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["consequence_proposals"][0]["core_read"]["core_version"] = 9

    receipt = run_payload(tmp_path, payload)

    assert receipt["effect_results"][0]["reason_codes"] == ["stale_core"]


def test_world_causal_mismatch_propagates_d64_reason(tmp_path: Path) -> None:
    payload = copied_payload()
    payload["consequence_proposals"][0]["world_parent_event_ids"] = [
        "WORLD_EVENT_UNKNOWN"
    ]

    receipt = run_payload(tmp_path, payload)

    result = receipt["effect_results"][0]
    assert result["reason_codes"] == ["causal_mismatch"]
    assert result["world_receipt"]["accepted"] is False


def test_forbidden_state_patch_propagates_d64_reason(tmp_path: Path) -> None:
    payload = copied_payload()
    consequence = payload["consequence_proposals"][0]
    consequence["state_patch"] = {
        "template_id": "PATCH_EXCON_FORBIDDEN_001",
        "effective_hour": 2,
        "causal_parent_ids": [consequence["consequence_proposal_id"]],
        "operations": [
            {
                "operation": "set_arbitrary_path",
                "path": "ground_truth.olvana_objective",
                "value": "rewritten",
            }
        ],
    }

    receipt = run_payload(tmp_path, payload)

    result = receipt["effect_results"][0]
    assert result["reason_codes"] == ["undeclared_operation"]
    assert result["world_receipt"]["accepted"] is False
    assert receipt["world"]["core_unchanged"] is True


def test_state_patch_target_must_be_disclosed_in_core_read(tmp_path: Path) -> None:
    payload = copied_payload()
    consequence = payload["consequence_proposals"][0]
    consequence["state_patch"] = {
        "template_id": "PATCH_EXCON_UNDISCLOSED_001",
        "effective_hour": 2,
        "causal_parent_ids": [consequence["consequence_proposal_id"]],
        "operations": [
            {
                "operation": "set_affordance_state",
                "affordance_id": "AFF_US_RIDGE_ISR_WINDOW",
                "expected": "available",
                "value": "intermittent",
            }
        ],
    }

    receipt = run_payload(tmp_path, payload)

    result = receipt["effect_results"][0]
    assert result["reason_codes"] == ["causal_mismatch"]
    assert result["world_receipt"] is None
    assert receipt["world"]["core_unchanged"] is True


def test_dependent_consequence_requires_admitted_world_parent(tmp_path: Path) -> None:
    payload = resolved_second_effect_payload()

    missing_parent = run_payload(tmp_path, payload)

    assert missing_parent["effect_results"][1]["reason_codes"] == ["causal_mismatch"]
    payload["consequence_proposals"][1]["world_parent_event_ids"] = [
        "EXCON_CONSEQUENCE_PREPARATION_001"
    ]

    admitted = run_payload(tmp_path, payload)

    assert admitted["status"] == "passed"
    assert admitted["effect_results"][1]["status"] == "admitted"
