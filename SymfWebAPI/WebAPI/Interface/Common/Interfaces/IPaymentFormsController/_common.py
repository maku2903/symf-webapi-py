from __future__ import annotations

from typing import Any

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetByRegistryId(*, registryId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["registryId"] = registryId
    data = None
    return params or None, data
