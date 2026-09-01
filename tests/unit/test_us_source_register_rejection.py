"""Fail-closed U.S. source-register tests."""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest
from tests.unit.us_source_test_support import minimal_source_register

from nuclear_war_contest.situation_room import load_source_register


@pytest.mark.parametrize(
    ("mutation", "reason_code"),
    [
        (lambda payload: payload.update({"unknown": True}), "invalid_envelope"),
        (
            lambda payload: payload["sources"].append(payload["sources"][0]),
            "duplicate_id",
        ),
        (
            lambda payload: payload["sources"][0].update(
                {"current_officeholder": "forbidden"}
            ),
            "forbidden_officeholder_field",
        ),
        (
            lambda payload: payload["sources"][0].update(
                {"fact_ids": ["FACT_UNKNOWN"]}
            ),
            "unbound_fact",
        ),
        (
            lambda payload: payload["sources"][0].update({"fact_ids": []}),
            "unbound_fact",
        ),
        (
            lambda payload: payload["sources"][0].update({"inference_ids": []}),
            "unbound_inference",
        ),
        (
            lambda payload: payload["facts"][0].update({"source_ids": []}),
            "unbound_fact",
        ),
        (
            lambda payload: payload["inferences"][0].update({"source_ids": []}),
            "unbound_inference",
        ),
        (
            lambda payload: payload["sources"][0].update(
                {"evidence_status": "official_truth"}
            ),
            "invalid_envelope",
        ),
    ],
)
def test_source_register_fails_closed(
    tmp_path: Path,
    mutation: Callable[[dict[str, Any]], None],
    reason_code: str,
) -> None:
    payload = minimal_source_register()
    mutation(payload)
    path = tmp_path / "source-register.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match=reason_code):
        load_source_register(path)


def test_source_register_rejects_duplicate_json_keys(tmp_path: Path) -> None:
    path = tmp_path / "source-register.json"
    path.write_text('{"register_id":"one","register_id":"two"}', encoding="utf-8")

    with pytest.raises(ValueError, match="invalid_envelope"):
        load_source_register(path)
