"""Dependency-cycle validation for U.S. Room Charter groups."""

from __future__ import annotations

from typing import Any

from .validation import fail


def reject_dependency_cycles(groups: list[dict[str, Any]]) -> None:
    dependencies = {
        group["group_id"]: set(group["dependency_group_ids"]) for group in groups
    }
    remaining = set(dependencies)
    while remaining:
        ready = {
            group_id for group_id in remaining if not dependencies[group_id] & remaining
        }
        if not ready:
            fail("dependency_cycle", "group dependency graph contains a cycle")
        remaining -= ready


__all__ = ["reject_dependency_cycles"]
