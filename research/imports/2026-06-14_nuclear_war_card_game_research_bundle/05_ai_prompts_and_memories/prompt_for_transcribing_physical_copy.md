# Prompt for transcribing the user's physical copy

Use this prompt when the user uploads photos or manually types card text from their legal copy.

Task:

Create a structured card manifest from the provided physical-copy evidence. For each card, extract:

- card name;
- edition/printing if visible;
- deck/color/back identifier;
- card type;
- quantity in the physical copy;
- exact card text;
- any megatonnage/capacity/population amount;
- timing window;
- target restrictions;
- defense/interception interactions;
- edge cases;
- source photo/file name;
- confidence and transcription uncertainty.

Rules:

- Do not silently normalize wording. Preserve exact punctuation/capitalization in `exact_card_text`.
- Also create a separate `effect_summary` written in plain simulation terms.
- Flag illegible words with `[unclear]` and request a close-up only for those cards.
- Compare the transcribed count against `03_card_data/base_game_card_inventory.csv` and report discrepancies.
- If a card is a duplicate, store exact text once and increment count.
