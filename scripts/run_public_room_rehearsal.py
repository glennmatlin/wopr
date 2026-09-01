"""Run the scripted Room rehearsal from the curated source export."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, cast


def main() -> None:
    """Expose the frozen agent protocol types, then run the retained tracer."""
    source = Path(__file__).resolve().parents[1] / "src"
    if str(source) not in sys.path:
        sys.path.insert(0, str(source))
    _expose_agent_protocol_types()
    from nuclear_war_contest.situation_room.scripted_rehearsal_tracer import (
        main as tracer_main,
    )

    tracer_main()


def _expose_agent_protocol_types() -> None:
    import nuclear_war_agents
    from nuclear_war_agents.llm_types import LLMCompletion, LLMModelClient

    exports = cast(Any, nuclear_war_agents)
    exports.LLMCompletion = LLMCompletion
    exports.LLMModelClient = LLMModelClient


if __name__ == "__main__":
    main()
