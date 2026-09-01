"""U.S. Charter source-register behavior tests."""

from __future__ import annotations

import json
from pathlib import Path

from tests.unit.us_source_test_support import minimal_source_register

from nuclear_war_contest.situation_room import load_source_register


def test_load_source_register_binds_candidate_identity(tmp_path: Path) -> None:
    path = tmp_path / "source-register.json"
    path.write_text(json.dumps(minimal_source_register()), encoding="utf-8")

    register = load_source_register(path)

    assert register.register_id == "US_PUBLIC_2026Q3.sources"
    assert register.register_version == "0.1.0"
    assert len(register.content_hash) == 64
    assert register.payload() == minimal_source_register()
