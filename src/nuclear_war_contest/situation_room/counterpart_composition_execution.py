"""Deterministic counterpart Room to D70 composition."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .counterpart_composition_identity import EXPECTED_IDENTITIES
from .counterpart_composition_models import (
    CounterpartCompositionFixture,
    CounterpartCompositionRun,
)
from .episode_execution import run_no_model_two_cycle_episode


def _us_two_cycle(d70: dict[str, Any], d70_run: dict[str, Any]) -> dict[str, Any]:
    return {
        "source_receipt_hash": d70["receipt_hash"],
        "source_executor_revision": d70["executor_revision"],
        "fixture_hash": d70["fixture_hash"],
        "run_hash": d70["run_hash"],
        "run": deepcopy(d70_run),
    }


def _migration_check(d70: dict[str, Any]) -> dict[str, Any]:
    return {
        "cycle1_fixture_hash": d70["cycle1_fixture_hash"],
        "status": "matched_not_final_provenance",
        "output_bytes_matched": True,
        "historical_counterpart_fixture_role": "fixture_load_reference_validation_only",
        "us_execution_input_source": "cycle1_watch_inputs",
    }


def _claim_boundary() -> list[str]:
    return [
        "no_model_behavior_evidence",
        "no_live_counterpart_room_evidence",
        "no_creative_excon_evidence",
        "no_counterpart_world_effect_evidence",
        "no_matched_us_condition_evidence",
        "no_date_evaluation_evidence",
    ]


def _composition_receipt(
    fixture: CounterpartCompositionFixture, d70_run: dict[str, Any]
) -> dict[str, Any]:
    receipts = fixture.receipts()
    d70 = receipts["d70"]
    return {
        "schema_version": "counterpart-room-composition-run.v0.1",
        "status": "passed",
        "evidence_status": "development_fixture_non_evidence",
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "counterparts": fixture.counterparts(),
        "us_two_cycle": _us_two_cycle(d70, d70_run),
        "migration_check": _migration_check(d70),
        "claim_boundary": _claim_boundary(),
    }


def run_no_model_counterpart_composition(
    fixture: CounterpartCompositionFixture,
) -> CounterpartCompositionRun:
    d70 = fixture.receipts()["d70"]
    rerun = run_no_model_two_cycle_episode(fixture.two_cycle_fixture())
    expected = EXPECTED_IDENTITIES["d70"]
    if rerun.content_hash != expected["run_hash"] or canonical_hash(
        rerun.receipt()
    ) != canonical_hash(d70["run"]):
        raise ValueError("identity_mismatch: exact D70 U.S. run changed")
    receipt = _composition_receipt(fixture, d70["run"])
    return CounterpartCompositionRun(
        content_hash=canonical_hash(receipt),
        _receipt=receipt,
        _fixture=fixture,
    )


__all__ = ["run_no_model_counterpart_composition"]
