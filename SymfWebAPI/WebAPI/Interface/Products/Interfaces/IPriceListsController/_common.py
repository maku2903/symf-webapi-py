from __future__ import annotations

from typing import Any

def _prepare_Get(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_GetByCode(*, code) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["code"] = code
    data = None
    return params or None, data

def _prepare_GetGet() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_IncrementalSync(*, dateFrom) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dateFrom"] = dateFrom
    data = None
    return params or None, data
