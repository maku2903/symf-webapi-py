from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetById(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_GetByBufferNumber(*, number, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["number"] = number
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_GetList(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByDeliverer(*, delivererId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["delivererId"] = delivererId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByDelivererByDateFromDateToDelivererCode(*, delivererCode, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["delivererCode"] = delivererCode
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListBySeller(*, sellerId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["sellerId"] = sellerId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListBySellerByDateFromDateToSellerCode(*, sellerCode, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["sellerCode"] = sellerCode
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByDimension(*, dimensionCode, dictionaryValue, value) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dimensionCode"] = dimensionCode
    params["dictionaryValue"] = dictionaryValue
    params["value"] = value
    data = None
    return params or None, data

def _prepare_GetPZ(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_GetPZByBufferOrderNumber(*, orderNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_GetFV(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_GetFVByBufferOrderNumber(*, orderNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_GetPDF(*, orderId, printNote) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    params["printNote"] = printNote
    data = None
    return params or None, data

def _prepare_GetPDFByBufferOrderNumberPrintNote(*, orderNumber, buffer, printNote) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    params["printNote"] = printNote
    data = None
    return params or None, data

def _prepare_GetZMWDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetZWWDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetDocumentSeries(*, documentTypeId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentTypeId"] = documentTypeId
    data = None
    return params or None, data

def _prepare_GetStatus(*, orderId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = None
    return params or None, data

def _prepare_GetStatusByBufferOrderNumber(*, orderNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = None
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

def _prepare_GetPositionRelations(*, positionId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["positionId"] = positionId
    data = None
    return params or None, data

def _prepare_GetPagedDocument(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data

def _prepare_GetPDFByOrderIdSettings(*, orderId, settings = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderId"] = orderId
    data = serialize_request_body(settings, prefer_model_dump=True, validate=validate, body_name='settings') if settings is not None else None
    return params or None, data

def _prepare_GetPDFByBufferOrderNumberSettings(*, orderNumber, buffer, settings = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["orderNumber"] = orderNumber
    params["buffer"] = buffer
    data = serialize_request_body(settings, prefer_model_dump=True, validate=validate, body_name='settings') if settings is not None else None
    return params or None, data

def _prepare_GetDocumentTypesWithRange(*, dateFrom, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data
