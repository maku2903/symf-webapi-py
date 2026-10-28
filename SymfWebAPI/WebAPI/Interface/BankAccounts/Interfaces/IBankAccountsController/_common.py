from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get(*, id) -> tuple[dict[str, Any] | None, Any]:
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

def _prepare_Insert(*, contractorId, bankAccount = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = serialize_request_body(bankAccount, prefer_model_dump=True, validate=validate, body_name='bankAccount') if bankAccount is not None else None
    return params or None, data

def _prepare_InsertByBankAccountContractorCode(*, contractorCode, bankAccount = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = serialize_request_body(bankAccount, prefer_model_dump=True, validate=validate, body_name='bankAccount') if bankAccount is not None else None
    return params or None, data

def _prepare_Update(*, bankAccount = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(bankAccount, prefer_model_dump=True, validate=validate, body_name='bankAccount') if bankAccount is not None else None
    return params or None, data

def _prepare_SetAsMain(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data
