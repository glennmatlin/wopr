"""Deterministic no-model U.S. cycle replay."""

from __future__ import annotations

from .charter import UsCharter
from .cycle_execution import UsCycleRun, run_no_model_us_cycle


def replay_us_cycle(charter: UsCharter, source: UsCycleRun) -> UsCycleRun:
    replayed = run_no_model_us_cycle(charter, source.fixture())
    if replayed.content_hash != source.content_hash:
        raise ValueError("replay_mismatch: U.S. cycle receipt changed")
    return replayed


__all__ = ["replay_us_cycle"]
