"""Lossless human review surface for a source-bound U.S. Charter."""

from __future__ import annotations

import json
from pathlib import Path

from .charter import UsCharter
from .source_register import SourceRegister


def _json_block(payload: dict[str, object]) -> str:
    return json.dumps(
        payload,
        allow_nan=False,
        ensure_ascii=False,
        indent=2,
        sort_keys=False,
    )


def render_us_charter_bundle(
    source_register: SourceRegister, charter: UsCharter
) -> str:
    """Render every serialized field with both canonical identities."""
    source_payload = source_register.payload()
    charter_payload = charter.payload()
    return "\n".join(
        [
            "# U.S. Room Charter candidate review",
            "",
            f"Source register: `{source_register.register_id}`",
            f"Source register SHA-256: `{source_register.content_hash}`",
            f"U.S. Charter: `{charter.charter_id}`",
            f"U.S. Charter SHA-256: `{charter.content_hash}`",
            "",
            "## Source register",
            "",
            "```json",
            _json_block(source_payload),
            "```",
            "",
            "## U.S. Charter",
            "",
            "```json",
            _json_block(charter_payload),
            "```",
            "",
        ]
    )


def write_us_charter_bundle_review(
    path: Path, source_register: SourceRegister, charter: UsCharter
) -> None:
    path.write_text(
        render_us_charter_bundle(source_register, charter),
        encoding="utf-8",
    )


__all__ = ["render_us_charter_bundle", "write_us_charter_bundle_review"]
