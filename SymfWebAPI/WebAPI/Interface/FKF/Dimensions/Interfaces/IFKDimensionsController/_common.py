from __future__ import annotations

from typing import Any

def _prepare_GetAccountChartByIdAndYear(*, id, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["yearId"] = yearId
    data = None
    return params or None, data

def _prepare_GetDocumentByIdAndYear(*, id, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["yearId"] = yearId
    data = None
    return params or None, data

def _prepare_GetClassification() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data
