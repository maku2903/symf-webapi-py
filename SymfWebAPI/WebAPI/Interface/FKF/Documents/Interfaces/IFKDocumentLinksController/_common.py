from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_AddNew(*, documentId, yearId, newDocumentLink = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    params["yearId"] = yearId
    data = serialize_request_body(newDocumentLink, prefer_model_dump=True, validate=validate, body_name='newDocumentLink') if newDocumentLink is not None else None
    return params or None, data

def _prepare_Update(*, documentId, yearId, newDocumentLink = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    params["yearId"] = yearId
    data = serialize_request_body(newDocumentLink, prefer_model_dump=True, validate=validate, body_name='newDocumentLink') if newDocumentLink is not None else None
    return params or None, data
