"""Trace collection used by contest admissibility classification."""

from __future__ import annotations

from typing import Any


def all_traces(result: dict[str, Any]) -> list[dict[str, Any]]:
    traces: list[dict[str, Any]] = []
    trace_artifact = result.get("trace_artifact", {})
    if isinstance(trace_artifact, dict):
        traces.extend(dict_list(trace_artifact.get("traces")))
    c2_artifact = result.get("c2_artifact", {})
    if isinstance(c2_artifact, dict):
        for deliberation in dict_list(c2_artifact.get("deliberations")):
            for member in dict_list(deliberation.get("members")):
                trace = member.get("trace")
                if isinstance(trace, dict):
                    traces.append(trace)
    press_payload = result.get("press_artifact")
    if isinstance(press_payload, dict):
        traces.extend(dict_list(press_payload.get("messages")))
    return traces


def dict_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


__all__ = ["all_traces"]
