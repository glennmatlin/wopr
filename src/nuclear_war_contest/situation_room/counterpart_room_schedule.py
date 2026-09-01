"""Deterministic scheduling for counterpart Room groups."""

from __future__ import annotations

from .counterpart_compiled_models import CompiledCounterpartCharter


def next_counterpart_wave(
    compiled: CompiledCounterpartCharter,
    remaining: tuple[str, ...],
    completed: frozenset[str],
) -> tuple[str, ...]:
    ready = [
        group_id
        for group_id in remaining
        if compiled.dependency_ids(group_id) <= completed
    ]
    wave: list[str] = []
    for group_id in ready:
        if all(compiled.can_run_concurrently(group_id, item) for item in wave):
            wave.append(group_id)
    return tuple(wave)


__all__ = ["next_counterpart_wave"]
