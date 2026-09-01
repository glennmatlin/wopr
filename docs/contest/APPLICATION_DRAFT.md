# WOPR: U.S. Situation Room evaluation application

Status: submission draft for owner review. This application describes the
DATE-first design and separates implemented machinery, executed development
evidence, specified-but-not-evaluated work, and future work. No live DATE result
is claimed.

## Evaluation title

**WOPR: A U.S. Situation Room for Open-Ended Crisis Decisions**

## Abstract (146 words)

WOPR is a simulation of a U.S. national-security Situation Room responding to a Himaldesh-Olvana conflict. The Room is built from institutionally distinct seats with mandates, portfolio information, working-group products, dissent, and routed decisions. The proposed two-cycle design gives seats selective evidence, requires attributable portfolio assessments, and assembles contributions into an open Policy Package recording immediate, conditional, and deferred action. A constrained interpreter serializes the package into proposals while a World-owned EXCON/MSEL path proposes consequences for validation. The first World is DATE-backed and keeps nuclear escalation reachable without prescribing it. The evaluation separates institutional process from World outcomes and retains the causal trace for replay. The repository contains the Room, World, replay, and receipt machinery plus no-model traces; no live DATE result is claimed. After the DATE Room is frozen, the same Room will be adapted to Nuclear War's finite legal-move World as a secondary stress test.

Word count: 146.

## One-sentence contribution

WOPR makes a U.S. Situation Room inspectable by tracing selective portfolio evidence and dissent into a replayable Policy Package across two World contracts.

## Evaluation question and first episode

Can a language model operate as a U.S. Situation Room made of distinct institutional seats, each with a mandate and partial information, and produce an attributable policy package as a crisis changes?

The first World is a DATE-backed Himaldesh-Olvana high-altitude occupation and recapture crisis. Nuclear warning, signaling, misinterpretation, or use remains reachable through the authored state and supported authorities; it is not a forced branch. The normal episode horizon is two complete U.S. Room Cycles, with an admitted consequence and a matched pressure inject returned between cycles.

The U.S. Charter describes Watch, specialist and synthesis groups, Presidential Committee integration, NSC/HSC routing, an Executive Secretary, and a triggered theater-commander role. Seats retain one identity across groups and cycles. They receive entitled Common Crisis Picture and portfolio information, produce attributable products, expose disagreement, and carry Dissent Dispositions into the integrated Policy Package. The package records policy-domain dispositions, dependencies, safeguards, uncertainty, authority, and reassessment without requiring one predetermined action.

The design permits the DATE Room to issue an Open Action Proposal in its original language. A constrained interpreter preserves that proposal and maps only its declared, supported components into the World contract. A distinct World-owned EXCON/MSEL layer may propose downstream consequences from recorded causal parents; a deterministic World Validator decides what enters the ledger or changes typed state. The Room cannot invent facts, capability, authority, or consequences.

## Two-World continuation

After the DATE Room identity is frozen, the same U.S. Charter, institution registry, mandates, group graph, routing, Policy Package contract, model condition, and evidence definitions will be reused in WOPR's deliberately unrealistic Nuclear War World. That World retains finite legal moves, hidden information, engine-owned consequences, and replay-linked action IDs. The secondary run tests Room identity and trace continuity across World contracts; it is not a realism claim or a matched outcome comparison.

## Evidence boundary

| Category | What this application can state | Evidence boundary |
| --- | --- | --- |
| Implemented | WOPR has a deterministic Nuclear War rules/replay engine, decision-agent and Concordia harnesses, a source-bound U.S. Charter compiler, DATE World Core and ledger scaffolding, Room-cycle orchestration, a fail-closed interpreter and proposal bridge, and receipt/replay validators. | Source and machine contracts; implementation tests. |
| Executed evidence | D64's DATE transition tracer and D68-D70's no-model U.S. controller, proposal bridge, and two-cycle receipts pass in their declared development-fixture scope and replay exactly. Historical Nuclear War runs remain engineering evidence for the closed World. | These receipts are labeled `development_fixture_non_evidence`; they are not live DATE or model results. |
| Specified, not evaluated | Live model-mediated Room behavior, live open proposal extraction, creative EXCON quality, MSEL consequences, final effect-level authority, model comparisons, and matched DATE evaluation. | The offline interpreter mechanics exist, but no live DATE result or model-quality claim is made. |
| Future work | Complete and freeze the live DATE Room, run the matched DATE condition, produce the same-Room Nuclear War receipt, and publish only shared institutional measures supported in both Worlds. | Each stage needs its own retained receipt. |

## Continuity and positioning

This application extends [No One Wins in Nuclear War: A Social Simulation of Military Decision-making](https://arxiv.org/abs/2608.01868), which documents the replay-validated WOPR engine and decision harness, and [Shall We Play a Game? Language Models for Open-ended Wargames](https://arxiv.org/abs/2509.17192), which motivates separating model action choice from adjudication. The new submission applies that separation to an institutionally explicit U.S. Room and a DATE-backed open World.

The [ChinaTalk contest brief](https://www.chinatalk.media/p/25k-contest-evals-for-the-situation) asks for concrete evaluation protocols for frontier systems in strategic and national-security settings. The [submission form](https://docs.google.com/forms/d/e/1FAIpQLSfSVOzLSEN-ke5tf87SE4WPSi0VJSH3aCsW0Np9pFKibCMW9A/viewform) receives the fields below.

## Submission fields

| Field | Value |
| --- | --- |
| Name and contributors | Owner-supplied in the submission form; omitted from the public repository |
| Email address | Owner-supplied in the submission form; omitted from the public repository |
| LinkedIn URL | Owner-supplied in the submission form; omitted from the public repository |
| Two-sentence author bio | I am a PhD candidate in computer science at Georgia Tech, where I study data provenance, interpretability, and evaluation for language models used in high-stakes settings. Before returning to academia, I worked on production NLP, healthcare analytics, credit risk, and recommendation systems. |
| Evaluation title | WOPR: A U.S. Situation Room for Open-Ended Crisis Decisions |
| Abstract | Final draft above; 146 words |
| Project microsite | <https://glennmatlin.doctor/wopr/> |
| GitHub repository | <https://github.com/glennmatlin/wopr> |
| Interest in working for ChinaTalk | Yes, part time |

## What support would fund

1. Complete a receipt-bound live DATE Room run and freeze its common identity.
2. Evaluate the two-cycle Room against a declared model condition, with process and World measures kept separate.
3. Adapt the frozen Room to Nuclear War's finite legal-move World and retain an independent secondary receipt.
4. Release the protocol, replay-linked evidence, source treatment, and claim boundaries through the public repository and microsite.

## Limitations

- DATE is a fictional, episode-bounded World informed by public DATE material; it is not an official or classified government simulator.
- The U.S. Charter records public-source facts and labeled WOPR inferences. It does not establish official procedure or predict government behavior.
- The current receipts prove machine and no-model development mechanics. They do not prove live model behavior, institutional quality, creative EXCON quality, or a DATE outcome.
- Nuclear War is intentionally unrealistic. Its finite rules and replay contract support a closed-form stress test, not physical or geopolitical realism.
- DATE and Nuclear War have different World mechanics. Their outcome vectors are not ranked; shared institutional measures require an explicit applicability argument.

## Useful design and evidence links

- [Evaluation protocol](PROTOCOL.md) and [one-Room cross-World contract](spec/12-one-room-across-open-and-closed-worlds.md).
- [DATE source and evidence contract](spec/08-sources-and-evidence.md), including the official DATE source register.
- [U.S. Charter machine contract](spec/15-us-charter-machine-contract.md) and [ratification receipt](US_CHARTER_RATIFICATION.json).
- [D64 DATE transition receipt](DATE_TRACER_RECEIPT.json), [D68 Cycle 1 receipt](US_CYCLE1_RECEIPT.json), and [D70 two-cycle receipt](US_TWO_CYCLE_RECEIPT.json).
- [Historical Nuclear War games register](GAMES_REGISTER.md), retained as engineering provenance rather than DATE evidence.

## Submission checklist

- [x] Replace the old game-centered title and abstract with a U.S.-first DATE narrative.
- [x] Label implemented machinery, executed development evidence, specified-not-evaluated work, and future work.
- [x] Keep live DATE results and model-quality claims out of the application.
- [x] Supply the public bio, links, and work-interest choice while keeping owner-controlled name, contact, and profile data out of the repository.
- [x] Record the owner-cleared source-rights treatment and MIT license; release-time scans remain bound to the exact published revision.
- [ ] Update any result claim only when new retained evidence supports it;
  otherwise keep the current evidence matrix unchanged.
