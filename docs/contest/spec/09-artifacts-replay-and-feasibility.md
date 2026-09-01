# 09. Artifacts, replay, and feasibility

## Run identity

`SR-RUN-001` A replayable run MUST bind at least:

- World version and content hash;
- Crisis Setup ID, version, and hash;
- Authoring Default profile ID, version, and content hash;
- World Seed and deterministic random-state policy;
- all three Room Charter IDs, versions, and hashes;
- Authored Risk Probe registry or evaluation-manifest ID, version, and hash;
- seating, model/provider configuration, decoding parameters, and prompt or persona hashes;
- Room-World Contract, World Core schema, semantic domains, Force Package resolution and roster, patch operations, and initial snapshot, World Event Ledger envelope, State Patch schema, proposal recorder, state-bounded EXCON, World Validator, and any non-exhaustive handler or closed legal-move catalog versions;
- executor release;
- Episode Horizon, Matched Pressure Inject and High-Altitude Access Degradation forecast-to-confirmation content, U.S.-enabled observation or ISR and Himaldeshi-controlled logistics or support affordance identities, ownership, beneficiaries and patch contract, U.S. specialist warning route and product contract, cycle-completion, substantive-terminal, run-abort, input, retry, budget, timeout, and terminal-policy versions.

Changing any bound item creates a different run identity. A path, branch name, or `latest` label is not an identity.

## Required causal artifacts

`SR-RUN-010` The replay bundle MUST retain:

1. Road to War, STARTEX, initial fictional Force Package and operational-map state, common and private fact records, and each delivery audience and time.
2. Seat activation and suppression events with predicate and cause.
3. Per-seat authorized inputs, persistent-memory lineage, calls, outputs, provider attempts, and failures.
4. Group dependencies, start barriers, isolated traces, canonical collection order, and products.
5. Disclosures, evidence requests, access decisions, and recipient-memory updates.
6. Portfolio Products, cell products, Policy Package drafts, reviews, dissent, dispositions, executive decisions, and confirmations.
7. Original Open Action Proposals or closed legal moves, minimal envelopes, clarifications, authority records, and non-action or failed-admission records.
8. EXCON consequence proposals, causal parents, Core reads and proposed writes, affected entities, evidence, assumptions, uncertainty, and alternatives; proposed State Patches with base version, read set, operations, and preconditions when required; World Validator results; admitted World Event Ledger entries, before-and-after Core versions, MSEL events, delays, and terminal or abort record.
9. Authored Risk Probe registry, applicability decisions, probe-to-trace links, Institutional Performance Vector, World Outcome Vector, cost and token accounting, and every declared non-measure.

The bundle MUST preserve policy language, proposals or legal moves, creative adjudication, deterministic admission, and resulting state as distinct layers. A transcript without state, or state without its institutional path and adjudication receipt, is insufficient.

`SR-RUN-011` [LOCKED D44, D48] The replay MUST identify the U.S. Policy Package version decided before the partner clock, distinguish immediate from conditional components, and link every component to its evidence, hypotheses, triggers, dependencies, safeguards, authority path, consultations, confirmations, dissent, disposition, reassessment point, and Open Action Proposal or recorded non-action. A failed-admission component and the proof used to separate any continuing component MUST remain inspectable.

`SR-RUN-012` [LOCKED D45] The replay MUST retain all six policy-domain dispositions, including the contributing seats, deciding forum, reason, and any no-action or not-applicable record. An omitted domain MUST remain a visible package-completeness failure rather than disappear from the artifact bundle.

`SR-RUN-013` [LOCKED D46] The replay MUST retain each requested support category, each explicit exclusion, the exact request version, delivery audience and time, and the U.S. disposition linked to every item. It MUST distinguish the partner's request from a decided U.S. proposal and from an admitted World effect.

`SR-RUN-014` [LOCKED D48-D50, SUPERSEDES D47 FOR DATE] The DATE replay MUST retain each proposal's original language, source package component or components, minimal envelope, authority path, clarification exchange, any non-exhaustive handler or analysis tags, EXCON causal account and consequence proposal, validator result, admitted ledger entry, and any linked State Patch and Core transition. Novel proposals, rejected consequences, and rejected patches MUST remain traceable even when no effect is admitted. No-action and not-applicable dispositions remain package records with no fabricated proposal or action ID.

`SR-RUN-015` [LOCKED D53] The replay MUST mark both U.S. Room Cycle boundaries; bind each cycle's input picture, work products, decision, proposals or non-action, adjudication, consequences, and returned information state; and retain the Cycle 2 reassessment links to changed evidence, state, dependencies, and risk. It MUST distinguish normal two-cycle completion, an early substantive World terminal, and an invalid run abort.

`SR-RUN-016` [LOCKED D54, CLARIFIED D62] The replay MUST identify the Matched Pressure Inject's frozen event, trigger, exogenous fact, timing, observation, applicability, direct patch and validator result when required, and delivery record separately from every endogenous Cycle 1 consequence. It MUST prove common event-template, patch-template, ordered-operation, observation, and delivery bytes and timing across normal matched runs while retaining divergent state and consequence lineage. Run-bound ledger and patch instances MAY differ only in declared run identity, sequence, current Core version and hash, derived instance ID, before-and-after identity, and receipt fields.

`SR-RUN-017` [LOCKED D55, AMENDED D58-D59] The replay MUST identify the weather source and event; the U.S.-enabled observation or ISR and Himaldeshi-controlled logistics or support affordance IDs, owners, beneficiaries, dependencies, before-and-after windows or reliability bands, patch operations and preconditions; atomic validator result; forecast and confirmation history; recovery clocks; entitled observation and delivery; and every divergent state-dependent descendant. It MUST distinguish the selected authored inject from background Seed friction and MUST NOT imply U.S. combat participation.

`SR-RUN-018` [LOCKED D56, AMENDED D58-D60] The replay MUST show the Cycle 1 forecast as a ledger-only observation with uncertainty, bounded risk interval, both mixed-ownership dependency classes, entitlement, delivery, and no Core transition; then link it to the barrier weather event, atomic paired State Patch, materially narrower confirmation, and Cycle 2 delivery under the frozen module 13 profile. Any profile, matched-stage, or direct-write mismatch MUST remain an invalid comparison artifact.

`SR-RUN-019` [LOCKED D57-D59] The replay MUST retain the raw forecast observation and specialist recipients; Threat and Attribution assessment of the U.S.-enabled observation window; Defense and Escalation assessment of the Himaldeshi-controlled support window; theater-commander activation; each product's fact links, confidence, gaps, dissent, and omissions; Presidential Synthesis and senior-forum inputs; every logged raw-report retrieval; and delivery of the linked two-window confirmation through the Cycle 2 Common Crisis Picture. A controller repair MUST remain distinguishable from model-mediated work and invalidates the selected route.

## Determinism and failure semantics

`SR-RUN-020` The controller MUST collect independent work in frozen Charter order, not provider completion order. Logical replay order, seat memory, and dependencies MUST match the declared serial graph even when calls run concurrently.

`SR-RUN-021` Retries, timeouts, clarification caps, review caps, and call budgets MUST be frozen before a run. A retry is retained as an attempt; it does not overwrite the failed call. Exhaustion MUST produce an explicit failure state.

`SR-RUN-022` Invalid output, missing product, missing review, unresolved meaning, absent authority or confirmation, unsupported capability, invalid ledger envelope, invalid State Patch, memory aliasing, trace aliasing, or dependency on the legacy three-member C2 artifact MUST fail closed for the affected effect. The proposal remains evidence, and novelty alone is not invalid. The World MAY advance time and admitted delay consequences.

`SR-RUN-023` Concurrent calls MUST receive separate mutable call-budget objects and MAY share only synchronized study-level cost accounting. Every logical call, provider attempt, token bound, and reservation MUST be attributable.

`SR-RUN-024` [LOCKED PROCESS D60] The replay MUST expose the exact module 13 profile version and hash, every value that differed from the prior profile version, the reason and pre-output time of change, and the final freeze receipt. A bound value changed after outputs invalidates the comparison; an implementation convenience MUST NOT become an unrecorded default.

## Verified reusable seams

The preserved 2026-08-24 offline probes are MEASURED only at these seams:

- Concordia 2.4.0 constructed six distinct entity, memory, and log objects; six workers completed two calls per seat without cross-seat aliasing.
- An ordered coordinator accepted six speaker IDs and returned them in declared order.
- Six portfolio entities retained one common token and only their assigned private token after correction of a probe-shape assertion error.
- A persistent Prime Minister memory received one controller-granted Finance disclosure without broadcasting it to Interior.
- Targeted Finance, Infrastructure, and Humanitarian reviews ran with different delays and were collected in Charter order while unaffected Interior received no call.
- Forty-three focused native-entity, runtime, coordinator, parity, and budget tests passed in the bounded audit.

`SR-FEAS-001` These receipts establish reusable entity isolation, persistence, selective delivery, bounded scheduling, and ordered collection. They do not establish the exact schemas, registry compiler, access resolver, material-change detector, Open Action Proposal path, state-bounded EXCON, World Core, World Event Ledger, State Patch, World Validator, DATE World, outcome validity, model quality, or end-to-end Room.

`SR-FEAS-002` [MEASURED CLOSED-WORLD BASELINE] Existing code represents Nuclear War legal actions with a stable ID, type, and payload; the current Concordia decision seam accepts only a finite legal ID and fails after bounded invalid responses; replay validation links the selected ID to the applied action. Eleven focused action-selection, trace-link, and replay tests passed on 2026-08-25. This supports D48's closed Nuclear War contract and reusable trace seams. It does not establish an Open Action Proposal adapter, creative EXCON, World Validator, DATE consequences, or an end-to-end DATE episode.

`SR-FEAS-003` [HISTORICAL ARCHITECTURE INSPECTION] The existing Nuclear War engine stores mutable typed `GameState` and `PlayerState` dataclasses, serializes frozen `EngineEvent` records into an ordered JSON replay, rejects unknown event types and invalid payload shapes, checks references and nondecreasing turns, and binds rule traces to declared actions and events. These were reusable patterns consistent with D50-D52, but the inspected closed engine itself contained no DATE World Core, open World Event Ledger, generic State Patch, episode-affordance or Force Package schema, or D49-D52 validator. D64 implements the first DATE transition slice in a separate contest-scoped package rather than changing that engine.

`SR-FEAS-004` [PARTIAL, MEASURED THROUGH D74] D64 measures the candidate forecast, branch, paired-weather patch, confirmation, projection, validator, and replay path described in `SR-FEAS-005`. D67-D70 add one source-bound U.S. institution and a deterministic no-model two-cycle composition across that World. D72 ratifies structurally checked counterpart source and Charter candidates, D73 executes both actor graphs as isolated authored no-model fixtures, and D74 composes their exact receipts into D70. Live Room judgment, creative EXCON, the reachable nuclear-escalation path, Setup freeze, and comparative quality remain unmeasured.

`SR-FEAS-005` [MEASURED MECHANICAL SLICE D64] Module 14 and `DATE_PROFILE.candidate.json` fix a candidate Core, derived Outcome Projections, event and patch templates, run-bound instances, semantic operations, canonical identity, validation order, reason codes, and two-branch tracer. Candidate version `0.1.1` hashes to `64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477`; its fresh-process receipt hashes to `4a582d72b6d8ff753c3e06adea4d36aef3c3b39b5284e4050ce9ed35e39815e3`. This implements the first mechanical transition slice only; it is not evidence that the candidate is frozen or that a Room, Open Action Proposal, creative EXCON consequence, or end-to-end DATE episode executes.

`SR-FEAS-006` [INSPECTED D65] Concordia's lower-level entity, persistent-memory, response, client, trace, and call-budget seams are eligible for narrow reuse. The legacy faction council, press-round coordinator, player-seat harness, and closed legal-action path do not implement a Room Charter graph and MUST NOT be counted as the U.S. Room controller or counterpart evidence.

## Required first tracer

`SR-FEAS-010` Before claiming the D71 Himaldesh candidate executable, an offline tracer MUST:

1. construct all eleven persistent seats and six distinct portfolio products from one ratified Charter;
2. activate a subset without inventing personas or treating absence as consent;
3. deliver common and seat-private inputs with no leakage;
4. run disjoint work concurrently and serialize shared seats;
5. merge in Charter order while preserving missing and dissenting products;
6. account for calls, attempts, tokens, and cost without mutable-budget aliasing;
7. fail closed on an invalid product, missing required review, memory or trace alias, activation error, or dependency on the legacy three-member schema.

Only an intrinsic count, isolation, memory, trace, or coordination failure after bounded repair activates the approved five-portfolio fallback. Failure of the old C2 artifact is expected and does not qualify. Module 19 additionally requires the Command and Cabinet separation, one Defense identity, Joint Executive route, local Interior gate, blocked direct force employment, and exact fixture-replacement composition.

`SR-FEAS-011` Before claiming the D50-D52 World executable, an offline tracer MUST construct one frozen first-episode Core with the selected fictional Force Package abstraction; admit a ledger-only observation without a Core write; accept one valid package-state patch; reject a stale base version, failed precondition, arbitrary path, undeclared domain or operation, retroactive time, and unearned package, actor, access path, or capability; and reproduce the final Core and ledger from the retained artifacts.

`SR-FEAS-012` Before claiming D53 executable, an offline tracer MUST produce two distinct U.S. Room Cycle records; return Cycle 1 consequences into authorized Cycle 2 inputs and persistent memories; link the second decision to changed evidence and state; adjudicate that decision; freeze and replay the final artifacts; and distinguish a substantive early terminal from an invalid run abort.

`SR-FEAS-013` Before claiming D54 executable, an offline tracer MUST admit the same frozen Matched Pressure Inject after two different valid Cycle 1 consequence paths; preserve common and endogenous provenance separately in Cycle 2 inputs; reject a precondition or delivery mismatch as an invalid comparison; and suppress the inject only after a valid substantive terminal.

`SR-FEAS-014` Before claiming D55 executable, that tracer MUST apply the same frozen High-Altitude Access Degradation event, direct patch, observation, and delivery after both paths; change only a predeclared environmental or access constraint; retain different downstream effects when state differs; distinguish the authored event from Seed weather friction; and replay the resulting Cycle 2 inputs.

`SR-FEAS-015` Before claiming D56 executable, that tracer MUST deliver the same uncertain forecast to both paths; prove it creates a ledger entry without a Core change; apply the same linked barrier event and patch; deliver a materially narrower confirmation; retain different downstream exposure when state differs; and reject any identity, content, entitlement, timing, delivery, or lineage mismatch.

`SR-FEAS-016` Before claiming D57 executable, that tracer MUST deliver the raw forecast only through the selected specialist entitlement path; serialize Threat and Attribution before Defense and Escalation; activate one persistent theater-commander seat; carry both attributable products and source links into Presidential Synthesis and the senior forum; preserve a valid substantive omission without controller repair; support logged raw-report retrieval; deliver the confirmation as common Cycle 2 information; and reject a recipient, dependency, product, activation, retrieval, or common-delivery mismatch.

`SR-FEAS-017` Before claiming D58-D60 executable, that tracer MUST construct one U.S.-enabled observation or ISR affordance for U.S. crisis assessment and one Himaldeshi-controlled logistics or support affordance for its recapture package from the frozen module 13 profile; atomically apply both writes against the same base Core after two valid Cycle 1 branches; reject either failed precondition without a partial change; preserve ownership, beneficiaries, values, dependency links, and descendants; reproduce the same direct state and ledger across matched runs; and bind the profile version and hash.

`SR-FEAS-018` [PASSED MECHANICAL D64] A fresh-process offline tracer loaded the module 14 candidate hash; admitted the forecast without a Core change; created two distinct valid package-readiness branches; instantiated the same paired-weather template against each branch's actual current Core; proved identical ordered operations, atomic writes, branch retention, linked confirmation, and correctly derived affordance projections; exercised every declared reason-code family; and reconstructed both final Core, ledger, and projection results from retained artifacts. [`DATE_TRACER_RECEIPT.json`](../DATE_TRACER_RECEIPT.json) binds executor `c7d57167bb1ab219b8e3e3a128866b71699e9977` and receipt hash `4a582d72b6d8ff753c3e06adea4d36aef3c3b39b5284e4050ce9ed35e39815e3`. This satisfies no later institutional or Room gate in `SR-FEAS-010` or `SR-FEAS-012` through `SR-FEAS-017`.

`SR-FEAS-019` [PASSED CONTROLLER D68] A fresh-process no-model tracer loaded the exact D67 source, Charter, and ratification identities; delivered twelve authored Watch inputs under selective entitlements; scheduled fourteen active seats across seven Charter-derived waves; retained eight attributable products, the six-domain Policy Package, presidential route, NSC record, and two record confirmations; exercised fail-closed and independent-branch behavior; and reproduced the run exactly. [`US_CYCLE1_RECEIPT.json`](../US_CYCLE1_RECEIPT.json) binds reviewed executor `6c06ed4a7e362cdee89ca15df7aff385aec0aaf8` and receipt hash `7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186`. This satisfies no model-mediated Room, proposal, effect-authority, World, counterpart, Cycle 2, matching, or end-to-end gate.

`SR-FEAS-020` [PASSED BRIDGE D69] A fresh-process no-model tracer loaded the exact D68 receipt and D64 profile; retained one original-language compound proposal and two authored effects; resolved one declared timing field without rewriting policy; required separate development authority and typed Core capability; admitted one ledger-only EXCON consequence; retained one unresolved dependent effect without a World transition; and replayed the run exactly. [`US_PROPOSAL_BRIDGE_RECEIPT.json`](../US_PROPOSAL_BRIDGE_RECEIPT.json) binds executor `1b912ff693a84c5e1081fc76d1ed1f71e4f810aa`, fixture hash `4b47bc86dad3226692146cc92b21f7b3da61a5919b87ce26924514d7f44ce465`, run hash `d43ad8544af90f8e44736133c11b6e8443275c901049ffb0800efd2e0978b996`, and receipt hash `cf78c92190e8b2739923c0977a0af316b332643b563d0ad4818b13048c726ec4`. This satisfies no model quality, official effect authority, creative EXCON, Cycle 2, counterpart, matching, or end-to-end gate.

## End-to-end claim gate

`SR-FEAS-021` A DATE Room is not `runnable`, `demonstrated`, or `evaluated` until a frozen run manifest, complete proposal-adjudication-validation replay bundle, and declared outcome extraction all succeed. D53's contest demonstration additionally requires one receipt-complete matched comparison in which both U.S. conditions complete two Room Cycles; every predeclared early substantive terminal remains valid run data but does not replace that evidence. D61's authenticity target may be explained from design artifacts, but comparative quality, predictive realism, and execution claims require their own evidence. The exact replay verifier remains OPEN. Local schema tests, individual model calls, a published branch, or a partial artifact are not completion evidence.

`SR-FEAS-022` [PASSED TWO-CYCLE TRACER D70] A fresh-process no-model tracer reran the exact D68 cycle and D69 bridge in a fresh D64 World; retained the admitted endogenous consequence and blocked transmission; applied the exact current-Core-bound matched weather event, paired patch, and confirmation; delivered separate matched and endogenous provenance to the same fourteen-seat U.S. institution; produced an exact-state-bound Cycle 2 reassessment and second decision; admitted final non-action without a Core write; and replayed the complete episode exactly. [`US_TWO_CYCLE_RECEIPT.json`](../US_TWO_CYCLE_RECEIPT.json) binds executor `67e8ec51281466aacb7b907c1c6212dde817e7c0`, episode fixture hash `2a7d484d4096e598cee64cbf30c60344c3cca57a7f9cf52f384e6b0ce8f94e66`, run hash `83a143f8712d9b6d012b6dde2f03940062f63b961ad68ccf5bb3b3ae25660597`, and receipt hash `7e5dbd8216d9ea9abc55cc457ceae3df44e3ee4192459012a5459944bddfe6ee`. This satisfies no live model, Counterpart Room, creative EXCON, matched-comparison, evaluation, or public-result gate.

`SR-FEAS-023` [PASSED CANDIDATE AUDIT D71] Strict JSON and a no-model audit pass for both exact source and Charter bundles. The audit verifies canonical and actor identity, bidirectional evidence references, identity uniqueness, source-hash binding, seat-group reciprocity, permission and entitlement closure, acyclic dependencies, route and confirmation ownership, blocked-gap closure, and absence of hidden World entitlements. It is candidate-structure evidence only; actor traces, fixture replacement, D70 composition, and fresh-process replay remain open under module 19.

`SR-FEAS-024` [RATIFIED D72] The exact-binding test first failed because no counterpart ratification receipt existed, then passed after the receipt bound remote candidate commit `8d65a6e05ed264193ddda3fbd5daea7bc1c88dee` and all four D71 canonical hashes. The receipt hashes to `bbab62ea681f2e513407b926de5adfbfaeb8e73baf5fb86ea34808b9fa524384`. This closes only the implementation-basis gate.

`SR-FEAS-025` [PASSED ISOLATED COUNTERPART TRACES D73] Two fresh-process tracers load exact source, Charter, D72 ratification, development fixture, and executor identities; retain authorized deliveries, Charter-order waves, products, decisions, confirmations, local failures, and output mappings; and replay exactly. Himaldesh binds fixture `d6f9eb6a546cdf5d6d512511eef8c46c4da0d2c9175e28c7c080ce5d385b406c`, run `4a1c917aa4e45bbd009bb1fe008ceb932997716c60b759b5160944327714a38b`, and receipt `98a006d17fe23c40d80ec6804da45a192106363d8b03fc7b096ce79d3cbfefc9`. Olvana binds fixture `a922444f415f0b592e5a657f2940524b6f01276c85a3280cb60782f5e8fc1a4b`, run `c6d212f7ed80ab77c2241920ec574d8577d7746a8e68f8ccef852bd3ad392a3a`, and receipt `5586513c594acd6d4acab97978b2624c2917a6a8d49bb81be55818b3c433d547`. These receipts do not satisfy model, World-effect, D70 composition, episode, authenticity, nuclear-behavior, comparison, or public-result gates.

`SR-FEAS-026` [PASSED COUNTERPART COMPOSITION D74] A fresh-process tracer loads both exact D73 Room receipts and exact D70; validates every source, Charter, Room fixture, Room run, decision route, projection, source decision, output byte, and U.S. Watch causal binding; rejects either historical fixture as final Room provenance; reruns the exact D70 run; and replays the composed receipt. [`COUNTERPART_ROOM_COMPOSITION_RECEIPT.json`](../COUNTERPART_ROOM_COMPOSITION_RECEIPT.json) binds executor `ace150092f513b11d57c75cca92b52bbc8aca652`, fixture hash `7a4aa15f1c3d93ee1f100c64ae06c3cb03093697e35f152651933aed6170bb37`, run hash `f4c6a2c9024eb7d0d1f00d0fc0cb4a1b2ab195827bc769f378b50b5429d258ef`, and receipt hash `4bc80ae10937fdc511451cd2b3df452604b6bc1c1c3ab709c1a810a71f67d0c0`. This satisfies no model, creative EXCON, World-effect, nuclear-behavior, matching, evaluation, authenticity, or public-result gate.
