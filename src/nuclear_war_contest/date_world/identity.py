"""Strict JSON loading and canonical DATE artifact identity."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def canonical_hash(payload: Any) -> str:
    encoded = json.dumps(
        payload,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def core_hash(core: dict[str, Any]) -> str:
    return canonical_hash(core)


def load_strict_json(path: Path) -> Any:
    def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        value: dict[str, Any] = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"Duplicate JSON key: {key}")
            value[key] = item
        return value

    def reject_constant(value: str) -> None:
        raise ValueError(f"Non-finite JSON value: {value}")

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_constant,
    )


__all__ = ["canonical_hash", "core_hash", "load_strict_json"]
