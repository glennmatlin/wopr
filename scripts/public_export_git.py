"""Read exact regular-file blobs from a committed Git tree."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GitBlob:
    mode: str
    object_type: str
    object_id: str


def committed_tree(root: Path, revision: str) -> tuple[str, dict[str, GitBlob]]:
    """Resolve one exact commit and return its tree hash and path index."""
    if len(revision) != 40 or any(
        character not in "0123456789abcdef" for character in revision
    ):
        raise ValueError("source revision must be a lowercase 40-character Git SHA")
    resolved = _git(root, "rev-parse", "--verify", f"{revision}^{{commit}}")
    if resolved.decode("ascii").strip() != revision:
        raise ValueError("source revision did not resolve to the exact commit")
    tree = _git(root, "rev-parse", f"{revision}^{{tree}}").decode("ascii").strip()
    payload = _git(root, "ls-tree", "-r", "-z", revision)
    return tree, _parse_tree(payload)


def read_blob(root: Path, blob: GitBlob) -> bytes:
    """Read one regular blob by object identity."""
    if blob.object_type != "blob" or blob.mode not in {"100644", "100755"}:
        raise ValueError("selected Git object is not a regular file")
    return _git(root, "cat-file", "blob", blob.object_id)


def _parse_tree(payload: bytes) -> dict[str, GitBlob]:
    entries: dict[str, GitBlob] = {}
    for raw in filter(None, payload.split(b"\0")):
        metadata, raw_path = raw.split(b"\t", 1)
        mode, object_type, object_id = metadata.decode("ascii").split()
        try:
            path = raw_path.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("Git tree contains a non-UTF-8 path") from exc
        entries[path] = GitBlob(mode, object_type, object_id)
    return entries


def _git(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args], check=False, capture_output=True
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(f"Git command failed: {detail or 'unknown error'}")
    return result.stdout


__all__ = ["GitBlob", "committed_tree", "read_blob"]
