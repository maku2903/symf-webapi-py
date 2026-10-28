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

def _prepare_IssuePZ(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_IssuePZByDocumentNumber(*, documentNumber) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    data = None
    return params or None, data

def _prepare_IssuePZCorrection(*, documentId, issue) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    params["issue"] = issue
    data = None
    return params or None, data

def _prepare_IssuePZCorrectionByDocumentNumberIssue(*, documentNumber, issue) -> tuple[dict[str, Any] | None, Any]:
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
