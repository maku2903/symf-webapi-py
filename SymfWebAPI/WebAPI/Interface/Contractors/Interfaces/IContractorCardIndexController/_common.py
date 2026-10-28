from __future__ import annotations

from typing import Any

def _prepare_GetByIdAsync(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_GetByCodeAsync(*, code) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["code"] = code
    data = None
    return params or None, data

def _prepare_GetByNIPAsync(*, nip) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["nip"] = nip
    data = None
    return params or None, data
