"""CLI adapter for the approval-gated model-screening runner."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .screening_execution import run_screening
from .screening_manifest import load_screening_manifest_file


def run_screening_command(args: Any) -> int:
    manifest_path = Path(args.manifest)
    manifest = load_screening_manifest_file(manifest_path)
    approval = _read_object(Path(args.approval))
    summary = run_screening(
        manifest,
        hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        approval,
        args.executor_revision,
        allow_network=bool(args.allow_network),
        out_dir=Path(args.out_dir),
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def _read_object(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return payload


__all__ = ["run_screening_command"]
