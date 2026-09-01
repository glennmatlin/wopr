"""Strict proposal bridge fixture envelope validation."""

from __future__ import annotations

from typing import Any

from .proposal_bridge_consequence_validation import validate_consequence
from .proposal_bridge_fixture_shape import (
    validate_authority as _validate_authority,
)
from .proposal_bridge_fixture_shape import (
    validate_capability as _validate_capability,
)
from .proposal_bridge_fixture_shape import (
    validate_clarification as _validate_clarification,
)
from .proposal_bridge_fixture_shape import (
    validate_effect as _validate_effect,
)
from .proposal_bridge_fixture_shape import (
    validate_proposal as _validate_proposal,
)
from .proposal_bridge_schema import (
    AUTHORITY_FIELDS,
    CAPABILITY_FIELDS,
    CLARIFICATION_FIELDS,
    CONSEQUENCE_FIELDS,
    EFFECT_FIELDS,
    PROPOSAL_FIELDS,
    TOP_FIELDS,
)
from .proposal_bridge_validation_helpers import (
    require_record,
    require_text,
)


def validate_bridge_fixture_shape(payload: dict[str, Any]) -> None:
    require_record(payload, TOP_FIELDS, "proposal bridge")
    fixed = {
        "schema_version": "proposal-bridge-fixture.v0.1",
        "status": "development_fixture_non_evidence",
    }
    if any(payload.get(key) != value for key, value in fixed.items()):
        raise ValueError("invalid_envelope: proposal bridge fixed fields are invalid")
    for field in ("fixture_id", "fixture_version"):
        require_text(payload[field], field)
    for field in ("cycle_receipt_hash", "cycle_run_hash", "date_profile_hash"):
        require_text(payload[field], field)
    for field in (
        "proposals",
        "clarifications",
        "effect_authority_records",
        "capability_records",
        "consequence_proposals",
    ):
        if not isinstance(payload[field], list):
            raise ValueError(f"invalid_envelope: {field} must be a list")
    if not payload["proposals"]:
        raise ValueError("invalid_envelope: at least one proposal is required")
    for proposal_value in payload["proposals"]:
        proposal = require_record(proposal_value, PROPOSAL_FIELDS, "proposal")
        _validate_proposal(proposal)
        for effect in proposal["effects"]:
            _validate_effect(require_record(effect, EFFECT_FIELDS, "proposal effect"))
    for item in payload["clarifications"]:
        _validate_clarification(
            require_record(item, CLARIFICATION_FIELDS, "clarification")
        )
    for item in payload["effect_authority_records"]:
        _validate_authority(require_record(item, AUTHORITY_FIELDS, "effect authority"))
    for item in payload["capability_records"]:
        _validate_capability(require_record(item, CAPABILITY_FIELDS, "capability"))
    for item in payload["consequence_proposals"]:
        validate_consequence(require_record(item, CONSEQUENCE_FIELDS, "consequence"))
