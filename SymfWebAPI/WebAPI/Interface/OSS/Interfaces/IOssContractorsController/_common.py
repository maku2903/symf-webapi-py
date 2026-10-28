from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_AddNew(*, syncFk, contractor = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["syncFk"] = syncFk
    data = serialize_request_body(contractor, prefer_model_dump=True, validate=validate, body_name='contractor') if contractor is not None else None
    return params or None, data

def _prepare_Update(*, syncFk, contractor = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["syncFk"] = syncFk
    data = serialize_request_body(contractor, prefer_model_dump=True, validate=validate, body_name='contractor') if contractor is not None else None
    return params or None, data
