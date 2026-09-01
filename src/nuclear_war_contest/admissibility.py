"""Run admissibility tiers for the contest primary analysis."""

from __future__ import annotations

from typing import Any

from nuclear_war_concordia.c2_artifacts import validate_c2_artifact
from nuclear_war_concordia.call_budget import partial_metrics
from nuclear_war_concordia.press_artifacts import validate_press_artifact
from nuclear_war_env.llm_trace_artifacts import validate_trace_artifact
from nuclear_war_env.replay_validation import validate_replay_payload

from .admissibility_metrics import transport_retry_count
from .admissibility_traces import all_traces
from .runner_budget import ChannelCapExceeded


def classify_result(result: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    try:
        validate_result_artifacts(result)
    except (KeyError, TypeError, ValueError):
        reasons.append("invalid_or_incomplete_artifacts")
    traces = all_traces(result)
    if not traces:
        reasons.append("missing_trace")
    if "c2_artifact" not in result:
        reasons.append("missing_c2_sidecar")
    press_enabled = result.get("config_snapshot", {}).get("press", {}).get("enabled")
    if press_enabled and "press_artifact" not in result:
        reasons.append("missing_press_sidecar")
    fallback_count = sum(bool(trace.get("fallback_used")) for trace in traces)
    output_reprompts = sum(int(trace.get("retries", 0)) for trace in traces)
    validation_errors = sum(len(trace.get("validation_errors", [])) for trace in traces)
    transport_retries = sum(
        int(trace.get("recoverable_provider_retries", 0)) for trace in traces
    )
    if fallback_count:
        reasons.append("fallback_used")
    if reasons:
        tier = "C"
    elif output_reprompts or validation_errors:
        tier = "B"
    else:
        tier = "A"
    return {
        "tier": tier,
        "reasons": reasons,
        "trace_count": len(traces),
        "fallback_count": fallback_count,
        "output_reprompt_count": output_reprompts,
        "validation_error_count": validation_errors,
        "transport_retry_count": transport_retries,
    }


def classify_failure(error: BaseException) -> dict[str, Any]:
    retryable = _retryable_error(error)
    budget_failure = _budget_failure(error)
    reason = (
        "channel_cap_exceeded"
        if isinstance(error, ChannelCapExceeded)
        or getattr(error, "channel_budget_exceeded", False)
        or budget_failure
        else "provider_or_runner_error"
    )
    payload: dict[str, Any] = {
        "tier": "C",
        "reasons": [reason],
        "retryable": retryable,
        "error_type": type(error).__name__,
        "error": "redacted",
        "trace_count": 0,
        "fallback_count": 0,
        "output_reprompt_count": 0,
        "validation_error_count": 0,
        "transport_retry_count": 0,
    }
    snapshot = getattr(error, "snapshot", None)
    if isinstance(snapshot, dict):
        payload["failure_snapshot"] = snapshot
        snapshot_metrics = snapshot.get("channel_metrics")
        if isinstance(snapshot_metrics, dict):
            payload["channel_metrics"] = snapshot_metrics
    metrics = partial_metrics(error)
    if metrics is not None:
        payload["channel_metrics"] = metrics
    payload["transport_retry_count"] = transport_retry_count(
        payload.get("channel_metrics")
    )
    metrics = payload.get("channel_metrics")
    if isinstance(metrics, dict) and any(
        _blocked_call(values) for values in metrics.values() if isinstance(values, dict)
    ):
        payload["blocked_before_dispatch"] = True
    return payload


def _blocked_call(values: dict[str, Any]) -> bool:
    calls = values.get("call_count")
    attempts = values.get("provider_attempt_count")
    return isinstance(calls, int) and isinstance(attempts, int) and calls > attempts


def _budget_failure(error: BaseException) -> bool:
    snapshot = getattr(error, "snapshot", None)
    if not isinstance(snapshot, dict):
        return False
    decision_failure = snapshot.get("decision_failure")
    if not isinstance(decision_failure, dict):
        return False
    exception = decision_failure.get("exception")
    return isinstance(exception, dict) and exception.get("type") in {
        "ChannelRequestBudgetExceeded",
        "ChannelCapExceeded",
    }


def validate_result_artifacts(result: dict[str, Any]) -> None:
    replay = result["replay"]
    validate_replay_payload(replay)
    validate_trace_artifact(result["trace_artifact"], replay)
    validate_c2_artifact(result["c2_artifact"], replay)
    press_enabled = result["config_snapshot"]["press"]["enabled"]
    if press_enabled:
        validate_press_artifact(result["press_artifact"], replay)
    elif "press_artifact" in result:
        validate_press_artifact(result["press_artifact"], replay)


def _retryable_error(error: BaseException) -> bool:
    if bool(getattr(error, "retryable", False)):
        return True
    if type(error).__name__ in {"LLMHttpError", "TimeoutError", "ConnectionError"}:
        return True
    snapshot = getattr(error, "snapshot", None)
    if not isinstance(snapshot, dict):
        return False
    decision_failure = snapshot.get("decision_failure")
    if not isinstance(decision_failure, dict):
        return False
    exception = decision_failure.get("exception")
    return isinstance(exception, dict) and exception.get("type") in {
        "LLMHttpError",
        "TimeoutError",
        "ConnectionError",
    }


__all__ = ["classify_failure", "classify_result", "validate_result_artifacts"]
