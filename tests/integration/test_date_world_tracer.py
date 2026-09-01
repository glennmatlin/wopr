"""Fresh-process DATE World tracer test."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)
PROFILE_HASH = "64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477"
EXECUTOR_REVISION = "0" * 40


def _canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def test_two_branch_tracer_passes_in_a_fresh_process() -> None:
    process = subprocess.run(
        [
            sys.executable,
            "-m",
            "nuclear_war_contest.date_world.tracer",
            str(PROFILE_PATH),
            EXECUTOR_REVISION,
        ],
        check=True,
        capture_output=True,
        cwd=PROFILE_PATH.parents[3],
        text=True,
    )
    receipt = json.loads(process.stdout)

    assert receipt["status"] == "passed"
    assert receipt["profile_hash"] == PROFILE_HASH
    assert receipt["executor_revision"] == EXECUTOR_REVISION
    assert receipt["forecast_core_unchanged"] is True
    assert receipt["weather_template_hash_equal"] is True
    assert receipt["weather_instance_ids_distinct"] is True
    assert receipt["branches"]["ready"]["readiness"] == "ready"
    assert receipt["branches"]["delayed"]["readiness"] == "delayed"
    for branch in receipt["branches"].values():
        assert branch["core_version"] == 2
        assert branch["replay_matched"] is True
        assert branch["outcomes"]["us_observation_state"] == "intermittent"
        assert branch["outcomes"]["himaldesh_support_state"] == "restricted"
        assert branch["ledger_template_ids"][-2:] == [
            "WX_RIDGE_FRONT_01",
            "OBS_WX_RIDGE_CONFIRMED_01",
        ]
    reasons = {item["case_id"]: item["reason_code"] for item in receipt["rejections"]}
    assert reasons["FAILED_AFFORDANCE_PRECONDITION"] == "failed_precondition"
    assert set(reasons.values()) >= {
        "invalid_envelope",
        "duplicate_id",
        "unknown_reference",
        "causal_mismatch",
        "retroactive_time",
        "terminal_world",
        "template_mismatch",
        "stale_core",
        "failed_precondition",
        "undeclared_operation",
        "forbidden_write",
        "invalid_value",
        "partial_patch",
    }
    receipt_hash = receipt.pop("receipt_hash")
    assert receipt_hash == _canonical_hash(receipt)
