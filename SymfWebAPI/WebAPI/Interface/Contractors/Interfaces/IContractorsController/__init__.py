from __future__ import annotations

from typing import Any, List, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Catalog
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import Contractor
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorCriteriaFilter
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorFilterCriteria
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorListElement
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorListElementWithDimensions
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import IncrementalSyncListElement
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Kind
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Marker
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetByCode,
    _prepare_GetByNIP,
    _prepare_GetByPesel,
    _prepare_GetByPosition,
    _prepare_GetByNIPAndPosition,
    _prepare_GetGet,
    _prepare_GetWithDimensions,
    _prepare_Filter,
    _prepare_FilterWithDimensions,
    _prepare_AddNew,
    _prepare_Update,
    _prepare_GetMarkers,
    _prepare_GetKinds,
    _prepare_GetCatalogs,
    _prepare_SyncFK,
    _prepare_SyncFKByContractorCodeIsNew,
    _prepare_IncrementalSync,
    _prepare_FilterSql,
    _prepare_GetPagedDocument,
    _prepare_GetPagedDocumentWithDimensions,
    _prepare_FilterSqlWithDimensions,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByCode,
    OP_GetByCode_RAW,
    OP_GetByNIP,
    OP_GetByNIP_RAW,
    OP_GetByPesel,
    OP_GetByPesel_RAW,
    OP_GetByPosition,
    OP_GetByPosition_RAW,
    OP_GetByNIPAndPosition,
    OP_GetByNIPAndPosition_RAW,
    OP_GetGet,
    OP_GetGet_RAW,
    OP_GetWithDimensions,
    OP_GetWithDimensions_RAW,
    OP_Filter,
    OP_Filter_RAW,
    OP_FilterWithDimensions,
    OP_FilterWithDimensions_RAW,
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_GetMarkers,
    OP_GetMarkers_RAW,
    OP_GetKinds,
    OP_GetKinds_RAW,
    OP_GetCatalogs,
    OP_GetCatalogs_RAW,
    OP_SyncFK,
    OP_SyncFK_RAW,
    OP_SyncFKByContractorCodeIsNew,
    OP_SyncFKByContractorCodeIsNew_RAW,
    OP_IncrementalSync,
    OP_IncrementalSync_RAW,
    OP_FilterSql,
    OP_FilterSql_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
    OP_GetPagedDocumentWithDimensions,
    OP_GetPagedDocumentWithDimensions_RAW,
    OP_FilterSqlWithDimensions,
    OP_FilterSqlWithDimensions_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def Get(api: SyncInvokerProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def Get(api: SyncRequestProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
def Get(api: object, id: object = _UNSET, code: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'code' if code is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'code'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByCode'
        exact_match_name = 'GetByCode'
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetGet'
        exact_match_name = 'GetGet'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'Get'))
        if {'code'}.issubset(provided_names) and provided_names.issubset({'code'}):
            candidates.append((1, -1, 'GetByCode'))
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'GetGet'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(id=id)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByCode':
        params, data = _prepare_GetByCode(code=code)
        return invoke_operation(api, OP_GetByCode if validate else OP_GetByCode_RAW, params=params, data=data)
    if selected == 'GetGet':
        params, data = _prepare_GetGet()
        return invoke_operation(api, OP_GetGet if validate else OP_GetGet_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetByNIP(api: SyncInvokerProtocol, nip: str, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
@overload
def GetByNIP(api: SyncRequestProtocol, nip: str, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
def GetByNIP(api: object, nip: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByNIP(nip=nip)
    return invoke_operation(api, OP_GetByNIP if validate else OP_GetByNIP_RAW, params=params, data=data)

@overload
def GetByPesel(api: SyncInvokerProtocol, pesel: str, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
@overload
def GetByPesel(api: SyncRequestProtocol, pesel: str, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
def GetByPesel(api: object, pesel: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByPesel(pesel=pesel)
    return invoke_operation(api, OP_GetByPesel if validate else OP_GetByPesel_RAW, params=params, data=data)

@overload
def GetByPosition(api: SyncInvokerProtocol, position: int, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
@overload
def GetByPosition(api: SyncRequestProtocol, position: int, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
def GetByPosition(api: object, position: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByPosition(position=position)
    return invoke_operation(api, OP_GetByPosition if validate else OP_GetByPosition_RAW, params=params, data=data)

@overload
def GetByNIPAndPosition(api: SyncInvokerProtocol, nip: str, position: int, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
@overload
def GetByNIPAndPosition(api: SyncRequestProtocol, nip: str, position: int, *, validate: bool = True) -> ResponseEnvelope[List[Contractor]]: ...
def GetByNIPAndPosition(api: object, nip: str, position: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByNIPAndPosition(nip=nip, position=position)
    return invoke_operation(api, OP_GetByNIPAndPosition if validate else OP_GetByNIPAndPosition_RAW, params=params, data=data)

@overload
def GetWithDimensions(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElementWithDimensions]]: ...
@overload
def GetWithDimensions(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElementWithDimensions]]: ...
def GetWithDimensions(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWithDimensions()
    return invoke_operation(api, OP_GetWithDimensions if validate else OP_GetWithDimensions_RAW, params=params, data=data)

@overload
def Filter(api: SyncInvokerProtocol, criteria: "ContractorFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
@overload
def Filter(api: SyncRequestProtocol, criteria: "ContractorFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
def Filter(api: object, criteria: "ContractorFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Filter(validate=validate, criteria=criteria)
    return invoke_operation(api, OP_Filter if validate else OP_Filter_RAW, params=params, data=data)

@overload
def FilterWithDimensions(api: SyncInvokerProtocol, criteria: "ContractorFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElementWithDimensions]]: ...
@overload
def FilterWithDimensions(api: SyncRequestProtocol, criteria: "ContractorFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElementWithDimensions]]: ...
def FilterWithDimensions(api: object, criteria: "ContractorFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterWithDimensions(validate=validate, criteria=criteria)
    return invoke_operation(api, OP_FilterWithDimensions if validate else OP_FilterWithDimensions_RAW, params=params, data=data)

@overload
def AddNew(api: SyncInvokerProtocol, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
@overload
def AddNew(api: SyncRequestProtocol, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Contractor]: ...
def AddNew(api: object, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, syncFk=syncFk, contractor=contractor)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, syncFk: bool, contractor: "Contractor", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Update(validate=validate, syncFk=syncFk, contractor=contractor)
    return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)

@overload
def GetMarkers(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Marker]]: ...
@overload
def GetMarkers(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Marker]]: ...
def GetMarkers(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetMarkers()
    return invoke_operation(api, OP_GetMarkers if validate else OP_GetMarkers_RAW, params=params, data=data)

@overload
def GetKinds(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Kind]]: ...
@overload
def GetKinds(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Kind]]: ...
def GetKinds(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetKinds()
    return invoke_operation(api, OP_GetKinds if validate else OP_GetKinds_RAW, params=params, data=data)

@overload
def GetCatalogs(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Catalog]]: ...
@overload
def GetCatalogs(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Catalog]]: ...
def GetCatalogs(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetCatalogs()
    return invoke_operation(api, OP_GetCatalogs if validate else OP_GetCatalogs_RAW, params=params, data=data)

@overload
def SyncFK(api: SyncInvokerProtocol, contractorId: int, isNew: bool, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def SyncFK(api: SyncRequestProtocol, contractorId: int, isNew: bool, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def SyncFK(api: SyncInvokerProtocol, contractorCode: str, isNew: bool, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def SyncFK(api: SyncRequestProtocol, contractorCode: str, isNew: bool, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def SyncFK(api: object, contractorId: object = _UNSET, isNew: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'isNew' if isNew is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorId', 'isNew'}:
        if exact_match_name is not None:
            raise TypeError("SyncFK(): ambiguous overload for provided arguments")
        exact_match = 'SyncFK'
        exact_match_name = 'SyncFK'
    if provided_names == {'isNew', 'contractorCode'}:
        if exact_match_name is not None:
            raise TypeError("SyncFK(): ambiguous overload for provided arguments")
        exact_match = 'SyncFKByContractorCodeIsNew'
        exact_match_name = 'SyncFKByContractorCodeIsNew'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorId', 'isNew'}.issubset(provided_names) and provided_names.issubset({'contractorId', 'isNew'}):
            candidates.append((2, -2, 'SyncFK'))
        if {'isNew', 'contractorCode'}.issubset(provided_names) and provided_names.issubset({'isNew', 'contractorCode'}):
            candidates.append((2, -2, 'SyncFKByContractorCodeIsNew'))
        if not candidates:
            raise TypeError("SyncFK(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("SyncFK(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'SyncFK':
        params, data = _prepare_SyncFK(contractorId=contractorId, isNew=isNew)
        return invoke_operation(api, OP_SyncFK if validate else OP_SyncFK_RAW, params=params, data=data)
    if selected == 'SyncFKByContractorCodeIsNew':
        params, data = _prepare_SyncFKByContractorCodeIsNew(contractorCode=contractorCode, isNew=isNew)
        return invoke_operation(api, OP_SyncFKByContractorCodeIsNew if validate else OP_SyncFKByContractorCodeIsNew_RAW, params=params, data=data)
    raise TypeError("SyncFK(): internal overload dispatch failure")

@overload
def IncrementalSync(api: SyncInvokerProtocol, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[List[IncrementalSyncListElement]]: ...
@overload
def IncrementalSync(api: SyncRequestProtocol, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[List[IncrementalSyncListElement]]: ...
def IncrementalSync(api: object, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IncrementalSync(dateFrom=dateFrom)
    return invoke_operation(api, OP_IncrementalSync if validate else OP_IncrementalSync_RAW, params=params, data=data)

@overload
def FilterSql(api: SyncInvokerProtocol, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
@overload
def FilterSql(api: SyncRequestProtocol, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElement]]: ...
def FilterSql(api: object, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterSql(validate=validate, criteriaFilter=criteriaFilter)
    return invoke_operation(api, OP_FilterSql if validate else OP_FilterSql_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

@overload
def GetPagedDocumentWithDimensions(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocumentWithDimensions(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocumentWithDimensions(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocumentWithDimensions(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocumentWithDimensions if validate else OP_GetPagedDocumentWithDimensions_RAW, params=params, data=data)

@overload
def FilterSqlWithDimensions(api: SyncInvokerProtocol, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElementWithDimensions]]: ...
@overload
def FilterSqlWithDimensions(api: SyncRequestProtocol, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ContractorListElementWithDimensions]]: ...
def FilterSqlWithDimensions(api: object, criteriaFilter: "ContractorCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterSqlWithDimensions(validate=validate, criteriaFilter=criteriaFilter)
    return invoke_operation(api, OP_FilterSqlWithDimensions if validate else OP_FilterSqlWithDimensions_RAW, params=params, data=data)

__all__ = ["Get", "GetByNIP", "GetByPesel", "GetByPosition", "GetByNIPAndPosition", "GetWithDimensions", "Filter", "FilterWithDimensions", "AddNew", "Update", "GetMarkers", "GetKinds", "GetCatalogs", "SyncFK", "IncrementalSync", "FilterSql", "GetPagedDocument", "GetPagedDocumentWithDimensions", "FilterSqlWithDimensions"]
