"""Exact envelope checks for DATE profile metadata."""

from __future__ import annotations

from typing import Any

EPISODE_FIELDS = {
    "startex_hour",
    "us_cycle_1_decision_hour",
    "cycle_1_consequences_close_hour",
    "matched_barrier_hour",
    "us_cycle_2_decision_hour",
    "himaldesh_recapture_decision_hour",
    "normal_terminal_hour",
}
PARTNER_FIELDS = {"request_id", "requested", "excluded", "disposition_due_hour"}
TERMINAL_FIELDS = {
    "normal_terminal_hour",
    "early_terminal_id",
    "early_conditions",
    "execution_failure_is_outcome",
}


def _integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"DATE profile {label} is invalid")
    return value


def _text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"DATE profile {label} is invalid")
    return value


def _text_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item for item in value
    ):
        raise ValueError(f"DATE profile {label} is invalid")
    if len(value) != len(set(value)):
        raise ValueError(f"DATE profile {label} has duplicate_id")
    return value


def _validate_episode(payload: dict[str, Any]) -> None:
    episode = payload.get("episode")
    if not isinstance(episode, dict) or set(episode) != EPISODE_FIELDS:
        raise ValueError("DATE profile episode fields are invalid")
    hours = [_integer(episode[field], f"episode {field}") for field in EPISODE_FIELDS]
    ordered_fields = (
        "startex_hour",
        "us_cycle_1_decision_hour",
        "cycle_1_consequences_close_hour",
        "matched_barrier_hour",
        "us_cycle_2_decision_hour",
        "himaldesh_recapture_decision_hour",
        "normal_terminal_hour",
    )
    if [episode[field] for field in ordered_fields] != sorted(hours):
        raise ValueError("DATE profile episode hours are not ordered")


def _validate_road_to_war(payload: dict[str, Any]) -> None:
    records = payload.get("road_to_war")
    if not isinstance(records, list) or not records:
        raise ValueError("DATE profile Road to War is invalid")
    prior_hour: int | None = None
    for record in records:
        if not isinstance(record, dict) or set(record) != {
            "episode_hour",
            "development",
        }:
            raise ValueError("DATE profile Road to War fields are invalid")
        hour = _integer(record["episode_hour"], "Road to War episode_hour")
        _text(record["development"], "Road to War development")
        if prior_hour is not None and hour < prior_hour:
            raise ValueError("DATE profile Road to War is not ordered")
        prior_hour = hour


def _validate_partner_request(payload: dict[str, Any]) -> None:
    request = payload.get("partner_request")
    if not isinstance(request, dict) or set(request) != PARTNER_FIELDS:
        raise ValueError("DATE profile partner request fields are invalid")
    _text(request["request_id"], "partner request identity")
    requested = _text_list(request["requested"], "partner requested support")
    excluded = _text_list(request["excluded"], "partner excluded support")
    if set(requested) & set(excluded):
        raise ValueError("DATE profile partner support overlaps")
    _integer(request["disposition_due_hour"], "partner disposition hour")


def _validate_terminal_policy(payload: dict[str, Any]) -> None:
    policy = payload.get("terminal_policy")
    if not isinstance(policy, dict) or set(policy) != TERMINAL_FIELDS:
        raise ValueError("DATE profile terminal policy fields are invalid")
    _integer(policy["normal_terminal_hour"], "terminal hour")
    _text(policy["early_terminal_id"], "early terminal identity")
    if not isinstance(policy["execution_failure_is_outcome"], bool):
        raise ValueError("DATE profile terminal execution policy is invalid")
    conditions = policy["early_conditions"]
    if not isinstance(conditions, list) or not conditions:
        raise ValueError("DATE profile terminal conditions are invalid")
    core = payload["initial_core"]
    location_ids = {item["location_id"] for item in core["locations"]}
    actor_ids = {item["actor_id"] for item in core["actors"]}
    authorization_ids = {item["authorization_id"] for item in core["authorizations"]}
    for condition in conditions:
        kind = condition.get("condition") if isinstance(condition, dict) else None
        if kind == "location_control_not_equals":
            if set(condition) != {"condition", "location_id", "actor_id"}:
                raise ValueError("DATE profile terminal condition fields are invalid")
            if (
                condition["location_id"] not in location_ids
                or condition["actor_id"] not in actor_ids
            ):
                raise ValueError("DATE terminal condition has unknown_reference")
        elif kind == "authorization_state_equals":
            if set(condition) != {"condition", "authorization_id", "value"}:
                raise ValueError("DATE profile terminal condition fields are invalid")
            if condition["authorization_id"] not in authorization_ids:
                raise ValueError("DATE terminal condition has unknown_reference")
            _text(condition["value"], "terminal condition value")
        else:
            raise ValueError("DATE profile terminal condition is invalid")


def validate_profile_metadata(payload: dict[str, Any]) -> None:
    if payload.get("status") != "candidate":
        raise ValueError("DATE profile status is invalid")
    _validate_episode(payload)
    _validate_road_to_war(payload)
    _validate_partner_request(payload)
    ladder = _text_list(payload.get("escalation_ladder"), "escalation ladder")
    if payload["initial_core"]["escalation_state"] not in ladder:
        raise ValueError("DATE escalation state has unknown_reference")
    _validate_terminal_policy(payload)


__all__ = ["validate_profile_metadata"]
