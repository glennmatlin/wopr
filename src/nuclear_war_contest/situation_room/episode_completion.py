"""Episode terminal and abort classification."""

from __future__ import annotations

from typing import Any


def classify_episode_end(
    core: dict[str, Any], *, cycle2_started: bool, failed: bool
) -> str:
    if core.get("terminal_state") != "open" and not cycle2_started and not failed:
        return "substantive_terminal"
    if failed:
        return "abort"
    return "normal"


__all__ = ["classify_episode_end"]
