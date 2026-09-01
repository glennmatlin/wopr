"""Deterministic Charter graph scheduling."""

from __future__ import annotations

from .compiled_models import CompiledUsCharter


def next_execution_wave(
    compiled: CompiledUsCharter,
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
        if all(compiled.can_run_concurrently(group_id, selected) for selected in wave):
            wave.append(group_id)
    return tuple(wave)


__all__ = ["next_execution_wave"]
