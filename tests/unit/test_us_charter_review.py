"""Lossless U.S. Charter bundle review tests."""

from __future__ import annotations

import json
from pathlib import Path

from tests.unit.us_charter_test_support import minimal_us_charter
from tests.unit.us_source_test_support import minimal_source_register

from nuclear_war_contest.situation_room import (
    load_source_register,
    load_us_charter,
    render_us_charter_bundle,
    write_us_charter_bundle_review,
)


def _load_bundle(tmp_path: Path):
    source_payload = minimal_source_register()
    source_path = tmp_path / "source-register.json"
    source_path.write_text(json.dumps(source_payload), encoding="utf-8")
    source_register = load_source_register(source_path)
    charter_payload = minimal_us_charter(source_register.content_hash)
    charter_path = tmp_path / "charter.json"
    charter_path.write_text(json.dumps(charter_payload), encoding="utf-8")
    charter = load_us_charter(charter_path, source_register)
    return source_register, charter


def _section_payload(rendered: str, heading: str) -> dict[str, object]:
    body = rendered.split(f"## {heading}\n\n```json\n", maxsplit=1)[1]
    return json.loads(body.split("\n```", maxsplit=1)[0])


def test_review_surface_round_trips_both_serialized_artifacts(tmp_path: Path) -> None:
    source_register, charter = _load_bundle(tmp_path)

    rendered = render_us_charter_bundle(source_register, charter)

    assert _section_payload(rendered, "Source register") == source_register.payload()
    assert _section_payload(rendered, "U.S. Charter") == charter.payload()


def test_review_surface_names_both_canonical_hashes(tmp_path: Path) -> None:
    source_register, charter = _load_bundle(tmp_path)

    rendered = render_us_charter_bundle(source_register, charter)

    assert source_register.content_hash in rendered
    assert charter.content_hash in rendered


def test_review_surface_preserves_declared_json_field_order(tmp_path: Path) -> None:
    source_register, charter = _load_bundle(tmp_path)

    rendered = render_us_charter_bundle(source_register, charter)

    source_body = rendered.split("## Source register\n\n```json\n", maxsplit=1)[1]
    charter_body = rendered.split("## U.S. Charter\n\n```json\n", maxsplit=1)[1]
    assert source_body.splitlines()[1].strip().startswith('"schema_version"')
    assert charter_body.splitlines()[1].strip().startswith('"schema_version"')


def test_review_writer_persists_exact_rendering(tmp_path: Path) -> None:
    source_register, charter = _load_bundle(tmp_path)
    path = tmp_path / "review.md"

    write_us_charter_bundle_review(path, source_register, charter)

    assert path.read_text(encoding="utf-8") == render_us_charter_bundle(
        source_register, charter
    )
