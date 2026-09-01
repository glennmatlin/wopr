# 16. No-model U.S. Cycle 1 machine contract

Status: MEASURED CONTROLLER CHECKPOINT D68; Milestone 2 PASSED

## Scope and public seams

`SR-USC1-001` Milestone 2 MUST execute one deterministic development trace of
the D67-ratified U.S. Charter through Watch delivery, the active specialist
graph, Presidential Synthesis, PC integration, the applicable decision route,
record-level Required Confirmations, and Executive Secretary distribution. It
MUST NOT call a model, admit a World effect, serialize an Open Action Proposal,
run creative EXCON, claim Counterpart Room behavior, or count as DATE episode
evidence.

`SR-USC1-002` The supported Python seams are `load_us_cycle_fixture`,
`run_no_model_us_cycle`, and `replay_us_cycle`. A fresh-process module entry
MUST load the exact source register, Charter, D67 ratification receipt, and
development fixture, run and replay the cycle, and emit one canonical receipt.
It MUST write to standard output by default and MAY write the same bytes to one
explicit output path for durable retention.

`SR-USC1-003` The fixture loader MUST bind the exact D67 ratification hash,
source hash, Charter hash, fixture status, actor, cycle, counterpart-fixture
identities, action class, Watch inputs, group product attempts, and record-level
confirmations. Unknown envelope fields, duplicate IDs, non-finite values,
identity mismatches, and unresolved Charter references fail closed.

## Development fixture boundary

`SR-USC1-010` Himaldesh and Olvana fixture outputs MUST be frozen, hashed, and
labeled `development_fixture_non_evidence`. They MAY supply the partner request,
observed posture, and other synthetic inputs needed to exercise the U.S. path.
They MUST NOT be described as actor decisions, Counterpart Rooms, live outputs,
or evidence about either fictional government.

`SR-USC1-011` The fixture MUST contain open JSON content inside strict input,
product, confirmation, and counterpart envelopes. Product validation MUST
require the ratified Charter fields without imposing an exhaustive vocabulary
inside those fields. This preserves open policy content while keeping identity,
information, process, and routing mechanically checkable.

`SR-USC1-012` Fixture content is authored test data. The controller MUST NOT
write analysis, choose a policy, summarize evidence, resolve dissent, repair a
missing field, infer a confirmation, or generate a counterpart response.

## Watch and information isolation

`SR-USC1-020` Every Watch input MUST retain an input ID, information-class ID,
sender ID, authored content, causal parents, and canonical hash. The controller
MUST derive recipients only from the compiled Charter and record one immutable
delivery per entitled active seat.

`SR-USC1-021` A common input MUST reach every active entitled seat. A private
input or raw forecast MUST reach only its declared recipients. World ground
truth, an undeclared sender, an unentitled recipient, or a union brief MUST fail
closed rather than enter any seat or group input.

`SR-USC1-022` Product delivery MUST use the Charter's information class and
declared sender group. A recipient is authorized by an explicit disclosure
permission or by both a declared dependency on that producer and a matching
group input entitlement. Senior groups receive attributable products and
hashes, not hidden raw inputs or controller-written summaries.

## Graph execution and products

`SR-USC1-030` Active groups MUST be scheduled from the ratified dependency
graph. A deterministic wave MAY contain multiple groups only when dependencies
are satisfied and `can_run_concurrently` proves no shared active seat. Attempts
and products MUST be collected in Charter order, never fixture order or
wall-clock order.

`SR-USC1-031` Each group attempt MUST bind its group, product schema, ordered
members, authorized input IDs, dependency product IDs, original product body,
and canonical hash. A valid body contains every required Charter field and MAY
contain additional open content.

`SR-USC1-032` The PC product MUST be the one versioned integrated Policy Package
and retain all six required domain dispositions, their responsible
contributions, deciding forum, reason, and disposition. These coverage fields
MUST NOT require action or constrain later Open Action Proposal content.

`SR-USC1-033` The selected first trace uses action class
`presidential_policy_direction`. The controller MUST resolve its route from the
Charter, require the declared PC and legal consultations, retain the exact NSC
decision record, and verify only the record-level confirmations ratified in
D67. It MUST NOT infer effect-level authority or capability.

## Failure, replay, and gate

`SR-USC1-040` A pre-execution envelope, identity, reference, or entitlement
defect MUST stop before a run with its stable rejection code. Once execution
starts, a missing or invalid product, blocked dependency, route mismatch,
missing consultation, missing confirmation, or replay mismatch MUST remain an
attributable failure receipt. A failed dependency blocks only descendants
proven by the compiled graph; no failed path may yield a supported decision or
World effect.

`SR-USC1-041` The successful receipt MUST bind executor revision, ratification,
source, Charter, fixture, counterpart fixtures, activation, schedule, Watch
deliveries, product attempts, Policy Package, decision route, decision record,
confirmations, failures, replay result, and canonical receipt hash. It MUST
declare `development_fixture_non_evidence` and `world_effects_admitted: false`.

`SR-USC1-042` Fresh-process replay MUST reconstruct the same ordered deliveries,
schedule, products, route, confirmations, and final cycle hash from the retained
fixture. Path names, branch names, process completion, or a passing unit test do
not substitute for exact artifact identity.

`SR-USC1-050` [PASSED D68] Milestone 2 passes only when the public seams above reject the
declared failure families, one complete no-model Cycle 1 trace replays in a
fresh process, focused lint and type checks pass, and the retained receipt binds
the exact D67 identities. This gate establishes controller mechanics only. It
does not establish model behavior, Room quality, counterpart behavior, World
consequences, a DATE episode, comparison, or contest result.

## D68 measured receipt

[`US_CYCLE1_RECEIPT.json`](../US_CYCLE1_RECEIPT.json) binds executor
`6c06ed4a7e362cdee89ca15df7aff385aec0aaf8`, the exact D67 source, Charter,
and ratification identities, development fixture hash
`ea7333ec4e7423ad628455d18638c6e0eefd9fdca3b0bd17f85d35fb2d2ac9fc`,
run hash `08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6`,
and canonical receipt hash
`7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186`.
The trace activates 14 seats, delivers 12 Watch inputs through 96 attributable
deliveries, accepts eight products over seven Charter-derived waves, retains
the six-domain Policy Package and NSC record, verifies two record
confirmations, replays exactly, supports the decision record, and admits no
World effect. The counterpart fixtures and all product bodies are authored
non-evidence. D68 closes only this controller gate.
