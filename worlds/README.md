# Worlds

A World is the authoritative environment that supplies state, affordances,
events, consequences, terminal conditions, and replay. The same institutional
Room can be evaluated in more than one World, but each World retains its own
action grammar and truth.

| World | Action surface | Consequence owner | Current evidence |
| --- | --- | --- | --- |
| [DATE](date/README.md) | Open policy proposals interpreted into supported effects | World validator plus EXCON/MSEL machinery | Offline scaffold and scripted rehearsal; live evaluation unrun |
| [Nuclear War](nuclear-war/README.md) | Closed game actions defined by deterministic rules | Nuclear War engine | Historical engine and Sounding; same-Room comparison unrun |

The comparison is intended to ask what changes when an institution moves from
an open crisis environment into a bounded game. It is not a claim that the two
Worlds are interchangeable or that the cross-World evaluation is complete.

The [architecture map](../ARCHITECTURE.md) defines the shared boundary, and the
[evidence matrix](../docs/contest/EVIDENCE_MATRIX.md) records what has actually
been executed.
