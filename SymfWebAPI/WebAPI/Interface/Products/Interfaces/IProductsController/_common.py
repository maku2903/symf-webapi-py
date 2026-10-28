from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_GetByCode(*, code) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["code"] = code
    data = None
    return params or None, data

def _prepare_GetGet() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetBySalePrices(*, salePrices) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["salePrices"] = salePrices
    data = None
    return params or None, data

def _prepare_GetWithSalePrices() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetWithDimensions() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_Filter(*, salePrices, criteria = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["salePrices"] = salePrices
    data = serialize_request_body(criteria, prefer_model_dump=True, validate=validate, body_name='criteria') if criteria is not None else None
    return params or None, data

def _prepare_FilterWithSalePrices(*, criteria = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteria, prefer_model_dump=True, validate=validate, body_name='criteria') if criteria is not None else None
    return params or None, data

def _prepare_FilterWithDimensions(*, criteria = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteria, prefer_model_dump=True, validate=validate, body_name='criteria') if criteria is not None else None
    return params or None, data

def _prepare_AddNew(*, product = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(product, prefer_model_dump=True, validate=validate, body_name='product') if product is not None else None
    return params or None, data

def _prepare_Update(*, product = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(product, prefer_model_dump=True, validate=validate, body_name='product') if product is not None else None
    return params or None, data

def _prepare_GetMarkers() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetKinds() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetCatalogs() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_IncrementalSync(*, dateFrom) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dateFrom"] = dateFrom
    data = None
    return params or None, data

def _prepare_GetBarcodes(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_GetBarcodesByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data

def _prepare_UpdateBarcodes(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_UpdateBarcodesByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data

def _prepare_FilterSql(*, criteriaFilter = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteriaFilter, prefer_model_dump=True, validate=validate, body_name='criteriaFilter') if criteriaFilter is not None else None
    return params or None, data

def _prepare_GetPagedDocument(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data

def _prepare_GetPageWithSalePrices(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data

def _prepare_GetPageWithDimensions(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data

def _prepare_FilterSqlWthSalePrices(*, criteriaFilter = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteriaFilter, prefer_model_dump=True, validate=validate, body_name='criteriaFilter') if criteriaFilter is not None else None
    return params or None, data

def _prepare_FilterSqlWthDimensions(*, criteriaFilter = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteriaFilter, prefer_model_dump=True, validate=validate, body_name='criteriaFilter') if criteriaFilter is not None else None
    return params or None, data

def _prepare_GetLogisticFields(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_GetLogisticFieldsByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data
