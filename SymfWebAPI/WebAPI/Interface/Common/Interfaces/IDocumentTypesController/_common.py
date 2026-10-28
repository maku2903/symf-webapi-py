from __future__ import annotations

from typing import Any

def _prepare_Get(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_GetByCharacter(*, documentCharacter) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentCharacter"] = documentCharacter
    data = None
    return params or None, data

def _prepare_GetCharacterRelations() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data
