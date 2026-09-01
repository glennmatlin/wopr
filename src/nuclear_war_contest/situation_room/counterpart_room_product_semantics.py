"""Actor-specific checks for authored counterpart fixture products."""

from __future__ import annotations

from typing import Any

from .counterpart_compiled_models import CompiledCounterpartCharter


def _seat_id(value: object) -> str | None:
    if not isinstance(value, dict):
        return None
    seat_id = value.get("seat_id")
    return seat_id if isinstance(seat_id, str) else None


def _ordered_members_are_valid(
    field: object, group_id: str, compiled: CompiledCounterpartCharter
) -> bool:
    expected = [seat.seat_id for seat in compiled.group_members(group_id)]
    observed = [_seat_id(item) for item in field] if isinstance(field, list) else []
    return observed == expected


def _himaldesh_executive_is_valid(content: dict[str, Any]) -> bool:
    dissent = content.get("dissent")
    return (
        _seat_id(content.get("prime_minister_position")) == "HD_SEAT_PRIME_MINISTER"
        and _seat_id(content.get("president_position")) == "HD_SEAT_PRESIDENT"
        and isinstance(dissent, list)
        and bool(dissent)
        and isinstance(content.get("output_components"), dict)
    )


def _himaldesh_product_is_valid(
    group_id: str, content: dict[str, Any], compiled: CompiledCounterpartCharter
) -> bool:
    if group_id.startswith("HD_GROUP_PORTFOLIO_"):
        seat = compiled.group_members(group_id)[0].seat_id
        return _seat_id(content.get("coordination_record")) == seat
    if group_id == "HD_GROUP_CABINET_REVIEW":
        dispositions = content.get("dissent_dispositions")
        ordered = _ordered_members_are_valid(
            content.get("ordered_reviews"), group_id, compiled
        )
        return ordered and isinstance(dispositions, list) and bool(dispositions)
    if group_id == "HD_GROUP_COMMAND_CELL":
        gaps = content.get("gaps")
        return isinstance(gaps, list) and "HD_GAP_OPERATIONAL_COMMANDER" in gaps
    if group_id == "HD_GROUP_JOINT_EXECUTIVE":
        return _himaldesh_executive_is_valid(content)
    return True


def _olvana_product_is_valid(
    group_id: str, content: dict[str, Any], compiled: CompiledCounterpartCharter
) -> bool:
    if group_id == "OLV_GROUP_NCA_PORTFOLIOS":
        positions = content.get("ordered_positions")
        expected = [seat.seat_id for seat in compiled.group_members(group_id)]
        observed = (
            [_seat_id(position) for position in positions]
            if isinstance(positions, list)
            else []
        )
        return observed == expected
    if group_id == "OLV_GROUP_SID_INTEGRATION":
        sources = content.get("source_product_ids")
        return sources == ["OLV_PRODUCT_NCA_POSITIONS_001", "OLV_PRODUCT_COMMAND_001"]
    if group_id == "OLV_GROUP_NCA_REVIEW":
        return _seat_id(content.get("president_position")) == "OLV_SEAT_PRESIDENT"
    if group_id == "OLV_GROUP_PARTY_DIRECTION":
        decision = _seat_id(content.get("general_secretary_decision"))
        output = content.get("output_components")
        return (
            decision == "OLV_SEAT_GENERAL_SECRETARY"
            and isinstance(content.get("retained_dissent"), list)
            and isinstance(output, dict)
            and output.get("no_further_advance") is True
        )
    return True


def counterpart_product_is_valid(
    actor_id: str,
    group_id: str,
    content: dict[str, Any],
    compiled: CompiledCounterpartCharter,
) -> bool:
    if actor_id == "ACTOR_HIMALDESH":
        return _himaldesh_product_is_valid(group_id, content, compiled)
    return _olvana_product_is_valid(group_id, content, compiled)


__all__ = ["counterpart_product_is_valid"]
