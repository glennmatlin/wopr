"""Fresh-process no-model U.S. Cycle 1 tracer."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

from .charter import load_us_charter
from .cycle_execution import run_no_model_us_cycle
from .cycle_fixture import load_us_cycle_fixture
from .cycle_replay import replay_us_cycle
from .source_register import load_source_register


def run_cycle_tracer(
    source_path: Path,
    charter_path: Path,
    ratification_path: Path,
    fixture_path: Path,
    executor_revision: str,
) -> dict[str, Any]:
    if len(executor_revision) != 40 or any(
        character not in "0123456789abcdef" for character in executor_revision
    ):
        raise ValueError("U.S. cycle tracer executor revision is invalid")
    source = load_source_register(source_path)
    charter = load_us_charter(charter_path, source)
    fixture = load_us_cycle_fixture(fixture_path, charter, ratification_path)
    ratification = load_strict_json(ratification_path)
    if not isinstance(ratification, dict):
        raise ValueError("invalid_envelope: ratification receipt must be an object")
    run = run_no_model_us_cycle(charter, fixture)
    replayed = replay_us_cycle(charter, run)
    fixture_payload = fixture.payload()
    receipt: dict[str, Any] = {
        "schema_version": "us-cycle-tracer-receipt.v0.1",
        "tracer_id": "m2-us-cycle1-no-model-v1",
        "status": run.receipt()["status"],
        "evidence_status": "development_fixture_non_evidence",
        "executor_revision": executor_revision,
        "source_register_id": source.register_id,
        "source_register_hash": source.content_hash,
        "charter_id": charter.charter_id,
        "charter_version": charter.charter_version,
        "charter_hash": charter.content_hash,
        "ratification_id": ratification["ratification_id"],
        "ratification_hash": fixture.ratification_hash,
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "counterpart_fixtures": [
            {
                "fixture_id": item["fixture_id"],
                "actor_id": item["actor_id"],
                "status": item["status"],
                "fixture_hash": canonical_hash(item),
            }
            for item in fixture_payload["counterpart_fixtures"]
        ],
        "run_hash": run.content_hash,
        "run": run.receipt(),
        "replay_matched": (
            replayed.content_hash == run.content_hash
            and replayed.receipt() == run.receipt()
        ),
        "claim_boundary": [
            "no_model_behavior_evidence",
            "no_counterpart_room_evidence",
            "no_world_effect_admission",
            "no_date_episode_evidence",
            "no_comparative_result",
        ],
    }
    receipt["receipt_hash"] = canonical_hash(receipt)
    return receipt


def main() -> None:
    if len(sys.argv) not in {6, 7}:
        raise SystemExit(
            "usage: situation_room.cycle_tracer SOURCE CHARTER "
            "RATIFICATION FIXTURE EXECUTOR_REVISION [OUTPUT]"
        )
    receipt = run_cycle_tracer(
        Path(sys.argv[1]),
        Path(sys.argv[2]),
        Path(sys.argv[3]),
        Path(sys.argv[4]),
        sys.argv[5],
    )
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if len(sys.argv) == 7:
        Path(sys.argv[6]).write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
