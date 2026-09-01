"""Candidate-bound live preflight receipt tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from nuclear_war_agents.llm_http_transport import HTTPResponse
from nuclear_war_contest.live_preflight import (
    run_candidate_preflight,
    validate_live_preflight_receipt,
)
from nuclear_war_contest.live_preflight_auth import build_live_preflight_approval
from nuclear_war_contest.preflight import load_candidate_manifest


def _candidate():
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "MODEL_MANIFEST.candidate.json"
    )
    return load_candidate_manifest(json.loads(path.read_text()), base_dir=path.parent)


EXECUTOR_REVISION = "a" * 40


def _approval(manifest):
    return build_live_preflight_approval(
        manifest, EXECUTOR_REVISION, manifest.proposed_max_cost_usd
    )


class RecordingTransport:
    def __init__(
        self,
        failed_model: str | None = None,
        response_content: str = '{"preflight":"ok"}',
        response_model: str | None = None,
    ) -> None:
        self.failed_model = failed_model
        self.response_content = response_content
        self.response_model = response_model
        self.bodies: list[dict[str, Any]] = []

    def __call__(self, url: str, headers: dict[str, str], body: bytes, timeout: int):
        del url, headers, timeout
        payload = json.loads(body)
        self.bodies.append(payload)
        if payload["model"] == self.failed_model:
            return HTTPResponse(500, '{"error":{"message":"temporary"}}')
        return HTTPResponse(
            200,
            json.dumps(
                {
                    "choices": [{"message": {"content": self.response_content}}],
                    "model": self.response_model or payload["model"],
                    "usage": {"prompt_tokens": 12, "completion_tokens": 4},
                }
            ),
        )


def test_candidate_preflight_records_each_model_seed_and_controls(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    transport = RecordingTransport()

    manifest = _candidate()
    receipt = run_candidate_preflight(
        manifest,
        transport=transport,
        allow_network=True,
        authorization=_approval(manifest),
        executor_revision=EXECUTOR_REVISION,
    )

    validate_live_preflight_receipt(receipt, manifest)
    assert receipt["status"] == "passed"
    assert receipt["approval_status"] == "pending_owner"
    assert receipt["network_calls"] == 6
    assert receipt["credentials_read"] is True
    assert receipt["request_bound"]["provider_attempts"] == 18
    assert receipt["cost_bound"]["upper_bound_usd"] > 0
    assert len(receipt["attempts"]) == 6
    assert {body["model"] for body in transport.bodies} == {
        "openai/gpt-oss-120b",
        "Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
    }
    assert all(body["reasoning"] == {"enabled": False} for body in transport.bodies)
    assert "test-secret" not in json.dumps(receipt)


def test_candidate_preflight_requires_explicit_network_without_transport() -> None:
    with pytest.raises(ValueError, match="allow_network"):
        run_candidate_preflight(_candidate())


def test_candidate_preflight_retains_failed_seed_attempts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    manifest = _candidate()
    receipt = run_candidate_preflight(
        manifest,
        transport=RecordingTransport("openai/gpt-oss-120b"),
        allow_network=True,
        authorization=_approval(manifest),
        executor_revision=EXECUTOR_REVISION,
    )

    validate_live_preflight_receipt(receipt, manifest)
    assert receipt["status"] == "failed"
    failures = [item for item in receipt["attempts"] if item["status"] == "failed"]
    assert len(failures) == 3
    assert all(item["provider_attempts"] == 3 for item in failures)
