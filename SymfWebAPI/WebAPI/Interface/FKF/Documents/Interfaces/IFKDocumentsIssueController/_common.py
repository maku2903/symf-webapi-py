from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_AddNew(*, documentIssue = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(documentIssue, prefer_model_dump=True, validate=validate, body_name='documentIssue') if documentIssue is not None else None
    return params or None, data

def _prepare_Validate(*, documentIssue = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(documentIssue, prefer_model_dump=True, validate=validate, body_name='documentIssue') if documentIssue is not None else None
    return params or None, data
