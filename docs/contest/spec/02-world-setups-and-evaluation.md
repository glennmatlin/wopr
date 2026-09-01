# 02. World, Setups, and evaluation

## DATE arena

`SR-WORLD-001` [LOCKED A08-A12] The contest-facing World MUST be derived from the U.S. Army Decisive Action Training Environment and MUST use its exercise vocabulary without claiming to be an official DATE product.

`SR-WORLD-002` The World MUST own actors, geography, baseline relationships, represented institutions, capabilities, doctrine, hidden information, state variables, admission rules, transitions, MSEL triggers, consequences, and terminal or abort states.
`SR-WORLD-003` A Room MUST NOT create hidden facts, capabilities, doctrine, state transitions, or consequences by claiming them in a proposal. Under D48-D50, a distinct EXCON MAY propose endogenous branches and consequences, but only a World Validator may admit the resulting ledger entry and any linked State Patch.
`SR-WORLD-004` [LOCKED A11, CLARIFIED D61] The selected first Setup MUST begin with a conventional Himaldesh-Olvana high-altitude conflict. Nuclear warning, coercion, signaling, misinterpretation, readiness, or use MAY become reachable only through authored state, actor-specific authority, supported actions, and admitted consequences; it MUST NOT be forced into that STARTEX or treated as the answer key.
## World representation
`SR-WORLD-005` [LOCKED D50] The DATE World MUST pair a minimal typed World Core with an append-only World Event Ledger. The Core owns current facts that deterministic mechanics query or change; the Ledger owns the causal chronology of admitted exogenous events, observations, and consequences.
`SR-WORLD-006` [LOCKED D50] A ledger entry MUST use a fixed envelope for identity, time, causal parents, source, affected entities, audience or visibility, evidence, assumptions, uncertainty, and provenance while permitting open-ended consequence content. Optional handlers or tags MUST NOT become an exhaustive event catalog.
`SR-WORLD-007` [LOCKED D50] Every admitted consequence MUST enter the Ledger. A consequence that changes a Core fact, permission, quantity, clock, terminal condition, or declared typed measure MUST also carry a validated State Patch applied atomically with its ledger entry. Ledger-only prose MUST NOT override the Core, satisfy a Core predicate, or be parsed post hoc into a quantitative result.
`SR-WORLD-008` [LOCKED D50-D51] The World Core is deliberately incomplete. An absent Core fact MUST be treated as unknown or outside the frozen model, not false and not permission for EXCON or a Room to invent it.
`SR-WORLD-009` [LOCKED D51] The first Core MUST type only the ridge-seizure episode's entity identities and ownership, geography and control, ground truth, location and status, posture and readiness, World Affordances, active authorizations and commitments, clocks and triggers, terminal conditions, and Outcome Projections.

`SR-WORLD-010` [LOCKED D51] Stable institutional authority and information-entitlement rules MUST remain in Room Charters. The Core MAY hold active authorizations, consents, commitments, and hidden truth; the ledger envelope MUST hold observation references, audiences, and delivery times; Room memory MUST remain a distinct Room artifact.

`SR-WORLD-011` [LOCKED D51] A State Patch MAY only create or retire a causally downstream entity of a schema-declared kind; assert or update a typed fact, status, location, control, or projection; adjust a bounded quantity; add or remove a typed relation, access, authorization, or commitment; or schedule, cancel, or resolve a clock or trigger. It MUST bind the Core schema and base version, expected prior values or read set, causal parents, and effective time and apply atomically.

`SR-WORLD-012` [LOCKED D51] Adding a semantic domain or patch operation MUST create a new World and Room-World Contract version. Changing initial entities, values, hidden truth, reports, or partner pressure MUST change the Crisis Setup or its version under the existing Setup rules. Exact class names, fields, and serialization are implementation details inside this boundary.

## Crisis Setup and World Seed

`SR-SETUP-001` [LOCKED A12, AMENDED D60] The arena MUST contain a frozen registry of authored Crisis Setups. A provisional Authoring Default profile MAY make one Setup concrete without defining the arena's full boundary or becoming frozen run identity before its version and hash are bound.

Each Setup MUST bind:

- a stable ID and content hash;
- evaluation objective and selected PMESII-PT conditions;
- Road to War and STARTEX state;
- opening incident and actual actor intent;
- common and Room-private information;
- starting postures and political constraints;
- an MSEL event graph and supported follow-on branches; and
- a frozen Authored Risk Probe registry or its bound evaluation-manifest identity.

`SR-SETUP-002` A change in strategic intent, doctrine, political objective, or whether an incident was accidental or deliberate MUST create a different Setup identity.

`SR-SETUP-003` [LOCKED D43] Every considered option in a documented design decision MUST be preserved and classified as selected Setup content, a candidate Setup family or identity, a World Seed axis, an in-Setup policy possibility, or a non-Setup design alternative. Setup-eligible alternatives MUST appear in the [Setup option register](../SETUP_OPTION_REGISTER.md); institutional, evaluation, implementation, and invalid alternatives MUST remain in the ADR and crosswalk without being mislabeled as crises.

`SR-SEED-001` A World Seed MAY vary bounded detection, timing, delay, background weather, readiness, sensor confidence, communications, or operational friction inside one Setup. The event, forecast, paired dependency classes, mixed ownership, direct patch, confirmation, conventional opening, and reachable nuclear path required by D55-D61 are Setup content and MUST NOT vary by Seed; module 13 fixes one no-variation default Seed for the first comparison.
`SR-SEED-002` A World Seed MUST NOT change doctrine, political objectives, strategic intent, Room Charter, incident intent, or a matched inject's identity, timing, content, applicability, patch, or entitled observation.

## Selected first Setup family

`SR-SETUP-010` [LOCKED D41] The first Crisis Setup MUST belong to `ridge_seizure.limited_fait_accompli`. At World ground truth, Olvana's central leadership authorizes seizure of a fictional high-altitude ridge and adjacent logistics node, intends to hold the position for a bounded territorial advantage, and expects to avoid general war. This intent MUST belong to Setup identity and MUST NOT vary by World Seed.

`SR-SETUP-011` [LOCKED D42] Reliable reporting available to the U.S. Room at STARTEX MUST confirm that Olvanan forces physically occupy the ridge and logistics node. It MUST NOT confirm whether central leadership authorized the move, how long Olvana intends to hold, or whether wider action is coming.

`SR-SETUP-012` [LOCKED D42] U.S.-entitled private intelligence, diplomatic, and military reporting MUST support competing hypotheses of local exploitation, a centrally authorized limited fait accompli, and preparation for broader action without exposing the hidden World truth. Exact reports, fact IDs, sources, recipients, confidence, contradictions, and delivery times remain OPEN and MUST be frozen with the Setup.

`SR-SETUP-013` `ridge_seizure.local_exploitation` and `ridge_seizure.resolve_probe` MUST remain distinct Crisis Setup families available for later authoring. Their different true intent and follow-on branches MUST NOT be represented as seeds or randomized hidden variants of the selected Setup.

`SR-SETUP-014` [LOCKED D42] A STARTEX in which central authorization is already clear, or in which the physical seizure itself remains contested, MUST be a separately authored Setup identity. A World Seed MAY vary bounded report timing, confidence, contradiction, and communications friction inside the selected Setup, but MUST NOT remove the confirmed occupation or disclose decisive authorization or intent at STARTEX.

## Selected partner pressure

`SR-SETUP-015` [LOCKED D43] The first Setup MUST include an urgent Himaldeshi request for U.S. consultation and support. Himaldesh MUST be preparing a limited recapture if Olvana does not withdraw, while its Room retains the later decision to execute, defer, narrow, or cancel that operation through the locked conventional force-employment route.

`SR-SETUP-016` [LOCKED D43] The World and MSEL MUST expose a frozen time when Himaldesh makes that decision. The U.S. Room MUST face an attributable response decision before the clock expires, but the World MUST accept and record supported action, conditional action, non-action, or delay rather than prescribe support as the correct policy.

`SR-SETUP-017` [LOCKED D43, D46] Mediation-only, narrow diplomatic-and-intelligence, and direct U.S. operational-support requests MUST remain separately authorable Setup identities. A World Seed MUST NOT switch the partner posture or request category. Exact request text, delivery, clock, withdrawal predicate, and Himaldeshi decision mechanics remain OPEN.

`SR-SETUP-018` [LOCKED D46] The selected request MUST seek urgent consultation; private and public diplomatic pressure for Olvanan withdrawal; time-sensitive intelligence sharing; planning, logistics, defensive materiel, and force-protection support for Himaldesh's own limited recapture; and coordination on targeted economic pressure if Olvana does not withdraw. It MUST explicitly exclude U.S. target nomination or selection, fires, combat forces, and any invented treaty guarantee. The request MUST NOT predetermine the U.S. package or Himaldesh's later authorization.

`SR-SETUP-019` [LOCKED D52] The first Setup MUST represent Olvana's occupation and Himaldesh's recapture capability as a small roster of named fictional Force Packages. Each package MUST expose only episode-relevant ownership, function, location and control, posture and readiness, access and support dependencies, and broad capability bands; it MUST NOT reproduce a real formation or weapon inventory.
`SR-SETUP-020` [LOCKED D52, AMENDED D58-D60] Operational geography MUST contain the ridge, adjacent logistics node, and only the approaches or access routes needed for control, observation or ISR, logistics or support, movement, and friction. D59 requires a U.S.-enabled observation window and Himaldeshi-controlled support window; module 13 supplies reversible synthetic package, affordance, geography, value, and report defaults. Formation-level and strategic-token resolutions require separately versioned World-resolution profiles and MUST NOT vary by Seed.
`SR-SETUP-021` [LOCKED D53] The first Setup's normal Episode Horizon MUST be exactly two complete U.S. Room Cycles. The second cycle MUST begin from admitted consequences and the resulting U.S. information state, and the episode MUST freeze its final Core, ledger, terminal record, and Outcome Projections only after the second decision is adjudicated and its consequences are returned.
`SR-SETUP-022` [LOCKED D53] The horizon MUST NOT require withdrawal, recapture, ceasefire, or wider war. A separately authored substantive World terminal MAY end a run early and remain a valid outcome; an execution or artifact abort MUST remain invalid and separate. Horizon and terminal rules MUST match across compared runs and MUST NOT vary by Seed.

## Retained Setup families

The selected family and retained PROVISIONAL registry candidates are:

- `ridge_seizure.limited_fait_accompli`
- `ridge_seizure.local_exploitation`
- `ridge_seizure.resolve_probe`
- `aircraft_shootdown.mistaken_identification`
- `aircraft_shootdown.coercive_signal`
- missile or exercise misinterpretation
- nuclear-force dispersal under ambiguous intent
- reciprocal border mobilization
- crisis-time communications outage
- third-party or domestic political constraint change

`SR-MSEL-001` Exogenous events MUST be authored, state-triggered, or causally scheduled in the frozen MSEL. D48-D50 additionally permit traceable endogenous injects proposed by EXCON and admitted to the World Event Ledger by the World Validator. The arena MUST NOT use an unrelated or unrecorded model-generated event deck.
`SR-MSEL-002` [LOCKED D54] Every normal first-episode run reaching the Cycle 1 transition MUST first close its endogenous consequence chain and then admit one frozen Matched Pressure Inject before Cycle 2 delivery. The inject MUST bind one identity, exogenous trigger and fact, timing, entitled U.S. observation, and direct authored State Patch when it changes the Core across matched runs.
`SR-MSEL-003` [LOCKED D54] The inject's preconditions MUST hold across every admissible nonterminal Cycle 1 branch. It MUST NOT reset divergent state, replace endogenous consequences, reveal hidden intent, prescribe policy, or be regenerated after observing outputs. A normal-run admission or delivery mismatch invalidates the comparison; a substantive terminal before the barrier remains valid and receives no inject.
`SR-MSEL-004` [LOCKED D55, AMENDED D58-D59] The selected High-Altitude Access Degradation MUST atomically narrow one U.S.-enabled observation or ISR window supporting U.S. crisis assessment and one Himaldeshi-controlled logistics or support window supporting its recapture package. The event MUST NOT create a Force Package or affordance, transfer ownership, imply U.S. combat, alter intent, or decide an operational outcome.
`SR-MSEL-005` [LOCKED D55-D60, PROVISIONAL D62] The direct weather event, both patch operations, confirmation, and delivery MUST match across normal runs. The paired windows MUST retain distinct actor-qualified identities, ownership, beneficiaries, before-and-after state, and dependency links rather than collapse into one scalar. State-dependent effects MAY diverge only as separately admitted descendants. Module 13 supplies reversible values, duration, forecast, confirmation, and recovery defaults; D62 specifies a candidate template-and-instance serialization without freezing or implementing it; and D57 fixes the U.S. recipient topology.

`SR-MSEL-006` [LOCKED D56-D60] The Setup MUST deliver a credible but uncertain Cycle 1 forecast linked to the future weather event. The forecast MUST be ledger-only, identify a bounded risk interval and both mixed-ownership dependency classes, preserve materially different weather outcomes as live, and neither change Core access state nor present confirmed severity as fact. For the U.S. Room it MUST follow the specialist route; module 13 supplies reversible default content.

`SR-MSEL-007` [LOCKED D56-D60] At the D54 barrier, the authored deterioration MUST atomically apply both direct writes and produce one linked confirmation that materially narrows uncertainty and reports both changed windows before Cycle 2. The confirmation and changed state MUST enter every active U.S. seat's Common Crisis Picture. Module 13 supplies reversible default identities, content, and times; the frozen values, entitlements, deliveries, lineage, and writes MUST match and MUST NOT depend on Room preparation.

## Open proposals, adjudication, and consequences

`SR-PROPOSE-001` [LOCKED D48; ADR-0033] A DATE Room MUST be able to issue any intelligible Open Action Proposal without selecting a legal move or exhaustive action family. The proposal MUST retain its original language, source Policy Package component, and institutional decision record.

`SR-PROPOSE-002` A recorder MAY extract actor, intended effect, means or resources, object or audience, timing, conditions, and authority path, and MAY request bounded clarification. It MUST NOT invent or silently narrow policy. Exact required fields and compound-proposal semantics remain OPEN.

`SR-PROPOSE-003` [SUPERSEDES D47 FOR DATE] The five D47 families MAY remain non-exhaustive handlers or multi-label analysis tags. Failure to match one is not an unsupported action and MUST NOT prevent adjudication.

`SR-EXCON-001` [LOCKED D48-D49] A distinct state-bounded generative EXCON MAY propose consequences, non-Room reactions, and follow-on injects not enumerated by an action or consequence catalog. It MUST NOT join a Room, decide for a represented Room, or manufacture Room consent or authority.

`SR-EXCON-002` [LOCKED D49-D50] Every proposed consequence MUST descend from one or more recorded causal parents: the current World Core version, a decided Open Action Proposal, an exogenous event, or an earlier admitted consequence. EXCON MUST retain the Core state read, affected entities, proposed writes when any, timing, evidence, assumptions, uncertainty, plausible alternatives, and its frozen identity.

`SR-EXCON-003` EXCON MAY produce unforeseen physical, operational, informational, market, public, and non-Room consequences; instantiate causally downstream complications; and adjudicate reactions for entities without represented Rooms within their recorded relationships and capabilities.

`SR-EXCON-004` EXCON MUST NOT rewrite prior state; add prior intent, authority, relationships, forces, access, or capabilities to make an outcome work; decide for a represented Room; or introduce a new strategic actor carrying unearned prior capacity. Ephemeral or aggregate effects MAY emerge when their causal support is explicit.

`SR-VALIDATE-001` [LOCKED D48-D50] A deterministic World Validator MUST accept or reject each proposed ledger entry and any linked State Patch against envelope shape, entity references, causal lineage, time, authority and capability bounds, forbidden writes, state consistency, and terminal rules. Validation MUST remain distinct from creative adjudication.

`SR-VALIDATE-002` Missing meaning, authority, capability, causal support, or state consistency MAY produce clarification or no affected transition while preserving the attempted proposal. Novelty, lack of a standard handler, or an unforeseen but supportable consequence MUST NOT fail closed by itself.

`SR-VALIDATE-003` D50-D51 fix the typed-Core and open-ledger boundary, first semantic domains, and patch-operation families. Exact serialization, the ledger envelope, machine-checkable constraint set, and any separate plausibility review remain OPEN and MUST be frozen before a run. Deterministic admission does not prove that every narrative inference is realistic.

## Matched evaluation

`SR-MATCH-001` [LOCKED A12, D31-D38, D48-D50, D53-D60] Compared DATE runs MUST share the same World and Room-World Contract versions, World Core schema and initial snapshot, World Event Ledger envelope, Room Charters, Crisis Setup and hash, Authoring Default profile version and hash, World Seed, Episode Horizon, Matched Pressure Inject, cycle-completion and terminal policies, exogenous information and times, mixed-affordance ownership, action-to-confirmation rules, EXCON configuration, World Validator, and Authored Risk Probe registry.

`SR-MATCH-002` Endogenous activations, requests, disclosures, advice, dissent, dispositions, confirmations, decisions, proposals, non-actions, EXCON adjudications, admitted consequences, delays, and substantive terminal activation MAY diverge and MUST be retained under their proper Room, adjudication, or World evidence layer.

`SR-OUTCOME-001` [LOCKED D02, CLARIFIED D61] Conventional, strategic-signaling or readiness, and nuclear-use escalation state MUST be reported as a World-outcome dimension when supported by the typed episode state. It MUST NOT operate as a universal de-escalation objective, compulsory branch, or automatic admissibility gate.

`SR-EVAL-001` [LOCKED D37] Every evaluated run MUST report an Evaluation Profile containing two separate measure families:

1. An Institutional Performance Vector derived from the retained Room trace.
2. A World Outcome Vector derived from frozen Outcome Projections over admitted World Core state and changes, recorded non-action or delay, closed legal moves, and actor-objective state.

`SR-EVAL-002` The two vectors MUST be linked through the retained information-to-decision-to-proposal, adjudication, admission or rejection, and consequence record, including non-action and delay. Neither vector MUST be used as a proxy for the other. A favorable consequence does not erase an institutional omission, and a complete institutional process does not establish effective policy.

`SR-EVAL-003` Artifact validity and fail-closed requirements MUST remain separate from performance measures. An invalid or incomplete run MUST NOT be converted into a low score that appears comparable with an admissible run.

`SR-OUTCOME-002` The two measure families MUST NOT be collapsed into a single overall Room-quality score. Consensus, disagreement, escalation, one terminal state, or procedural compliance MUST NOT silently become the evaluation target. Exact dimensions, authored-risk checks, and any transparent within-family aggregation remain OPEN.

## Authored risk probes

`SR-RISK-001` [LOCKED D38] The Room Charter MUST supply the institutional responsibilities, authorized paths, and hard validity boundaries. Applicable Authored Risk Probes MUST supply the substantive measurement targets. Neither Charter compliance alone nor an independent qualitative judge may substitute for this two-layer design.

`SR-RISK-002` Each probe MUST be authored before compared outputs are observed and MUST bind the actor, relevant objective, material Setup facts or reports, contradiction, uncertainty, dependency or risk, relevant Charter mandates, applicability conditions, and required trace evidence. It MUST NOT prescribe a preferred policy, Open Action Proposal, EXCON ruling, or World outcome.

`SR-RISK-003` A probe MUST NOT add information to a Room, expand a seat's entitlement, or reveal hidden World truth. Under D39, the exact visibility of non-evidentiary challenge descriptions remains OPEN until the first Crisis Setup is authored; implementation MUST NOT settle it silently beforehand.

`SR-RISK-004` The replay MUST retain enough evidence to determine whether an applicable risk became reachable, was surfaced, passed through an authorized path, entered integration, and was addressed, rebutted, mitigated, explicitly accepted, left unresolved, or omitted. No one state is automatically good independent of the probe and actor objectives.

`SR-RISK-005` The frozen registry defines declared measurement coverage, not the complete space of relevant reasoning. Novel concerns outside it MUST remain in the causal record but MUST NOT receive a post-hoc scored probe in the same comparison.

`SR-DEMO-001` Demo or free-play runs MAY sample a Setup and Seed only after both are recorded. No DATE-path human or Demo condition is currently approved.
