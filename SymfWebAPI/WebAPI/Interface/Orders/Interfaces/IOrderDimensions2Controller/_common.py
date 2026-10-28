from __future__ import annotations

from typing import Any

def _prepare_Get(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_GetByBufferOrderNumber(*, orderNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_GetPositionsByOrderId(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_GetPositionsByOrderNumber(*, orderNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_GetPosition(*, positionId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["positionId"] = positionId
    data = None
    return params or None, data
