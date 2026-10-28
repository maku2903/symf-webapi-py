from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Create(*, map = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(map, prefer_model_dump=True, validate=validate, body_name='map') if map is not None else None
    return params or None, data

def _prepare_Delete(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetByCountry(*, countryId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["countryId"] = countryId
    data = None
    return params or None, data

def _prepare_GetByErpProduct(*, erpProductId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["erpProductId"] = erpProductId
    data = None
    return params or None, data

def _prepare_GetByShopProduct(*, shopProductId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["shopProductId"] = shopProductId
    data = None
    return params or None, data
