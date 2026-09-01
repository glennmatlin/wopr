# 06. Himaldesh Cabinet process

Status: LOCKED through D36; D72 ratifies the exact serialized process, D73 mechanically executes its authored path, and D74 composes the resulting request into D70

The entire information, drafting, review, dissent, and confirmation procedure in this module is a WOPR design inference from DATE-supported functions. DATE does not publish this machine-operated Cabinet procedure.

## Brief construction

`SR-HDC-001` [LOCKED D31] Before each bounded portfolio phase, the World MUST provide each active seat with the same versioned Common Crisis Picture and that seat's own Portfolio Brief.

Every brief fact MUST bind a fact ID, actor, recipient, first availability time, source class, content, uncertainty or confidence boundary, Setup, and Seed. An active seat with no private fact receives an explicit empty brief artifact. Initial matched runs receive identical exogenous versions and availability times.

A later-activated seat receives the current common picture and its own already-available backlog, never another seat's brief or discussion. The adapter MUST construct separate authorized inputs, never a union prompt. A private fact becomes common only through logged disclosure or an independent World event, and that transition receives a new picture version.

## Portfolio Product and evidence requests

`SR-HDC-010` [LOCKED D32] Every active portfolio MUST return one valid Portfolio Product before a dependent component advances. It contains:

1. Position: assessment, recommendation, alternatives, and opposed actions.
2. Basis: assumptions and immutable common, private, or disclosed fact references.
3. Uncertainty: gaps, confidence bounds, missing information, and decision-relevant questions.
4. Conditions and blockers: safeguards, dependencies, constraints, objections, and affected action classes.
5. Coordination record: needed reviews, confirmations, safe dissent, and availability of underlying material.

Each category may be empty but MUST be present. A Product is advice and evidence, not a state-changing action.

`SR-HDC-011` The Prime Minister receives Products first, not all raw briefs. A logged request MUST identify source portfolio, product or brief reference, requested fact IDs or scope, and policy question. The deterministic resolver returns `granted`, `denied_compartmented`, `denied_outside_entitlement`, `invalid_scope`, or `unavailable` against the frozen Charter.

A grant delivers immutable World-authored bytes directly into the Prime Minister's persistent memory and records request, decision, facts, hash, time, and recipient. The source portfolio MUST receive a linked notification in its disclosure history but cannot alter the delivered material. A professional clarification is a new portfolio call and dependency; it MUST NOT replace the source fact. A denial blocks only a path whose Charter requires that material.

## Prime Minister draft and targeted review

`SR-HDC-020` [LOCKED D33] After valid Products and resolved requests, the Prime Minister authors one versioned Cabinet Policy Draft. It MUST bind policy intent and stop criteria; typed action components, targets, timing, and sequence; resources, owners, dependencies, and confirmations; evidence, uncertainty, and alternatives; and every inherited dissent, condition, safeguard, or blocker.

The Prime Minister may adopt, change, or decline advice but MUST retain the immutable source-product link.

`SR-HDC-021` A deterministic Charter router MUST select every portfolio affected because the draft touches its mandate, cites, changes, or rejects its product or fact, consumes its resource, changes its condition or confirmation, or triggers a typed cross-effect. The draft's own reviewer list is non-authoritative. Ambiguity routes to the union of plausible reviewers until the action is narrowed.

Every reviewer receives the same draft hash plus only its own authorized context. Independent reviews MAY run concurrently and MUST be collected in Charter order. A Portfolio Review records component scope, `concur`, `concur_with_conditions`, `nonconcur`, or `outside_mandate`, rationale and references, conditions and blockers, bounded alternative, and new dependencies or requests. `outside_mandate`, silence, timeout, or malformed output is not support.

`SR-HDC-022` A material change to action class, target, timing, sequence, resource, owner, evidence, blocker treatment, safeguard, stop condition, or confirmation MUST reroute affected components. Byte-identical components MAY retain version-bound reviews. Review cycles and call budget MUST be frozen; exhaustion with an incomplete dependency fails closed.

## Advisory dissent and binding confirmation

`SR-HDC-030` [LOCKED D34] Review position and Required Confirmation MUST remain separate records. The Prime Minister MAY proceed over a valid advisory objection only after a Dissent Disposition of `adopted`, `mitigated`, `narrowed_or_sequenced`, `withdrawn`, or `proceed_with_unresolved_opposition`. Each disposition MUST bind the exact Review, draft component, changed fields or unchanged risk, supporting evidence, and resulting action-class dependencies; free prose without those bindings is invalid. The last disposition is valid only for advisory opposition with every separate gate satisfied and a reassessment or stop condition.

A Required Confirmation records rule ID, component, type, criteria, evidence, conditions, and `confirmed`, `confirmed_with_conditions`, or `not_confirmed`. Silence, timeout, invalid output, or unmet conditions are controller failure states. A seat cannot promote advice into a gate, and the Prime Minister cannot demote or self-certify a gate.

Objectively encoded conditions are World Validator checks. Judgmental advisory conditions require a Dissent Disposition. Conditions on a Required Confirmation require objective verification or a revised component and new confirmation.

`SR-HDC-031` Component handling MUST follow this table:

| State | Effect |
|---|---|
| Valid advisory concurrence | Continue to remaining checks |
| Valid opposition plus valid disposition | Cabinet-only component may continue; original opposition remains |
| Opposition without valid disposition | Dependent component invalid |
| Required Confirmation satisfied | Continue to remaining checks |
| Confirmation missing, invalid, timed out, negative, or condition-unsatisfied | Named component and declared dependents blocked |

Separable unrelated components MAY continue only when the dependency graph proves separation.

## Gate eligibility and initial map

`SR-HDC-040` [LOCKED D35] A Cabinet gate is valid only when it names one typed component and predicate; follows from a source-backed controlled capability, resource, handoff, or safeguard; asks a bounded question separate from policy support; requires an institutional judgment or act not reducible to World state; freezes criteria, evidence, seat, and dependents before the run; and fails locally. Relevance, symmetry, model prose, broad domain ownership, or a Setup-hidden rule cannot create a gate.

`SR-HDC-041` [LOCKED D36] The initial map contains exactly one Cabinet gate. The provisionally named `interior_force_transfer_to_defense_control` action triggers it only when a component transfers an identified Interior-administered force to an identified Defense command. The component MUST state start condition or time, operational-control scope, continuing domestic coverage plan, and reversion condition.

The Interior-to-Defense administrative relationship is a DATE FACT. The action-class name, exact confirmation question, condition semantics, and component-local failure rule are WOPR INFERENCES.

Interior answers:

> Is the specified administrative handoff, continuing domestic coverage, and reversion arrangement executable for the identified Interior-administered force under the facts currently available to this seat?

Interior confirms only administrative handoff, coverage, and reversion. It does not decide the military objective, operational plan, or national policy. The World owns force identity, location, readiness, equipment, assignment, encoded legal availability, transfer occurrence, and consequences. A missing or negative confirmation blocks only the transfer and declared dependents.

External Affairs, Finance and Economic Resilience, Information and Communications, Civil Infrastructure and Continuity, and Humanitarian and Social Cohesion currently have no binding Cabinet gate. They retain Products, targeted Review, conditions, and attributable opposition. A later gate requires a new typed action and the full eligibility test.

## Causal record

`SR-HDC-050` The retained chain MUST preserve, in order, Common Crisis Picture and private brief hashes, immutable Product, evidence requests, access decisions, recipient delivery and source-portfolio notification, Policy Draft versions, routed Reviews, Dissent Dispositions, Required Confirmations, Open Action Proposals, EXCON adjudications, World Validator results, and consequences. Agreement is not inherently good, and override is not inherently failure; analysis MUST relate the path to authored dependencies, risks, and outcomes.

`SR-HDC-051` [MEASURED D73] The accepted Charter serializes six Portfolio Products, a Prime Minister draft, targeted version-bound review, visible dissent disposition, a separate Command Cell, one persistent Defense bridge, a Joint Executive route, and only the Interior handoff gate. The D73 fixture executes that exact path and its missing-review, dissent, confirmation, route, output, and blocked-action failures. This remains authored machine-contract evidence rather than an observed, official, or model-mediated Himaldeshi process.
