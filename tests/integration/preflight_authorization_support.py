"""Shared live-study authorization fixture construction."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

import pytest

from nuclear_war_contest.live_preflight import run_candidate_preflight
from nuclear_war_contest.live_preflight_auth import build_live_preflight_approval
from nuclear_war_contest.live_preflight_promotion import (
    build_live_preflight_promotion_approval,
    promote_live_preflight_receipt,
)
from nuclear_war_contest.preflight import load_candidate_manifest


def base_payload() -> dict[str, object]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


def approved_live_payload(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> dict[str, object]:
    from tests.unit.test_contest_live_preflight import RecordingTransport

    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    docs = Path(__file__).parents[2] / "docs" / "contest"
    candidate_path = docs / "MODEL_MANIFEST.candidate.json"
    candidate_payload = json.loads(candidate_path.read_text(encoding="utf-8"))
    candidate = load_candidate_manifest(candidate_payload, base_dir=docs)
    executor_revision = "a" * 40
    approval = build_live_preflight_approval(
        candidate, executor_revision, candidate.proposed_max_cost_usd
    )
    live = run_candidate_preflight(
        candidate,
        transport=RecordingTransport(),
        allow_network=True,
        authorization=approval,
        executor_revision=executor_revision,
    )
    promotion = build_live_preflight_promotion_approval(approval, live)
    receipt = promote_live_preflight_receipt(candidate, live, promotion)
    receipt_path = tmp_path / "approved-receipt.json"
    receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
    payload = base_payload()
    payload.update(
        source_revision=candidate.source_revision,
        seeds=list(candidate.study_seeds),
        models=[
            {
                key: model[key]
                for key in (
                    "model_id",
                    "backend",
                    "provider",
                    "client",
                    "max_retries",
                    "role_prompt_hashes",
                )
            }
            for model in candidate_payload["models"]
        ],
        request_budget={
            "max_c2_calls_per_game": candidate.max_c2_calls_per_game,
            "max_press_calls_per_game": candidate.max_press_calls_per_game,
            "input_tokens_bound": candidate.input_tokens_bound,
            "max_output_tokens": candidate.max_tokens,
            "max_cost_usd": candidate.proposed_max_cost_usd,
            "max_cost_per_request_usd": 0.0019456,
            "transport_retry_margin": candidate.transport_retry_margin,
        },
        preflight_receipt_hash=sha256(receipt_path.read_bytes()).hexdigest(),
        preflight_approval_status="approved",
        preflight_candidate_manifest_path=str(candidate_path),
        preflight_candidate_manifest_hash=receipt["candidate_manifest_hash"],
        preflight_receipt_path=str(receipt_path),
        preflight_executor_revision=executor_revision,
    )
    return payload
