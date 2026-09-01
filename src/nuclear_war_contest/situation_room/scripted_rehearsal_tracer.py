"""Fresh-process tracer for the complete scripted Room rehearsal."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .episode_fixture import load_two_cycle_fixture
from .episode_models import TwoCycleFixture
from .scripted_rehearsal import run_scripted_two_cycle_rehearsal
from .scripted_rehearsal_replay import replay_scripted_two_cycle_rehearsal

_CALL_KINDS = (
    ("portfolio_product", "portfolio_product_calls"),
    ("group_product", "group_product_calls"),
    ("confirmation", "confirmation_calls"),
)


def run_scripted_rehearsal_tracer(
    fixture_path: Path, executor_revision: str
) -> dict[str, Any]:
    _validate_revision(executor_revision)
    fixture = load_two_cycle_fixture(fixture_path)
    run = run_scripted_two_cycle_rehearsal(fixture)
    replayed = replay_scripted_two_cycle_rehearsal(run)
    payload = run.receipt()
    manifest = _call_manifest(payload)
    counts = {kind: len(payload[field]) for kind, field in _CALL_KINDS}
    counts["total"] = sum(counts.values())
    receipt = _identity_receipt(fixture, run.content_hash, payload, executor_revision)
    receipt.update(
        {
            "call_counts": counts,
            "call_manifest_hash": canonical_hash(manifest),
            "call_manifest": manifest,
            "replay_matched": (
                replayed.content_hash == run.content_hash
                and replayed.receipt() == payload
            ),
            "claim_boundary": _claim_boundary(),
        }
    )
    receipt["receipt_hash"] = canonical_hash(receipt)
    return receipt


def _identity_receipt(
    fixture: TwoCycleFixture,
    run_hash: str,
    payload: dict[str, Any],
    executor_revision: str,
) -> dict[str, Any]:
    return {
        "schema_version": "scripted-room-rehearsal-receipt.v0.1",
        "tracer_id": "m6-complete-scripted-us-room-v1",
        "status": payload["status"],
        "evidence_status": "scripted_rehearsal_non_evidence",
        "executor_revision": executor_revision,
        "source_register_hash": fixture.source.content_hash,
        "charter_hash": fixture.charter.content_hash,
        "date_profile_hash": fixture.profile().content_hash,
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "cycle1_fixture_hash": fixture.cycle1_fixture().content_hash,
        "bridge_fixture_hash": fixture.bridge_fixture().content_hash,
        "cycle2_fixture_hash": fixture.cycle2_fixture().content_hash,
        "run_hash": run_hash,
        "episode_run_hash": payload["episode_run_hash"],
        "active_seat_ids": payload["active_seat_ids"],
        "cycle_schedules": payload["cycle_schedules"],
    }


def _claim_boundary() -> list[str]:
    return [
        "no_live_model_behavior_evidence",
        "no_government_behavior_evidence",
        "no_creative_excon_evidence",
        "no_matched_us_condition_evidence",
        "no_date_evaluation_evidence",
    ]


def _call_manifest(payload: dict[str, Any]) -> list[dict[str, Any]]:
    manifest: list[dict[str, Any]] = []
    for kind, field in _CALL_KINDS:
        for trace in payload[field]:
            attempts = trace["attempts"]
            manifest.append(
                {
                    "call_type": kind,
                    "call_id": trace["call"]["call_id"],
                    "cycle_id": trace["call"]["cycle_id"],
                    "group_id": trace["call"]["group_id"],
                    "seat_id": trace["seat_id"],
                    "status": trace["status"],
                    "attempt_count": len(attempts),
                    "prompt_hashes": [
                        canonical_hash(item["prompt"]) for item in attempts
                    ],
                    "raw_response_hashes": [
                        canonical_hash(item["raw_response"]) for item in attempts
                    ],
                    "parsed_product_hash": canonical_hash(
                        attempts[-1]["parsed_product"]
                    ),
                    "trace_hash": canonical_hash(trace),
                }
            )
    return manifest


def _validate_revision(executor_revision: str) -> None:
    if len(executor_revision) != 40 or any(
        character not in "0123456789abcdef" for character in executor_revision
    ):
        raise ValueError("scripted Room tracer executor revision is invalid")


def main() -> None:
    if len(sys.argv) not in {3, 4}:
        raise SystemExit(
            "usage: situation_room.scripted_rehearsal_tracer "
            "FIXTURE EXECUTOR_REVISION [OUTPUT]"
        )
    receipt = run_scripted_rehearsal_tracer(Path(sys.argv[1]), sys.argv[2])
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if len(sys.argv) == 4:
        Path(sys.argv[3]).write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()


__all__ = ["run_scripted_rehearsal_tracer"]
