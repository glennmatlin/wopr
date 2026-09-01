"""Handoff current-state documentation tests."""

from __future__ import annotations

from pathlib import Path


def test_handoff_records_variant_acceptance_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "variant acceptance criteria merged in" in text
    assert "PR [#29](https://github.com/eilab-gt/WOPR/pull/29)" in text
    assert "| Variant acceptance criteria | done |" in text
    assert "Variant acceptance criteria | done on branch" not in text


def test_handoff_records_decision_heuristic_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "decision heuristic agent merged in" in text
    assert "PR [#31](https://github.com/eilab-gt/WOPR/pull/31)" in text
    assert "| Decision heuristic agent | done |" in text
    assert "Decision heuristic agent | done on branch" not in text
    assert "/decision-heuristic-agent" not in text
    assert "Review and merge that branch" not in text


def test_handoff_records_rules_trace_scaffold_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "rules trace scaffold merged in" in text
    assert "PR [#32](https://github.com/eilab-gt/WOPR/pull/32)" in text
    assert "| Rules trace scaffold | done |" in text
    assert "Rules trace scaffold | done on branch" not in text
    assert "Merge PR #32" not in text


def test_handoff_records_rules_text_step_map_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "rules text step map merged in" in text
    assert "PR [#33](https://github.com/eilab-gt/WOPR/pull/33)" in text
    assert "| Rules text step map | done |" in text
    assert "Rules text step map | current branch |" not in text


def test_handoff_records_full_semantic_trace_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "full semantic rules trace merged in" in text
    assert "PR [#34](https://github.com/eilab-gt/WOPR/pull/34)" in text
    assert "| Full semantic rules trace | done |" in text
    assert "| Full semantic rules trace | current branch |" not in text
    assert "282 full-game semantic trace entries" in text
    assert "`rules_trace_steps`" in text
    assert "no trace" in text
    assert "source, step, or full-game gaps" in text
    assert "full-game" in text
    assert "gaps" in text


def test_handoff_records_llm_game_pickup_and_source_boundary() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "Next is PR review and merge" not in text
    assert "Prepare it for PR" not in text
    assert "Current pickup points" in text
    assert "The ladder to re-check first" in text
    assert "provider preset work is implemented" in text
    assert "HTTP provider presets" in text
    assert (
        "source acquisition remains a separate blocked source-evidence thread"
        in text
    )
    assert "The immediate next step is source acquisition" not in text


def test_handoff_records_concordia_press_ladder() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "Concordia no-press harness" in text
    assert "press-light, multi-turn public press, and full press" in text
    assert "native Concordia entity logs" in text
    assert "Concordia capability map" in text


def test_handoff_records_postal_replay_validation_fixed() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "| D1 postal replay validation | done |" in text
    assert "postal CLI replay sweep passes" in text
    assert "Postal mode has pre-existing CLI replay bugs" not in text
    assert "They are present on the original HEAD" not in text


def test_handoff_records_expansion_composition_intake_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "expansion composition evidence intake merged in" in text
    assert "PR [#37](https://github.com/eilab-gt/WOPR/pull/37)" in text
    assert "| Expansion composition evidence intake | done |" in text
    assert "| Expansion composition evidence intake | current branch |" not in text


def test_handoff_records_source_evidence_capture_packet_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence capture packet merged in" in text
    assert "PR [#40](https://github.com/eilab-gt/WOPR/pull/40)" in text
    assert "| Source evidence capture packet | done |" in text
    assert "| Source evidence capture packet | current branch |" not in text


def test_handoff_records_private_capture_guard_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "private source capture ignore guard merged in" in text
    assert "PR [#42](https://github.com/eilab-gt/WOPR/pull/42)" in text
    assert "| Private source capture ignore guard | done |" in text
    assert "| Private source capture ignore guard | current branch |" not in text


def test_handoff_records_private_reference_preflight_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "private physical-copy evidence reference preflight merged in" in text
    assert "PR [#44](https://github.com/eilab-gt/WOPR/pull/44)" in text
    assert "| Private physical-copy evidence reference preflight | done |" in text
    assert (
        "| Private physical-copy evidence reference preflight | current branch |"
        not in text
    )


def test_handoff_records_card_effect_known_id_preflight_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "card-effect evidence known-id preflight merged in" in text
    assert "PR [#46](https://github.com/eilab-gt/WOPR/pull/46)" in text
    assert "| Card-effect evidence known-id preflight | done |" in text
    assert "| Card-effect evidence known-id preflight | current branch |" not in text


def test_handoff_records_source_evidence_draft_preflight_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence draft preflight merged in" in text.lower()
    assert "PR [#48](https://github.com/eilab-gt/WOPR/pull/48)" in text
    assert "| Source evidence draft preflight | done |" in text
    assert "| Source evidence draft preflight | current branch |" not in text
    assert "Current branch plan for draft" not in text
    assert "validate-source-evidence" in text
    assert "1080 tests pass with 35 warnings" in text
    assert "CAPTURE_RUNBOOK.md" in text


def test_handoff_records_source_evidence_capture_runbook_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence capture runbook merged in" in text.lower()
    assert "PR [#50](https://github.com/eilab-gt/WOPR/pull/50)" in text
    assert "| Source evidence capture runbook | done |" in text
    assert "| Source evidence capture runbook | current branch |" not in text


def test_handoff_records_source_evidence_capture_checklist_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence capture checklist merged in" in text.lower()
    assert "PR [#52](https://github.com/eilab-gt/WOPR/pull/52)" in text
    assert "| Source evidence capture checklist | done |" in text
    assert "| Source evidence capture checklist | current branch |" not in text
    assert "CAPTURE_CHECKLIST.md" in text


def test_handoff_records_source_evidence_coverage_report_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence coverage report merged in" in text.lower()
    assert "PR [#54](https://github.com/eilab-gt/WOPR/pull/54)" in text
    assert "| Source evidence coverage report | done |" in text
    assert "| Source evidence coverage report | current branch |" not in text
    assert "Current branch plan for source-evidence" not in text
    assert "card_effect_evidence_coverage" in text
    assert "expansion_composition_evidence_coverage" in text


def test_handoff_records_source_evidence_live_promotion_gate_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence live promotion gate merged in" in text.lower()
    assert "PR [#56](https://github.com/eilab-gt/WOPR/pull/56)" in text
    assert "After PR #46" not in text
    assert "After PR #56" in text
    assert "| Source evidence live promotion gate | done |" in text
    assert "| Source evidence live promotion gate | current branch |" not in text
    assert "Current branch plan for live source-evidence" not in text
    assert "card_effect_evidence_promotion_errors" in text
    assert "expansion_composition_evidence_promotion_errors" in text
