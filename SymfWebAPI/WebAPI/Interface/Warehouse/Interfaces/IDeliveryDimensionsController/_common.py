from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get(*, deliveryId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["deliveryId"] = deliveryId
    data = None
    return params or None, data

def _prepare_GetClassification() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_Update(*, deliveryId, deliveryDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["deliveryId"] = deliveryId
    data = serialize_request_body(deliveryDimension, prefer_model_dump=True, validate=validate, body_name='deliveryDimension') if deliveryDimension is not None else None
    return params or None, data

def _prepare_UpdateByDeliveryDimensionsDeliveryId(*, deliveryId, deliveryDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["deliveryId"] = deliveryId
    data = serialize_request_body(deliveryDimensions, prefer_model_dump=False, validate=validate, body_name='deliveryDimensions') if deliveryDimensions is not None else None
    return params or None, data
