"""Receipt-hash binding tests for live preflight promotion."""

from __future__ import annotations

import pytest
from tests.unit.test_contest_live_preflight import (
    EXECUTOR_REVISION,
    RecordingTransport,
    _candidate,
)

from nuclear_war_contest.live_preflight import run_candidate_preflight
from nuclear_war_contest.live_preflight_auth import build_live_preflight_approval
from nuclear_war_contest.live_preflight_promotion import (
    build_live_preflight_promotion_approval,
    promote_live_preflight_receipt,
)


def test_promotion_approval_must_bind_completed_receipt(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
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
    promotion = build_live_preflight_promotion_approval(approval, receipt)
    promotion["live_receipt_sha256"] = "bad"

    with pytest.raises(ValueError, match="not bound to the receipt"):
        promote_live_preflight_receipt(manifest, receipt, promotion)
