from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_AddNew(*, issue, invoiceKind, document = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["issue"] = issue
    params["invoiceKind"] = invoiceKind
    data = serialize_request_body(document, prefer_model_dump=True, validate=validate, body_name='document') if document is not None else None
    return params or None, data

def _prepare_IssueAdvancePayment(*, contractId, invoiceKind) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractId"] = contractId
    params["invoiceKind"] = invoiceKind
    data = None
    return params or None, data

def _prepare_IssueContractInvoice(*, contractId, invoiceKind) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractId"] = contractId
    params["invoiceKind"] = invoiceKind
    data = None
    return params or None, data
