"""Exact replay for scripted Room rehearsal."""

from __future__ import annotations

from .scripted_rehearsal import run_scripted_two_cycle_rehearsal
from .scripted_rehearsal_models import ScriptedRehearsalRun


def replay_scripted_two_cycle_rehearsal(
    source: ScriptedRehearsalRun,
) -> ScriptedRehearsalRun:
    replayed = run_scripted_two_cycle_rehearsal(source.fixture())
    if replayed.content_hash != source.content_hash:
        raise ValueError("scripted Room rehearsal replay hash does not match")
    return replayed


__all__ = ["replay_scripted_two_cycle_rehearsal"]
