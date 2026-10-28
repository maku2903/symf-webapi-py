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

def _prepare_GetListByContractor(*, contractorId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByContractorByContractorCodeDateFromDateTo(*, contractorCode, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByWarehouse(*, warehouseId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["warehouseId"] = warehouseId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByWarehouseByDateFromDateToWarehouseCode(*, warehouseCode, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["warehouseCode"] = warehouseCode
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

def _prepare_GetFV(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_GetFVByBufferDocumentNumber(*, documentNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["buffer"] = buffer
    data = None
    return params or None, data

def _prepare_GetStatus(*, documentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = None
    return params or None, data

def _prepare_GetStatusByBufferDocumentNumber(*, documentNumber, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
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

def _prepare_GetWarehouseRegistries() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetPWDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetRWDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetWZODocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetPZODocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetMMMinusDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetDocumentSeries(*, documentTypeId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentTypeId"] = documentTypeId
    data = None
    return params or None, data

def _prepare_GetPDF(*, documentId, printNote) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    params["printNote"] = printNote
    data = None
    return params or None, data

def _prepare_GetPDFByBufferDocumentNumberPrintNote(*, documentNumber, buffer, printNote) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["buffer"] = buffer
    params["printNote"] = printNote
    data = None
    return params or None, data

def _prepare_GetPagedDocument(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data

def _prepare_GetPDFByDocumentIdSettings(*, documentId, settings = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    data = serialize_request_body(settings, prefer_model_dump=True, validate=validate, body_name='settings') if settings is not None else None
    return params or None, data

def _prepare_GetPDFByBufferDocumentNumberSettings(*, documentNumber, buffer, settings = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
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
