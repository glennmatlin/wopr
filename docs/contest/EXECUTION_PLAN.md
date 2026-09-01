# WOPR Situation Room Contest Execution Plan

> **HISTORICAL PACKET.** I retain this plan as the execution history for the
> Nuclear War-only packet. Its milestones and authority sequence are not the
> current DATE work program. Start at [CURRENT_STATUS.md](CURRENT_STATUS.md).

Status: corrected M4 execution complete. M5 packaging and owner decisions are
active.

Deadline: September 1, 2026

## Delivery claim

I am extending the existing replay-validated WOPR environment into a
configurable Room Instrument. The Sounding varies Organizational type
(presidential staff, equal council, chair-weighted council) while holding the
model, World rules, initial state, engine seed, and full-press setting fixed.
Overlay stays off except for one Demo trajectory. Completion requires
inspectable Sounding evidence and an application package, not only a functioning
harness.

## Milestones

| Milestone | Target | Exit receipt |
| --- | --- | --- |
| M0: freeze execution contract | August 15 | protocol, this plan, authority ledger |
| M1: compose C2 and full press | August 19 | tests, type checks, replay sweep, bounded smoke |
| M2: build study pipeline | August 22 | offline 2 x 2 dry run, ledger, measures, analysis |
| M3: screen and freeze models | August 23 | three-model screen, final-pair preflight, cost estimate, approved manifest |
| M4: execute pilot | August 27 | validated attempts, admissibility report, paired tables |
| M5: package submission | August 31 | public-ready repository, microsite build, form checklist |

The September 1 deadline remains a final submission buffer. Dates are planning
targets rather than evidence that a milestone is complete.

## Work sequence

### M1: composition gate

1. Parse and snapshot the authority configuration without resolved credentials.
2. Build persistent member agents behind the existing `DecisionAgent` seam.
3. Introduce a seat runtime with one press spokesperson and three memory recipients.
4. Persist and validate member votes in a dedicated C2 sidecar.
5. Run full press under presidential staff, equal council, and chair-weighted council.
6. Pass focused tests, the full suite, type checks, lint, and the replay sweep.

If chair-weighted council fails the provider-backed gate, I will drop that
Preset and run presidential staff and equal council only. I will not report a
three-Preset Instrument from mixed harnesses.

### M2: study pipeline

The runner must enumerate fixed condition-model-seed cells, resume without
overwriting attempts, and append every started attempt to a run ledger. Each
attempt records its source revision, condition manifest hash, prompt hash,
backend and model manifest hash, seed, request policy, artifact paths, terminal
state, and admissibility tier.

Deterministic measures will be derived from validated replay and sidecar data.
They will separate ordinary agent-shaped escalation from forced final strikes,
retain seed-level paired values, and exclude Tier C attempts from behavioral
claims without deleting them.

### M3: backend and model freeze

Direct APIs are the primary backend because exact model identifiers, request
settings, usage, retries, and provider errors can be recorded. The bounded
screen of three inexpensive families on seeds 101-103 is complete: six cells
passed the operational receipt rule and three Qwen3.5 cells were terminal Tier
C. The deterministic selection retained DeepSeek V4 Flash and GPT-OSS 20B, and
the pair-specific candidate plus zero-network preflight receipt are checked in.
The corrected six-cell live preflight passed and was promoted on executor
`fd48b11e49675c3a8a82319e13f07c7900a5ddba`.

A headless code-agent backend is a separately labeled system. It is eligible
only if the executable version and model selection are pinned, noninteractive
input and output are stable, hidden retries and fallbacks are disabled or fully
observable, complete trace retention is permitted, and automated evaluation use
complies with its terms. It cannot be treated as equivalent to the same model
through a direct API without a separate parity study.

### M4: Sounding execution

The intended Sounding is 3 Organizational Presets x 2 retained models x 3
matched seeds (51, 52, 53), for 18 games, plus one Overlay Demo. The
three-model screen and the final pair preflight use separate seeds and do not
enter Sounding cells. Failed attempts remain in the ledger and cannot be
silently replaced. Configuration changes create new attempt identities rather
than overwriting the original record. Historical factorial manifests are not
executable.

Every admitted run must have a valid replay, ordinary decision traces, press
traces, C2 deliberations, frozen configuration, runtime metadata, and a
terminal summary. The analysis publishes seed-level Preset values and
council-minus-staff differences without a single composite score.

The August 18 execution produced 15 Tier-A cells, but its strict floating-point
boundary required unanimity in equal council instead of two of three votes.
ADR 0009 retains those artifacts as operational evidence and requires a clean,
newly bound executor to rerun all 18 cells plus the Demo. Corrected attempts
must use a new output directory and cannot overwrite the superseded ledger.
The corrected runner accepts `--max-workers` through `contest-run-study`.
Sounding uses two workers inside one coordinator process so attempt directories
remain disjoint while ledger appends and study-wide spend accounting stay
locked. The composition smoke is a receipt-bound `room_instrument_smoke`
manifest: seed 51, two turns, one approved candidate model, and all three
Presets. Its checked template is
`STUDY_MANIFEST.room_instrument_smoke.candidate.json`. The Overlay Demo remains
one approved candidate model, seed 51, and equal council only.

The corrected run completed all 18 terminal attempts: 12 Tier A and 6 Tier C.
Analysis admits 12 rows and five matched pairs. The Overlay Demo ran but failed
terminal before an admissible trace, so M5 cannot include a Demo trajectory.

### M5: submission package

The package contains the frozen protocol and manifests, public-safe code,
attempt ledger, validated raw artifacts, derived tables, analysis code,
limitations, and a replay-linked example trajectory. The microsite presents the
question, design, aggregate evidence, replay, artifacts, limitations, and funded
extension. The application includes an approximately 150-word abstract plus the
microsite and repository links.

## Authority and cost gates

The active topic branch may receive scoped source, test, documentation, commit,
and push changes. Local offline runs and temporary artifacts are allowed.

The following remain owner decisions:

- Any billable model call, including the three-model screen and final-pair preflight, requires a
  recorded maximum spend and approved credentials path.
- Making the repository public requires a license, source-material, and secret
  scan plus explicit authorization.
- Publishing the microsite or submitting the form requires explicit authorization.
- New scientific factors, different study seeds, or changes to primary measures
  require a protocol revision before study execution.

Before spend approval, the runner will produce an upper-bound request and token
estimate from offline fixtures and bounded nonbillable instrumentation. The
model manifest remains unfrozen until access, version stability, and the budget
are confirmed.

## Completion receipts

M1 is complete only when composition artifacts validate and engine replay gates
remain green. M2 is complete only when an offline dry run can resume
and reproduce its derived tables. M3 is complete only when the exact manifest
and spend authorization are recorded. M4 is complete only when every attempted
Sounding and Demo cell is terminal and classified. M5 is complete only when the site build,
repository package, abstract, and submission checklist are ready for owner
review.
