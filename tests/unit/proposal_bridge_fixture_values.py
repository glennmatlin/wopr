"""Static values for no-model proposal bridge tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import core_hash

ROOT = Path(__file__).parents[2]
CONTEST_DIR = ROOT / "docs/contest"
PROFILE_PATH = CONTEST_DIR / "DATE_PROFILE.candidate.json"
CYCLE_RECEIPT_PATH = CONTEST_DIR / "US_CYCLE1_RECEIPT.json"


def effect_record(
    effect_id: str,
    component_id: str,
    language: str,
    consequence_id: str,
    *,
    dependencies: list[str] | None = None,
    unresolved: bool = False,
) -> dict[str, Any]:
    return {
        "effect_id": effect_id,
        "source_component_ids": [component_id],
        "original_language": language,
        "intended_effect": "Prepare defensive intelligence for possible release.",
        "means_or_resources": ["US_CRISIS_ASSESSMENT"],
        "object_or_audience": None if unresolved else ["Himaldesh liaison channel"],
        "timing": "before the hour-four disposition clock",
        "conditions": ["recipient restrictions remain satisfied"],
        "dependency_effect_ids": dependencies or [],
        "unresolved_field_ids": ["object_or_audience"] if unresolved else [],
        "authority_record_id": None if unresolved else "AUTH_EFFECT_PREPARE_001",
        "capability_record_ids": [] if unresolved else ["CAP_ACTIVITY_US_001"],
        "consequence_proposal_id": consequence_id,
        "open_content": {"novel_detail": "No action-family label is required."},
    }


def consequence_record(
    profile_hash: str,
    initial_core: dict[str, Any],
    proposal_id: str,
    effect_id: str,
    consequence_id: str,
    content: str = "Assessment staff begin preparing the defensive package.",
) -> dict[str, Any]:
    return {
        "consequence_proposal_id": consequence_id,
        "source_proposal_id": proposal_id,
        "effect_id": effect_id,
        "adjudicator_id": "EXCON_DEVELOPMENT_FIXTURE",
        "evidence_status": "development_fixture_non_evidence",
        "artifact_parent_ids": [
            "USC1_PRODUCT_NSC_DECISION_001",
            proposal_id,
            effect_id,
        ],
        "core_read": {
            "profile_hash": profile_hash,
            "core_version": initial_core["core_version"],
            "core_hash": core_hash(initial_core),
            "entity_ids": ["US_CRISIS_ASSESSMENT"],
        },
        "world_parent_event_ids": [],
        "affected_entity_ids": ["US_CRISIS_ASSESSMENT"],
        "episode_hour": 2,
        "audience_ids": ["US_ACTIVE_SEATS"],
        "evidence_ids": ["SYNTHETIC_AUTHORING_DEFAULT"],
        "assumptions": ["preparation does not imply transmission"],
        "uncertainty": {"confidence": "authored_fixture"},
        "alternatives": ["delay preparation pending further review"],
        "content": content,
        "represented_room_decision_actor_ids": [],
        "resulting_injects": [],
        "state_patch": None,
        "open_content": {"unexpected_consequence_detail": "retained"},
    }


__all__ = [
    "CYCLE_RECEIPT_PATH",
    "PROFILE_PATH",
    "consequence_record",
    "effect_record",
]
