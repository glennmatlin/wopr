# Source map

The current package names reflect the implementation history. This map groups
them by responsibility without moving imports or changing runtime behavior.

| Responsibility | Package |
| --- | --- |
| Open DATE state, validation, consequences, and replay | [`nuclear_war_contest/date_world`](nuclear_war_contest/date_world/) |
| Shared Room Charter, cycles, proposals, and rehearsal | [`nuclear_war_contest/situation_room`](nuclear_war_contest/situation_room/) |
| Contest study, publication, and validation support | [`nuclear_war_contest`](nuclear_war_contest/) |
| Closed Nuclear War rules, environments, CLI, and replay | [`nuclear_war_env`](https://github.com/glennmatlin/wopr/tree/main/src/nuclear_war_env) |
| Decision and baseline agents | [`nuclear_war_agents`](https://github.com/glennmatlin/wopr/tree/main/src/nuclear_war_agents) |
| Concordia integration | [`nuclear_war_concordia`](nuclear_war_concordia/) |
| Optional external simulator adapter | [`nuclear_war_silisocs`](https://github.com/glennmatlin/wopr/tree/main/src/nuclear_war_silisocs) |

The DATE and Situation Room subpackages are the contest implementation. The
other top-level modules under `nuclear_war_contest` include historical study,
screening, release, and provider-control machinery. They remain in place so
the deadline cleanup does not invalidate imports or retained receipts.

Absolute links above intentionally follow the living public `main` branch when
their packages sit outside the curated contest export. The export receipt binds
only the files selected by its manifest.

See [WOPR architecture](../ARCHITECTURE.md) for dependency boundaries and
[Worlds](../worlds/README.md) for the difference between open and closed action
resolution.
