"""Filesystem helpers for contest manifests and attempt artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .manifest import manifest_payload
from .manifest_types import StudyManifest


def artifact_paths(paths: dict[str, Path], root: Path) -> dict[str, str]:
    return {key: str(path.relative_to(root)) for key, path in paths.items()}


def write_manifest(out_dir: Path, manifest: StudyManifest) -> None:
    path = out_dir / "STUDY_MANIFEST.json"
    payload = manifest_payload(manifest)
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        if existing != payload:
            raise ValueError("Study manifest already exists with different content")
        return
    write_json(path, payload)


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


__all__ = ["artifact_paths", "write_json", "write_manifest"]
