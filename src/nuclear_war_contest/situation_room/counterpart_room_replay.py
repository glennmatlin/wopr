"""Exact deterministic replay for counterpart Room traces."""

from __future__ import annotations

from .counterpart_artifacts import CounterpartCharter
from .counterpart_room_execution import (
    CounterpartRoomRun,
    run_no_model_counterpart_room,
)


def replay_counterpart_room(
    charter: CounterpartCharter, source: CounterpartRoomRun
) -> CounterpartRoomRun:
    replayed = run_no_model_counterpart_room(charter, source.fixture())
    if replayed.content_hash != source.content_hash:
        raise ValueError("replay_mismatch: counterpart Room receipt changed")
    return replayed


__all__ = ["replay_counterpart_room"]
