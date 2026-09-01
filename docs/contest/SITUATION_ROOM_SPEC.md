# Situation Room design specification

Version: 0.38
Date: 2026-08-26
Design status: locked choices through D61 and D65, with measured checkpoints D64 and D66-D74
Implementation status: the DATE transition tracer, complete no-model two-cycle U.S. vertical slice, both isolated no-model Counterpart Room traces, and their exact U.S. composition pass their bounded checks; deterministic no-model Milestone 5 is complete

This specification is the proposed canonical design surface for the ChinaTalk DATE-backed Situation Room pivot. It restates the active locked choices without rewriting the archival reasoning. Draft ADRs explain hard choices, the decision crosswalk accounts for every recorded choice, and the sealed archive plus append-only continuation preserve chronology.

## Authority order

1. The [complete pivot archive](../plans/2026-08-22-chinatalk-situation-room-complete-record.md) and [design continuation](../plans/2026-08-23-chinatalk-situation-room-design-continuation.md) are the current authority for locked owner choices.
2. Proposed ADRs 0010 through 0047 cluster those hard choices, implementation defaults, and supersession; their wording remains subject to one owner ratification pass.
3. This draft specification restates the intended normative contract and explicit provisional or open fields; if it conflicts with the preserved decision record before ratification, the decision record wins.
4. [`DECISION_CROSSWALK.md`](DECISION_CROSSWALK.md) and its appendices map every archived and continuation decision into the ADR and specification layers; [`SETUP_OPTION_REGISTER.md`](SETUP_OPTION_REGISTER.md) classifies retained crisis alternatives.
5. ADRs 0001 through 0009 and the existing Nuclear War Packet remain historical evidence. The locked DATE pivot, not an unreviewed wording change, removes them from active design authority.

An explicit later ADR may supersede a locked requirement. Implementation convenience, a Setup author, or model prose may not.

## Requirements language

- **MUST** and **MUST NOT** define a required design or fail-closed boundary.
- **SHOULD** and **SHOULD NOT** define a default that only a versioned Charter or later ADR may change with a recorded reason.
- **MAY** defines permitted variation inside the frozen World, Charter, Setup, and run identity.
- **LOCKED**, **PROVISIONAL**, **OPEN**, **HISTORICAL**, and **CORRECTED** describe design status, not implementation completion.
- **FACT**, **INFERENCE**, **MEASURED**, and **CLAIM BOUNDARY** describe the evidence supporting a statement.

## Specification modules

| Module | Responsibility |
|---|---|
| [00. U.S.-first minimum design](spec/00-us-first-minimum-design.md) | Focal Room, minimum episode, matched comparison, evidence gate, and claim boundary |
| [01. Authority and scope](spec/01-authority-and-scope.md) | Task, claim boundary, status model, and represented actors |
| [02. World, Setups, and evaluation](spec/02-world-setups-and-evaluation.md) | DATE arena, episode-bounded Core and open ledger, Setup/Seed split, matching, evaluation vectors, and Authored Risk Probes |
| [03. Shared Room contract](spec/03-shared-room-contract.md) | Charter schema, outer cycle, information, activation, groups, and scheduling |
| [04. United States Charter](spec/04-united-states-charter.md) | Dated public roster, objectives, cells, decision routing, and theater commander |
| [05. Himaldesh institution](spec/05-himaldesh-institution.md) | Executive dyad, group topology, registry, activation, and six portfolios |
| [06. Himaldesh Cabinet process](spec/06-himaldesh-cabinet-process.md) | Briefs, products, evidence requests, drafting, review, dissent, and Interior gate |
| [07. Olvana candidate Charter](spec/07-olvana-provisional-charter.md) | Dated source facts, nine-seat candidate, inferred party-NCA path, blocked gaps, and batch-ratification boundary |
| [08. Sources and evidence](spec/08-sources-and-evidence.md) | Public-source facts, design inferences, historical receipts, and non-claims |
| [09. Artifacts, replay, and feasibility](spec/09-artifacts-replay-and-feasibility.md) | Run identity, required artifacts, failure semantics, and measured seams |
| [10. Microsite narrative](spec/10-microsite-narrative.md) | Required presentation of history, decisions, information, and causal replay |
| [11. Open decisions](spec/11-open-decisions.md) | Remaining scientific, World, Olvana, implementation, and publication gates |
| [12. One Room across open and closed Worlds](spec/12-one-room-across-open-and-closed-worlds.md) | Shared U.S. Room identity, typed-Core and open-ledger DATE contract, closed Nuclear War contract, and cross-World claim boundary |
| [13. First-episode default profile](spec/13-first-episode-default-profile.md) | Reversible concrete Road to War, fictional packages and geography, mixed affordances, MSEL clock, Seed, probes, projections, and freeze checks |
| [14. First DATE machine contract](spec/14-first-date-machine-contract.md) | Candidate profile serialization, Core and ledger envelopes, matched template instances, validator order, replay, and the first offline tracer |
| [15. U.S. Charter machine contract](spec/15-us-charter-machine-contract.md) | Source-register and machine-readable Charter envelope, coverage, strict validation, no-model checks, and Milestone 1 gate |
| [16. No-model U.S. Cycle 1 machine contract](spec/16-us-cycle-one-machine-contract.md) | D68 measured development fixture, Watch isolation, graph execution, open product bodies, decision routing, failure receipts, replay, and Milestone 2 receipt |
| [17. Open proposal and consequence bridge](spec/17-open-proposal-consequence-bridge.md) | Original-language proposals, compound effects, bounded clarification, development effect-authority and Core-capability checks, EXCON consequences, D64 admission, and Milestone 3 gate |
| [18. Two-cycle U.S. tracer](spec/18-two-cycle-us-tracer.md) | Exact D68-D69-D64 composition, persistent seat identity and input history, matched weather barrier, Cycle 2 reassessment and decision, final non-action adjudication, terminal versus abort, and replay |
| [19. Minimum Counterpart Rooms](spec/19-minimum-counterpart-rooms.md) | Exact Himaldesh and Olvana source and Charter candidates, actor-specific graphs, blocked source gaps, batch ratification, no-model traces, fixture replacement, and composition gate |

## Current freeze boundary

D54-D61 lock the first episode's two-cycle hybrid pressure, mixed U.S.-Himaldesh weather dependencies, default-authoring process, nuclear-risk subject, and inspectable-authenticity boundary. D62 provisionally fixes the smallest contest-scoped World kernel, distinguishes frozen matched templates from run-bound patch instances, and defines the no-model two-branch tracer. D63 corrects candidate Outcome Projections to deterministic typed Core views so the two-operation patch creates neither stale copies nor hidden writes. D64 supplies the exact mechanical receipt for that candidate transition slice. D65 locks the U.S.-first implementation sequence and lower-level Concordia reuse boundary. D66 supplies the source register, complete machine-readable U.S. Charter candidate, strict compiler, and lossless review surface. D67 ratifies those exact source and Charter hashes through a separate receipt. D68 executes and replays the Charter's deterministic information-to-decision graph against labeled non-evidence fixtures. D69 carries one compound original-language proposal through clarification, effect-level authority and capability checks, EXCON consequence proposal, D64 admission, a blocked dependent effect, and exact replay. D70 composes those exact sources across matched weather, a second cycle of the same U.S. Room, explicit non-action, final consequence, and full replay. D71 presents exact source-bound minimum Himaldesh and Olvana Charter candidates and corrects an Olvana source-drift boundary. D72 ratifies the exact commit and four canonical hashes through a separate receipt. D73 executes and exactly replays both actor-specific graphs as isolated authored no-model fixtures. D74 binds those Room receipts, decision routes, projections, outputs, and causal U.S. Watch inputs into an exact replay of the retained D70 U.S. run, closing deterministic no-model Milestone 5.

The U.S.-first submission focus, Himaldesh-Olvana belligerent pair, `ridge_seizure.limited_fait_accompli` first family, confirmed-seizure and uncertain-intent opening, bounded no-U.S.-combat support request and recapture clock, integrated U.S. Policy Package, actor-specific Rooms, shared outer contract, open DATE proposal and state-bounded consequence path, typed Core plus open ledger, abstract Force Packages, two-cycle hybrid pressure, specialist warning route, paired mixed-ownership weather dependencies, two-family evaluation, Charter-plus-probe grounding, alternative preservation, inspectable-authenticity boundary, and D65 work order are locked. Modules 13-19 supply the provisional World and episode contracts, D64's mechanical receipt, the exact D67-ratified U.S. Charter basis, D68's no-model Cycle 1 controller receipt, D69's no-model proposal-consequence bridge receipt, D70's complete no-model two-cycle receipt, D72's exact counterpart ratification basis, D73's two isolated no-model actor receipts, and D74's exact counterpart-to-U.S. composition receipt. Module 17 uses explicit development-only effect-authority records so implementation can fail closed without pretending the D67-D68 record confirmations establish real effect authority. Module 18 preserves the same fourteen-seat U.S. institution across matched and endogenous Cycle 2 pressure without broadening that evidence. Module 19 preserves different counterpart politics under one strict envelope, blocks unsupported Olvanan strategic routes, and makes exact Room receipts the final counterpart provenance for D70. None is a frozen Setup, model-mediated Room receipt, creative-EXCON receipt, matched comparison, or end-to-end arena receipt. Final effect-level authority and confirmation maps, live proposal extraction and creative EXCON, the compared U.S. condition, final measures and probes, Nuclear War adapter, runtime choice, and end-to-end evidence remain provisional or open. D72-D74 authorize and measure deterministic no-model Milestone 5 work only; they authorize no paid experiment, Packet rewrite, publication, or submission.
