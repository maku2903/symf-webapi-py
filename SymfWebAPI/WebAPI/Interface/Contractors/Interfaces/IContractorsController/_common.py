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

def _prepare_GetByNIP(*, nip) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["nip"] = nip
    data = None
    return params or None, data

def _prepare_GetByPesel(*, pesel) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["pesel"] = pesel
    data = None
    return params or None, data

def _prepare_GetByPosition(*, position) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["position"] = position
    data = None
    return params or None, data

def _prepare_GetByNIPAndPosition(*, nip, position) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["nip"] = nip
    params["position"] = position
    data = None
    return params or None, data

def _prepare_GetGet() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetWithDimensions() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_Filter(*, criteria = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteria, prefer_model_dump=True, validate=validate, body_name='criteria') if criteria is not None else None
    return params or None, data

def _prepare_FilterWithDimensions(*, criteria = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteria, prefer_model_dump=True, validate=validate, body_name='criteria') if criteria is not None else None
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

def _prepare_SyncFK(*, contractorId, isNew) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    params["isNew"] = isNew
    data = None
    return params or None, data

def _prepare_SyncFKByContractorCodeIsNew(*, contractorCode, isNew) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    params["isNew"] = isNew
    data = None
    return params or None, data

def _prepare_IncrementalSync(*, dateFrom) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["dateFrom"] = dateFrom
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

def _prepare_GetPagedDocumentWithDimensions(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data

def _prepare_FilterSqlWithDimensions(*, criteriaFilter = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteriaFilter, prefer_model_dump=True, validate=validate, body_name='criteriaFilter') if criteriaFilter is not None else None
    return params or None, data
