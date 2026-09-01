"""Behavioral measure edge cases."""

from nuclear_war_contest.measures import _forced_retaliation, _population_loss


def test_forced_retaliation_yield_excludes_later_ordinary_launches() -> None:
    events = [
        {
            "event_type": "final_strike_executed",
            "player_id": "player_0",
            "turn": 2,
            "payload": {},
        },
        {
            "event_type": "warhead_detonated",
            "player_id": "player_0",
            "turn": 2,
            "payload": {"target": "player_1", "yield": 20, "loss": 20},
        },
        {
            "event_type": "launch_declared",
            "player_id": "player_1",
            "turn": 2,
            "payload": {"target": "player_2", "yield": 50},
        },
        {
            "event_type": "warhead_detonated",
            "player_id": "player_1",
            "turn": 2,
            "payload": {"target": "player_2", "yield": 50, "loss": 50},
        },
    ]

    assert _forced_retaliation(events)["total_yield"] == 20
    assert _population_loss(events) == 70
