"""Stable values for no-model U.S. cycle test fixtures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

ROOT = Path(__file__).parents[2]
SOURCE_PATH = ROOT / "docs/contest/US_SOURCE_REGISTER.candidate.json"
CHARTER_PATH = ROOT / "docs/contest/US_CHARTER.candidate.json"
RATIFICATION_PATH = ROOT / "docs/contest/US_CHARTER_RATIFICATION.json"
RATIFICATION_HASH = "0b831d55ba60dd458e44b0e63d714a82eaf05b508a32694f96181caba0b5ad13"
POLICY_DOMAINS = (
    "diplomacy_private_channels",
    "intelligence_collection_sharing",
    "defense_support_posture",
    "economic_financial_measures",
    "public_communication",
    "contingency_reassessment",
)


def development_counterparts() -> list[dict[str, Any]]:
    return [
        {
            "fixture_id": "HIM_CYCLE1_REQUEST.test",
            "actor_id": "ACTOR_HIMALDESH",
            "status": "development_fixture_non_evidence",
            "outputs": [
                {
                    "output_id": "HIM_OUTPUT_REQUEST_001",
                    "content": {"request": "synthetic bounded support request"},
                }
            ],
        },
        {
            "fixture_id": "OLV_CYCLE1_POSTURE.test",
            "actor_id": "ACTOR_OLVANA",
            "status": "development_fixture_non_evidence",
            "outputs": [
                {
                    "output_id": "OLV_OUTPUT_POSTURE_001",
                    "content": {"posture": "synthetic observed ridge posture"},
                }
            ],
        },
    ]


__all__ = [
    "CHARTER_PATH",
    "POLICY_DOMAINS",
    "RATIFICATION_HASH",
    "RATIFICATION_PATH",
    "SOURCE_PATH",
    "development_counterparts",
]
