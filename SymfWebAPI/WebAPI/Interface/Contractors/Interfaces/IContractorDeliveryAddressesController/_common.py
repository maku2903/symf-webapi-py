from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get(*, contractorId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = None
    return params or None, data

def _prepare_GetByContractorCode(*, contractorCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = None
    return params or None, data

def _prepare_AddNew(*, contractorId, contractorDeliveryAddress = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = serialize_request_body(contractorDeliveryAddress, prefer_model_dump=True, validate=validate, body_name='contractorDeliveryAddress') if contractorDeliveryAddress is not None else None
    return params or None, data

def _prepare_AddNewByContractorCodeContractorDeliveryAddress(*, contractorCode, contractorDeliveryAddress = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = serialize_request_body(contractorDeliveryAddress, prefer_model_dump=True, validate=validate, body_name='contractorDeliveryAddress') if contractorDeliveryAddress is not None else None
    return params or None, data

def _prepare_Update(*, contractorId, contractorDeliveryAddress = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = serialize_request_body(contractorDeliveryAddress, prefer_model_dump=True, validate=validate, body_name='contractorDeliveryAddress') if contractorDeliveryAddress is not None else None
    return params or None, data

def _prepare_UpdateByContractorCodeContractorDeliveryAddress(*, contractorCode, contractorDeliveryAddress = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = serialize_request_body(contractorDeliveryAddress, prefer_model_dump=True, validate=validate, body_name='contractorDeliveryAddress') if contractorDeliveryAddress is not None else None
    return params or None, data
