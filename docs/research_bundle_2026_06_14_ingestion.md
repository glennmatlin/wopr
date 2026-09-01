# 2026-06-14 Research Bundle Ingestion

This page records how I ingested the 2026-06-14 Nuclear War research bundle and
what it changes in the v1 specification.

## Import Record

- Source archive:
  `~/Downloads/nuclear_war_card_game_research_bundle.zip`.
- Project copy:
  `research/imports/2026-06-14_nuclear_war_card_game_research_bundle/`.
- Archive SHA256:
  `2d3e23e2bd9322519c52cef7482e3dbab271de35b1e5801a9963311ebc04ee0d`.
- Archive integrity check: `unzip -t` reported no compressed-data errors on
  2026-06-14.
- Project-copy verification: an extracted archive tree matched the project
  import under `diff -qr` on 2026-06-14.
- Manifest count: 53 non-directory files in `BUNDLE_FILE_MANIFEST.md`.
- Source-index count: 34 source IDs in `source_index.json`.
- PDF verification report count: 5 downloaded PDF records with page counts and
  SHA256 hashes.

The project copy is the canonical local import. The original zip is provenance
evidence, not a runtime dependency.

## Ingestion Review

I reviewed these bundle inputs against the v1 specification:

- `README.md` and `full_research_report.md`.
- `02_rules_and_variants/rules_reconstruction_summary.md`.
- `02_rules_and_variants/press_no_press_and_pbm_variants.md`.
- `03_card_data/base_game_card_inventory.csv`.
- `04_simulation_model/rules_variants.json`.
- `04_simulation_model/simulation_cards_schema.json`.
- `04_simulation_model/spinner_and_die_tables.json`.
- `05_ai_prompts_and_memories/source_priority_and_confidence.md`.
- `07_gaps_and_next_steps/exact_text_gap_list.md`.
- `07_gaps_and_next_steps/edition_reconciliation_checklist.md`.
- `99_sources/pdf_verification_report.md`.

I rechecked the archive SHA256, `unzip -t`, imported file count, source-index
count, downloaded PDF verification record count, and extracted-tree comparison
on 2026-06-14. The reviewed project copy still contains 53 non-directory files.

## Specification Impact

- V1 remains scoped to a deterministic classic/base table game plus postal
  no-press mechanics.
- The active default table variant remains `base_later_two_d10`: hand draw
  target 10, 20-card population model, two-d10 fallout table, press disabled,
  and non-simultaneous table turns.
- Classic spinner rules, current Nuclear Destruction, postal press, no-press
  house play, and combined-expansion play must remain separate variant inputs.
- Postal no-press is not established by the bundle as an official source
  variant. In WOPR it is a controlled mode that disables communication while
  preserving non-communication postal mechanics from `UNOFF-001`.
- Current Nuclear Destruction material is useful for future edition modules. It
  is not the active v1 ruleset.
- Exact card text, exact spinner probabilities, expansion counts, and
  edition-specific disputed behavior still require physical-copy or authorized
  source verification.
- The runtime `active_variant` payload records the imported schema fields:
  `initial_face_down_cards`, `anti_missile_turn_jump`, `expansion_sets`,
  `special_powers_enabled`, and `trading_enabled`.
- Imported prompt and memory files are retained only as research artifacts. They
  do not define v1 runtime behavior.

## Source Inputs To Use

- `source_index.csv` and `source_index.json` are the provenance ledger for new
  source labels.
- `02_rules_and_variants/rules_reconstruction_summary.md` is the summary of
  edition conflicts.
- `03_card_data/base_game_card_inventory.csv` is a card-name and count lead. It
  is not exact card text.
- `04_simulation_model/rules_variants.json` records variant boundaries that the
  code should not collapse.
- `04_simulation_model/spinner_and_die_tables.json` is a table lead for
  randomizer audit work.
- `07_gaps_and_next_steps/exact_text_gap_list.md` is the next physical-copy
  verification checklist.

## Required Follow-Up

- Capture the user's physical copy before importing exact card wording.
- Confirm whether the user's copy uses 20 or 40 population cards.
- Confirm whether the user's copy uses the spinner, the two-d10 chart, or both.
- Confirm exact delivery capacity and bomber payload handling from the user's
  rules/cards.
- Keep expansion cards out of the default base deck until card counts and
  source authority are verified.
- Use the current anti-missile turn-order tests as the model for future variant
  fields that affect turn flow.
