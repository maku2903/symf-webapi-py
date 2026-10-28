from __future__ import annotations

from typing import Any

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetByDate(*, date) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["date"] = date
    data = None
    return params or None, data
