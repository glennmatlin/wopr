"""Shared no-model proposal bridge fixtures."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from tests.unit.proposal_bridge_fixture_values import (
    CYCLE_RECEIPT_PATH,
    PROFILE_PATH,
    consequence_record,
    effect_record,
)

from nuclear_war_contest.date_world.identity import canonical_hash
from nuclear_war_contest.date_world.profile import load_profile


def bridge_payload() -> dict[str, Any]:
    profile = load_profile(PROFILE_PATH)
    initial_core = profile.initial_core()
    cycle_receipt = json.loads(CYCLE_RECEIPT_PATH.read_text(encoding="utf-8"))
    proposal_id = "US_PROPOSAL_COMPOUND_001"
    first = effect_record(
        "EFFECT_PREPARE_INTELLIGENCE_001",
        "COMP_INTELLIGENCE_SHARING",
        "Prepare a releasable defensive intelligence package for Himaldesh.",
        "EXCON_CONSEQUENCE_PREPARATION_001",
    )
    first["timing"] = None
    first["unresolved_field_ids"] = ["timing"]
    resolved_first = deepcopy(first)
    resolved_first["timing"] = "before the hour-four disposition clock"
    resolved_first["unresolved_field_ids"] = []
    second = effect_record(
        "EFFECT_TRANSMIT_INTELLIGENCE_001",
        "COMP_INTELLIGENCE_SHARING",
        "Transmit only after the recipient restriction is identified.",
        "EXCON_CONSEQUENCE_TRANSMISSION_001",
        dependencies=[first["effect_id"]],
        unresolved=True,
    )
    return {
        "schema_version": "proposal-bridge-fixture.v0.1",
        "fixture_id": "US_PROPOSAL_BRIDGE.development.test",
        "fixture_version": "0.1.0",
        "status": "development_fixture_non_evidence",
        "cycle_receipt_hash": cycle_receipt["receipt_hash"],
        "cycle_run_hash": cycle_receipt["run_hash"],
        "date_profile_hash": profile.content_hash,
        "proposals": [
            {
                "proposal_id": proposal_id,
                "proposal_version": "0.1.0",
                "actor_id": "USA",
                "original_language": (
                    "Prepare a defensive intelligence package for potential release, "
                    "and transmit it only after recipient restrictions are identified."
                ),
                "source_policy_package_id": "USC1_PRODUCT_POLICY_PACKAGE_001",
                "source_component_ids": ["COMP_INTELLIGENCE_SHARING"],
                "institutional_decision_record_id": "USC1_PRODUCT_NSC_DECISION_001",
                "effects": [first, second],
                "open_content": {"format": "open natural-language policy"},
            }
        ],
        "clarifications": [
            {
                "clarification_id": "CLARIFY_TIMING_001",
                "proposal_id": proposal_id,
                "effect_id": first["effect_id"],
                "original_effect_hash": canonical_hash(first),
                "status": "resolved",
                "question": "When should preparation begin?",
                "response": "Begin before the hour-four disposition clock.",
                "requested_field_ids": ["timing"],
                "resolved_fields": {"timing": "before the hour-four disposition clock"},
            },
            {
                "clarification_id": "CLARIFY_RECIPIENT_001",
                "proposal_id": proposal_id,
                "effect_id": second["effect_id"],
                "original_effect_hash": canonical_hash(second),
                "status": "unresolved",
                "question": "Which recipient channel satisfies the restrictions?",
                "response": "No recipient channel is yet confirmed.",
                "requested_field_ids": ["object_or_audience"],
                "resolved_fields": {},
            },
        ],
        "effect_authority_records": [
            {
                "authority_record_id": "AUTH_EFFECT_PREPARE_001",
                "effect_id": first["effect_id"],
                "resolved_effect_hash": canonical_hash(resolved_first),
                "actor_id": "USA",
                "authorizing_seat_id": "SEAT_PRESIDENT",
                "decision_record_id": "USC1_PRODUCT_NSC_DECISION_001",
                "status": "authorized",
                "evidence_status": "development_fixture_non_evidence",
                "basis": "Authored fixture authority for mechanics only.",
            }
        ],
        "capability_records": [
            {
                "capability_record_id": "CAP_ACTIVITY_US_001",
                "effect_id": first["effect_id"],
                "predicate_type": "activity_owned_by",
                "entity_id": "US_CRISIS_ASSESSMENT",
                "actor_id": "USA",
                "expected_value": None,
                "evidence_status": "development_fixture_non_evidence",
            }
        ],
        "consequence_proposals": [
            consequence_record(
                profile.content_hash,
                initial_core,
                proposal_id,
                first["effect_id"],
                first["consequence_proposal_id"],
            ),
            consequence_record(
                profile.content_hash,
                initial_core,
                proposal_id,
                second["effect_id"],
                second["consequence_proposal_id"],
                content=(
                    "If the recipient gate is satisfied, transmit the prepared package "
                    "through the confirmed liaison channel."
                ),
            ),
        ],
    }


def write_payload(path: Path, payload: dict[str, Any] | None = None) -> Path:
    selected = bridge_payload() if payload is None else payload
    path.write_text(json.dumps(selected), encoding="utf-8")
    return path


def copied_payload() -> dict[str, Any]:
    return deepcopy(bridge_payload())
