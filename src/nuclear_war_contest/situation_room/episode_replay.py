"""Deterministic two-cycle episode replay."""

from __future__ import annotations

from .episode_execution import run_no_model_two_cycle_episode
from .episode_models import TwoCycleRun


def replay_two_cycle_episode(source: TwoCycleRun) -> TwoCycleRun:
    replayed = run_no_model_two_cycle_episode(source.fixture())
    if replayed.content_hash != source.content_hash:
        raise ValueError("two-cycle replay hash does not match")
    return replayed


__all__ = ["replay_two_cycle_episode"]
