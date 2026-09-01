"""DATE candidate-profile loading."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .core_validation import core_entity_ids
from .identity import canonical_hash, load_strict_json
from .profile_validation import validate_profile

PROFILE_SCHEMA_VERSION = "date-profile.v0.2"


@dataclass(frozen=True)
class DateProfile:
    """A loaded profile bound to its canonical serialized identity."""

    profile_id: str
    profile_version: str
    content_hash: str
    _payload: dict[str, Any]

    def initial_core(self) -> dict[str, Any]:
        return deepcopy(self._payload["initial_core"])

    def event_template(self, template_id: str) -> dict[str, Any]:
        return self._template("authored_event_templates", template_id)

    def patch_template(self, template_id: str) -> dict[str, Any]:
        return self._template("patch_templates", template_id)

    def declared_ids(self, field: str) -> set[str]:
        if field not in {"audience_ids", "evidence_ids"}:
            raise ValueError(f"Unknown DATE declared-ID field: {field}")
        return set(self._payload[field])

    def entity_ids(self) -> set[str]:
        return core_entity_ids(self._payload["initial_core"])

    def _template(self, collection: str, template_id: str) -> dict[str, Any]:
        templates = self._payload[collection]
        matches = [item for item in templates if item.get("template_id") == template_id]
        if len(matches) != 1:
            raise ValueError(f"Unknown DATE template: {template_id}")
        return deepcopy(matches[0])


def load_profile(path: Path) -> DateProfile:
    payload = load_strict_json(path)
    if not isinstance(payload, dict):
        raise ValueError("DATE profile must be an object")
    validate_profile(payload)
    profile_id = payload.get("profile_id")
    profile_version = payload.get("profile_version")
    assert isinstance(profile_id, str)
    assert isinstance(profile_version, str)
    return DateProfile(
        profile_id=profile_id,
        profile_version=profile_version,
        content_hash=canonical_hash(payload),
        _payload=deepcopy(payload),
    )


__all__ = ["DateProfile", "load_profile"]
