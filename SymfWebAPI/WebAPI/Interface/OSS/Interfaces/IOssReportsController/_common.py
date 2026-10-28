from __future__ import annotations

from typing import Any

def _prepare_GetOrderPDF(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_GetSaleDocumentPDF(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_GetWarehouseDocumentPDF(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data
