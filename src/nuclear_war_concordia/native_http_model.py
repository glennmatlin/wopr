"""HTTP-backed language model adapter for native Concordia entities."""

from __future__ import annotations

import json
import re
from collections.abc import Collection, Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from nuclear_war_agents import LLMCompletion, LLMModelClient
from nuclear_war_agents.llm_completion import normalize_completion

from .native_prompt_guard import require_scene_payload
from .response import parse_concordia_response


@dataclass
class ConcordiaHTTPChoiceModel:
    client: LLMModelClient
    last_completion: LLMCompletion | None = None
    last_prompt: str | None = None

    def sample_text(
        self,
        prompt: str,
        *,
        max_tokens: int = 5000,
        terminators: Collection[str] = (),
        temperature: float = 1.0,
        top_p: float = 0.95,
        top_k: int = 64,
        timeout: float = 60,
        seed: int | None = None,
    ) -> str:
        del max_tokens, terminators, temperature, top_p, top_k, timeout, seed
        self.last_prompt = prompt
        require_scene_payload(prompt)
        completion = normalize_completion(self.client.complete(prompt))
        self.last_completion = completion
        return completion.raw_response

    def sample_choice(
        self,
        prompt: str,
        responses: Sequence[str],
        *,
        seed: int | None = None,
    ) -> tuple[int, str, Mapping[str, Any]]:
        del seed
        require_scene_payload(prompt)
        options_by_letter = _options_by_letter(prompt, responses)
        completion = normalize_completion(
            self.client.complete(_choice_prompt(prompt, responses, options_by_letter))
        )
        self.last_completion = completion
        choice = _choice_from_raw(completion.raw_response, responses, options_by_letter)
        if choice is None:
            error = _invalid_response_error("Concordia HTTP model returned no choice")
            error.__dict__["completion"] = completion
            raise error
        return responses.index(choice), choice, _completion_info(completion)


# Concordia's InteractiveDocument renders choice options as "  (a) <option>"
# lines and expects the answer letter back from sample_choice.
_OPTION_LINE_PATTERN = re.compile(r"^\s*\(([a-z]+)\)\s+(\S.*?)\s*$")


def _options_by_letter(prompt: str, responses: Sequence[str]) -> dict[str, str]:
    lines = prompt.splitlines()
    question_starts = [
        index for index, line in enumerate(lines) if line.startswith("Question:")
    ]
    start = question_starts[-1] + 1 if question_starts else 0
    options: dict[str, str] = {}
    for line in lines[start:]:
        match = _OPTION_LINE_PATTERN.match(line)
        if match is not None and match.group(1) in responses:
            options[match.group(1)] = match.group(2)
    return options


def _choice_prompt(
    prompt: str,
    responses: Sequence[str],
    options_by_letter: Mapping[str, str],
) -> str:
    action_ids = list(options_by_letter.values()) or list(responses)
    lines = [
        prompt,
        "",
        "Choose exactly one legal action_id from this list.",
        json.dumps(action_ids, indent=2),
        "",
        'Return JSON only: {"action_id": "..."}',
    ]
    return "\n".join(lines)


def _choice_from_raw(
    raw_response: str,
    responses: Sequence[str],
    options_by_letter: Mapping[str, str],
) -> str | None:
    letters_by_option = {option: letter for letter, option in options_by_letter.items()}
    candidates: list[str] = []
    stripped = raw_response.strip()
    candidates.append(stripped)
    try:
        value = json.loads(stripped)
    except json.JSONDecodeError:
        value = None
    if isinstance(value, str):
        candidates.append(value)
    parsed = parse_concordia_response(stripped)
    if parsed.action_id is not None:
        candidates.append(parsed.action_id)
    for candidate in candidates:
        if candidate in responses:
            return candidate
        if candidate in letters_by_option:
            return letters_by_option[candidate]
    return None


def _invalid_response_error(message: str) -> Exception:
    try:
        from concordia.language_model import language_model
    except ImportError:
        return ValueError(message)
    return language_model.InvalidResponseError(message)


def _completion_info(completion: LLMCompletion) -> dict[str, Any]:
    return {
        "provider_label": completion.provider_label,
        "provider_model": completion.provider_model,
        "provider_latency_ms": completion.provider_latency_ms,
        "provider_usage": completion.provider_usage,
    }
