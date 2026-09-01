# Nuclear War — Spec Roadmap

Forward-looking scope. Companion to `core_engine_repair_plan.md` (the repair changelog),
`NUCLEAR_WAR_METHODOLOGY.md` (v1 doctrine), `docs/v1_acceptance.md`, and
`docs/rule_fidelity_matrix.md`. Last updated 2026-06-20.

## Direction (2026-06-16)

End goal: an **LM-agent experimental environment** (Concordia-style) on a faithful, complete
rules substrate — all rules/editions implemented in code first, LM experiments after. This
reprioritizes the work: the "agent decision interface" (sub-projects A + B) is now **P0**, because
the strategic rules *are* agent choices and LM agents need the observe→choose→step contract.
Design spec: `docs/specs/2026-06-16-agent-decision-interface-design.md`.

Subproject order (each gets spec → plan → implementation):
**A+B** agent decision interface + observations (P0, specced, implemented through B1) ->
**C** core table rules completeness -> **D** postal fixes -> **E** expansions ->
**F** editions/variants -> **G** Concordia/LM harness.

## Where we are (the honest line)

**The core base-game TABLE loop is functionally complete and internally consistent.**
A full match plays end-to-end: per-player population deal → peace-phase propaganda &
secrets → war (build launch, attack, retaliate) → elimination → final strike (with
chaining) → peace restoration → decisive winner (or mutual annihilation / global loss).
Recent gates through the full semantic rules trace passed the full suite, the table 240-game CLI
sweep (seeds 1-60 x {heuristic,random} x {3,4 players}), ruff, pyright, and `validate-rules`.
The semantic trace gate keeps that surface behavior unchanged while asserting a complete
deterministic table replay against source-mapped rule steps. The postal no-press sweep passed after
D1 and has not been intentionally changed by later source-boundary metadata work.

**This is "V1 core works," NOT "fidelity-verified complete Nuclear War."** What is
verified is *completeness + internal consistency + termination*, not exact-rule fidelity
to a physical copy. See the gaps below.

## Tier 1 — Finish core TABLE fidelity (highest priority)

These make the base game *correct against the physical rules*, not just self-consistent.

- [ ] **Card-effect verification.** Registry effects are "low-confidence summaries"
      (per methodology). Transcribe exact secret/top-secret/propaganda/delivery/anti-missile
      effects from a physical copy or authorized source; replace summary metadata. This is
      the single biggest fidelity gap — the engine *applies* effects correctly, but the
      effect *values/semantics* are unverified.
- [x] **Modify-Deterrents turn step** (rules turn step 2). Implemented 2026-06-18 as
      `MODIFY_DETERRENT`, the pre-place window, deterrent slots, and place-from-deterrent.
- [x] **Interactive choices replace deterministic V1 policies.** Targeting for secrets,
      propaganda, final strike, deterrents, and interception are now decision-loop choices.
      The baseline heuristic still reproduces the V1 policy through ordered options.
- [x] **Spinner/fallout-chart fidelity.** VERIFIED 2026-06-16: `_SPINNER_TABLE` matches the
      documented two-d10 chart exactly (all 10 ranges, modifiers, 100Mt super-chain-reaction).
      Locked by `tests/unit/test_fallout_fidelity.py` against the source. No fix needed.
- [x] **Population bank make-change** (audit SETUP-004 LOW). Implemented 2026-06-19:
      population loss/gain routes through `population_bank` as discrete cards, global loss
      returns cards to the bank, and replay summaries remain integer population totals.
- [x] **Per-instance card identity** (audit DELIV-002). Implemented 2026-06-19:
      playable non-population deck cards get unique runtime ids per physical copy while retaining
      base-card metadata. This intentionally updated the heuristic golden for affected seeds.

## Tier 2 — Postal (no-press) mode

Code exists and now passes the 240-game postal CLI replay-validation sweep.
- [x] Fix postal `intercept_success` payload-shape rejection.
- [x] Fix postal-path elimination/result mismatches by logging propaganda eliminations and
      dropping dead actors' queued postal propaganda/secret/secret-theft orders.
- [x] Verify full postal phase ordering produces replay-valid complete games across seeds.

## Tier 3 — Expansion mechanics (exist as code, unverified)

Modules present under `engine/postal/`: cruise (+drop/+launch), submarine (+setup),
space_platform, space_shuttle, killer_satellite, atomic_cannon (+setup), supervirus,
sabotage; plus MX missile and smart bomb. All currently `count_in_deck=0` in the registry
(no proven expansion deck counts).
- [x] Add E1 expansion mechanic catalog validation so implemented mechanics, registry metadata,
      supported modes, and action coverage are checked before deck composition.
- [x] Add E2 expansion mode-boundary validation so current implemented mechanics are explicitly
      postal-only until source-backed table or combined-expansion composition exists.
- [x] Add E3 expansion source-boundary validation so cataloged expansion metadata cannot become
      playable deck cards without authorized source-backed composition.
- [x] Add a public-safe expansion deck-composition evidence intake gate. This records and validates
      future evidence manifests but does not establish deck composition by itself.
- [ ] Establish expansion deck composition from an authorized source.
- [ ] Per-mechanic rules verification + replay-valid behavior tests.
- [ ] Revisit table-mode availability only after source-backed composition or per-mechanic
      evidence justifies changing a mechanic from postal-only.

## Tier 4 — Editions / variants

Schema defines: `base_later_two_d10` (active), `classic_spinner_scan` (40-card deck,
physical spinner), `nuclear_destruction_modern` (ND spinner / Nuclear Escalation die),
`postal_press`, `no_press_house`, `combined_expansions`.
- [x] Add F1 variant catalog validation so known edition boundaries are machine-readable before
      alternate variants are enabled.
- [x] Add F2 variant selection guards so runtime configs can name the active variant while
      deferred variants fail before alternate behavior runs.
- [x] Add F3 CLI variant flag plumbing so scriptable runs can name the active variant while
      deferred variants stay blocked before alternate behavior runs.
- [x] Add F4 active variant resolution so setup and result metadata use the requested active
      variant instead of hard-coded active globals.
- [ ] Classic spinner edition: transcribe spinner probabilities; 9-card hand model.
- [ ] Nuclear Destruction modern: ND deck, escalation die, 6 player mats.
- [ ] Press / diplomacy adjudication (currently rejected by design).
- [ ] Variant-flag plumbing so each edition is a config, not a fork.

## Tier 5 — Agents & experiments

- [x] Typed engine `Observation` contract for B1, with hidden-info-safe self/public views and
      decision-owner-only options/context.
- [x] PettingZoo `env_table`: aligned with the table decision loop in A6, including defender
      intercept decisions and pending-decision action masks.
- [x] Table-only observation-driven `decision_heuristic` agent, separate from the
      parity-preserving `heuristic` baseline.
- [x] WOPR-native no-press LLM agent scaffold. `LLMDecisionAgent` renders typed observations and
      legal actions, parses one legal action from model output, records traces, retries invalid
      output, falls back to a legal action, and records optional provider metadata when a
      deterministic client supplies it. The current clients are deterministic/test-only, not a
      live provider integration.
- [x] Mixed table seating helper for injected `DecisionAgent` instances without changing the
      replay schema.
- [x] No-press LLM harness for deterministic mixed seats. It supports `llm_scripted`, `random`,
      `heuristic`, `decision_heuristic`, and prompt-driven `llm_first_legal` seats, emits a
      separate trace artifact payload, and summarizes winner, win/loss, eliminations, turns,
      invalid-action count, retry count, trace count, per-player trace decision metrics, aggregate
      outcomes by agent label, aggregate trace decision metric counts/rates by agent label, and
      provider latency/cost when present in trace metadata.
- [x] Multi-run no-press LLM batch runner and CLI. `nuclear-war llm-experiment` reads a JSON
      batch config, runs deterministic mixed-seat games across seed ranges, writes replay JSON,
      separate trace artifacts, and a compact `summary.json` with a strict config snapshot.
      `nuclear-war llm-summarize` validates a written batch summary against its config snapshot,
      seed sequence, replay active variant, replay player count, max-turns bound, replay outcomes,
      and linked replay and trace files. Config parsing rejects malformed seat ids, player/seat
      mismatches, unknown top-level or seat fields, non-positive run bounds, retry budgets,
      fallback policies, and provider metadata instead of coercing them. A checked-in
      no-provider starter config lives at
      `docs/examples/no_press_llm_experiment.json`.
- [x] Trace artifact IO and validation. Trace payloads are separate from replay JSON and selected
      trace actions must link to replay actions with matching action id, player, and turn.
      Prompt and raw-response attempt lists must align with the stored retry count. Selected
      actions must appear in legal options. Schema v3 trace artifacts include a structured
      `rendered_observation` field.
- [x] Replay workbench trace inspection. The visualizer imports separate `.traces.json` artifacts
      and shows linked rendered observations, legal options, prompts, raw responses, parse
      results, retries, validation errors, and selected actions in the Decision tab, plus provider
      latency/cost metadata when present.
- [x] Generic HTTP LLM client. `llm_http` uses an OpenAI-compatible chat-completions endpoint,
      records client-side latency and provider usage/model metadata in trace sidecars, and keeps
      provider secrets in environment variables.
- [x] SiliSocs demo adapter. `nuclear_war_silisocs` adds a SiliSocs-compatible no-press backend,
      an offline demo command, and artifact outputs for replay workbench inspection without making
      SiliSocs a base dependency.
- [ ] Search / rollout agents beyond the current heuristics.
- [ ] Concordia adapters for later press, memory, persona, scene, and social reasoning layers.
- [ ] HPC run templates for endpoint-backed larger batches.

## Cross-cutting — fidelity verification harness

- [x] Source-blocker report in `validate-rules` for remaining physical-copy and authorized-source
      gates.
- [x] Source-linked rules-trace scaffold in `validate-rules` for current table replay action/event
      families.
- [x] Source-mapped rule-step catalog in `validate-rules` for the current rules-trace scaffold.
- [x] Full turn-by-turn rules trace: replay a full game and assert each step against source-mapped
      rules text.
- [x] Public-safe source-evidence intake gates for card effects and expansion deck composition.
      These gates validate future manifests but do not supply the missing source evidence.
- [x] Draft source-evidence CLI preflight for explicit local manifest paths. This helps check
      capture work before live manifests exist, but it does not supply source evidence.
- [x] Public-safe source-evidence target export and draft preflight target details. These expose
      current missing and unverified capture queues, but they do not supply source evidence.
- [x] Public-safe official source leads inventory. This records current public product and download
      leads for source workers, but it does not supply source evidence or clear blockers.
- [x] Public-safe source-evidence draft stub export. This emits starter JSONL records from current
      target metadata, but it does not supply source evidence or clear blockers.
- [ ] Physical-copy card transcription pass (feeds Tier 1 + Tier 3).
- [x] Per-edition acceptance criteria in `docs/v1_acceptance.md` and
      `docs/variant_acceptance.md`.
