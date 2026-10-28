from __future__ import annotations

from typing import Any

def _prepare_GetStatus() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_Fiscalize(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data
