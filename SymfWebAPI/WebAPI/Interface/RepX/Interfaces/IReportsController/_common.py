from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get(*, reportId, objectId, data = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["reportId"] = reportId
    params["objectId"] = objectId
    data = serialize_request_body(data, prefer_model_dump=True, validate=validate, body_name='data') if data is not None else None
    return params or None, data

def _prepare_GetDefinitions() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data
