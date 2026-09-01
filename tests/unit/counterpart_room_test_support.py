"""Shared helpers for counterpart Room mutation tests."""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from nuclear_war_contest.situation_room import (
    load_actor_source_register,
    load_counterpart_charter,
    load_counterpart_room_fixture,
    run_no_model_counterpart_room,
)

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"
RATIFICATION = CONTEST / "COUNTERPART_CHARTER_RATIFICATION.json"


def mutated_room_run(
    prefix: str,
    tmp_path: Path,
    mutation: Callable[[dict[str, Any]], None],
) -> dict[str, Any]:
    source = load_actor_source_register(
        CONTEST / f"{prefix}_SOURCE_REGISTER.candidate.json"
    )
    charter = load_counterpart_charter(
        CONTEST / f"{prefix}_CHARTER.candidate.json", source
    )
    fixture_path = CONTEST / f"{prefix}_ROOM_FIXTURE.development.json"
    payload = json.loads(fixture_path.read_text(encoding="utf-8"))
    mutation(payload)
    path = tmp_path / f"{prefix.lower()}-fixture.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_counterpart_room_fixture(path, charter, RATIFICATION)
    return run_no_model_counterpart_room(charter, fixture).receipt()


def room_product(payload: dict[str, Any], group_id: str) -> dict[str, Any]:
    return next(
        item for item in payload["group_products"] if item["group_id"] == group_id
    )


__all__ = ["mutated_room_run", "room_product"]
