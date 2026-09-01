"""Fail-closed scene delivery guard for native Concordia prompts."""

_SCENE_JSON_MARKER = "Scene JSON:"


def require_scene_payload(prompt: str) -> None:
    if _SCENE_JSON_MARKER not in prompt:
        raise ValueError(
            "Concordia HTTP model prompt is missing the scene payload "
            f"marker {_SCENE_JSON_MARKER!r}; the entity would choose "
            "blind (context components not delivering observations)"
        )


__all__ = ["require_scene_payload"]
