from __future__ import annotations

from typing import Any

def _prepare_Get(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_GetByBufferDocumentNumber(*, documentNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_GetPositionsByOrderId(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_GetPositionsByOrderNumber(*, documentNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_GetPosition(*, positionId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["positionId"] = positionId
    data = None
    return params or None, data
