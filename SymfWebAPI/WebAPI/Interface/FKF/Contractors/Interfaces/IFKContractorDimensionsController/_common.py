from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

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

def _prepare_UpdateById(*, contractorId, contractorDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = serialize_request_body(contractorDimension, prefer_model_dump=True, validate=validate, body_name='contractorDimension') if contractorDimension is not None else None
    return params or None, data

def _prepare_UpdateByPosition(*, contractorPosition, contractorDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    data = serialize_request_body(contractorDimension, prefer_model_dump=True, validate=validate, body_name='contractorDimension') if contractorDimension is not None else None
    return params or None, data

def _prepare_UpdateByCode(*, contractorCode, contractorDimension = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = serialize_request_body(contractorDimension, prefer_model_dump=True, validate=validate, body_name='contractorDimension') if contractorDimension is not None else None
    return params or None, data

def _prepare_UpdateByIdByContractorDimensionsContractorId(*, contractorId, contractorDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = serialize_request_body(contractorDimensions, prefer_model_dump=False, validate=validate, body_name='contractorDimensions') if contractorDimensions is not None else None
    return params or None, data

def _prepare_UpdateByPositionByContractorDimensionsContractorPosition(*, contractorPosition, contractorDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    data = serialize_request_body(contractorDimensions, prefer_model_dump=False, validate=validate, body_name='contractorDimensions') if contractorDimensions is not None else None
    return params or None, data

def _prepare_UpdateByCodeByContractorCodeContractorDimensions(*, contractorCode, contractorDimensions = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = serialize_request_body(contractorDimensions, prefer_model_dump=False, validate=validate, body_name='contractorDimensions') if contractorDimensions is not None else None
    return params or None, data

def _prepare_GetClassification() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data
