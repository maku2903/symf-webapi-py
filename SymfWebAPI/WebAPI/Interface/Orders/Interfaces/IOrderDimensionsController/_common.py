from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

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

def _prepare_GetClassification() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetPositionClassification() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_Update(*, orderId, orderDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = serialize_request_body(orderDimension, prefer_model_dump=True, validate=validate, body_name='orderDimension') if orderDimension is not None else None
    return params or None, data

def _prepare_UpdateByBufferOrderDimensionOrderNumber(*, orderNumber, buffer, orderDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = serialize_request_body(orderDimension, prefer_model_dump=True, validate=validate, body_name='orderDimension') if orderDimension is not None else None
    return params or None, data

def _prepare_UpdateByOrderDimensionsOrderId(*, orderId, orderDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = serialize_request_body(orderDimensions, prefer_model_dump=False, validate=validate, body_name='orderDimensions') if orderDimensions is not None else None
    return params or None, data

def _prepare_UpdateByBufferOrderDimensionsOrderNumber(*, orderNumber, buffer, orderDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = serialize_request_body(orderDimensions, prefer_model_dump=False, validate=validate, body_name='orderDimensions') if orderDimensions is not None else None
    return params or None, data

def _prepare_UpdatePosition(*, positionId, positionDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["positionId"] = positionId
    data = serialize_request_body(positionDimension, prefer_model_dump=True, validate=validate, body_name='positionDimension') if positionDimension is not None else None
    return params or None, data

def _prepare_UpdatePositionByPositionDimensionsPositionId(*, positionId, positionDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["positionId"] = positionId
    data = serialize_request_body(positionDimensions, prefer_model_dump=False, validate=validate, body_name='positionDimensions') if positionDimensions is not None else None
    return params or None, data

def _prepare_UpdatePositionByPositionDimension(*, positionDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(positionDimension, prefer_model_dump=False, validate=validate, body_name='positionDimension') if positionDimension is not None else None
    return params or None, data

def _prepare_GetAspects(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_GetAspectsByBufferOrderNumber(*, orderNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_UpdateAspect(*, aspectPosition = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(aspectPosition, prefer_model_dump=True, validate=validate, body_name='aspectPosition') if aspectPosition is not None else None
    return params or None, data
