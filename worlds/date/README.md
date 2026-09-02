# DATE World

The DATE World is WOPR's open-ended crisis environment. Episode 1 uses an
authored high-altitude confrontation in which Olvana occupies Kestrel Ridge and
Talus Node, Himaldesh prepares a limited conventional recapture, and the United
States considers a bounded support request while nuclear escalation remains
reachable but is not scripted.

## Read the episode

1. [Episode 1](../../docs/contest/EPISODE_1.md) gives the presentation-ready
   narrative, starting state, two U.S. cycles, weather barrier, open policy
   path, and escalation boundary.
2. [Protocol](../../docs/contest/PROTOCOL.md) defines the intended evaluation.
3. [Evidence matrix](../../docs/contest/EVIDENCE_MATRIX.md) separates the
   implemented scaffold from unrun live behavior.
4. [Context vocabulary](../../docs/contest/CONTEXT.md) defines World, Room,
   Setup, Charter, Open Action Proposal, EXCON, and State Patch.

## Implementation

The transition kernel, typed state, event ledger, validator, EXCON proposal
contract, state patches, and replay are in
[`src/nuclear_war_contest/date_world`](../../src/nuclear_war_contest/date_world/).
The U.S. cycle and proposal machinery is in the
[Situation Room package](../../situation-room/README.md).

The World keeps policy language open but state changes bounded. A proposal may
contain a new action or combination of effects. The interpreter preserves that
language, asks bounded clarifying questions when allowed, and rejects only the
unsupported components. The deterministic validator alone can admit an event
or atomically apply a preconditioned state patch.

## Current boundary

The checked-in profile and fixtures are authored development artifacts. The
offline machinery and exact replay have been exercised, but no complete live
U.S. Room DATE evaluation, creative consequence study, matched comparison, or
behavioral result is claimed.

Run the offline two-cycle path from the repository root:

```bash
uv sync --extra concordia
REVISION="$(git rev-parse HEAD)"
uv run python scripts/run_public_room_rehearsal.py \
  docs/contest/US_TWO_CYCLE_FIXTURE.development.json \
  "$REVISION" \
  /tmp/us-room-rehearsal.json
```
