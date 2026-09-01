"""Complete candidate U.S. Charter contract tests."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.situation_room import (
    compile_us_charter,
    load_source_register,
    load_us_charter,
    render_us_charter_bundle,
)

ROOT = Path(__file__).parents[2]
SOURCE_PATH = ROOT / "docs/contest/US_SOURCE_REGISTER.candidate.json"
CHARTER_PATH = ROOT / "docs/contest/US_CHARTER.candidate.json"
REVIEW_PATH = ROOT / "docs/contest/US_CHARTER_REVIEW.candidate.md"


def _bundle():
    source = load_source_register(SOURCE_PATH)
    charter = load_us_charter(CHARTER_PATH, source)
    return source, charter, compile_us_charter(charter)


def test_candidate_hashes_bind_exact_review_bytes() -> None:
    source, charter, _ = _bundle()

    assert source.content_hash == (
        "73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f"
    )
    assert charter.content_hash == (
        "fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2"
    )


def test_candidate_serializes_complete_roster_services_and_groups() -> None:
    _, charter, compiled = _bundle()
    payload = charter.payload()

    assert {item["seat_id"] for item in payload["institution_registry"]["seats"]} == {
        "SEAT_PRESIDENT",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_PANDEMIC_PREPAREDNESS",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_INTERIOR",
        "SEAT_CHIEF_OF_STAFF",
        "SEAT_NSA",
        "SEAT_HOMELAND_SECURITY",
        "SEAT_HSA",
        "SEAT_DNI",
        "SEAT_CJCS",
        "SEAT_CIA_DIRECTOR",
        "SEAT_WHITE_HOUSE_COUNSEL",
        "SEAT_POLICY_ASSISTANT",
        "SEAT_COUNSELOR",
        "SEAT_THEATER_COMMANDER",
    }
    assert {
        item["service_id"] for item in payload["institution_registry"]["services"]
    } == {
        "SERVICE_WATCH",
        "SERVICE_EXECUTIVE_SECRETARY",
    }
    assert {item["group_id"] for item in payload["groups"]} == {
        "GROUP_THREAT_ATTRIBUTION",
        "GROUP_DIPLOMATIC_ECONOMIC",
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_NUCLEAR_RADIOLOGICAL",
        "GROUP_LEGAL_AUTHORITY",
        "GROUP_HOMELAND_CONSEQUENCES",
        "GROUP_PRESIDENTIAL_SYNTHESIS",
        "GROUP_PC",
        "GROUP_NSC",
        "GROUP_HSC",
    }
    assert len(compiled.active_seat_ids()) == 14
    assert "SEAT_THEATER_COMMANDER" in compiled.active_seat_ids()


def test_candidate_delivery_excludes_inactive_seats_and_hidden_truth() -> None:
    _, charter, compiled = _bundle()
    expected_active = tuple(sorted(compiled.active_seat_ids()))

    assert (
        compiled.recipients_for("INFO_COMMON_CRISIS_PICTURE", "SERVICE_WATCH")
        == expected_active
    )
    assert compiled.recipients_for("INFO_RAW_WEATHER_FORECAST", "SERVICE_WATCH") == (
        "SEAT_CIA_DIRECTOR",
        "SEAT_CJCS",
        "SEAT_DEFENSE",
        "SEAT_DNI",
        "SEAT_STATE",
        "SEAT_THEATER_COMMANDER",
    )
    assert compiled.recipients_for("INFO_WORLD_GROUND_TRUTH", "SERVICE_WATCH") == ()
    assert all(
        "INFO_WORLD_GROUND_TRUTH" not in seat["information_entitlement_ids"]
        for seat in charter.payload()["institution_registry"]["seats"]
    )


def test_candidate_preserves_adviser_status_dependencies_and_routes() -> None:
    _, _, compiled = _bundle()

    assert compiled.voting_member_ids("GROUP_PC") == (
        "SEAT_NSA",
        "SEAT_VICE_PRESIDENT",
        "SEAT_STATE",
        "SEAT_TREASURY",
        "SEAT_DEFENSE",
        "SEAT_ENERGY",
        "SEAT_ATTORNEY_GENERAL",
        "SEAT_CHIEF_OF_STAFF",
    )
    assert not compiled.can_run_concurrently(
        "GROUP_THREAT_ATTRIBUTION", "GROUP_DEFENSE_ESCALATION"
    )
    assert compiled.can_run_concurrently(
        "GROUP_DIPLOMATIC_ECONOMIC", "GROUP_NUCLEAR_RADIOLOGICAL"
    )
    assert compiled.route_id_for("presidential_policy_direction") == (
        "ROUTE_PRESIDENTIAL_POLICY"
    )


def test_candidate_retains_blocking_gaps_instead_of_inventing_delegation() -> None:
    source, charter, _ = _bundle()

    gaps = {item["gap_id"]: item for item in source.payload()["gaps"]}
    assert gaps["GAP_PC_DELEGATION_INSTRUMENT"]["blocks_activation"] is True
    assert gaps["GAP_EFFECT_AUTHORITY_CONFIRMATION_MAP"]["blocks_activation"] is True
    assert {item["action_class"] for item in charter.payload()["decision_routes"]} == {
        "presidential_policy_direction",
        "presidential_homeland_policy_direction",
    }


def test_candidate_review_file_is_exact_lossless_rendering() -> None:
    source, charter, _ = _bundle()

    assert REVIEW_PATH.read_text(encoding="utf-8") == render_us_charter_bundle(
        source, charter
    )
