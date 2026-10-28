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

def _prepare_GetByPosition(*, position) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["position"] = position
    data = None
    return params or None, data

def _prepare_GetByCode(*, code) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["code"] = code
    data = None
    return params or None, data

def _prepare_AddNew(*, employee = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(employee, prefer_model_dump=True, validate=validate, body_name='employee') if employee is not None else None
    return params or None, data

def _prepare_Update(*, employee = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(employee, prefer_model_dump=True, validate=validate, body_name='employee') if employee is not None else None
    return params or None, data

def _prepare_GetPagedDocument(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data
