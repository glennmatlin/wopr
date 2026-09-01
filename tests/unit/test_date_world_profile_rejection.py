"""Fail-closed DATE candidate-profile loading tests."""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest

from nuclear_war_contest.date_world import load_profile

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)


def _add_projection(payload: dict[str, Any], selector: dict[str, str]) -> None:
    payload["initial_core"]["outcome_projections"]["bad"] = selector
    payload["outcome_projection_ids"].append("bad")


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda payload: payload.update({"unknown": True}), "fields"),
        (
            lambda payload: payload["initial_core"]["actors"].append(
                payload["initial_core"]["actors"][0]
            ),
            "duplicate_id",
        ),
        (
            lambda payload: payload["initial_core"]["locations"][0].update(
                {"location_id": "USA"}
            ),
            "duplicate_id",
        ),
        (
            lambda payload: payload["initial_core"]["actors"][0].update(
                {"unknown": True}
            ),
            "fields",
        ),
        (
            lambda payload: payload["initial_core"]["force_packages"][0].update(
                {"readiness": "teleporting"}
            ),
            "readiness",
        ),
        (
            lambda payload: payload["initial_core"].update({"terminal_state": None}),
            "Core state",
        ),
        (
            lambda payload: payload["authored_event_templates"][0].update(
                {"unknown": True}
            ),
            "fields",
        ),
        (
            lambda payload: payload["authored_event_templates"][0].update(
                {"episode_hour": True}
            ),
            "episode_hour",
        ),
        (
            lambda payload: payload["authored_event_templates"].append(
                payload["authored_event_templates"][0]
            ),
            "duplicate_id",
        ),
        (
            lambda payload: payload["authored_event_templates"][0].update(
                {"affected_entity_ids": ["ENTITY_UNEARNED"]}
            ),
            "unknown_reference",
        ),
        (
            lambda payload: payload["authored_event_templates"][1].update(
                {"causal_parent_ids": ["OBS_WX_RIDGE_CONFIRMED_01"]}
            ),
            "causal parent is not prior",
        ),
        (
            lambda payload: payload["episode"].update({"unknown": 1}),
            "episode fields",
        ),
        (
            lambda payload: payload["road_to_war"][0].update({"unknown": 1}),
            "Road to War fields",
        ),
        (
            lambda payload: payload["partner_request"].update({"unknown": 1}),
            "partner request fields",
        ),
        (
            lambda payload: payload["terminal_policy"]["early_conditions"][0].update(
                {"unknown": 1}
            ),
            "terminal condition fields",
        ),
        (
            lambda payload: payload["authored_event_templates"][0][
                "uncertainty"
            ].update({"unknown": 1}),
            "uncertainty fields",
        ),
        (
            lambda payload: _add_projection(
                payload, {"selector": "arbitrary_path", "path": "actors.0"}
            ),
            "selector",
        ),
        (
            lambda payload: _add_projection(
                payload,
                {
                    "selector": "affordance_state",
                    "affordance_id": "AFF_UNEARNED",
                },
            ),
            "unresolved",
        ),
    ],
)
def test_profile_loading_fails_closed(
    tmp_path: Path,
    mutation: Callable[[dict[str, Any]], None],
    message: str,
) -> None:
    payload = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    mutation(payload)
    path = tmp_path / "candidate.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        load_profile(path)


def test_profile_loading_rejects_duplicate_json_keys(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.json"
    path.write_text(
        '{"schema_version":"date-profile.v0.2","profile_id":"one","profile_id":"two"}',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Duplicate JSON key: profile_id"):
        load_profile(path)
