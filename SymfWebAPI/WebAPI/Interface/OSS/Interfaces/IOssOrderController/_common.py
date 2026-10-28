from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_AddNew(*, issue, order = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["issue"] = issue
    data = serialize_request_body(order, prefer_model_dump=True, validate=validate, body_name='order') if order is not None else None
    return params or None, data

def _prepare_IssueFV(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_IssueWZ(*, orderId, inBuffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    params["inBuffer"] = inBuffer
    data = None
    return params or None, data
