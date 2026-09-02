# U.S. Situation Room

The contest entry models the U.S. Situation Room as an institution rather than
one decision-making agent. Persistent seats have distinct mandates and
information entitlements. They produce attributable advice, work through
portfolio groups, preserve dissent, and assemble an integrated policy package
over two cycles.

## Institutional path

```text
source register -> Room Charter -> Common Crisis Picture + portfolio briefs
-> seat products -> working-group products -> presidential synthesis
-> open policy package -> World-specific admission
```

The first episode activates groups for threat and attribution, diplomatic and
economic options, nuclear and radiological risk, defense and escalation, legal
authority, homeland consequences, and presidential synthesis. The groups are
episode composition, not universal claims about every real meeting.

## Implementation

The implemented controllers, compiler, Charter validation, selective delivery,
free-output contracts, cycle orchestration, proposal bridge, and scripted
rehearsal are in
[`src/nuclear_war_contest/situation_room`](../src/nuclear_war_contest/situation_room/).
The [DATE World](../worlds/date/README.md) owns state and consequences after the
Room issues a disposition.

Key artifacts:

- [U.S. Charter candidate](../docs/contest/US_CHARTER.candidate.json)
- [Episode 1](../docs/contest/EPISODE_1.md)
- [Two-cycle fixture](../docs/contest/US_TWO_CYCLE_FIXTURE.development.json)
- [Proposal bridge contract](../docs/contest/spec/17-open-proposal-consequence-bridge.md)
- [Offline rehearsal receipt](../docs/contest/US_SCRIPTED_ROOM_REHEARSAL_RECEIPT.json)

## Evidence boundary

The retained rehearsal uses scripted, explicitly non-evidence responses across
114 logical calls. It verifies ordering, selective information delivery,
attribution, proposal materialization, deterministic admission, and replay. It
does not show how a model, a real institution, or a government would behave.
The complete live DATE Room and cross-World comparison remain unrun.
