from __future__ import annotations

from typing import Any

def _prepare_GetById(*, contractorId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = None
    return params or None, data

def _prepare_GetByPosition(*, contractorPosition) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    data = None
    return params or None, data

def _prepare_GetByCode(*, contractorCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = None
    return params or None, data
