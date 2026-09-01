"""Demo-only chair text. The World does not read these strings."""

from __future__ import annotations

from .identity import canonical_hash

NEUTRAL_STAFF_ID = "neutral_staff"

NEUTRAL_STAFF_ROOM = {
    "role": "room",
    "objective": "keep the faction alive through the crisis",
}

NEUTRAL_STAFF_CHAIRS = {
    "executive": {
        "title": "Chair",
        "role": "chair",
        "objective": "hear staff, then choose one legal action",
    },
    "strategic_advisor": {
        "title": "Operations",
        "role": "operations",
        "objective": "name the legal action that keeps options open",
    },
    "risk_advisor": {
        "title": "Dissent",
        "role": "dissent",
        "objective": "say what can go wrong before the chair decides",
    },
}

OVERLAY_IDS = {NEUTRAL_STAFF_ID}


def room_identity(player_index: int) -> dict[str, str]:
    return {
        "name": f"Room {player_index}",
        **NEUTRAL_STAFF_ROOM,
    }


def chair_identity(player_index: int, member_id: str) -> dict[str, str]:
    chair = NEUTRAL_STAFF_CHAIRS[member_id]
    return {
        "name": f"Room {player_index} {chair['title']}",
        "role": chair["role"],
        "objective": chair["objective"],
    }


def overlay_pack_hash() -> str:
    return canonical_hash(
        {
            "overlay_id": NEUTRAL_STAFF_ID,
            "room": NEUTRAL_STAFF_ROOM,
            "chairs": NEUTRAL_STAFF_CHAIRS,
        }
    )


__all__ = [
    "NEUTRAL_STAFF_CHAIRS",
    "NEUTRAL_STAFF_ID",
    "OVERLAY_IDS",
    "chair_identity",
    "overlay_pack_hash",
    "room_identity",
]
