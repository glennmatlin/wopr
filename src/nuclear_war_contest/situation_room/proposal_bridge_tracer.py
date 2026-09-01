"""Fresh-process no-model proposal and consequence bridge tracer."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash
from nuclear_war_contest.date_world.profile import load_profile

from .proposal_bridge_execution import run_no_model_proposal_bridge
from .proposal_bridge_fixture import load_proposal_bridge_fixture
from .proposal_bridge_replay import replay_proposal_bridge


def run_proposal_bridge_tracer(
    profile_path: Path,
    cycle_receipt_path: Path,
    fixture_path: Path,
    executor_revision: str,
) -> dict[str, Any]:
    if len(executor_revision) != 40 or any(
        character not in "0123456789abcdef" for character in executor_revision
    ):
        raise ValueError("proposal bridge executor revision is invalid")
    profile = load_profile(profile_path)
    fixture = load_proposal_bridge_fixture(fixture_path, cycle_receipt_path, profile)
    run = run_no_model_proposal_bridge(profile, fixture)
    replayed = replay_proposal_bridge(profile, run)
    run_receipt = run.receipt()
    summary = run_receipt["effect_summary"]
    replay_matched = (
        replayed.content_hash == run.content_hash and replayed.receipt() == run_receipt
    )
    gate_passed = (
        run_receipt["status"] == "passed"
        and summary["admitted"] >= 1
        and summary["blocked"] >= 1
        and replay_matched
    )
    receipt: dict[str, Any] = {
        "schema_version": "proposal-bridge-tracer-receipt.v0.1",
        "tracer_id": "m3-open-proposal-consequence-no-model-v1",
        "status": "passed" if gate_passed else "failed",
        "evidence_status": "development_fixture_non_evidence",
        "executor_revision": executor_revision,
        "cycle_receipt_hash": fixture.cycle_receipt_hash,
        "date_profile_hash": fixture.date_profile_hash,
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "run_hash": run.content_hash,
        "run": run_receipt,
        "replay_matched": replay_matched,
        "claim_boundary": [
            "no_model_proposal_evidence",
            "no_creative_excon_evidence",
            "no_official_effect_authority_evidence",
            "no_counterpart_room_evidence",
            "no_date_episode_evidence",
            "no_comparative_result",
        ],
    }
    receipt["receipt_hash"] = canonical_hash(receipt)
    return receipt


def main() -> None:
    if len(sys.argv) not in {5, 6}:
        raise SystemExit(
            "usage: situation_room.proposal_bridge_tracer PROFILE "
            "CYCLE_RECEIPT FIXTURE EXECUTOR_REVISION [OUTPUT]"
        )
    receipt = run_proposal_bridge_tracer(
        Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
    )
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if len(sys.argv) == 6:
        Path(sys.argv[5]).write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
