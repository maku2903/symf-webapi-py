from __future__ import annotations

from typing import Any, List, Optional, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import Document
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import DocumentListElement
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import DocumentType
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import DocumentV2
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import Feature
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Marker
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Transactions import TransactionDocument
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetByIdYearId,
    _prepare_GetV2,
    _prepare_GetFromBuffer,
    _prepare_GetFromAccountingBooks,
    _prepare_GetFromSchemes,
    _prepare_GetFromBufferByContractorPositionDateFromDateToYearId,
    _prepare_GetFromAccountingBooksByContractorPositionDateFromDateToYearId,
    _prepare_GetFromSchemesByContractorPositionDateFromDateToYearId,
    _prepare_GetDocumentFeatures,
    _prepare_GetDocumentFeaturesByYearId,
    _prepare_GetDocumentRecordFeatures,
    _prepare_GetDocumentRecordFeaturesByYearId,
    _prepare_GetDocumentTypes,
    _prepare_GetDocumentTypesByYearId,
    _prepare_GetMarkers,
    _prepare_GetPagedDocument,
    _prepare_GetDocumentTransactions,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByIdYearId,
    OP_GetByIdYearId_RAW,
    OP_GetV2,
    OP_GetV2_RAW,
    OP_GetFromBuffer,
    OP_GetFromBuffer_RAW,
    OP_GetFromAccountingBooks,
    OP_GetFromAccountingBooks_RAW,
    OP_GetFromSchemes,
    OP_GetFromSchemes_RAW,
    OP_GetFromBufferByContractorPositionDateFromDateToYearId,
    OP_GetFromBufferByContractorPositionDateFromDateToYearId_RAW,
    OP_GetFromAccountingBooksByContractorPositionDateFromDateToYearId,
    OP_GetFromAccountingBooksByContractorPositionDateFromDateToYearId_RAW,
    OP_GetFromSchemesByContractorPositionDateFromDateToYearId,
    OP_GetFromSchemesByContractorPositionDateFromDateToYearId_RAW,
    OP_GetDocumentFeatures,
    OP_GetDocumentFeatures_RAW,
    OP_GetDocumentFeaturesByYearId,
    OP_GetDocumentFeaturesByYearId_RAW,
    OP_GetDocumentRecordFeatures,
    OP_GetDocumentRecordFeatures_RAW,
    OP_GetDocumentRecordFeaturesByYearId,
    OP_GetDocumentRecordFeaturesByYearId_RAW,
    OP_GetDocumentTypes,
    OP_GetDocumentTypes_RAW,
    OP_GetDocumentTypesByYearId,
    OP_GetDocumentTypesByYearId_RAW,
    OP_GetMarkers,
    OP_GetMarkers_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
    OP_GetDocumentTransactions,
    OP_GetDocumentTransactions_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Document]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Document]: ...
def Get(api: object, id: object = _UNSET, yearId: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'yearId' if yearId is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'id', 'yearId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByIdYearId'
        exact_match_name = 'GetByIdYearId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'Get'))
        if {'id', 'yearId'}.issubset(provided_names) and provided_names.issubset({'id', 'yearId'}):
            candidates.append((2, -2, 'GetByIdYearId'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get()
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByIdYearId':
        params, data = _prepare_GetByIdYearId(id=id, yearId=yearId)
        return invoke_operation(api, OP_GetByIdYearId if validate else OP_GetByIdYearId_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetV2(api: SyncInvokerProtocol, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[DocumentV2]: ...
@overload
def GetV2(api: SyncRequestProtocol, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[DocumentV2]: ...
def GetV2(api: object, id: int, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetV2(id=id, yearId=yearId)
    return invoke_operation(api, OP_GetV2 if validate else OP_GetV2_RAW, params=params, data=data)

@overload
def GetFromBuffer(api: SyncInvokerProtocol, yearId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromBuffer(api: SyncRequestProtocol, yearId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromBuffer(api: SyncInvokerProtocol, yearId: int, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromBuffer(api: SyncRequestProtocol, yearId: int, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
def GetFromBuffer(api: object, yearId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, contractorPosition: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'yearId' if yearId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'contractorPosition' if contractorPosition is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo', 'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetFromBuffer(): ambiguous overload for provided arguments")
        exact_match = 'GetFromBuffer'
        exact_match_name = 'GetFromBuffer'
    if provided_names == {'contractorPosition', 'dateFrom', 'dateTo', 'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetFromBuffer(): ambiguous overload for provided arguments")
        exact_match = 'GetFromBufferByContractorPositionDateFromDateToYearId'
        exact_match_name = 'GetFromBufferByContractorPositionDateFromDateToYearId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'yearId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'yearId'}):
            candidates.append((1, -3, 'GetFromBuffer'))
        if {'contractorPosition', 'yearId'}.issubset(provided_names) and provided_names.issubset({'contractorPosition', 'dateFrom', 'dateTo', 'yearId'}):
            candidates.append((2, -4, 'GetFromBufferByContractorPositionDateFromDateToYearId'))
        if not candidates:
            raise TypeError("GetFromBuffer(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetFromBuffer(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetFromBuffer':
        params, data = _prepare_GetFromBuffer(yearId=yearId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetFromBuffer if validate else OP_GetFromBuffer_RAW, params=params, data=data)
    if selected == 'GetFromBufferByContractorPositionDateFromDateToYearId':
        params, data = _prepare_GetFromBufferByContractorPositionDateFromDateToYearId(yearId=yearId, contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetFromBufferByContractorPositionDateFromDateToYearId if validate else OP_GetFromBufferByContractorPositionDateFromDateToYearId_RAW, params=params, data=data)
    raise TypeError("GetFromBuffer(): internal overload dispatch failure")

@overload
def GetFromAccountingBooks(api: SyncInvokerProtocol, yearId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromAccountingBooks(api: SyncRequestProtocol, yearId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromAccountingBooks(api: SyncInvokerProtocol, yearId: int, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromAccountingBooks(api: SyncRequestProtocol, yearId: int, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
def GetFromAccountingBooks(api: object, yearId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, contractorPosition: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'yearId' if yearId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'contractorPosition' if contractorPosition is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo', 'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetFromAccountingBooks(): ambiguous overload for provided arguments")
        exact_match = 'GetFromAccountingBooks'
        exact_match_name = 'GetFromAccountingBooks'
    if provided_names == {'contractorPosition', 'dateFrom', 'dateTo', 'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetFromAccountingBooks(): ambiguous overload for provided arguments")
        exact_match = 'GetFromAccountingBooksByContractorPositionDateFromDateToYearId'
        exact_match_name = 'GetFromAccountingBooksByContractorPositionDateFromDateToYearId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'yearId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'yearId'}):
            candidates.append((1, -3, 'GetFromAccountingBooks'))
        if {'contractorPosition', 'yearId'}.issubset(provided_names) and provided_names.issubset({'contractorPosition', 'dateFrom', 'dateTo', 'yearId'}):
            candidates.append((2, -4, 'GetFromAccountingBooksByContractorPositionDateFromDateToYearId'))
        if not candidates:
            raise TypeError("GetFromAccountingBooks(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetFromAccountingBooks(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetFromAccountingBooks':
        params, data = _prepare_GetFromAccountingBooks(yearId=yearId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetFromAccountingBooks if validate else OP_GetFromAccountingBooks_RAW, params=params, data=data)
    if selected == 'GetFromAccountingBooksByContractorPositionDateFromDateToYearId':
        params, data = _prepare_GetFromAccountingBooksByContractorPositionDateFromDateToYearId(yearId=yearId, contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetFromAccountingBooksByContractorPositionDateFromDateToYearId if validate else OP_GetFromAccountingBooksByContractorPositionDateFromDateToYearId_RAW, params=params, data=data)
    raise TypeError("GetFromAccountingBooks(): internal overload dispatch failure")

@overload
def GetFromSchemes(api: SyncInvokerProtocol, yearId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromSchemes(api: SyncRequestProtocol, yearId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromSchemes(api: SyncInvokerProtocol, yearId: int, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
@overload
def GetFromSchemes(api: SyncRequestProtocol, yearId: int, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentListElement]]: ...
def GetFromSchemes(api: object, yearId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, contractorPosition: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'yearId' if yearId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'contractorPosition' if contractorPosition is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo', 'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetFromSchemes(): ambiguous overload for provided arguments")
        exact_match = 'GetFromSchemes'
        exact_match_name = 'GetFromSchemes'
    if provided_names == {'contractorPosition', 'dateFrom', 'dateTo', 'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetFromSchemes(): ambiguous overload for provided arguments")
        exact_match = 'GetFromSchemesByContractorPositionDateFromDateToYearId'
        exact_match_name = 'GetFromSchemesByContractorPositionDateFromDateToYearId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'yearId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'yearId'}):
            candidates.append((1, -3, 'GetFromSchemes'))
        if {'contractorPosition', 'yearId'}.issubset(provided_names) and provided_names.issubset({'contractorPosition', 'dateFrom', 'dateTo', 'yearId'}):
            candidates.append((2, -4, 'GetFromSchemesByContractorPositionDateFromDateToYearId'))
        if not candidates:
            raise TypeError("GetFromSchemes(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetFromSchemes(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetFromSchemes':
        params, data = _prepare_GetFromSchemes(yearId=yearId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetFromSchemes if validate else OP_GetFromSchemes_RAW, params=params, data=data)
    if selected == 'GetFromSchemesByContractorPositionDateFromDateToYearId':
        params, data = _prepare_GetFromSchemesByContractorPositionDateFromDateToYearId(yearId=yearId, contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetFromSchemesByContractorPositionDateFromDateToYearId if validate else OP_GetFromSchemesByContractorPositionDateFromDateToYearId_RAW, params=params, data=data)
    raise TypeError("GetFromSchemes(): internal overload dispatch failure")

@overload
def GetDocumentFeatures(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Feature]]: ...
@overload
def GetDocumentFeatures(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Feature]]: ...
@overload
def GetDocumentFeatures(api: SyncInvokerProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[Feature]]: ...
@overload
def GetDocumentFeatures(api: SyncRequestProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[Feature]]: ...
def GetDocumentFeatures(api: object, yearId: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'yearId' if yearId is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("GetDocumentFeatures(): ambiguous overload for provided arguments")
        exact_match = 'GetDocumentFeatures'
        exact_match_name = 'GetDocumentFeatures'
    if provided_names == {'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetDocumentFeatures(): ambiguous overload for provided arguments")
        exact_match = 'GetDocumentFeaturesByYearId'
        exact_match_name = 'GetDocumentFeaturesByYearId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'GetDocumentFeatures'))
        if {'yearId'}.issubset(provided_names) and provided_names.issubset({'yearId'}):
            candidates.append((1, -1, 'GetDocumentFeaturesByYearId'))
        if not candidates:
            raise TypeError("GetDocumentFeatures(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetDocumentFeatures(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetDocumentFeatures':
        params, data = _prepare_GetDocumentFeatures()
        return invoke_operation(api, OP_GetDocumentFeatures if validate else OP_GetDocumentFeatures_RAW, params=params, data=data)
    if selected == 'GetDocumentFeaturesByYearId':
        params, data = _prepare_GetDocumentFeaturesByYearId(yearId=yearId)
        return invoke_operation(api, OP_GetDocumentFeaturesByYearId if validate else OP_GetDocumentFeaturesByYearId_RAW, params=params, data=data)
    raise TypeError("GetDocumentFeatures(): internal overload dispatch failure")

@overload
def GetDocumentRecordFeatures(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Feature]]: ...
@overload
def GetDocumentRecordFeatures(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Feature]]: ...
@overload
def GetDocumentRecordFeatures(api: SyncInvokerProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[Feature]]: ...
@overload
def GetDocumentRecordFeatures(api: SyncRequestProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[Feature]]: ...
def GetDocumentRecordFeatures(api: object, yearId: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'yearId' if yearId is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("GetDocumentRecordFeatures(): ambiguous overload for provided arguments")
        exact_match = 'GetDocumentRecordFeatures'
        exact_match_name = 'GetDocumentRecordFeatures'
    if provided_names == {'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetDocumentRecordFeatures(): ambiguous overload for provided arguments")
        exact_match = 'GetDocumentRecordFeaturesByYearId'
        exact_match_name = 'GetDocumentRecordFeaturesByYearId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'GetDocumentRecordFeatures'))
        if {'yearId'}.issubset(provided_names) and provided_names.issubset({'yearId'}):
            candidates.append((1, -1, 'GetDocumentRecordFeaturesByYearId'))
        if not candidates:
            raise TypeError("GetDocumentRecordFeatures(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetDocumentRecordFeatures(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetDocumentRecordFeatures':
        params, data = _prepare_GetDocumentRecordFeatures()
        return invoke_operation(api, OP_GetDocumentRecordFeatures if validate else OP_GetDocumentRecordFeatures_RAW, params=params, data=data)
    if selected == 'GetDocumentRecordFeaturesByYearId':
        params, data = _prepare_GetDocumentRecordFeaturesByYearId(yearId=yearId)
        return invoke_operation(api, OP_GetDocumentRecordFeaturesByYearId if validate else OP_GetDocumentRecordFeaturesByYearId_RAW, params=params, data=data)
    raise TypeError("GetDocumentRecordFeatures(): internal overload dispatch failure")

@overload
def GetDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetDocumentTypes(api: SyncInvokerProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetDocumentTypes(api: SyncRequestProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetDocumentTypes(api: object, yearId: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'yearId' if yearId is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("GetDocumentTypes(): ambiguous overload for provided arguments")
        exact_match = 'GetDocumentTypes'
        exact_match_name = 'GetDocumentTypes'
    if provided_names == {'yearId'}:
        if exact_match_name is not None:
            raise TypeError("GetDocumentTypes(): ambiguous overload for provided arguments")
        exact_match = 'GetDocumentTypesByYearId'
        exact_match_name = 'GetDocumentTypesByYearId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'GetDocumentTypes'))
        if {'yearId'}.issubset(provided_names) and provided_names.issubset({'yearId'}):
            candidates.append((1, -1, 'GetDocumentTypesByYearId'))
        if not candidates:
            raise TypeError("GetDocumentTypes(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetDocumentTypes(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetDocumentTypes':
        params, data = _prepare_GetDocumentTypes()
        return invoke_operation(api, OP_GetDocumentTypes if validate else OP_GetDocumentTypes_RAW, params=params, data=data)
    if selected == 'GetDocumentTypesByYearId':
        params, data = _prepare_GetDocumentTypesByYearId(yearId=yearId)
        return invoke_operation(api, OP_GetDocumentTypesByYearId if validate else OP_GetDocumentTypesByYearId_RAW, params=params, data=data)
    raise TypeError("GetDocumentTypes(): internal overload dispatch failure")

@overload
def GetMarkers(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Marker]]: ...
@overload
def GetMarkers(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Marker]]: ...
def GetMarkers(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetMarkers()
    return invoke_operation(api, OP_GetMarkers if validate else OP_GetMarkers_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

@overload
def GetDocumentTransactions(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[TransactionDocument]]: ...
@overload
def GetDocumentTransactions(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[TransactionDocument]]: ...
def GetDocumentTransactions(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentTransactions()
    return invoke_operation(api, OP_GetDocumentTransactions if validate else OP_GetDocumentTransactions_RAW, params=params, data=data)

__all__ = ["Get", "GetV2", "GetFromBuffer", "GetFromAccountingBooks", "GetFromSchemes", "GetDocumentFeatures", "GetDocumentRecordFeatures", "GetDocumentTypes", "GetMarkers", "GetPagedDocument", "GetDocumentTransactions"]
