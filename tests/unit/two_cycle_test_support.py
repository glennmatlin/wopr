"""Build strict no-model two-cycle test artifacts."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from tests.unit.two_cycle_fixture_values import (
    ARTIFACT_NAMES,
    WORLD_PARENT_IDS,
    barrier_core_binding,
    load_json,
    replace_cycle_ids,
)
from tests.unit.two_cycle_product_support import apply_cycle2_reassessment

from nuclear_war_contest.date_world.identity import canonical_hash


def cycle2_payload() -> dict[str, Any]:
    payload = replace_cycle_ids(load_json(ARTIFACT_NAMES["cycle1_fixture"]))
    cycle1 = load_json(ARTIFACT_NAMES["cycle1_receipt"])
    binding = barrier_core_binding()
    reassessment = {
        "prior_decision_id": "USC1_PRODUCT_NSC_DECISION_001",
        "prior_decision_hash": cycle1["run"]["decision_record"]["content_hash"],
        "changed_evidence_ids": list(WORLD_PARENT_IDS),
        "core_version": binding["core_version"],
        "core_hash": binding["core_hash"],
        "disposition": "condition",
    }
    payload["fixture_id"] = "US_CYCLE2_NO_MODEL.development.test"
    payload["fixture_version"] = "0.1.0"
    payload["watch_inputs"] = [
        {
            "input_id": "USC2_INPUT_COMMON_WORLD_001",
            "information_class_id": "INFO_COMMON_CRISIS_PICTURE",
            "sender_id": "SERVICE_WATCH",
            "causal_parent_ids": list(WORLD_PARENT_IDS),
            "content": {
                "matched_pressure": WORLD_PARENT_IDS[1:],
                "endogenous_consequences": [WORLD_PARENT_IDS[0]],
                "confirmation": (
                    "Ridge observation is intermittent and South Pass support is "
                    "restricted."
                ),
            },
        },
        {
            "input_id": "USC2_INPUT_INTELLIGENCE_PRIVATE_001",
            "information_class_id": "INFO_INTELLIGENCE_PRIVATE",
            "sender_id": "SERVICE_WATCH",
            "causal_parent_ids": [WORLD_PARENT_IDS[0]],
            "content": {"preparation_status": "prepared_not_transmitted"},
        },
    ]
    apply_cycle2_reassessment(payload, reassessment)
    return payload


def episode_payload() -> dict[str, Any]:
    cycle1 = load_json(ARTIFACT_NAMES["cycle1_receipt"])
    bridge = load_json(ARTIFACT_NAMES["bridge_receipt"])
    return {
        "schema_version": "us-two-cycle-fixture.v0.1",
        "fixture_id": "US_TWO_CYCLE_EPISODE.development.test",
        "fixture_version": "0.1.0",
        "status": "development_fixture_non_evidence",
        "artifact_paths": deepcopy(ARTIFACT_NAMES),
        "artifact_hashes": {},
        "forecast_binding": {
            "cycle1_input_id": "USC1_INPUT_RAW_WEATHER_001",
            "world_event_id": "OBS_WX_RIDGE_FORECAST_01",
            "relationship": "authored_summary_of",
            "shared_entity_ids": [
                "AFF_US_RIDGE_ISR_WINDOW",
                "AFF_HIM_SOUTH_PASS_SUPPORT_WINDOW",
            ],
        },
        "cycle2_external_parent_ids": list(WORLD_PARENT_IDS),
        "cycle2_reassessment": {
            "prior_decision_id": "USC1_PRODUCT_NSC_DECISION_001",
            "prior_decision_hash": cycle1["run"]["decision_record"]["content_hash"],
            "changed_evidence_ids": list(WORLD_PARENT_IDS),
            **barrier_core_binding(),
            "disposition": "condition",
        },
        "final_adjudication": _final_adjudication(),
        "upstream_receipt_hashes": {
            "cycle1": cycle1["receipt_hash"],
            "bridge": bridge["receipt_hash"],
            "date": load_json(ARTIFACT_NAMES["date_tracer_receipt"])["receipt_hash"],
        },
    }


def _final_adjudication() -> dict[str, Any]:
    return {
        "adjudication_id": "USC2_NON_ACTION_TRANSMISSION_001",
        "cycle_id": "CYCLE_2",
        "actor_id": "USA",
        "decision_record_id": "USC2_PRODUCT_NSC_DECISION_001",
        "source_component_ids": ["COMP_INTELLIGENCE_SHARING"],
        "status": "recorded_non_action",
        "original_language": "Do not transmit until a compliant channel is confirmed.",
        "reason_codes": ["recipient_channel_unresolved", "access_degraded"],
        "adjudicator_id": "EXCON_DEVELOPMENT_FIXTURE",
        "evidence_status": "development_fixture_non_evidence",
        "represented_room_decision_actor_ids": [],
        "world_event": {
            "template_id": "EXCON_CONSEQUENCE_NON_ACTION_002",
            "event_kind": "excon_consequence",
            "episode_hour": 7,
            "causal_parent_ids": [WORLD_PARENT_IDS[0], WORLD_PARENT_IDS[2]],
            "source": "excon_consequence",
            "affected_entity_ids": ["US_CRISIS_ASSESSMENT"],
            "audience_ids": ["US_ACTIVE_SEATS"],
            "evidence_ids": ["SYNTHETIC_AUTHORING_DEFAULT"],
            "assumptions": ["non-action does not imply future refusal"],
            "uncertainty": {"confidence": "authored_fixture"},
            "content": "The prepared package remains withheld pending a valid channel.",
            "patch_template_id": None,
        },
    }


def stage_episode(tmp_path: Path, payload: dict[str, Any] | None = None) -> Path:
    selected = episode_payload() if payload is None else deepcopy(payload)
    for key, name in ARTIFACT_NAMES.items():
        if key == "cycle2_fixture":
            artifact = cycle2_payload()
        else:
            artifact = load_json(name)
        (tmp_path / name).write_text(json.dumps(artifact), encoding="utf-8")
        selected["artifact_hashes"][key] = canonical_hash(artifact)
    path = tmp_path / "US_TWO_CYCLE_FIXTURE.development.json"
    path.write_text(json.dumps(selected), encoding="utf-8")
    return path


__all__ = ["cycle2_payload", "episode_payload", "stage_episode"]
