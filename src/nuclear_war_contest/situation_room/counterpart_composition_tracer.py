"""Fresh-process deterministic counterpart Room composition tracer."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .counterpart_composition_execution import run_no_model_counterpart_composition
from .counterpart_composition_fixture import load_counterpart_composition_fixture
from .counterpart_composition_replay import replay_counterpart_composition

IDENTITY_FIELDS = (
    "actor_id",
    "source_register_hash",
    "charter_hash",
    "room_fixture_hash",
    "room_run_hash",
    "room_receipt_hash",
    "decision_route_id",
    "mapping_owner",
    "mapping_type",
    "projection_id",
    "source_decision_record_id",
    "output_id",
    "output_hash",
)


def _require_revision(executor_revision: str) -> None:
    if len(executor_revision) != 40 or any(
        character not in "0123456789abcdef" for character in executor_revision
    ):
        raise ValueError("counterpart composition executor revision is invalid")


def _counterpart_identities(run_receipt: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {key: item[key] for key in IDENTITY_FIELDS}
        for item in run_receipt["counterparts"]
    ]


def _tracer_receipt(
    fixture: Any, run: Any, replayed: Any, executor_revision: str
) -> dict[str, Any]:
    receipts = fixture.receipts()
    run_receipt = run.receipt()
    receipt: dict[str, Any] = {
        "schema_version": "counterpart-room-composition-tracer-receipt.v0.1",
        "tracer_id": "m5-counterpart-room-composition-no-model-v1",
        "status": run_receipt["status"],
        "evidence_status": "development_fixture_non_evidence",
        "executor_revision": executor_revision,
        "upstream_receipt_hashes": {
            key: value["receipt_hash"] for key, value in receipts.items()
        },
        "counterpart_identities": _counterpart_identities(run_receipt),
        "us_two_cycle_source_receipt_hash": run_receipt["us_two_cycle"][
            "source_receipt_hash"
        ],
        "us_two_cycle_run_hash": run_receipt["us_two_cycle"]["run_hash"],
        "fixture_id": fixture.fixture_id,
        "fixture_hash": fixture.content_hash,
        "run_hash": run.content_hash,
        "run": run_receipt,
        "replay_matched": replayed.content_hash == run.content_hash
        and replayed.receipt() == run_receipt,
        "claim_boundary": list(run_receipt["claim_boundary"]),
    }
    receipt["receipt_hash"] = canonical_hash(receipt)
    return receipt


def run_counterpart_composition_tracer(
    fixture_path: Path, executor_revision: str
) -> dict[str, Any]:
    _require_revision(executor_revision)
    fixture = load_counterpart_composition_fixture(fixture_path)
    run = run_no_model_counterpart_composition(fixture)
    replayed = replay_counterpart_composition(run)
    return _tracer_receipt(fixture, run, replayed, executor_revision)


def main() -> None:
    if len(sys.argv) not in {3, 4}:
        raise SystemExit(
            "usage: situation_room.counterpart_composition_tracer "
            "FIXTURE EXECUTOR_REVISION [OUTPUT]"
        )
    receipt = run_counterpart_composition_tracer(Path(sys.argv[1]), sys.argv[2])
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if len(sys.argv) == 4:
        Path(sys.argv[3]).write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()


__all__ = ["run_counterpart_composition_tracer"]
