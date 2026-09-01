# Games and evaluation references

_Deadline packet register for the ChinaTalk Situation Room submission. It separates the primary DATE World, the proposed closed-form Nuclear War comparison, and earlier comparator and history references._

---

## 🌐 Worlds in the Packet

The Packet's primary World is a DATE-backed, fictional Himaldesh-Olvana crisis.
It is the realism-oriented open crisis World in the design: policy enters as an
attributable open proposal, consequences are proposed against current state,
and a deterministic validator admits state changes. DATE grounds the exercise
context and public-source facts; the first episode's geography, profiles,
force packages, timings, and procedures are WOPR authoring inferences. They
must not be presented as official DATE facts, a fully realistic simulator, or
a completed DATE run.

Nuclear War (Flying Buffalo) is the proposed closed-form comparison World for the same U.S. Room. Its finite legal moves, engine-owned consequences, and deterministic replay provide a controlled secondary stressor and historical engineering foundation. It is deliberately unrealistic, is not a national command model or DATE realism evidence, and does not make World outcomes commensurate. A same-Room Nuclear War comparison remains proposed until its own evidence exists.

| World | Packet role | Contract | Evidence boundary |
| --- | --- | --- | --- |
| DATE-backed Himaldesh-Olvana | Primary realism-oriented open crisis World | Open Action Proposal, typed World Core, open World Event Ledger, deterministic validation | Fictional authored profile and WOPR inference; no official DATE or completed-episode claim |
| Nuclear War (Flying Buffalo) | Proposed secondary closed-form comparison | Finite legal moves, engine-owned consequences, deterministic replay | Deliberately unrealistic stressor and historical engineering evidence; not DATE evidence |

The authoritative cross-World boundary is recorded in [CONTEXT.md](CONTEXT.md) and [12. One Room across open and closed Worlds](spec/12-one-room-across-open-and-closed-worlds.md). The provisional first episode is described in [13. First-episode default profile](spec/13-first-episode-default-profile.md).

## 📚 Prior work and design history

These links preserve the research history and comparator context. They are not additional Packet Worlds, and a reference link does not establish an adapter, a run, or redistribution rights.

| Work | Link | Relevance |
| --- | --- | --- |
| No One Wins in Nuclear War: A Social Simulation of Military Decision-making | https://arxiv.org/abs/2608.01868 | Replay-validated WOPR engine, press ladder, and collective command structures |
| Shall We Play a Game? Language Models for Open-ended Wargames | https://arxiv.org/abs/2509.17192 | Separating model action choice from World adjudication |

### Earlier comparator references named in the ChinaTalk brief

| Name | Link | Kind | Why it was named |
| --- | --- | --- | --- |
| Diplomacy / Good Start Labs | https://github.com/GoodStartLabs/AI_Diplomacy | Multi-player negotiation game | Talk, betrayal, peace-versus-victory |
| Civilization V / CivBench | https://www.lwilko.com/blog/i-gave-an-ai-a-civilization | Long-horizon strategy game | Dynamic play; Chen and Wilkinson both work here |
| TaiwanBench | https://taiwanbench-site.vercel.app/ | Scripted crisis tree, LM adjudicator | House exemplar: one sentence, microsite, language contrast |
| CFPD-Benchmark | https://arxiv.org/abs/2503.06263 | Multiple-choice foreign-policy items | Escalation items without a stateful World |
| WarAgent | https://arxiv.org/html/2403.13433v1 | Historical counterfactual simulation | WWI still emerges under a no-war fine-tune |
| Cuban Missile Crisis / EXCOMM | https://www.jfklibrary.org/learn/about-jfk/jfk-in-history/cuban-missile-crisis | Historical committee, not a game | Jordan's "model in EXCOMM" prompt |
| 13 Days: The Cuban Missile Crisis | https://boardgamegeek.com/boardgame/177478/13-days-the-cuban-missile-crisis | Published 2p board game | Closest published game analog to that prompt |
| Paradox grand strategy | Contest prose only | Commercial strategy series | Brief example; no adapter here |
| EVE Online | Contest prose only | MMO | Brief example; ToS and no adapter here |
| Declassified NIEs | Contest prose only | Historical intelligence estimates | Scoring idea; training-data contamination risk |

### Instrument analogs named in the design history

These are labs, not Worlds the Packet seats. They are product-shape analogs for the separation between model chairs and World adjudication.

| Name | Link | Split | Relevance |
| --- | --- | --- | --- |
| GenWar Lab | https://www.jhuapl.edu/news/news-releases/251030-genwar-lab | Lab that holds TTX + Sim + X | Configurable wargame lab, not a leaderboard |
| GenWar Sim | https://www.jhuapl.edu/work/projects-and-missions/genwar-sim | LLM talks; AFSIM adjudicates | Same split as WOPR: model does not own physics |
| GenWar TTX | [GenWar Lab article](https://www.jhuapl.edu/news/news-releases/251030-genwar-lab) | AI advisers, adversary leaders, human players | Closest analog to a Room |
| SAGE (in press) | https://breakingdefense.com/2025/08/johns-hopkins-is-building-classified-versions-of-its-ai-wargaming-tools-for-dod-ic/ | NSC-style table; some or all seats are models | "Goal isn't to find the answer"; all-AI mode goes off the rails |
| March 2025 GenWar writeup | https://www.jhuapl.edu/news/news-releases/250303-generative-wargaming | Any player can be human or LLM | Demand signal: faster tabletop, inspectable moves |

### Related published games discussed in the thread

| Name | Link | Kind | Decision |
| --- | --- | --- | --- |
| 13 Days | [BoardGameGeek reference](https://boardgamegeek.com/boardgame/177478/13-days-the-cuban-missile-crisis) | CMC two-player | Rejected as a September 1 World |
| Any new EXCOMM tree | n/a | Would be a new World, likely LM-adjudicated | Rejected for this Packet |
