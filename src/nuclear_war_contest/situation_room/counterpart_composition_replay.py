"""Exact replay for counterpart Room composition."""

from __future__ import annotations

from .counterpart_composition_execution import run_no_model_counterpart_composition
from .counterpart_composition_models import CounterpartCompositionRun


def replay_counterpart_composition(
    source: CounterpartCompositionRun,
) -> CounterpartCompositionRun:
    replayed = run_no_model_counterpart_composition(source.fixture())
    if (
        replayed.content_hash != source.content_hash
        or replayed.receipt() != source.receipt()
    ):
        raise ValueError("replay_mismatch: counterpart composition changed")
    return replayed


__all__ = ["replay_counterpart_composition"]
