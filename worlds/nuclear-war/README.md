# Nuclear War World

Nuclear War is WOPR's closed-form comparison World. Its deterministic engine
defines legal actions, card and population effects, terminal conditions, event
logging, and replay. Language-model adapters sit outside that rules authority.

## Implementation

- [`src/nuclear_war_env`](https://github.com/glennmatlin/wopr/tree/main/src/nuclear_war_env)
  owns deterministic state transitions, environments, CLI behavior, and replay.
- [`src/nuclear_war_agents`](https://github.com/glennmatlin/wopr/tree/main/src/nuclear_war_agents)
  contains decision adapters and baseline agents.
- [`docs/rule_fidelity_matrix.md`](https://github.com/glennmatlin/wopr/blob/main/docs/rule_fidelity_matrix.md)
  records rules coverage and source confidence.

```bash
nuclear-war validate-rules
nuclear-war simulate --mode postal --players 3 --seed 1 --agent heuristic --out run.json
nuclear-war replay run.json
```

## Relationship to the contest entry

The historical Nuclear War Sounding is retained evidence for a separate
closed-world instrument. It is not DATE evidence and did not run the current
institutional U.S. Room. The proposed same-Room comparison would translate a
Room policy disposition into this World's bounded action interface, then
compare institutional behavior across the open and closed settings. That
comparison has not been run.

See the [World comparison](../README.md), the
[historical Sounding](../../docs/contest/SOUNDING.md), and the
[evidence matrix](../../docs/contest/EVIDENCE_MATRIX.md).
