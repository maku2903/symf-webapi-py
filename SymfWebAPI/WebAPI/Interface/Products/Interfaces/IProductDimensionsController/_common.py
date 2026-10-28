from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_GetByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data

def _prepare_Update(*, productId, productDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = serialize_request_body(productDimension, prefer_model_dump=True, validate=validate, body_name='productDimension') if productDimension is not None else None
    return params or None, data

def _prepare_UpdateByProductCodeProductDimension(*, productCode, productDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = serialize_request_body(productDimension, prefer_model_dump=True, validate=validate, body_name='productDimension') if productDimension is not None else None
    return params or None, data

def _prepare_UpdateByProductDimensionsProductId(*, productId, productDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = serialize_request_body(productDimensions, prefer_model_dump=False, validate=validate, body_name='productDimensions') if productDimensions is not None else None
    return params or None, data

def _prepare_UpdateByProductCodeProductDimensions(*, productCode, productDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = serialize_request_body(productDimensions, prefer_model_dump=False, validate=validate, body_name='productDimensions') if productDimensions is not None else None
    return params or None, data

def _prepare_GetClassification() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data
