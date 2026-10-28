from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetById(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_GetListByContractor(*, contractorId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = None
    return params or None, data

def _prepare_GetListByContractorByContractorCode(*, contractorCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = None
    return params or None, data

def _prepare_GetListByProduct(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_GetListByProductByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data

def _prepare_AddNew(*, reservation = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(reservation, prefer_model_dump=True, validate=validate, body_name='reservation') if reservation is not None else None
    return params or None, data

def _prepare_AdvancedAddNew(*, reservation = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(reservation, prefer_model_dump=True, validate=validate, body_name='reservation') if reservation is not None else None
    return params or None, data

def _prepare_Delete(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_AdvancedDelete(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data
