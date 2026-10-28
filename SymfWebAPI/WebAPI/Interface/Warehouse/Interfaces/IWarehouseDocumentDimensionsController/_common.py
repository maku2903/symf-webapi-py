from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

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

def _prepare_GetClassification() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetPositionClassification() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_Update(*, documentId, documentDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = serialize_request_body(documentDimension, prefer_model_dump=True, validate=validate, body_name='documentDimension') if documentDimension is not None else None
    return params or None, data

def _prepare_UpdateByBufferDocumentDimensionDocumentNumber(*, documentNumber, buffer, documentDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["buffer"] = buffer
    data = serialize_request_body(documentDimension, prefer_model_dump=True, validate=validate, body_name='documentDimension') if documentDimension is not None else None
    return params or None, data

def _prepare_UpdateByDocumentDimensionsDocumentId(*, documentId, documentDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = serialize_request_body(documentDimensions, prefer_model_dump=False, validate=validate, body_name='documentDimensions') if documentDimensions is not None else None
    return params or None, data

def _prepare_UpdateByBufferDocumentDimensionsDocumentNumber(*, documentNumber, buffer, documentDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["buffer"] = buffer
    data = serialize_request_body(documentDimensions, prefer_model_dump=False, validate=validate, body_name='documentDimensions') if documentDimensions is not None else None
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

def _prepare_GetAspects(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_GetAspectsByBufferDocumentNumber(*, documentNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_UpdateAspect(*, aspectPosition = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(aspectPosition, prefer_model_dump=True, validate=validate, body_name='aspectPosition') if aspectPosition is not None else None
    return params or None, data
