"""Derived metrics retained on contest failure receipts."""

from __future__ import annotations

from typing import Any


def transport_retry_count(metrics: Any) -> int:
    if not isinstance(metrics, dict):
        return 0
    total = 0
    for channel in ("c2", "press"):
        values = metrics.get(channel)
        if not isinstance(values, dict):
            continue
        retries = values.get("transport_retry_count")
        if not isinstance(retries, int) or isinstance(retries, bool):
            retries = values.get("recoverable_provider_retry_count")
        if isinstance(retries, int) and not isinstance(retries, bool) and retries >= 0:
            total += retries
    return total


__all__ = ["transport_retry_count"]
