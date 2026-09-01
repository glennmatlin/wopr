# 18. Two-cycle U.S. tracer

Status: MEASURED D70; MILESTONE 4 PASSED AT THE RETAINED TWO-CYCLE RECEIPT

## Scope and public seams

`SR-EPISODE-001` Milestone 4 MUST execute one deterministic no-model U.S.
episode from the exact D68 Cycle 1 source through the D69 endogenous
consequence, D64 matched weather barrier, an attributable Cycle 2 reassessment
and decision, final adjudication, consequence delivery, and exact replay. It
MUST NOT call a model, replace Counterpart Fixtures with Rooms, claim creative
EXCON quality, or count as a DATE evaluation run.

`SR-EPISODE-002` The supported Python seams MUST load one strict development
fixture, execute the episode, and replay it. A fresh-process tracer MUST bind
the exact source, Charter, D68, D69, D64, fixture, executor, run, replay, and
canonical receipt identities.

`SR-EPISODE-003` The Cycle 2 products, reassessment, non-action adjudication,
and final consequence are authored fixture data labeled
`development_fixture_non_evidence`. The controller MAY validate, order,
transport, and record them. It MUST NOT generate policy, infer adaptation,
decide for a Room, or repair missing lineage.

## Exact upstream boundary

`SR-EPISODE-010` The loader MUST require D68 receipt hash
`7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186` and run
hash `08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6`.
It MUST rerun Cycle 1 from the retained fixture and reproduce that run before
continuing.

`SR-EPISODE-011` The loader MUST require D69 receipt hash
`cf78c92190e8b2739923c0977a0af316b332643b563d0ad4818b13048c726ec4`, run
hash `d43ad8544af90f8e44736133c11b6e8443275c901049ffb0800efd2e0978b996`, and
fixture hash
`4b47bc86dad3226692146cc92b21f7b3da61a5919b87ce26924514d7f44ce465`.
It MUST rerun the bridge and reproduce its mixed admitted-and-blocked result.

`SR-EPISODE-012` The loader MUST require D64 profile hash
`64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477` and
tracer receipt hash
`4a582d72b6d8ff753c3e06adea4d36aef3c3b39b5284e4050ce9ed35e39815e3`.
The episode uses the candidate profile, not a copied or rewritten weather
event, patch, confirmation, Core, or outcome projection.

## Ordered World and cycle barriers

`SR-EPISODE-020` The normal trace order MUST be forecast admission, Cycle 1,
D69 consequence admission, matched weather event and atomic paired patch,
matched confirmation, Cycle 2, final adjudication, and final consequence. A
later phase MUST NOT run when an earlier required phase fails.

`SR-EPISODE-021` Cycle 1's raw forecast input MUST bind the D64 forecast by
declared event identity and content relationship while retaining the Charter's
specialist recipients. The forecast MUST be admitted before Cycle 1 and leave
the Core unchanged.

`SR-EPISODE-022` The admitted D69 preparation event MUST be re-admitted to the
episode World from its retained raw event, not reconstructed from ledger prose.
The D69 blocked transmission MUST remain visible and MUST NOT produce an event.

`SR-EPISODE-023` The barrier MUST instantiate the exact D64 weather patch
against the episode's current Core, admit the exact weather event atomically,
and then admit its exact confirmation. Template bytes and ordered operations
MUST match D64. Run-bound patch identity MAY differ because the run and base
Core identity differ.

## Cycle 2 inputs and persistent institutional identity

`SR-EPISODE-030` The Cycle 2 fixture MUST use the D67-ratified Charter and the
same active seat IDs, group graph, decision route, and confirmation rules as
Cycle 1. A cycle loader MAY accept `CYCLE_2` only when its caller supplies the
exact expected cycle ID; the existing Cycle 1 loader MUST remain fail closed.

`SR-EPISODE-031` Every World-derived Cycle 2 Watch input MUST name its exact
ledger causal parents and provenance class. The matched confirmation MUST be a
common input to all active seats. Endogenous D69 consequence content MUST remain
separate from authored matched-weather content even when both enter one common
picture.

`SR-EPISODE-032` A per-seat memory ledger MUST retain the same seat identity
across cycles and append each cycle's exact delivery IDs without aliasing or
reset. This no-model ledger proves deterministic identity and input-history
mechanics only; it is not evidence of model memory or institutional behavior.

## Reassessment, decision, and final adjudication

`SR-EPISODE-040` Cycle 2 MUST produce a supported Policy Package and decision
record that bind the prior decision ID and hash, changed evidence IDs, current
Core version and hash, and one declared disposition: `reaffirm`, `change`,
`condition`, `withdraw`, or `decline`. Repeating policy without those retained
reassessment links MUST NOT count as adaptation.

`SR-EPISODE-041` The retained development trace SHOULD use `condition` so the
test demonstrates an attributable changed decision without prescribing a
preferred policy. The second package MUST still cover all six D45 policy
domains and may retain arbitrary additional open content.

`SR-EPISODE-042` The final adjudication MAY be an Open Action Proposal bridge or
an explicit non-action record. The retained trace uses non-action for unresolved
transmission. It MUST preserve original language, source component, Cycle 2
decision, reasons, causal World parents, and an EXCON consequence proposal.

`SR-EPISODE-043` A valid final non-action consequence MAY enter the ledger but
MUST NOT create a represented-Room decision, claim a capability, or change the
Core. Its delivery to Cycle 2 recipients closes the normal episode only after
the World validator accepts it.

## Completion, terminal, abort, and replay

`SR-EPISODE-050` Normal completion requires two distinct supported cycle
records, retained Cycle 1 and barrier consequences in Cycle 2 inputs and memory,
an attributable second decision, final adjudication, admitted final consequence,
frozen Core and ledger, and exact replay. Missing any item is an invalid abort.

`SR-EPISODE-051` A substantive early terminal is valid only when the frozen Core
terminal predicate becomes non-open before Cycle 2 and the terminal receipt is
retained. A fixture flag, controller exception, missing input, failed barrier,
or budget exhaustion is an abort, not a terminal. The retained normal trace
MUST complete both cycles.

`SR-EPISODE-052` Focused tests MUST cover exact identities, phase order,
forecast linkage, blocked-effect non-admission, current-Core patching, atomic
weather, common confirmation delivery, endogenous-versus-matched provenance,
same-seat memory retention, reassessment linkage, non-action admission,
terminal-versus-abort classification, failure isolation, and exact replay.

`SR-EPISODE-053` Milestone 4 passes only when one fresh-process normal trace
meets every completion condition and replay reconstructs the same cycles,
memory, adjudication, Core, ledger, projections, validation receipts, and run
hash. Passing proves authored no-model episode mechanics only. It does not prove
live Room behavior, counterpart behavior, creative EXCON quality, matching
between U.S. conditions, evaluation validity, or contest results.

## D70 measured receipt

`SR-EPISODE-054` [MEASURED D70] The retained trace binds executor
`67e8ec51281466aacb7b907c1c6212dde817e7c0`, fixture hash
`2a7d484d4096e598cee64cbf30c60344c3cca57a7f9cf52f384e6b0ce8f94e66`,
Cycle 2 fixture hash
`dc99ac7a92e2402451973041325f670c0bb626058068a221f695ee4cd0d9119f`,
run hash `83a143f8712d9b6d012b6dde2f03940062f63b961ad68ccf5bb3b3ae25660597`,
and receipt hash
`7e5dbd8216d9ea9abc55cc457ceae3df44e3ee4192459012a5459944bddfe6ee`.
[`US_TWO_CYCLE_RECEIPT.json`](../US_TWO_CYCLE_RECEIPT.json) passes and replays
exactly under the evidence boundary in `SR-EPISODE-053`.
