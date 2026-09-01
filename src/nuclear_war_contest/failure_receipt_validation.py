"""Structural checks for preserved contest failure receipts."""

from __future__ import annotations

import math
from typing import Any

from .admissibility_metrics import transport_retry_count


def validate_failure_receipt(payload: dict[str, Any]) -> None:
    if payload.get("tier") != "C":
        raise ValueError("Failure receipt tier must be C")
    reasons = payload.get("reasons")
    if (
        not isinstance(reasons, list)
        or not reasons
        or not all(isinstance(item, str) and item for item in reasons)
    ):
        raise ValueError("Failure receipt reasons are invalid")
    if type(payload.get("retryable")) is not bool:
        raise ValueError("Failure receipt retryable flag is invalid")
    blocked = payload.get("blocked_before_dispatch", False)
    if type(blocked) is not bool:
        raise ValueError("Failure receipt blocked-before-dispatch flag is invalid")
    error_type = payload.get("error_type")
    if not isinstance(error_type, str) or not error_type:
        raise ValueError("Failure receipt error type is invalid")
    for field in (
        "trace_count",
        "fallback_count",
        "output_reprompt_count",
        "validation_error_count",
        "transport_retry_count",
    ):
        value = payload.get(field)
        if type(value) is not int or value < 0:
            raise ValueError(f"Failure receipt {field} is invalid")
    metrics = payload.get("channel_metrics")
    snapshot = payload.get("failure_snapshot")
    if blocked and not isinstance(metrics, dict):
        raise ValueError("Failure receipt blocked metrics are missing")
    if metrics is not None:
        _validate_metrics(metrics, blocked)
        if blocked and len(_deficit_channels(metrics)) != 1:
            raise ValueError(
                "Failure receipt blocked-before-dispatch channel is invalid"
            )
        if payload["transport_retry_count"] != transport_retry_count(metrics):
            raise ValueError("Failure receipt transport retries do not match")
    if snapshot is not None:
        if not isinstance(snapshot, dict):
            raise ValueError("Failure receipt snapshot is invalid")
        snapshot_metrics = snapshot.get("channel_metrics")
        if snapshot_metrics is not None:
            _validate_metrics(snapshot_metrics, blocked)
            if blocked and len(_deficit_channels(snapshot_metrics)) != 1:
                raise ValueError(
                    "Failure receipt blocked-before-dispatch channel is invalid"
                )
            if metrics is not None and snapshot_metrics != metrics:
                raise ValueError("Failure receipt channel metrics do not match")


def _validate_metrics(metrics: Any, blocked: bool = False) -> None:
    if not isinstance(metrics, dict):
        raise ValueError("Failure receipt channel metrics are invalid")
    for channel in ("c2", "press"):
        values = metrics.get(channel)
        if not isinstance(values, dict):
            raise ValueError(f"Failure receipt {channel} metrics are invalid")
        calls = values.get("call_count")
        if type(calls) is not int or calls < 0:
            raise ValueError(f"Failure receipt {channel} call count is invalid")
        attempts = values.get("provider_attempt_count")
        retries = values.get("transport_retry_count")
        if type(attempts) is not int or attempts < 0:
            raise ValueError(f"Failure receipt {channel} attempts are invalid")
        if type(retries) is not int or retries < 0:
            raise ValueError(f"Failure receipt {channel} retries are invalid")
        if attempts < calls and (not blocked or calls - attempts != 1):
            raise ValueError(f"Failure receipt {channel} attempts are invalid")
        expected_retries = max(0, attempts - calls)
        if retries != expected_retries:
            raise ValueError(f"Failure receipt {channel} retries are invalid")
        usage = values.get("provider_usage")
        if usage is not None:
            _validate_usage(usage)
    _validate_costs(metrics)


def _deficit_channels(metrics: dict[str, Any]) -> list[str]:
    deficits: list[str] = []
    for channel in ("c2", "press"):
        values = metrics.get(channel)
        if not isinstance(values, dict):
            continue
        calls = values.get("call_count")
        attempts = values.get("provider_attempt_count")
        if isinstance(calls, int) and isinstance(attempts, int) and calls > attempts:
            deficits.append(channel)
    return deficits


def _validate_costs(metrics: dict[str, Any]) -> None:
    for field in (
        "reserved_cost_usd",
        "actual_cost_usd",
        "study_reserved_cost_usd",
        "study_actual_cost_usd",
    ):
        value = metrics.get(field)
        if value is not None and (
            not isinstance(value, int | float)
            or isinstance(value, bool)
            or not math.isfinite(float(value))
            or value < 0
        ):
            raise ValueError(f"Failure receipt {field} is invalid")


def _validate_usage(usage: Any) -> None:
    if not isinstance(usage, dict) or any(
        not isinstance(value, int | float) or isinstance(value, bool) or value < 0
        for value in usage.values()
    ):
        raise ValueError("Failure receipt provider usage is invalid")


__all__ = ["validate_failure_receipt"]
