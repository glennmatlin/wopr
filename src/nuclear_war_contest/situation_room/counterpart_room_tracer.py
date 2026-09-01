"""Fresh-process deterministic counterpart Room tracer."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json

from .counterpart_artifacts import (
    load_actor_source_register,
    load_counterpart_charter,
)
from .counterpart_room_execution import run_no_model_counterpart_room
from .counterpart_room_fixture import load_counterpart_room_fixture
from .counterpart_room_replay import replay_counterpart_room


def _ratification(path: Path) -> dict[str, Any]:
    payload = load_strict_json(path)
    if not isinstance(payload, dict):
        raise ValueError("invalid_envelope: counterpart ratification must be an object")
    return payload


def _require_revision(executor_revision: str) -> None:
    if len(executor_revision) != 40 or any(
        character not in "0123456789abcdef" for character in executor_revision
    ):
        raise ValueError("counterpart Room tracer executor revision is invalid")


def _identity_fields(
    source: Any,
    charter: Any,
    ratification: dict[str, Any],
    fixture: Any,
    executor_revision: str,
) -> dict[str, Any]:
    actor_slug = charter.actor_id.removeprefix("ACTOR_").lower()
    return {
        "schema_version": "counterpart-room-tracer-receipt.v0.1",
        "tracer_id": f"m5-{actor_slug}-room-no-model-v1",
        "evidence_status": "development_fixture_non_evidence",
        "actor_id": charter.actor_id,
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
    }


def _claim_boundary() -> list[str]:
    return [
        "no_model_behavior_evidence",
        "no_live_counterpart_room_evidence",
        "no_world_effect_admission",
        "no_date_episode_evidence",
        "no_comparative_result",
    ]


def _tracer_receipt(
    source: Any,
    charter: Any,
    ratification: dict[str, Any],
    fixture: Any,
    executor_revision: str,
) -> dict[str, Any]:
    run = run_no_model_counterpart_room(charter, fixture)
    replayed = replay_counterpart_room(charter, run)
    receipt = _identity_fields(
        source, charter, ratification, fixture, executor_revision
    )
    receipt.update(
        {
            "status": run.receipt()["status"],
            "run_hash": run.content_hash,
            "run": run.receipt(),
            "replay_matched": (
                replayed.content_hash == run.content_hash
                and replayed.receipt() == run.receipt()
            ),
            "claim_boundary": _claim_boundary(),
        }
    )
    receipt["receipt_hash"] = canonical_hash(receipt)
    return receipt


def run_counterpart_room_tracer(
    source_path: Path,
    charter_path: Path,
    ratification_path: Path,
    fixture_path: Path,
    executor_revision: str,
) -> dict[str, Any]:
    _require_revision(executor_revision)
    source = load_actor_source_register(source_path)
    charter = load_counterpart_charter(charter_path, source)
    fixture = load_counterpart_room_fixture(fixture_path, charter, ratification_path)
    ratification = _ratification(ratification_path)
    return _tracer_receipt(source, charter, ratification, fixture, executor_revision)


def main() -> None:
    if len(sys.argv) not in {6, 7}:
        raise SystemExit(
            "usage: situation_room.counterpart_room_tracer SOURCE CHARTER "
            "RATIFICATION FIXTURE EXECUTOR_REVISION [OUTPUT]"
        )
    receipt = run_counterpart_room_tracer(
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


__all__ = ["run_counterpart_room_tracer"]
