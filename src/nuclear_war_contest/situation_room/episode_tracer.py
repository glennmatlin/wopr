"""Fresh-process deterministic two-cycle episode tracer."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .episode_execution import run_no_model_two_cycle_episode
from .episode_fixture import load_two_cycle_fixture
from .episode_replay import replay_two_cycle_episode


def run_episode_tracer(fixture_path: Path, executor_revision: str) -> dict[str, Any]:
    if len(executor_revision) != 40 or any(
        character not in "0123456789abcdef" for character in executor_revision
    ):
        raise ValueError("two-cycle tracer executor revision is invalid")
    fixture = load_two_cycle_fixture(fixture_path)
    run = run_no_model_two_cycle_episode(fixture)
    replayed = replay_two_cycle_episode(run)
    upstream = fixture.receipts()
    receipt: dict[str, Any] = {
        "schema_version": "us-two-cycle-tracer-receipt.v0.1",
        "tracer_id": "m4-us-two-cycle-no-model-v1",
        "status": run.receipt()["status"],
        "evidence_status": "development_fixture_non_evidence",
        "executor_revision": executor_revision,
        "source_register_hash": fixture.source.content_hash,
        "charter_hash": fixture.charter.content_hash,
        "date_profile_hash": fixture.profile().content_hash,
        "upstream_receipt_hashes": {
            key: value["receipt_hash"] for key, value in upstream.items()
        },
        "cycle1_fixture_hash": fixture.cycle1_fixture().content_hash,
        "bridge_fixture_hash": fixture.bridge_fixture().content_hash,
        "cycle2_fixture_hash": fixture.cycle2_fixture().content_hash,
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "run_hash": run.content_hash,
        "run": run.receipt(),
        "replay_matched": (
            replayed.content_hash == run.content_hash
            and replayed.receipt() == run.receipt()
        ),
        "claim_boundary": [
            "no_model_behavior_evidence",
            "no_creative_excon_evidence",
            "no_counterpart_room_evidence",
            "no_matched_us_condition_evidence",
            "no_date_evaluation_evidence",
        ],
    }
    receipt["receipt_hash"] = canonical_hash(receipt)
    return receipt


def main() -> None:
    if len(sys.argv) not in {3, 4}:
        raise SystemExit(
            "usage: situation_room.episode_tracer FIXTURE EXECUTOR_REVISION [OUTPUT]"
        )
    receipt = run_episode_tracer(Path(sys.argv[1]), sys.argv[2])
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if len(sys.argv) == 4:
        Path(sys.argv[3]).write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()


__all__ = ["run_episode_tracer"]
