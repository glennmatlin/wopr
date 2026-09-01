"""Authorization and response-evidence tests for live preflight."""

from __future__ import annotations

import pytest
from tests.unit.test_contest_live_preflight import (
    EXECUTOR_REVISION,
    RecordingTransport,
    _approval,
    _candidate,
)

from nuclear_war_contest.live_preflight import run_candidate_preflight


def test_injected_transport_still_requires_explicit_network_flag(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    manifest = _candidate()
    with pytest.raises(ValueError, match="allow_network"):
        run_candidate_preflight(
            manifest,
            transport=RecordingTransport(),
            authorization=_approval(manifest),
            executor_revision=EXECUTOR_REVISION,
        )


def test_candidate_preflight_requires_candidate_bound_approval(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")

    with pytest.raises(ValueError, match="approval"):
        run_candidate_preflight(
            _candidate(),
            transport=RecordingTransport(),
            allow_network=True,
            executor_revision=EXECUTOR_REVISION,
        )


def test_candidate_preflight_missing_credentials_makes_no_transport_call(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("TOGETHER_API_KEY", raising=False)
    transport = RecordingTransport()
    manifest = _candidate()
    receipt = run_candidate_preflight(
        manifest,
        transport=transport,
        allow_network=True,
        authorization=_approval(manifest),
        executor_revision=EXECUTOR_REVISION,
    )

    assert receipt["status"] == "failed"
    assert receipt["network_calls"] == 0
    assert receipt["credentials_read"] is False
    assert transport.bodies == []


def test_candidate_preflight_rejects_wrong_response_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    manifest = _candidate()
    receipt = run_candidate_preflight(
        manifest,
        transport=RecordingTransport(response_content='{"preflight":"no"}'),
        allow_network=True,
        authorization=_approval(manifest),
        executor_revision=EXECUTOR_REVISION,
    )

    assert receipt["status"] == "failed"
    assert {item["error_type"] for item in receipt["attempts"]} == {
        "unexpected_response"
    }


def test_candidate_preflight_rejects_wrong_provider_model(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    manifest = _candidate()
    receipt = run_candidate_preflight(
        manifest,
        transport=RecordingTransport(response_model="unapproved-model"),
        allow_network=True,
        authorization=_approval(manifest),
        executor_revision=EXECUTOR_REVISION,
    )

    assert receipt["status"] == "failed"
    assert {item["error_type"] for item in receipt["attempts"]} == {
        "unexpected_provider_model"
    }


def test_candidate_preflight_retains_transport_exception_receipt(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    manifest = _candidate()

    def raising_transport(url, headers, body, timeout):
        del url, headers, body, timeout
        raise TimeoutError("synthetic transport outage")

    receipt = run_candidate_preflight(
        manifest,
        transport=raising_transport,
        allow_network=True,
        authorization=_approval(manifest),
        executor_revision=EXECUTOR_REVISION,
    )

    assert receipt["status"] == "failed"
    assert receipt["network_calls"] == 6
    assert {item["error_type"] for item in receipt["attempts"]} == {"TimeoutError"}


def test_public_preflight_boundary_verifies_executor_before_transport(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from nuclear_war_contest import live_preflight

    manifest = _candidate()
    transport = RecordingTransport()
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    monkeypatch.setattr(
        live_preflight,
        "verify_executor_revision",
        lambda _: (_ for _ in ()).throw(ValueError("dirty executor")),
    )

    with pytest.raises(ValueError, match="dirty executor"):
        run_candidate_preflight(
            manifest,
            transport=transport,
            allow_network=True,
            authorization=_approval(manifest),
            executor_revision=EXECUTOR_REVISION,
        )
    assert transport.bodies == []
