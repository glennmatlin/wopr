"""Verification of the exact clean checkout used for live requests."""

from __future__ import annotations

import subprocess
from pathlib import Path


def verify_executor_revision(requested: str, repo_root: Path | None = None) -> None:
    root = repo_root or Path(__file__).resolve().parents[3]
    try:
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        dirty = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("Could not verify the executor checkout") from exc
    if dirty:
        raise ValueError("Live preflight requires a clean executor checkout")
    if requested != head:
        raise ValueError("Executor revision does not match the clean checkout")


__all__ = ["verify_executor_revision"]
