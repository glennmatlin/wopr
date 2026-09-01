"""Build per-cell Concordia payloads from a frozen study manifest."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .manifest_types import StudyCell, StudyCondition, StudyManifest, StudyModel
from .overlay_packs import chair_identity, room_identity
from .prompt_identity import MEMBER_ROLE_DEFINITIONS

_COMMANDER_ROLES = (
    ("cautious", "cautious nuclear commander", "preserve strategic options"),
    ("risk_accepting", "risk-accepting nuclear commander", "pressure opponents"),
    ("deterrence", "deterrence-focused nuclear commander", "avoid vulnerability"),
    ("opportunistic", "opportunistic nuclear commander", "exploit weak opponents"),
)


def build_concordia_payload(
    manifest: StudyManifest,
    cell: StudyCell,
) -> dict[str, Any]:
    condition = _condition(manifest, cell.condition_id)
    model = _model(manifest, cell.model_id)
    seats = {
        f"player_{index}": _seat_payload(index, condition, model, manifest.overlay)
        for index in range(manifest.players)
    }
    return {
        "players": manifest.players,
        "seed": cell.seed,
        "max_turns": manifest.max_turns,
        "runtime": "auto",
        "press": _press_payload(condition),
        "seats": seats,
    }


def _seat_payload(
    player_index: int,
    condition: StudyCondition,
    model: StudyModel,
    overlay: str,
) -> dict[str, Any]:
    commander_role, commander_objective = _commander_profile(player_index)
    identity = (
        room_identity(player_index)
        if overlay == "neutral_staff"
        else {
            "name": f"Commander {player_index}",
            "role": commander_role,
            "objective": commander_objective,
        }
    )
    seat: dict[str, Any] = {
        "agent": model.backend,
        "identity": identity,
        "max_retries": model.max_retries,
        "authority": _authority_payload(player_index, condition, overlay),
    }
    if model.client:
        client = deepcopy(model.client)
        client["provider"] = model.provider
        seat["client"] = client
    return seat


def _authority_payload(
    player_index: int,
    condition: StudyCondition,
    overlay: str,
) -> dict[str, Any]:
    members = [
        {
            "member_id": member_id,
            "identity": (
                chair_identity(player_index, member_id)
                if overlay == "neutral_staff"
                else {
                    "name": f"Commander {player_index} {member_id}",
                    **MEMBER_ROLE_DEFINITIONS[member_id],
                }
            ),
        }
        for member_id in MEMBER_ROLE_DEFINITIONS
    ]
    return {
        "archetype": condition.authority,
        "parameters": deepcopy(condition.authority_parameters),
        "spokesperson": "executive",
        "members": members,
    }


def _press_payload(condition: StudyCondition) -> dict[str, Any]:
    if condition.communication == "no_press":
        return {"mode": "none", "enabled": False}
    if condition.communication == "press_light":
        return {"mode": "press_light", "enabled": True}
    return {
        "mode": "full_press",
        "enabled": True,
        "passes": condition.press_passes,
    }


def _condition(manifest: StudyManifest, condition_id: str) -> StudyCondition:
    for condition in manifest.conditions:
        if condition.condition_id == condition_id:
            return condition
    raise ValueError(f"Unknown study condition: {condition_id}")


def _model(manifest: StudyManifest, model_id: str) -> StudyModel:
    for model in manifest.models:
        if model.model_id == model_id:
            return model
    raise ValueError(f"Unknown study model: {model_id}")


def _commander_profile(index: int) -> tuple[str, str]:
    _, label, objective = _COMMANDER_ROLES[index % len(_COMMANDER_ROLES)]
    return label, objective


__all__ = ["build_concordia_payload"]
