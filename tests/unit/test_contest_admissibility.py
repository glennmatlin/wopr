"""Tests for primary and sensitivity admissibility tiers."""

from __future__ import annotations

import copy
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from nuclear_war_concordia.config import load_concordia_no_press_config
from nuclear_war_concordia.harness import run_concordia_no_press_game
from nuclear_war_contest.admissibility import classify_failure, classify_result
from nuclear_war_contest.config_builder import build_concordia_payload
from nuclear_war_contest.manifest import load_study_manifest


def _result(trace: dict[str, object]) -> dict[str, Any]:
    result = copy.deepcopy(_valid_result())
    member_trace = result["c2_artifact"]["deliberations"][0]["members"][0]["trace"]
    result["trace_artifact"]["traces"] = [copy.deepcopy(member_trace)]
    ordinary_trace = result["trace_artifact"]["traces"][0]
    ordinary_trace.update(trace)
    if ordinary_trace["retries"]:
        ordinary_trace["prompts"].append(ordinary_trace["prompts"][-1])
        ordinary_trace["raw_responses"].append(ordinary_trace["raw_responses"][-1])
        ordinary_trace["prompt"] = ordinary_trace["prompts"][-1]
        ordinary_trace["raw_response"] = ordinary_trace["raw_responses"][-1]
    return result


@lru_cache(maxsize=1)
def _valid_result() -> dict[str, Any]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    manifest = load_study_manifest(json.loads(path.read_text(encoding="utf-8")))
    payload = build_concordia_payload(manifest, manifest.cells[0])
    return run_concordia_no_press_game(load_concordia_no_press_config(payload))


def test_clean_result_is_tier_a() -> None:
    result = classify_result(
        _result({"fallback_used": False, "retries": 0, "validation_errors": []})
    )

    assert result["tier"] == "A"
    assert result["transport_retry_count"] == 0


def test_output_reprompt_is_tier_b_but_transport_retry_is_allowed() -> None:
    result = classify_result(
        _result(
            {
                "fallback_used": False,
                "retries": 1,
                "validation_errors": ["invalid action"],
                "recoverable_provider_retries": 2,
            }
        )
    )

    assert result["tier"] == "B"
    assert result["transport_retry_count"] == 2


def test_fallback_and_runner_failure_are_tier_c() -> None:
    fallback = classify_result(
        _result({"fallback_used": True, "retries": 0, "validation_errors": []})
    )

    assert fallback["tier"] == "C"
    assert "fallback_used" in fallback["reasons"]
    assert classify_failure(RuntimeError("provider down"))["tier"] == "C"
