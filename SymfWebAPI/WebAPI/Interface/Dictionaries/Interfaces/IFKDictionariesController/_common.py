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

def _prepare_AddNew(*, dictionaryId, element = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dictionaryId"] = dictionaryId
    data = serialize_request_body(element, prefer_model_dump=True, validate=validate, body_name='element') if element is not None else None
    return params or None, data

def _prepare_Update(*, dictionaryId, element = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dictionaryId"] = dictionaryId
    data = serialize_request_body(element, prefer_model_dump=True, validate=validate, body_name='element') if element is not None else None
    return params or None, data

def _prepare_SetElementPosition(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_SetElementPositionByIdPosition(*, id, position) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["position"] = position
    data = None
    return params or None, data

def _prepare_SetContractorPosition(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_SetContractorPositionByIdPosition(*, id, position) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["position"] = position
    data = None
    return params or None, data

def _prepare_GetBusiness(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_AddNewBusiness(*, dictionaryId, element = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dictionaryId"] = dictionaryId
    data = serialize_request_body(element, prefer_model_dump=True, validate=validate, body_name='element') if element is not None else None
    return params or None, data

def _prepare_UpdateBusiness(*, dictionaryId, element = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dictionaryId"] = dictionaryId
    data = serialize_request_body(element, prefer_model_dump=True, validate=validate, body_name='element') if element is not None else None
    return params or None, data
