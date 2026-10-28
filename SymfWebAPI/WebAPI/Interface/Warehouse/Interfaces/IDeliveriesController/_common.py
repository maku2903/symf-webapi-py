from __future__ import annotations

from typing import Any

def _prepare_GetInWarehouse(*, warehouseId, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["warehouseId"] = warehouseId
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_GetInWarehouseByProductCodeWarehouseCode(*, warehouseCode, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["warehouseCode"] = warehouseCode
    params["productCode"] = productCode
    data = None
    return params or None, data
