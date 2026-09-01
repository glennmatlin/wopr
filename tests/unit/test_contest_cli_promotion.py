"""CLI tests for receipt-bound live-preflight promotion."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pytest

from nuclear_war_contest.cli import run_contest_command


def test_contest_builds_promotion_approval_from_receipt(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from tests.unit.test_contest_live_preflight import (
        EXECUTOR_REVISION,
        RecordingTransport,
        _candidate,
    )

    from nuclear_war_contest.live_preflight import run_candidate_preflight
    from nuclear_war_contest.live_preflight_auth import build_live_preflight_approval

    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    monkeypatch.setattr(
        "nuclear_war_contest.live_preflight.verify_executor_revision", lambda _: None
    )
    manifest = _candidate()
    approval = build_live_preflight_approval(
        manifest, EXECUTOR_REVISION, manifest.proposed_max_cost_usd
    )
    receipt = run_candidate_preflight(
        manifest,
        transport=RecordingTransport(),
        allow_network=True,
        authorization=approval,
        executor_revision=EXECUTOR_REVISION,
    )
    approval_path = tmp_path / "approval.json"
    receipt_path = tmp_path / "live.json"
    output = tmp_path / "promotion.json"
    approval_path.write_text(json.dumps(approval), encoding="utf-8")
    receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

    assert (
        run_contest_command(
            argparse.Namespace(
                command="contest-build-promotion-approval",
                approval=str(approval_path),
                receipt=str(receipt_path),
                out=str(output),
            )
        )
        == 0
    )
    promotion = json.loads(output.read_text(encoding="utf-8"))
    assert promotion["live_receipt_sha256"]


def test_contest_promotes_passing_live_receipt(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from tests.unit.test_contest_live_preflight import (
        EXECUTOR_REVISION,
        RecordingTransport,
        _candidate,
    )

    from nuclear_war_contest.live_preflight import run_candidate_preflight
    from nuclear_war_contest.live_preflight_auth import build_live_preflight_approval
    from nuclear_war_contest.live_preflight_promotion import (
        build_live_preflight_promotion_approval,
    )

    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    monkeypatch.setattr(
        "nuclear_war_contest.live_preflight.verify_executor_revision", lambda _: None
    )
    manifest = _candidate()
    approval = build_live_preflight_approval(
        manifest, EXECUTOR_REVISION, manifest.proposed_max_cost_usd
    )
    live = run_candidate_preflight(
        manifest,
        transport=RecordingTransport(),
        allow_network=True,
        authorization=approval,
        executor_revision=EXECUTOR_REVISION,
    )
    promotion = build_live_preflight_promotion_approval(approval, live)
    docs = Path(__file__).parents[2] / "docs" / "contest"
    candidate = docs / "MODEL_MANIFEST.candidate.json"
    live_path = tmp_path / "live.json"
    approval_path = tmp_path / "promotion.json"
    output = tmp_path / "approved.json"
    live_path.write_text(json.dumps(live), encoding="utf-8")
    approval_path.write_text(json.dumps(promotion), encoding="utf-8")

    assert (
        run_contest_command(
            argparse.Namespace(
                command="contest-promote-preflight",
                manifest=str(candidate),
                receipt=str(live_path),
                approval=str(approval_path),
                out=str(output),
            )
        )
        == 0
    )
    promoted = json.loads(output.read_text(encoding="utf-8"))
    assert promoted["status"] == "approved"
    assert promoted["live_preflight"]["approval_status"] == "approved"
