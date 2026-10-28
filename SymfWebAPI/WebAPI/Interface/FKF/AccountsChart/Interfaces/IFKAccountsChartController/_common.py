from __future__ import annotations

from typing import Any

def _prepare_GetFlatList(*, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    data = None
    return params or None, data

def _prepare_GetTreeList(*, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    data = None
    return params or None, data
