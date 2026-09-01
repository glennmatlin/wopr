"""Append-only attempt ledger for resumable contest studies."""

from __future__ import annotations

import json
import threading
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

TERMINAL_STATUSES = {"completed", "failed_terminal"}
_LEDGER_LOCK = threading.Lock()


def append_ledger_record(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"recorded_at": _now(), **record}
    with _LEDGER_LOCK:
        with path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(payload, sort_keys=True) + "\n")


def read_ledger(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    if not path.is_file():
        raise ValueError(f"Attempt ledger path is not a file: {path}")
    records: list[dict[str, Any]] = []
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Attempt ledger line {index} is not valid JSON") from exc
        if not isinstance(record, dict):
            raise ValueError(f"Attempt ledger line {index} must be an object")
        records.append(record)
    return records


def latest_attempts(path: Path) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for record in read_ledger(path):
        attempt_id = record.get("attempt_id")
        if isinstance(attempt_id, str) and attempt_id:
            latest[attempt_id] = record
    return latest


def is_terminal(record: dict[str, Any] | None) -> bool:
    return isinstance(record, dict) and record.get("status") in TERMINAL_STATUSES


def _now() -> str:
    return datetime.now(UTC).isoformat()


__all__ = [
    "TERMINAL_STATUSES",
    "append_ledger_record",
    "is_terminal",
    "latest_attempts",
    "read_ledger",
]
