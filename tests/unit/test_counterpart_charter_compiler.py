"""Deterministic counterpart Room Charter compiler tests."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.situation_room import (
    compile_counterpart_charter,
    load_actor_source_register,
    load_counterpart_charter,
)

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"


def _compiled(prefix: str):
    source = load_actor_source_register(
        CONTEST / f"{prefix}_SOURCE_REGISTER.candidate.json"
    )
    charter = load_counterpart_charter(
        CONTEST / f"{prefix}_CHARTER.candidate.json", source
    )
    return compile_counterpart_charter(charter)


def test_compiles_actor_specific_active_rosters_and_collection_order() -> None:
    himaldesh = _compiled("HIMALDESH")
    olvana = _compiled("OLVANA")

    assert len(himaldesh.active_seat_ids()) == 11
    assert len(olvana.active_seat_ids()) == 9
    assert himaldesh.active_group_ids() == (
        "HD_GROUP_PORTFOLIO_EXTERNAL",
        "HD_GROUP_PORTFOLIO_INTERIOR",
        "HD_GROUP_PORTFOLIO_FINANCE",
        "HD_GROUP_PORTFOLIO_INFORMATION",
        "HD_GROUP_PORTFOLIO_INFRASTRUCTURE",
        "HD_GROUP_PORTFOLIO_HUMANITARIAN",
        "HD_GROUP_COMMAND_CELL",
        "HD_GROUP_CABINET_DRAFT",
        "HD_GROUP_CABINET_REVIEW",
        "HD_GROUP_JOINT_EXECUTIVE",
    )
    assert olvana.active_group_ids() == (
        "OLV_GROUP_NCA_PORTFOLIOS",
        "OLV_GROUP_COMMAND_ASSESSMENT",
        "OLV_GROUP_SID_INTEGRATION",
        "OLV_GROUP_NCA_REVIEW",
        "OLV_GROUP_PARTY_DIRECTION",
    )


def test_resolves_scope_recipients_without_world_truth() -> None:
    for prefix, common, watch, hidden in (
        (
            "HIMALDESH",
            "HD_INFO_COMMON",
            "HD_SERVICE_WATCH",
            "HD_INFO_WORLD_GROUND_TRUTH",
        ),
        (
            "OLVANA",
            "OLV_INFO_COMMON",
            "OLV_SERVICE_WATCH",
            "OLV_INFO_WORLD_GROUND_TRUTH",
        ),
    ):
        compiled = _compiled(prefix)
        assert compiled.recipients_for(common, watch) == tuple(
            sorted(compiled.active_seat_ids())
        )
        assert compiled.recipients_for(hidden, watch) == ()


def test_preserves_shared_seats_dependencies_and_concurrency() -> None:
    himaldesh = _compiled("HIMALDESH")
    olvana = _compiled("OLVANA")

    assert himaldesh.can_run_concurrently(
        "HD_GROUP_COMMAND_CELL", "HD_GROUP_PORTFOLIO_EXTERNAL"
    )
    assert not himaldesh.can_run_concurrently(
        "HD_GROUP_CABINET_DRAFT", "HD_GROUP_PORTFOLIO_EXTERNAL"
    )
    defense_a = olvana.group_members("OLV_GROUP_NCA_PORTFOLIOS")[-1]
    defense_b = olvana.group_members("OLV_GROUP_COMMAND_ASSESSMENT")[1]
    assert defense_a is defense_b
    assert not olvana.can_run_concurrently(
        "OLV_GROUP_NCA_PORTFOLIOS", "OLV_GROUP_COMMAND_ASSESSMENT"
    )


def test_indexes_routes_confirmations_and_blocked_gaps() -> None:
    himaldesh = _compiled("HIMALDESH")
    olvana = _compiled("OLVANA")

    hd_route = himaldesh.route_for("partner_support_request_and_recapture_planning")
    assert hd_route.decision_authority_seat_ids == (
        "HD_SEAT_PRIME_MINISTER",
        "HD_SEAT_PRESIDENT",
    )
    assert hd_route.required_confirmation_ids == (
        "HD_CONFIRM_DEFENSE_FEASIBILITY",
        "HD_CONFIRM_GENERAL_STAFF_ASSESSMENT",
    )
    assert (
        olvana.route_for("limited_ridge_hold_and_integrated_pressure").route_id
        == "OLV_ROUTE_RIDGE_POSTURE"
    )
    assert olvana.blocked_gap_ids(
        "strategic_or_nuclear_readiness_signaling_or_use"
    ) == ("OLV_GAP_NUCLEAR_DECISION_PATH",)
