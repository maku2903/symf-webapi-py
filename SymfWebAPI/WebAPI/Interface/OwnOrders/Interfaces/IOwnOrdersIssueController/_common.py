from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_AddNew(*, issue, order = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["issue"] = issue
    data = serialize_request_body(order, prefer_model_dump=True, validate=validate, body_name='order') if order is not None else None
    return params or None, data

def _prepare_Delete(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_DeleteByBufferNumber(*, number, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["number"] = number
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_Issue(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_IssueByNumber(*, number) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["number"] = number
    data = None
    return params or None, data

def _prepare_IssuePZ(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_IssuePZByOrderNumber(*, orderNumber) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    data = None
    return params or None, data

def _prepare_ChangeDocumentNumber(*, id, number) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["number"] = number
    data = None
    return params or None, data

def _prepare_IssueFV(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_IssueFVByOrderNumber(*, orderNumber) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    data = None
    return params or None, data
