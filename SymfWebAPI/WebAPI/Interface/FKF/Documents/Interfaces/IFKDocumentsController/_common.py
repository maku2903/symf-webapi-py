from __future__ import annotations

from typing import Any

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetByIdYearId(*, id, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["yearId"] = yearId
    data = None
    return params or None, data

def _prepare_GetV2(*, id, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    params["yearId"] = yearId
    data = None
    return params or None, data

def _prepare_GetFromBuffer(*, yearId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetFromAccountingBooks(*, yearId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetFromSchemes(*, yearId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetFromBufferByContractorPositionDateFromDateToYearId(*, yearId, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetFromAccountingBooksByContractorPositionDateFromDateToYearId(*, yearId, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetFromSchemesByContractorPositionDateFromDateToYearId(*, yearId, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDocumentFeatures() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetDocumentFeaturesByYearId(*, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    data = None
    return params or None, data

def _prepare_GetDocumentRecordFeatures() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetDocumentRecordFeaturesByYearId(*, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    data = None
    return params or None, data

def _prepare_GetDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetDocumentTypesByYearId(*, yearId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["yearId"] = yearId
    data = None
    return params or None, data

def _prepare_GetMarkers() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetPagedDocument(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data

def _prepare_GetDocumentTransactions() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data
