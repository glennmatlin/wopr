# Prompt for implementing the simulation engine

Build a deterministic, auditable *Nuclear War* rules engine.

Inputs:

- `04_simulation_model/rules_variants.json`
- `04_simulation_model/spinner_and_die_tables.json`
- `03_card_data/base_game_card_inventory.csv`
- any verified exact-card manifest from the user's physical copy.

Requirements:

- Model population as denominations/cards, with bank change operations.
- Keep private hands hidden from other agents.
- Implement the launch track with face-up, first face-down, second face-down slots.
- Implement peace/war state and propaganda legality.
- Implement delivery-system/warhead compatibility.
- Implement anti-missile response timing and turn-order jump where variant requires it.
- Implement final retaliation chains.
- Log every stochastic event and source table.
- Do not use unverified exact card text in user-facing public output; use effect summaries.
- Make edition differences explicit configuration settings.

Deliverables:

- rules-engine source code;
- unit tests for attack/fallout outcomes;
- unit tests for final-retaliation chain elimination;
- tests for propaganda during peace vs war;
- seeded random simulations;
- event log schema.
