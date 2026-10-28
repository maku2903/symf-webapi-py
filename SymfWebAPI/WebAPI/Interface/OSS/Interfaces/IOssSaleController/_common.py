from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_AddNew(*, issue, invoiceKind, saleDocument = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["issue"] = issue
    params["invoiceKind"] = invoiceKind
    data = serialize_request_body(saleDocument, prefer_model_dump=True, validate=validate, body_name='saleDocument') if saleDocument is not None else None
    return params or None, data

def _prepare_AddNewReceipt(*, issue, invoiceKind, receipt = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["issue"] = issue
    params["invoiceKind"] = invoiceKind
    data = serialize_request_body(receipt, prefer_model_dump=True, validate=validate, body_name='receipt') if receipt is not None else None
    return params or None, data

def _prepare_IssueWZ(*, documentId, inBuffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    params["inBuffer"] = inBuffer
    data = None
    return params or None, data
