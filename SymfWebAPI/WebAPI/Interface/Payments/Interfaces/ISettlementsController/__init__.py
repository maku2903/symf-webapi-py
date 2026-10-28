from __future__ import annotations

from typing import Any, List, Optional, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels import Settlement
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels.Issue import SettlementIssue
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels import SettlementListElement
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByBufferNumber,
    _prepare_GetByDocument,
    _prepare_GetByDocumentByBufferDocumentNumber,
    _prepare_GetListByIssueDate,
    _prepare_GetListByIssueDateByContractorIdDateFromDateTo,
    _prepare_GetListByIssueDateByContractorCodeDateFromDateTo,
    _prepare_GetListByMaturityDate,
    _prepare_GetListByMaturityDateByContractorIdDateFromDateTo,
    _prepare_GetListByMaturityDateByContractorCodeDateFromDateTo,
    _prepare_GetNotSettled,
    _prepare_GetNotSettledByIssueDate,
    _prepare_GetNotSettledByIssueDateByContractorIdDateFromDateTo,
    _prepare_GetNotSettledByIssueDateByContractorCodeDateFromDateTo,
    _prepare_GetNotSettledByMaturityDate,
    _prepare_GetNotSettledByMaturityDateByContractorIdDateFromDateTo,
    _prepare_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo,
    _prepare_Issue,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetById,
    OP_GetById_RAW,
    OP_GetByBufferNumber,
    OP_GetByBufferNumber_RAW,
    OP_GetByDocument,
    OP_GetByDocument_RAW,
    OP_GetByDocumentByBufferDocumentNumber,
    OP_GetByDocumentByBufferDocumentNumber_RAW,
    OP_GetListByIssueDate,
    OP_GetListByIssueDate_RAW,
    OP_GetListByIssueDateByContractorIdDateFromDateTo,
    OP_GetListByIssueDateByContractorIdDateFromDateTo_RAW,
    OP_GetListByIssueDateByContractorCodeDateFromDateTo,
    OP_GetListByIssueDateByContractorCodeDateFromDateTo_RAW,
    OP_GetListByMaturityDate,
    OP_GetListByMaturityDate_RAW,
    OP_GetListByMaturityDateByContractorIdDateFromDateTo,
    OP_GetListByMaturityDateByContractorIdDateFromDateTo_RAW,
    OP_GetListByMaturityDateByContractorCodeDateFromDateTo,
    OP_GetListByMaturityDateByContractorCodeDateFromDateTo_RAW,
    OP_GetNotSettled,
    OP_GetNotSettled_RAW,
    OP_GetNotSettledByIssueDate,
    OP_GetNotSettledByIssueDate_RAW,
    OP_GetNotSettledByIssueDateByContractorIdDateFromDateTo,
    OP_GetNotSettledByIssueDateByContractorIdDateFromDateTo_RAW,
    OP_GetNotSettledByIssueDateByContractorCodeDateFromDateTo,
    OP_GetNotSettledByIssueDateByContractorCodeDateFromDateTo_RAW,
    OP_GetNotSettledByMaturityDate,
    OP_GetNotSettledByMaturityDate_RAW,
    OP_GetNotSettledByMaturityDateByContractorIdDateFromDateTo,
    OP_GetNotSettledByMaturityDateByContractorIdDateFromDateTo_RAW,
    OP_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo,
    OP_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo_RAW,
    OP_Issue,
    OP_Issue_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
@overload
def Get(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
@overload
def Get(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
def Get(api: object, id: object = _UNSET, number: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'number' if number is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetById'
        exact_match_name = 'GetById'
    if provided_names == {'buffer', 'number'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByBufferNumber'
        exact_match_name = 'GetByBufferNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'Get'))
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'GetById'))
        if {'buffer', 'number'}.issubset(provided_names) and provided_names.issubset({'buffer', 'number'}):
            candidates.append((2, -2, 'GetByBufferNumber'))
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
    if selected == 'GetById':
        params, data = _prepare_GetById(id=id)
        return invoke_operation(api, OP_GetById if validate else OP_GetById_RAW, params=params, data=data)
    if selected == 'GetByBufferNumber':
        params, data = _prepare_GetByBufferNumber(number=number, buffer=buffer)
        return invoke_operation(api, OP_GetByBufferNumber if validate else OP_GetByBufferNumber_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetByDocument(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
@overload
def GetByDocument(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
@overload
def GetByDocument(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
@overload
def GetByDocument(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
def GetByDocument(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId'}:
        if exact_match_name is not None:
            raise TypeError("GetByDocument(): ambiguous overload for provided arguments")
        exact_match = 'GetByDocument'
        exact_match_name = 'GetByDocument'
    if provided_names == {'documentNumber', 'buffer'}:
        if exact_match_name is not None:
            raise TypeError("GetByDocument(): ambiguous overload for provided arguments")
        exact_match = 'GetByDocumentByBufferDocumentNumber'
        exact_match_name = 'GetByDocumentByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetByDocument'))
        if {'documentNumber', 'buffer'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'buffer'}):
            candidates.append((2, -2, 'GetByDocumentByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetByDocument(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetByDocument(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetByDocument':
        params, data = _prepare_GetByDocument(documentId=documentId)
        return invoke_operation(api, OP_GetByDocument if validate else OP_GetByDocument_RAW, params=params, data=data)
    if selected == 'GetByDocumentByBufferDocumentNumber':
        params, data = _prepare_GetByDocumentByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetByDocumentByBufferDocumentNumber if validate else OP_GetByDocumentByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetByDocument(): internal overload dispatch failure")

@overload
def GetListByIssueDate(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetListByIssueDate(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetListByIssueDate(api: SyncInvokerProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetListByIssueDate(api: SyncRequestProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetListByIssueDate(api: SyncInvokerProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetListByIssueDate(api: SyncRequestProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def GetListByIssueDate(api: object, dateFrom: object = _UNSET, dateTo: object = _UNSET, contractorId: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'contractorId' if contractorId is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByIssueDate(): ambiguous overload for provided arguments")
        exact_match = 'GetListByIssueDate'
        exact_match_name = 'GetListByIssueDate'
    if provided_names == {'contractorId', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByIssueDate(): ambiguous overload for provided arguments")
        exact_match = 'GetListByIssueDateByContractorIdDateFromDateTo'
        exact_match_name = 'GetListByIssueDateByContractorIdDateFromDateTo'
    if provided_names == {'contractorCode', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByIssueDate(): ambiguous overload for provided arguments")
        exact_match = 'GetListByIssueDateByContractorCodeDateFromDateTo'
        exact_match_name = 'GetListByIssueDateByContractorCodeDateFromDateTo'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo'}):
            candidates.append((0, -2, 'GetListByIssueDate'))
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByIssueDateByContractorIdDateFromDateTo'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByIssueDateByContractorCodeDateFromDateTo'))
        if not candidates:
            raise TypeError("GetListByIssueDate(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByIssueDate(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByIssueDate':
        params, data = _prepare_GetListByIssueDate(dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByIssueDate if validate else OP_GetListByIssueDate_RAW, params=params, data=data)
    if selected == 'GetListByIssueDateByContractorIdDateFromDateTo':
        params, data = _prepare_GetListByIssueDateByContractorIdDateFromDateTo(contractorId=contractorId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByIssueDateByContractorIdDateFromDateTo if validate else OP_GetListByIssueDateByContractorIdDateFromDateTo_RAW, params=params, data=data)
    if selected == 'GetListByIssueDateByContractorCodeDateFromDateTo':
        params, data = _prepare_GetListByIssueDateByContractorCodeDateFromDateTo(contractorCode=contractorCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByIssueDateByContractorCodeDateFromDateTo if validate else OP_GetListByIssueDateByContractorCodeDateFromDateTo_RAW, params=params, data=data)
    raise TypeError("GetListByIssueDate(): internal overload dispatch failure")

@overload
def GetListByMaturityDate(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetListByMaturityDate(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetListByMaturityDate(api: SyncInvokerProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetListByMaturityDate(api: SyncRequestProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetListByMaturityDate(api: SyncInvokerProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetListByMaturityDate(api: SyncRequestProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
def GetListByMaturityDate(api: object, dateFrom: object = _UNSET, dateTo: object = _UNSET, contractorId: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'contractorId' if contractorId is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByMaturityDate(): ambiguous overload for provided arguments")
        exact_match = 'GetListByMaturityDate'
        exact_match_name = 'GetListByMaturityDate'
    if provided_names == {'contractorId', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByMaturityDate(): ambiguous overload for provided arguments")
        exact_match = 'GetListByMaturityDateByContractorIdDateFromDateTo'
        exact_match_name = 'GetListByMaturityDateByContractorIdDateFromDateTo'
    if provided_names == {'contractorCode', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByMaturityDate(): ambiguous overload for provided arguments")
        exact_match = 'GetListByMaturityDateByContractorCodeDateFromDateTo'
        exact_match_name = 'GetListByMaturityDateByContractorCodeDateFromDateTo'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo'}):
            candidates.append((0, -2, 'GetListByMaturityDate'))
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByMaturityDateByContractorIdDateFromDateTo'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByMaturityDateByContractorCodeDateFromDateTo'))
        if not candidates:
            raise TypeError("GetListByMaturityDate(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByMaturityDate(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByMaturityDate':
        params, data = _prepare_GetListByMaturityDate(dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByMaturityDate if validate else OP_GetListByMaturityDate_RAW, params=params, data=data)
    if selected == 'GetListByMaturityDateByContractorIdDateFromDateTo':
        params, data = _prepare_GetListByMaturityDateByContractorIdDateFromDateTo(contractorId=contractorId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByMaturityDateByContractorIdDateFromDateTo if validate else OP_GetListByMaturityDateByContractorIdDateFromDateTo_RAW, params=params, data=data)
    if selected == 'GetListByMaturityDateByContractorCodeDateFromDateTo':
        params, data = _prepare_GetListByMaturityDateByContractorCodeDateFromDateTo(contractorCode=contractorCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByMaturityDateByContractorCodeDateFromDateTo if validate else OP_GetListByMaturityDateByContractorCodeDateFromDateTo_RAW, params=params, data=data)
    raise TypeError("GetListByMaturityDate(): internal overload dispatch failure")

@overload
def GetNotSettled(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetNotSettled(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
def GetNotSettled(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetNotSettled()
    return invoke_operation(api, OP_GetNotSettled if validate else OP_GetNotSettled_RAW, params=params, data=data)

@overload
def GetNotSettledByIssueDate(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetNotSettledByIssueDate(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetNotSettledByIssueDate(api: SyncInvokerProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetNotSettledByIssueDate(api: SyncRequestProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetNotSettledByIssueDate(api: SyncInvokerProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetNotSettledByIssueDate(api: SyncRequestProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def GetNotSettledByIssueDate(api: object, dateFrom: object = _UNSET, dateTo: object = _UNSET, contractorId: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'contractorId' if contractorId is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetNotSettledByIssueDate(): ambiguous overload for provided arguments")
        exact_match = 'GetNotSettledByIssueDate'
        exact_match_name = 'GetNotSettledByIssueDate'
    if provided_names == {'contractorId', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetNotSettledByIssueDate(): ambiguous overload for provided arguments")
        exact_match = 'GetNotSettledByIssueDateByContractorIdDateFromDateTo'
        exact_match_name = 'GetNotSettledByIssueDateByContractorIdDateFromDateTo'
    if provided_names == {'contractorCode', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetNotSettledByIssueDate(): ambiguous overload for provided arguments")
        exact_match = 'GetNotSettledByIssueDateByContractorCodeDateFromDateTo'
        exact_match_name = 'GetNotSettledByIssueDateByContractorCodeDateFromDateTo'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo'}):
            candidates.append((0, -2, 'GetNotSettledByIssueDate'))
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetNotSettledByIssueDateByContractorIdDateFromDateTo'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetNotSettledByIssueDateByContractorCodeDateFromDateTo'))
        if not candidates:
            raise TypeError("GetNotSettledByIssueDate(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetNotSettledByIssueDate(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetNotSettledByIssueDate':
        params, data = _prepare_GetNotSettledByIssueDate(dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetNotSettledByIssueDate if validate else OP_GetNotSettledByIssueDate_RAW, params=params, data=data)
    if selected == 'GetNotSettledByIssueDateByContractorIdDateFromDateTo':
        params, data = _prepare_GetNotSettledByIssueDateByContractorIdDateFromDateTo(contractorId=contractorId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetNotSettledByIssueDateByContractorIdDateFromDateTo if validate else OP_GetNotSettledByIssueDateByContractorIdDateFromDateTo_RAW, params=params, data=data)
    if selected == 'GetNotSettledByIssueDateByContractorCodeDateFromDateTo':
        params, data = _prepare_GetNotSettledByIssueDateByContractorCodeDateFromDateTo(contractorCode=contractorCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetNotSettledByIssueDateByContractorCodeDateFromDateTo if validate else OP_GetNotSettledByIssueDateByContractorCodeDateFromDateTo_RAW, params=params, data=data)
    raise TypeError("GetNotSettledByIssueDate(): internal overload dispatch failure")

@overload
def GetNotSettledByMaturityDate(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetNotSettledByMaturityDate(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetNotSettledByMaturityDate(api: SyncInvokerProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetNotSettledByMaturityDate(api: SyncRequestProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetNotSettledByMaturityDate(api: SyncInvokerProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
@overload
def GetNotSettledByMaturityDate(api: SyncRequestProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SettlementListElement]]: ...
def GetNotSettledByMaturityDate(api: object, dateFrom: object = _UNSET, dateTo: object = _UNSET, contractorId: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'contractorId' if contractorId is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetNotSettledByMaturityDate(): ambiguous overload for provided arguments")
        exact_match = 'GetNotSettledByMaturityDate'
        exact_match_name = 'GetNotSettledByMaturityDate'
    if provided_names == {'contractorId', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetNotSettledByMaturityDate(): ambiguous overload for provided arguments")
        exact_match = 'GetNotSettledByMaturityDateByContractorIdDateFromDateTo'
        exact_match_name = 'GetNotSettledByMaturityDateByContractorIdDateFromDateTo'
    if provided_names == {'contractorCode', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetNotSettledByMaturityDate(): ambiguous overload for provided arguments")
        exact_match = 'GetNotSettledByMaturityDateByContractorCodeDateFromDateTo'
        exact_match_name = 'GetNotSettledByMaturityDateByContractorCodeDateFromDateTo'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo'}):
            candidates.append((0, -2, 'GetNotSettledByMaturityDate'))
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetNotSettledByMaturityDateByContractorIdDateFromDateTo'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetNotSettledByMaturityDateByContractorCodeDateFromDateTo'))
        if not candidates:
            raise TypeError("GetNotSettledByMaturityDate(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetNotSettledByMaturityDate(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetNotSettledByMaturityDate':
        params, data = _prepare_GetNotSettledByMaturityDate(dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetNotSettledByMaturityDate if validate else OP_GetNotSettledByMaturityDate_RAW, params=params, data=data)
    if selected == 'GetNotSettledByMaturityDateByContractorIdDateFromDateTo':
        params, data = _prepare_GetNotSettledByMaturityDateByContractorIdDateFromDateTo(contractorId=contractorId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetNotSettledByMaturityDateByContractorIdDateFromDateTo if validate else OP_GetNotSettledByMaturityDateByContractorIdDateFromDateTo_RAW, params=params, data=data)
    if selected == 'GetNotSettledByMaturityDateByContractorCodeDateFromDateTo':
        params, data = _prepare_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo(contractorCode=contractorCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo if validate else OP_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo_RAW, params=params, data=data)
    raise TypeError("GetNotSettledByMaturityDate(): internal overload dispatch failure")

@overload
def Issue(api: SyncInvokerProtocol, settlement: "SettlementIssue", *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
@overload
def Issue(api: SyncRequestProtocol, settlement: "SettlementIssue", *, validate: bool = True) -> ResponseEnvelope[Settlement]: ...
def Issue(api: object, settlement: "SettlementIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Issue(validate=validate, settlement=settlement)
    return invoke_operation(api, OP_Issue if validate else OP_Issue_RAW, params=params, data=data)

__all__ = ["Get", "GetByDocument", "GetListByIssueDate", "GetListByMaturityDate", "GetNotSettled", "GetNotSettledByIssueDate", "GetNotSettledByMaturityDate", "Issue"]
