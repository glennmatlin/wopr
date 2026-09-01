# 17. Open proposal and consequence bridge

Status: MEASURED D69; MILESTONE 3 PASSED AT THE RETAINED BRIDGE RECEIPT

## Scope and public seams

`SR-BRIDGE-001` Milestone 3 MUST execute one deterministic no-model development
trace from the exact D68 U.S. Policy Package and NSC decision record through
Open Action Proposals, bounded clarification, effect-level authority and
capability checks, state-bounded consequence proposals, and D64 World
admission. It MUST NOT call a model, claim creative-EXCON quality, run a
Counterpart Room, execute Cycle 2, or count as DATE episode evidence.

`SR-BRIDGE-002` The supported Python seams MUST load a strict development
fixture, execute the bridge, and replay it. A fresh-process tracer MUST bind the
exact D68 receipt, exact D64 profile, fixture, executor revision, run, World
admission receipts, replay result, and canonical receipt hash.

`SR-BRIDGE-003` All proposal, clarification, effect-authority, capability, and
EXCON content in this milestone is authored fixture data labeled
`development_fixture_non_evidence`. The controller MAY transport, validate,
order, and record it. The controller MUST NOT parse policy prose, repair an
effect, infer authority, create capability, answer clarification, or generate a
consequence.

## Upstream identity

`SR-BRIDGE-010` The loader MUST require D68 receipt hash
`7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186`, run
hash `08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6`,
and a supported decision with no admitted World effect. Proposal references
MUST resolve to the retained Policy Package, decided component, and NSC record.

`SR-BRIDGE-011` The loader MUST require D64 profile hash
`64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477`.
Every Core read, actor, activity, force package, affordance, affected entity,
audience, evidence ID, World parent, and patch operation MUST resolve through
that loaded profile or current run.

## Open proposals and compound effects

`SR-BRIDGE-020` An Open Action Proposal MUST retain its proposal ID, version,
actor, original natural-language proposal, source Policy Package and component
IDs, institutional decision-record ID, and an authored ordered effect list.
The envelope MUST NOT require an action family, handler, or exhaustive policy
type. Novel language or an unmatched action family is never a rejection reason.

`SR-BRIDGE-021` Each authored effect MUST retain its effect ID, source component
IDs, original language, intended effect, means or resources, object or
audience, timing, conditions, dependency effect IDs, unresolved field IDs,
authority-record ID, capability-record IDs, and consequence-proposal ID. These
fields describe an attempt; they do not establish that the effect is valid,
authorized, capable, or admitted.

`SR-BRIDGE-022` The effect graph MUST be acyclic and may cross components only
through explicit authored dependencies. A failed effect blocks only its proven
descendants. An independent sibling MAY continue, but the controller MUST NOT
split, combine, or reorder effects by interpreting the original language.

## Bounded clarification

`SR-BRIDGE-030` One authored clarification record MAY address each effect. It
MUST bind the original effect hash, question, response, requested field IDs,
and replacement values. It may fill only fields explicitly marked unresolved;
it may not overwrite existing content, add a new effect, change dependencies,
or narrow a proposal without a retained response.

`SR-BRIDGE-031` An absent or unresolved required clarification blocks that
effect as `unresolved_clarification` while preserving the proposal, question,
response if any, and dependent failure receipts. Clarification success proves
only deterministic field binding, not semantic correctness.

## Effect authority and capability

`SR-BRIDGE-040` Record-level D67 confirmations and D68 policy approval MUST NOT
be treated as effect-level authority. Every effect that may reach the World
MUST bind a separate effect-authority record to the exact resolved effect hash,
actor, authorizing seat, NSC decision record, status, and explicit development
evidence label.

`SR-BRIDGE-041` The first successful authority record is fixture scaffolding,
not a claim about official delegation or real implementation authority.
Missing, stale, mismatched, or non-authorized records block only the bound
effect with `missing_effect_authority` or `invalid_effect_authority`.

`SR-BRIDGE-042` Every effect that proceeds beyond clarification and authority
MUST bind one or more typed Core capability requirements. The first catalog may
test declared activity ownership, affordance control or state, and
force-package ownership. Open prose, a ledger description, an office title, or
an authority record cannot create capability. Unknown or false predicates block
the effect as `missing_capability`.

## Consequence proposal and World admission

`SR-BRIDGE-050` EXCON MUST remain distinct from the represented Rooms and emit
a retained consequence proposal rather than truth. The artifact MUST bind its
proposal and effect parents, exact Core version and hash read, World parent
event IDs, affected entities, episode hour, audience, evidence, assumptions,
uncertainty, plausible alternatives, open content, adjudicator identity,
represented-Room decisions if any, resulting injects, and optional State Patch.

`SR-BRIDGE-051` A consequence proposal that decides for the U.S., Himaldesh,
or Olvana Room, invents a prior entity or capability, cites stale Core, breaks
World causality, or requests a forbidden write MUST be rejected without a
World transition. An affected represented actor is not by itself a Room
decision; the explicit represented-decision field controls this boundary.

`SR-BRIDGE-052` A valid consequence MUST translate without semantic repair to
one D64 event with source `excon_consequence`. Ledger-only consequences leave
the Core unchanged. A Core-changing consequence MUST carry a D64-compatible
semantic patch and is admitted atomically by the existing validator. The
bridge MUST retain proposal validity, authority and capability results,
consequence validation, D64 receipt, patch, ledger entry, and Core transition
as distinct artifacts.

## Failure, replay, and milestone gate

`SR-BRIDGE-060` Pre-execution envelope, identity, duplicate, graph, and static
artifact-reference defects MUST stop before a run. State-dependent
clarification, dependency, authority, capability, consequence, World-parent,
and admission failures MUST remain attributable in-cycle effect receipts. No
failed effect may produce an admitted ledger entry or Core change.

`SR-BRIDGE-061` Focused tests MUST cover strict identity, original-language
preservation, open extra content, clarification non-rewrite, dependency-local
failure, authority and capability binding, represented-Room exclusion, stale
Core, causal mismatch, forbidden patch, D64 reason propagation, and exact
replay. Novelty alone MUST have a passing control.

`SR-BRIDGE-062` Milestone 3 passes only when one fresh-process trace admits at
least one state-valid consequence, retains at least one blocked effect, and
replays the same proposals, clarifications, effect receipts, World ledger,
Core, and canonical run hash. Passing proves bridge mechanics over authored
fixtures only. It does not prove model proposal quality, EXCON plausibility,
official effect authority, Counterpart Room behavior, or an end-to-end DATE
episode.

## D69 measured receipt

`SR-BRIDGE-063` [MEASURED D69] The retained fresh-process trace passes with
executor `1b912ff693a84c5e1081fc76d1ed1f71e4f810aa`, fixture hash
`4b47bc86dad3226692146cc92b21f7b3da61a5919b87ce26924514d7f44ce465`, run
hash `d43ad8544af90f8e44736133c11b6e8443275c901049ffb0800efd2e0978b996`,
and receipt hash `cf78c92190e8b2739923c0977a0af316b332643b563d0ad4818b13048c726ec4`.
It admits one ledger-only effect, blocks one unresolved dependent effect,
leaves Core unchanged, and replays exactly. This closes only the no-model M3
bridge gate; live extraction, creative EXCON, Cycle 2, and episode evidence
remain open.
