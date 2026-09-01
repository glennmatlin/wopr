"""Canonical member-role instructions and their content hashes."""

from __future__ import annotations

import hashlib
import json

MEMBER_ROLE_DEFINITIONS = {
    "executive": {
        "role": "executive decision authority",
        "objective": "preserve survival options",
    },
    "strategic_advisor": {
        "role": "strategic advisor",
        "objective": "identify advantageous actions",
    },
    "risk_advisor": {
        "role": "risk advisor",
        "objective": "surface escalation risks",
    },
}


def role_prompt_hashes() -> dict[str, str]:
    return {
        role_id: _hash_payload(payload)
        for role_id, payload in MEMBER_ROLE_DEFINITIONS.items()
    }


def _hash_payload(payload: dict[str, str]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


__all__ = ["MEMBER_ROLE_DEFINITIONS", "role_prompt_hashes"]
