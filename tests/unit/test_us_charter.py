"""U.S. Room Charter behavior tests."""

from __future__ import annotations

import json
from pathlib import Path

from tests.unit.us_charter_test_support import minimal_us_charter
from tests.unit.us_source_test_support import minimal_source_register

from nuclear_war_contest.situation_room import load_source_register, load_us_charter


def test_load_us_charter_binds_source_snapshot_and_identity(tmp_path: Path) -> None:
    source_path = tmp_path / "source-register.json"
    source_path.write_text(json.dumps(minimal_source_register()), encoding="utf-8")
    source_register = load_source_register(source_path)
    charter_payload = minimal_us_charter(source_register.content_hash)
    charter_path = tmp_path / "charter.json"
    charter_path.write_text(json.dumps(charter_payload), encoding="utf-8")

    charter = load_us_charter(charter_path, source_register)

    assert charter.charter_id == "US_PUBLIC_2026Q3"
    assert charter.charter_version == "0.1.0"
    assert charter.source_register_hash == source_register.content_hash
    assert len(charter.content_hash) == 64
    assert charter.payload() == charter_payload
