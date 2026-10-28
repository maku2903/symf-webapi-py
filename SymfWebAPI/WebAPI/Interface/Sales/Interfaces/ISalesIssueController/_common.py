from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_AddNew(*, issue, document = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["issue"] = issue
    data = serialize_request_body(document, prefer_model_dump=True, validate=validate, body_name='document') if document is not None else None
    return params or None, data

def _prepare_AddNewByCorrectionIssue(*, issue, correction = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["issue"] = issue
    data = serialize_request_body(correction, prefer_model_dump=True, validate=validate, body_name='correction') if correction is not None else None
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

def _prepare_IssueAdvancePayment(*, documentId, options = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = serialize_request_body(options, prefer_model_dump=True, validate=validate, body_name='options') if options is not None else None
    return params or None, data

def _prepare_IssueAdvancePaymentByDocumentNumberOptions(*, documentNumber, options = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    data = serialize_request_body(options, prefer_model_dump=True, validate=validate, body_name='options') if options is not None else None
    return params or None, data

def _prepare_IssueWZ(*, documentId, inBuffer = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    if inBuffer is not None:
        params["inBuffer"] = inBuffer
    data = None
    return params or None, data

def _prepare_IssueWZByDocumentNumberInBuffer(*, documentNumber, inBuffer = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    if inBuffer is not None:
        params["inBuffer"] = inBuffer
    data = None
    return params or None, data

def _prepare_IssueWZCorrection(*, documentId, issue) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    params["issue"] = issue
    data = None
    return params or None, data

def _prepare_IssueWZCorrectionByDocumentNumberIssue(*, documentNumber, issue) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["issue"] = issue
    data = None
    return params or None, data

def _prepare_ChangeDocumentNumber(*, id, number) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["number"] = number
    data = None
    return params or None, data

def _prepare_IssuePN(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_IssuePNByDocumentNumber(*, documentNumber) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    data = None
    return params or None, data

def _prepare_ChangeFiscalStatus(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_ChangeFiscalStatusByDocumentNumber(*, documentNumber) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    data = None
    return params or None, data
