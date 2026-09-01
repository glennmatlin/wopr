# Nuclear War: Agent Handoff

> **Development record.** This file tracks how the engine was built,
> milestone by milestone. The `PR #N` links point at the private
> development repository and will not resolve publicly; they are kept
> because the milestone table is what the test suite checks against.
> For design rather than chronology, start at `docs/contest/CURRENT_DESIGN.md`.

This is the entry point for an agent picking up this project. Read this file first, then the
linked docs. Everything you need is in the repo. This file is self-contained.
Base Nuclear War handoff last updated 2026-07-05. ChinaTalk overlay added
2026-08-30.

## ChinaTalk contest overlay

For the current ChinaTalk Situation Room work, read
[`contest/README.md`](contest/README.md) before using the older contest packet
or the Nuclear War mission below. The contest now centers one complete U.S.
Room across the open DATE crisis and the closed Nuclear War game. The remainder
of this handoff still describes the Nuclear War engine foundation and should not
override that dated contest status.

## 1. The mission (end goal)

I am building an LM-agent experimental environment (Concordia-style) for the card game Nuclear
War (Flying Buffalo), on a faithful, complete rules substrate. The order of work is rules-in-code
first, LM experiments after. I get every rule, edition, and variant working deterministically and
verifiably, then I layer language-model agents and a Concordia harness on top. Human-interactive
play is a long-term, low-priority concern.

The reason for that order: the strategic rules are the agent's choices. So the foundation is an
agent-decision interface. It is a decision-point state machine where every strategic choice is
made by an agent through `choose(observation, options)`, on a deterministic, replay-validated
engine.

## 2. Where we are (status, 2026-06-21)

The base-game TABLE loop is functionally complete, internally consistent, and rules-faithful. I
repaired it across 5 phases (see `core_engine_repair_plan.md`). A full match plays end to end:
population deal, then peace (propaganda, secrets), then war (build launch, attack, intercept,
retaliate), then elimination, then final strike with chaining, then peace restoration, then a
decisive winner or mutual annihilation or global loss. Runs are deterministic and reproducible.
The heuristic agent beats random.

The agent-driven decision-machine workstream is implemented through B1. Sub-project A merged in
PR [#17](https://github.com/eilab-gt/WOPR/pull/17), B1 typed observations merged in
PR [#18](https://github.com/eilab-gt/WOPR/pull/18), C1/C2 merged in
PR [#19](https://github.com/eilab-gt/WOPR/pull/19), and D1 merged in
PR [#20](https://github.com/eilab-gt/WOPR/pull/20), E1 merged in
PR [#21](https://github.com/eilab-gt/WOPR/pull/21), E2 merged in
PR [#22](https://github.com/eilab-gt/WOPR/pull/22), and E3 merged in
PR [#23](https://github.com/eilab-gt/WOPR/pull/23), and F1 merged in
PR [#24](https://github.com/eilab-gt/WOPR/pull/24), and F2 merged in
PR [#25](https://github.com/eilab-gt/WOPR/pull/25), and F3 merged in
PR [#26](https://github.com/eilab-gt/WOPR/pull/26), and F4 merged in
PR [#27](https://github.com/eilab-gt/WOPR/pull/27), and source-blocker reporting merged in
PR [#28](https://github.com/eilab-gt/WOPR/pull/28), and variant acceptance criteria merged in
PR [#29](https://github.com/eilab-gt/WOPR/pull/29), and decision heuristic agent merged in
PR [#31](https://github.com/eilab-gt/WOPR/pull/31), and rules trace scaffold merged in
PR [#32](https://github.com/eilab-gt/WOPR/pull/32), and rules text step map merged in
PR [#33](https://github.com/eilab-gt/WOPR/pull/33), and full semantic rules trace merged in
PR [#34](https://github.com/eilab-gt/WOPR/pull/34), and card-effect source evidence intake merged
in PR [#36](https://github.com/eilab-gt/WOPR/pull/36), expansion composition evidence intake merged in PR [#37](https://github.com/eilab-gt/WOPR/pull/37), source evidence capture packet merged in PR [#40](https://github.com/eilab-gt/WOPR/pull/40), private source capture ignore guard merged in PR [#42](https://github.com/eilab-gt/WOPR/pull/42), private physical-copy evidence reference preflight merged in PR [#44](https://github.com/eilab-gt/WOPR/pull/44), and card-effect evidence known-id preflight merged in PR [#46](https://github.com/eilab-gt/WOPR/pull/46).
The source evidence draft preflight merged in PR [#48](https://github.com/eilab-gt/WOPR/pull/48).
The source evidence capture runbook merged in PR [#50](https://github.com/eilab-gt/WOPR/pull/50).
The source evidence capture checklist merged in PR [#52](https://github.com/eilab-gt/WOPR/pull/52).
The source evidence coverage report merged in PR [#54](https://github.com/eilab-gt/WOPR/pull/54).
The source evidence live promotion gate merged in PR [#56](https://github.com/eilab-gt/WOPR/pull/56).
The source evidence target export command merged in PR [#59](https://github.com/eilab-gt/WOPR/pull/59).
The source evidence coverage target details merged in PR [#60](https://github.com/eilab-gt/WOPR/pull/60).
The publisher authorization request packet merged in PR [#62](https://github.com/eilab-gt/WOPR/pull/62).
The official public source leads inventory merged in PR [#63](https://github.com/eilab-gt/WOPR/pull/63).
The source evidence draft stub export merged in PR [#65](https://github.com/eilab-gt/WOPR/pull/65).
The faction C2 collective-decision workstream merged in PR [#76](https://github.com/eilab-gt/WOPR/pull/76).
It adds a composite `FactionDecisionAgent` that maps member votes to one
`LegalAction` via a pure aggregation function, exposed as the `faction_c2` harness
seat. Four archetypes are implemented: sole-authority, council, distributed, and
automated, with configurable seat parameters (`deference`, `weights`, `threshold`,
`quorum`, `policy_action_id`). Deliberation is recorded on
`agent.last_deliberation`, not in the trace sidecar, so the replay schema is
untouched and same-seed determinism is preserved. Design spec:
`docs/superpowers/specs/2026-06-25-faction-c2-collective-decision-making-design.md`.
Example config: `docs/examples/faction_c2_experiment.json`. The engine decision and
apply path is unchanged; a faction is a `DecisionAgent` whose `choose` returns one
validated `LegalAction`. This is additive and does not change the source-evidence
gate for rules and variant work.
The 2026-06-21 local alpha pass added a WOPR-native no-press LLM agent scaffold and mixed
`DecisionAgent` table seating helper. This is not a live model-provider integration.
The continuation pass added `run_no_press_llm_game()` for deterministic mixed seats and separate
LLM trace artifacts. Trace data remains outside replay JSON.
The replay workbench now imports those `.traces.json` artifacts separately and shows linked
decision traces and provider metadata in the `Decision` inspector tab when trace artifacts contain
those fields.
The batch continuation added `run_no_press_llm_batch()` and `nuclear-war llm-experiment` for
deterministic mixed-seat runs across seed ranges, with per-game replay JSON, separate trace
artifacts, per-player decision metrics, aggregate outcomes and decision metrics by agent label,
trace-normalized invalid/retry rates, optional provider latency/cost metadata, and a compact
`summary.json` with a strict config snapshot. `nuclear-war llm-summarize` validates a written
`summary.json` against its config snapshot, seed sequence, replay active variant, replay player
count, replay turn cap, replay-derived outcomes, and linked replay and trace artifacts before
printing the aggregate summary. Trace artifact validation also rejects unknown top-level fields,
prompt/raw-response attempt lists whose stored retry count does not match the recorded attempts,
selected actions that are missing from trace legal options, and parsed legal actions that differ
from the selected replay-linked action. Validation-error counts must match the recorded retry and
fallback shape. Schema v3 traces include a structured `rendered_observation` field beside the
prompt text and legal options, and validation requires that its player and turn match the trace
context and its rendered decision options match the trace legal options when present.
Trace ids must be unique, match the trace player and turn context, and use positive numeric
indexes.
The `llm-experiment` config parser rejects malformed seat ids, player/seat mismatches,
unknown top-level or seat fields, non-positive run bounds, retry budgets, fallback policies,
non-empty scripted-only fields on non-scripted seats, non-default LLM control fields on baseline
seats, malformed provider metadata, and extra scripted provider metadata entries instead of
coercing them.
The checked-in no-provider starter config is
`docs/examples/no_press_llm_experiment.json`.
The deterministic fake LLM seats are `llm_scripted` and `llm_first_legal`; `llm_first_legal`
reads the rendered prompt and returns the first legal action id, so it can run full no-provider
experiments without hand-authored scripted action ids.
The 2026-06-22 workshop demo pass added `llm_http`, a generic OpenAI-compatible
chat-completions client for local, hosted, vLLM, or SGLang-style endpoints. It records
client-side latency plus provider usage, label, and model metadata when present. Trace sidecars
are now schema v4; replay JSON remains unchanged.
The same pass added the optional `nuclear_war_silisocs` adapter package, the
`nuclear-war silisocs-demo` command, a SiliSocs-compatible `NuclearWarNoPressBackend`, and
offline/hosted example configs in `docs/examples/`. The adapter writes `wopr/replay.json`,
`wopr/traces.json`, `wopr/summary.json`, `silisocs/config_snapshot.json`, and
`silisocs/telemetry.json` for replay workbench inspection.
Later LLM-game work added the Concordia no-press harness and the press ladder:
press-light, multi-turn public press, and full press. These modes use WOPR as
the rules engine and keep speech trace-only in separate Concordia press
sidecars. Replay JSON stays unchanged when press is disabled. Full press adds
single-recipient private messages, filtered per-speaker memory, and structured
commitments recorded as data only. The native Concordia entity logs are captured in
decision trace sidecars so the true model-visible prompt can be inspected. The
Concordia capability map records which upstream components are used, excluded,
or candidates for later experiment design.
The HTTP provider preset pass added a small provider abstraction around the
OpenAI-compatible client. Configs can now name `provider: "openai_compatible"`
or `provider: "together"` and inherit the expected base URL, model environment
variable, API-key environment variable, and provider label unless a config
overrides those fields. The provider response parser accepts both chat-message
and text-style completion payloads.
The 2026-07-05 and 2026-07-06 model calibration passes added a measured
serverless scorecard, debugged the first run's false failures, repaired
Concordia parser and provider-error paths, and ran bounded press-light
robustness checks across all 23 official chat model lanes. The corrected Stage
2 artifact, bounded Stage 3 no-press evidence, repair checks, catalog-wide
press-light aggregate, and final scorecard are recorded in
`research/llm_model_calibration/research-state.yaml`,
`research/llm_model_calibration/findings.md`,
`research/llm_model_calibration/research-log.md`, and
`research/llm_model_calibration/stage3_press_light_scorecard.md`.
Use `/tmp/wopr_stage3_presslight_robustness/press_light_aggregate.json` and the
checked-in scorecard for Stage 3 press-light candidate selection.
Current low-cost default is `openai/gpt-oss-20b` with `reasoning_effort=low`.
Useful low-cost or diversity lanes are `Qwen/Qwen3.5-9B`,
`Qwen/Qwen2.5-7B-Instruct-Turbo`, and
`Qwen/Qwen3-235B-A22B-Instruct-2507-tput`. Kimi, GLM, Cogito, DeepSeek, Gemma 4,
and Llama lanes are comparison lanes when role-play behavior matters more than
cost. `MiniMaxAI/MiniMax-M3` is a silent legality baseline for press-light,
not a role-play lane. MiniMax M2.7, Qwen Plus/Max lanes, and Pearl Gemma remain
on hold for press-light until a separate timeout or empty-content recovery task
exists.

| Sub-project | Status | What it did |
|---|---|---|
| A0 scaffolding | done | Added the `pending_decision` / `apply_decision` contract. `run_simulation` table path is driven by the decision loop. Faithful round-based turn cadence. (A1 folded in, since PLACE and LAUNCH_TARGET were already agent-driven.) |
| A2 secret/propaganda targets | done | `SECRET_TARGET` and `PROPAGANDA_TARGET` are now agent decisions. Offensive secrets and peace-time propaganda surface a target choice. |
| A3 interception interrupt | done | `INTERCEPT` is a defender decision, always offered (even with no anti-missile, for hidden-information safety). Attack resolution pauses for it. |
| A4 final-strike target | done | `FINAL_STRIKE_TARGET` is a table decision. Chaining is preserved, including secret-triggered final strikes. |
| A5 deterrents | done | `MODIFY_DETERRENT` decision plus place-from-deterrent are implemented. |
| A6 converge loops | done | `env_table` uses the decision loop and table simulation no longer branches through the legacy table turn loop. |
| B1 observations | done | Added typed `Observation` dataclasses, preserved hidden-information safety, and passed observations into decision agents. |
| C1 population bank | done | Population loss/gain now makes change through `population_bank`; global loss returns population cards to the bank; replay summaries and public observations keep bank contents out. |
| C2 card identity | done | Playable non-population deck cards now get unique runtime ids per physical copy, with base-card metadata retained; duplicate runtime id registration fails fast. |
| D1 postal replay validation | done | Postal `intercept_success` payloads match replay schema; dead actors no longer execute queued postal propaganda/secret/secret-theft orders; postal CLI replay sweep passes. |
| E1 expansion mechanic catalog | done | Adds a source-gated catalog for implemented expansion/postal mechanics and validates registry metadata, supported modes, and action coverage without enabling expansion deck counts. |
| E2 expansion mode boundary | done | Validates catalog mode values and locks current implemented expansion mechanics to postal-only availability until source-backed table or combined-expansion composition exists. |
| E3 expansion source boundary | done | Prevents cataloged expansion metadata records from becoming playable deck cards before authorized source-backed composition exists. |
| F1 variant catalog validation | done | Makes known edition and variant boundaries machine-readable before alternate editions are implemented. |
| F2 variant selection guard | done | Lets runtime configs name the active variant while rejecting deferred variants before alternate edition behavior can run. |
| F3 CLI variant flag plumbing | done | Lets CLI simulation and experiment commands name the active variant while keeping deferred variants blocked. |
| F4 active variant resolution | done | Routes setup and simulation result metadata through the resolved active variant while keeping deferred variants blocked. |
| Source blocker report | done | Reports remaining source-gated C/E/F work from `validate-rules` without enabling deferred behavior. |
| Variant acceptance criteria | done | Adds per-edition criteria to the variant catalog and docs without enabling deferred variants. |
| Decision heuristic agent | done | Adds table-only `decision_heuristic`, an observation-driven agent that leaves parity-preserving `heuristic` unchanged. |
| Rules trace scaffold | done | Adds source-linked trace records for current table replay action/event families without claiming full semantic trace verification. |
| Rules text step map | done | Adds a source-mapped catalog for the rule-step IDs used by trace records and reports source/step gaps from `validate-rules`. |
| Full semantic rules trace | done | Adds a deterministic full-game semantic trace helper and bounded `validate-rules` summary. |
| Card-effect evidence intake | done | Adds a public-safe manifest validator for future card-effect source evidence without changing effect metadata. |
| Expansion composition evidence intake | done | Adds a public-safe manifest validator for future expansion deck-composition evidence without enabling expansion deck counts. |
| Source evidence capture packet | done | Adds public-safe draft templates and source-worker instructions without creating live evidence manifests. |
| Private source capture ignore guard | done | Ignores local `research/source_evidence/private/` captures so private source photos stay out of the public repository. |
| Private physical-copy evidence reference preflight | done | Requires physical-copy evidence manifest source references to use `private/` paths while preserving publisher-authorized references. |
| Card-effect evidence known-id preflight | done | Requires card-effect evidence `card_id` values to match the active registry before a present manifest can pass. |
| Source evidence draft preflight | done | Adds `validate-source-evidence` for explicit draft manifest paths without changing `validate-rules` live-manifest behavior. |
| Source evidence capture runbook | done | Adds a public-safe `CAPTURE_RUNBOOK.md` for physical-copy or publisher-authorized capture sessions without creating live evidence manifests. |
| Source evidence capture checklist | done | Adds a public-safe `CAPTURE_CHECKLIST.md` target list derived from active card IDs and expansion registry IDs without creating live evidence manifests. |
| Source evidence coverage report | done | Adds `card_effect_evidence_coverage` and `expansion_composition_evidence_coverage` reports to source-evidence preflight and rules validation without creating evidence or clearing blockers. |
| Source evidence live promotion gate | done | Adds `card_effect_evidence_promotion_errors` and `expansion_composition_evidence_promotion_errors` so live manifests fail unless records are second-pass verified, while draft preflight stays permissive. |
| Source evidence target export | done | Adds `nuclear-war source-evidence-targets` for public-safe capture target metadata without creating evidence or clearing blockers. |
| Source evidence coverage target details | done | Adds public-safe missing and unverified target details to draft preflight coverage without creating evidence or clearing blockers. |
| Publisher authorization request packet | done | Adds a public-safe request packet for publisher-authorized source acquisition without creating evidence or clearing blockers. |
| Official public source leads inventory | done | Surfaces official public product and download leads from the imported source index without creating evidence or clearing blockers. |
| Source evidence draft stub export | done | Emits public-safe draft JSONL starter records from current target metadata without creating evidence or clearing blockers. |
| LLM agent scaffold | done | Adds deterministic WOPR-native no-press LLM decision plumbing, trace recording, retry/fallback behavior, direct retry-budget validation, injected mixed table seating, strict known-agent harness config parsing, checked-in no-provider example config, trace artifact IO with rendered observations, strict trace sidecar top-level fields, trace-id uniqueness, context, and positive-index consistency, rendered-observation player/turn/options consistency, selected-action id/player/turn, legal-option membership, parse-result selection consistency, validation-error count consistency, retry-attempt consistency validation, non-empty scripted-only seat field validation, baseline LLM-control field validation, scripted provider metadata length validation, replay workbench trace inspection with optional provider metadata, optional provider metadata summaries, mixed-seat summaries with agent outcome and decision metric counts/rates, multi-run batch CLI, prompt-driven fake LLM seats, generic HTTP LLM seats, provider usage/model trace sidecar metadata, optional SiliSocs demo adapter outputs, summary config snapshots, and batch artifact validation with seed-sequence, variant, player-count, max-turns, and outcome checks without changing the replay schema. |
| HTTP provider presets | done | Adds provider-name defaults for the existing HTTP client and checked-in example configs so endpoint-backed no-press, SiliSocs, and Concordia runs can use environment-driven provider setup without repeating base URL or key variable fields. |
| Concordia press ladder | done | Adds no-press, press-light, multi-turn public press, and full-press Concordia runs on top of the WOPR decision loop with separate trace sidecars and replay-schema preservation. |
| Native Concordia prompt logging | done | Captures native entity logs in decision trace sidecars and documents used, excluded, and candidate Concordia components in `docs/concordia_capability_map.md`. |

Verified after the LLM baseline control field validation pass: 1080 tests pass with 35 warnings.
`ruff` and `pyright` are clean. `validate-rules` returns `ok: true` while preserving the expected
source blockers. Draft preflight now reports
`card_effect_evidence_target_details` and
`expansion_composition_evidence_target_details` for public-safe missing and unverified target
queues. `validate-rules` reports `ok: true`, missing non-failing
card-effect and expansion composition evidence manifests, `card_effect_evidence_coverage` with 30
target IDs and zero recorded or verified live IDs, `expansion_composition_evidence_coverage` with
10 target IDs and zero recorded or verified live IDs, empty
`card_effect_evidence_promotion_errors` and
`expansion_composition_evidence_promotion_errors` because the live manifests are absent, 35
`rules_trace` records, 19 `rules_trace_steps`, 282 full-game semantic trace entries, and no trace
source, step, or full-game gaps. The table 240-game CLI replay sweep passes.

After PR #56: remaining C-stage card-effect verification and E-stage expansion deck
composition are still gated on a physical copy or authorized source. The intake manifests validate
future evidence, and coverage payloads report capture progress; neither supplies evidence or clears
source blockers. Runtime configs can name only the active variant for now; deferred variants fail
before alternate edition behavior can run. F4 removes the remaining hard-coded active-variant
setup/result seams without enabling alternate editions. Variant acceptance criteria are now
explicit, but the deferred variants still require source evidence before implementation. See
`roadmap.md`.

## 3. Architecture (the decision-machine contract)

There are three engine entry points (in `src/nuclear_war_env/decision_loop.py` and
`engine/decision.py`):

- `pending_decision(state) -> Decision | None`. The current choice, or `None` at a terminal state.
- `apply_decision(state, action) -> list[EngineEvent]`. Apply the chosen action, then run all
  mandatory steps until the next genuine choice, and store it on the state.
- `observe(state, agent_id) -> Observation`. A structured per-agent view. The table loop passes
  this object into `choose(observation, options)`.

An agent is anything with `choose(observation, options) -> action`. Baseline agents live in
`src/nuclear_war_agents/baseline.py` (`HeuristicAgent`, `RandomAgent`). The table-only
`ObservationHeuristicAgent` lives in `src/nuclear_war_agents/observation_heuristic.py` and is
exposed as CLI/simulation agent `decision_heuristic`. The no-press `LLMDecisionAgent` lives in
`src/nuclear_war_agents/llm_agent.py` and accepts clients returning plain response strings or
`LLMCompletion` records with optional provider latency/cost metadata. It records model-visible
prompts, raw responses, parse results, retries, validation errors, selected actions, optional
stated rationale, and optional provider metadata. The generic OpenAI-compatible HTTP client lives
in `src/nuclear_war_agents/llm_http_client.py` and is exposed as harness seat `llm_http`. The
`run_no_press_llm_game()` harness in `src/nuclear_war_env/llm_harness.py` builds mixed
`llm_scripted`, `llm_first_legal`, `llm_http`, `random`, `heuristic`, and
`decision_heuristic` seats and
returns replay, separate trace artifact payload, seat labels, and summary metrics. The
`run_no_press_llm_batch()` runner in `src/nuclear_war_env/llm_harness_batch.py` repeats that
harness across seed ranges and writes per-game artifacts through
`src/nuclear_war_env/llm_harness_batch_io.py`. Batch summary validation lives in
`src/nuclear_war_env/llm_harness_batch_validation.py` and checks the config snapshot plus linked
replay and trace artifacts, including the expected `seed_start + result index` sequence and
replay-derived active variant, player count, max-turns bound, and `win_loss` outcomes.
Decision metrics include trace counts, invalid-action counts, retry counts, and trace-normalized
invalid/retry rates.
Batch config parsing lives in `src/nuclear_war_env/llm_harness_batch_config.py`.
Trace artifact read/write and validation live in `src/nuclear_war_env/llm_trace_artifacts.py`;
selected trace actions must match replay action id, player, and turn, prompt/raw-response attempt
lists must align with the stored retry count, selected actions must appear in legal options, parsed
legal actions must match selected actions, validation-error counts must match retry outcomes,
trace ids must be unique, match player and turn context, and use positive numeric indexes,
top-level artifact fields are strict, and schema v4 stores a structured `rendered_observation`
field whose player, turn, and rendered decision options must match the trace when present.
The replay workbench imports trace artifacts through `wopr_visualizer/src/replay/traceArtifacts.js`
and shows linked rendered observations, legal options, prompts, raw responses, parse results,
retries, validation errors, selected actions, and optional provider metadata in the `Decision`
tab. The optional SiliSocs adapter lives in `src/nuclear_war_silisocs/` and wraps the WOPR
harness without making SiliSocs a base dependency. The
`as_decision_agent()`
adapter in `agent_protocol.py` wraps legacy `choose(actions)` agents.

A turn is a sequence of phases on a `DecisionCursor` (`engine/decision.py`):
SETUP (opening commitment, game start only), DRAW, SECRETS, SLIDE, PROPAGANDA, DETERRENTS,
PLACE, ATTACK, INTERCEPT, FINAL_STRIKE, END. Mandatory steps auto-advance. Only genuine
choices pause as a `Decision`. Decision types so
far: SETUP_PLACE (opening face-down commitment), PLACE, LAUNCH_TARGET, SECRET_TARGET,
PROPAGANDA_TARGET, INTERCEPT (defender), FINAL_STRIKE_TARGET, MODIFY_DETERRENT, and
STRATEGY_REPLACE (peace-restoration replacement window, decline-first).

### The engine-orders pattern (a design decision I made on 2026-06-17)

The engine presents option lists pre-ordered by the V1 policy. Examples: weakest opponent first
for LAUNCH_TARGET, highest-population first for SECRET_TARGET and PROPAGANDA_TARGET, eligible
anti-missiles first then decline for INTERCEPT. The baseline `HeuristicAgent` picks `options[0]`.
That reproduces the old deterministic engine policy and consumes zero RNG draws. `RandomAgent`
picks uniformly. B1 wires typed observations into the same choose call; the baseline adapter still
ignores them. For this to hold, every new `ActionType` must be added to `HeuristicAgent`'s priority
list. Otherwise the heuristic falls through to `rng.choose` and breaks parity.

### The parity and fidelity contract

- A+B decision-migration work preserved heuristic-agent table outcomes byte-identical to the
  pre-migration engine. That invariant keeps decision-interface refactors honest.
- C-stage fidelity fixes may intentionally change seeded outcomes when they remove a documented
  model bug. C2 did this for duplicate physical card ids. The current C2 golden is in
  `tests/integration/test_decision_loop_parity.py::test_heuristic_table_outcomes_match_c2_golden`,
  and the pre-C2 divergence is asserted explicitly in
  `test_heuristic_table_outcomes_intentionally_diverged_after_c2`.
- Random-agent outcomes diverge by design wherever targeting or interception became a real
  decision, because random now draws RNG to choose. That divergence is asserted explicitly in
  `test_random_table_outcomes_diverged_from_a0`. It is not hidden.
- The `LegalAction` and `EngineEvent` vocabulary and the replay schema are preserved. New action
  types are registered with the replay validators (`replay_action_payload_validation.py`,
  `replay_action_validation.py`, `replay_payload_shapes.py`).

## 4. The working process (use this for every sub-project)

This process landed A0, A2, and A3 with the parity invariant verified each time.

1. Scout before planning. Read the exact functions you are replacing. Find the seams, the event
   and RNG side effects, and the replay-validation registration points. A0, A2, and A3 each had a
   latent bug found only by reading the real source. Examples: dropped `alive` guards, lost
   `_last_placed` bookkeeping, a missing replay registration.
2. Write a TDD plan, then harden it. Plans go in `docs/plans/YYYY-MM-DD-<name>.md` as small TDD
   tasks (failing test, then minimal code, then commit). Fix latent parity bugs in the plan before
   you implement. Order the tasks so the suite stays green at every step: behavior-preserving
   refactors, then any parity-test changes, then wiring, then verify.
3. Build with parity gating. Implement one task at a time. After each task, re-run the full suite,
   read the diff, and check the specific parity properties. Use a bounded fix loop. Stop if a task
   cannot go green. (This branch used multi-agent workflows for this. The same discipline works
   task by task by hand.)
4. Verify independently. Reproduce the full suite, `pyright`, `ruff`, and the 240-game sweep
   yourself. For the strongest parity check: `git worktree add --detach /tmp/x <prior-head>`, run
   the baseline-agent outcomes there, and diff against current. This proves outcomes are unchanged
   for decision-interface refactors, or shows exactly which seeded outcomes changed for a documented
   C-stage fidelity fix, without depending only on a hardcoded golden. Note that JSON round-trips
   tuples to lists, so normalize before diffing.

## 5. How to run things

All Python tooling runs through `uv` from the `nuclear_war/` directory.

The `dev` extra includes the `concordia` extra (`gdm-concordia`), so the default
test command below also runs the native Concordia harness tests. Before
2026-07-01 those tests silently skipped unless `--extra concordia` was added
by hand. The only expected skips in a default run are the two live-endpoint
smokes that need model env vars. Set `WOPR_REQUIRE_CONCORDIA=1` (any
non-empty value works) to make an unavailable gdm-concordia install fail the
concordia-gated tests instead of skipping them; use it when the run is meant
to prove native coverage.

```bash
cd nuclear_war
uv run --extra dev python -m pytest -o addopts="" -q      # full suite. pytest is not on PATH. -o addopts="" overrides pytest.ini maxfail.
uv run --extra dev ruff check src tests                   # lint
uv run --extra dev ruff format src tests                  # format
uv run --extra dev pyright <files>                        # type check. This project uses pyright, not ty.
uv run nuclear-war simulate --mode table --players 3 --seed 42 --agent heuristic --max-turns 100 --out /tmp/sim.json
uv run nuclear-war llm-experiment --config docs/examples/no_press_llm_experiment.json --out-dir /tmp/llm_runs
uv run nuclear-war llm-summarize /tmp/llm_runs/summary.json
uv run nuclear-war silisocs-demo --config docs/examples/silisocs_no_press_scripted_demo.json --out-dir /tmp/wopr_silisocs_demo
uv run nuclear-war validate-source-evidence --card-effects /tmp/card_effects.jsonl --expansion-composition /tmp/expansion.jsonl
uv run nuclear-war source-evidence-targets                # public-safe capture target metadata
uv run nuclear-war source-evidence-draft-stubs --kind card-effects
```

Minimal no-provider LLM experiment config:

```json
{
  "players": 4,
  "seed_start": 31,
  "runs": 2,
  "max_turns": 20,
  "seats": {
    "player_0": {"agent": "llm_first_legal"},
    "player_1": {"agent": "random"},
    "player_2": {"agent": "heuristic"},
    "player_3": {"agent": "decision_heuristic"}
  }
}
```

The 240-game replay sweep is the end-to-end gate.

```bash
uv run --extra dev python - <<'PY'
import subprocess
bad=[]
for players in (3,4):
    for ag in ("heuristic","random"):
        for seed in range(1,61):
            p=subprocess.run(["uv","run","nuclear-war","simulate","--mode","table",
                "--players",str(players),"--seed",str(seed),"--agent",ag,
                "--max-turns","100","--out","/tmp/sweep.json"],capture_output=True,text=True)
            if p.returncode!=0: bad.append((players,ag,seed))
print("all 240 pass" if not bad else f"FAILED: {bad[:8]}")
PY
```

## 6. Key files

Engine and decision machine:
- `src/nuclear_war_env/decision_loop.py`. The state machine: `start_game`, `pending_decision`,
  `apply_decision`, `apply_decision_result`, `_advance`, the per-phase decision builders, and the
  `_RoundStamper` plus `turn_player_ids` port for faithful round-based turn numbering.
- `src/nuclear_war_env/engine/decision.py`. `DecisionType`, `TurnPhase`, `Decision`, `DecisionCursor`.
- `src/nuclear_war_env/agent_protocol.py`. The `DecisionAgent` protocol and `as_decision_agent`.
- `src/nuclear_war_env/simulation.py`. `run_simulation`. `_run_table_simulation` drives the loop.
- `src/nuclear_war_agents/baseline.py`. `HeuristicAgent` (priority-list pick-first), `RandomAgent`.
- `src/nuclear_war_env/rules_trace.py`, `rules_trace_catalog.py`, `rules_trace_steps.py`,
  `rules_trace_step_catalog.py`, and `rules_trace_replay.py`. Source-linked scaffold mapping
  current table replay action/event families to source-mapped rule-step IDs and a deterministic
  full-game semantic trace summary.

Engine mechanics (the loop reuses these, it does not reimplement them):
- `engine/launch.py` (`execute_launches`), `engine/launch_resolution.py` (spinner, backfire,
  global loss), `engine/launch_helpers.py` (`attempt_intercept` and the `use_hand_intercept`
  seam, `eligible_hand_antimissiles`, `schedule_final_retaliation`, `assign_retaliation_targets`),
  `engine/final_strike.py` (`run_final_strike`).
- `engine/secret_resolution.py`, `engine/propaganda_resolution.py`, `engine/target_policy.py`
  (`highest_population_opponent`, `opponents_by_population`).
- `engine/draw.py`, `actions.py`,
  `action_models.py`, `engine/events.py`.

Replay validation (register new action and event types here): `replay_action_validation.py` (the
action-type allowlist is `{item.value for item in ActionType}` plus
`ACTION_PLAYER_REFERENCE_FIELDS`), `replay_action_payload_validation.py`, `replay_payload_shapes.py`,
`event_types.py`, `replay_event_identity_validation.py`.

## 7. Documentation map

- `docs/roadmap.md`. Forward scope. Sub-project order A and B, then C, D, E, F, G.
- `docs/specs/2026-06-16-agent-decision-interface-design.md`. The approved A and B design spec:
  decision catalog, turn-as-decisions, observation contract, migration sequence A0 to B1.
- `docs/plans/2026-06-16-A0-...md`, `...A2-...md`, `...A3-...md`,
  `...A4-...md`, `...A5-...md`, and `...A6-...md`. These are executed TDD plans.
- `docs/plans/2026-06-19-B1-typed-observations.md`. The executed B1 TDD plan.
- `docs/plans/2026-06-19-F2-variant-selection-guard.md`. The executed F2 TDD plan.
- `docs/plans/2026-06-19-F3-cli-variant-flag-plumbing.md`. The executed F3 TDD plan.
- `docs/plans/2026-06-19-F4-active-variant-resolution.md`. The executed F4 TDD plan.
- `docs/plans/2026-06-19-source-blocker-report.md`. The executed source-blocker report plan.
- `docs/plans/2026-06-19-variant-acceptance-criteria.md`. The executed variant acceptance plan.
- `docs/plans/2026-06-20-rules-text-step-map.md`. The executed rules text step map plan.
- `docs/plans/2026-06-20-full-semantic-rules-trace.md`. The executed full semantic trace plan.
- `docs/plans/2026-06-20-card-effect-source-evidence-intake.md`. The executed card-effect
  evidence intake plan.
- `docs/plans/2026-06-20-expansion-composition-source-evidence-intake.md`. The executed expansion
  composition evidence intake plan.
- `docs/plans/2026-06-20-source-evidence-capture-packet.md`. The executed plan for capture
  templates and source-worker instructions.
- `docs/plans/2026-06-20-source-evidence-draft-preflight.md`. The executed plan for draft
  manifest preflight validation.
- `docs/plans/2026-06-20-source-evidence-coverage-report.md`. The executed plan for
  source-evidence target coverage reporting.
- `docs/plans/2026-06-20-source-evidence-live-promotion-gate.md`. The executed plan for live
  source-evidence promotion validation.
- `docs/plans/2026-06-21-public-source-leads-inventory.md`. The executed plan for official public
  source leads inventory support.
- `docs/plans/2026-06-21-public-source-leads-merge-handoff.md`. The executed plan for recording
  the PR #63 merge state in the handoff.
- `docs/plans/2026-06-21-source-evidence-draft-stub-export.md`. The executed plan for public-safe
  draft JSONL stub export.
- `docs/plans/2026-06-21-source-evidence-draft-stub-merge-handoff.md`. The executed plan for
  recording the PR #65 merge state in the handoff.
- `docs/core_engine_repair_plan.md`. The 5-phase repair changelog: what was broken and how I fixed
  it.
- `docs/rule_fidelity_matrix.md`, `docs/v1_acceptance.md`, `docs/variant_acceptance.md`,
  `docs/v1_source_evidence.md`. Fidelity status, acceptance criteria, source evidence.
- `NUCLEAR_WAR_METHODOLOGY.md`, `docs/source_research_policy.md`. V1 doctrine and research-source
  rules.
- `nuclear_war/research/`. Source bundles and derived notes that back the implementation.

## 8. Gotchas and scope boundaries

- Type-check with `pyright`, not `ty`. The IDE's `ty` checker often resolves against a stale
  python3.12 site-packages instead of the project's 3.13 `.venv`, and it emits unresolved-import
  and type errors that are not real. `pyright` (via `uv run --extra dev pyright`) is the one to
  trust.
- Commits are 1Password-signed (`op-ssh-sign`). If signing fails with "failed to fill whole
  buffer", the vault auto-locked. Unlock it and retry. Do not create unsigned commits.
- Postal no-press replay validation passes after D1. Treat postal as a guarded surface: keep
  mode-specific replay payloads schema-valid, and run a postal sweep before postal behavior changes.
  Do not change postal while doing source-bound or table-only work unless the plan explicitly
  requires it.
- Final-strike targeting and final-strike interception are now decision-loop paths. Keep chaining
  behavior and the secret-triggered final-strike path covered by tests when changing this area.
- Card-effect values and semantics are low-confidence summaries pending transcription from a
  physical copy (Tier 1, sub-project C). The engine applies effects correctly. The effect metadata
  is unverified.
- Card-effect and expansion composition evidence manifests are intake gates only. Missing manifests
  are non-failing. Present invalid manifests fail validation. Do not treat these gates as source
  evidence or use them to enable expansion `count_in_deck` values.

## 9. Current pickup points

For LLM-game work, the verification and provider preset work is implemented.
The ladder to re-check first is: no-press LLM experiments, SiliSocs adapter
output, Concordia no-press, press-light, multi-turn public press, full press,
replay-workbench press loading, native prompt logging, the capability map, and
HTTP provider presets. Run the focused Concordia/press tests plus provider
config tests, then the broader suite and static checks.

The LLM model calibration branch is now collated for PR review. Start with
`research/llm_model_calibration/README.md`, then use
`research/llm_model_calibration/stage3_press_light_scorecard.md`,
`research/llm_model_calibration/playground/stage3_results_playground.html`, and
`/tmp/wopr_stage3_presslight_robustness/press_light_aggregate.json` as the
final study package. The next execution track is small provider-backed LLM and Concordia runs
before expanding experiment design. Start with the env-gated no-press HTTP
smoke and Concordia HTTP smoke when the local API-key and model environment
variables are present. Then run short no-press, press-light, multi-turn public,
or full-press demo configs under `/tmp` for artifact
inspection before creating new batch experiments. Keep generated live-run
artifacts out of the repo unless a later plan explicitly promotes bounded smoke
data.

The source acquisition remains a separate blocked source-evidence thread. Use
`research/source_evidence/README.md`, `CAPTURE_RUNBOOK.md`,
`CAPTURE_CHECKLIST.md`, `PUBLIC_SOURCE_LEADS.md`,
`PUBLISHER_AUTHORIZATION_REQUEST.md`, and the `.template.jsonl` files only when
resuming card-effect or expansion deck-composition evidence work. The templates
are not evidence; they are draft shapes for physical-copy capture or
publisher-authorized evidence that can populate the live intake manifests later.
Official public leads are source-acquisition aids and do not clear blockers by
themselves. Do not enable alternate editions or expansion `count_in_deck` values
until the relevant source evidence is explicit, validated, and followed by a
separate registry-change branch. Live manifest records must be second-pass
verified or `validate-rules` reports promotion errors.
