from __future__ import annotations

from typing import Any

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
