from __future__ import annotations

from typing import Any, List, Optional, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentSeries
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentType
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels import Payment
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels.Issue import PaymentIssue
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels.IssueKP import PaymentKPIssue
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels import PaymentListElement
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByBufferNumber,
    _prepare_GetList,
    _prepare_GetListByContractor,
    _prepare_GetListByContractorByContractorCodeDateFromDateTo,
    _prepare_GetListByPaymentRegistry,
    _prepare_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode,
    _prepare_GetListByReceivingPaymentRegistry,
    _prepare_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode,
    _prepare_GetPDF,
    _prepare_GetPDFByBufferDocumentNumberPrintNote,
    _prepare_GetNALDocumentTypes,
    _prepare_GetZOBDocumentTypes,
    _prepare_GetKPDocumentTypes,
    _prepare_GetKWDocumentTypes,
    _prepare_GetBPDocumentTypes,
    _prepare_GetBWDocumentTypes,
    _prepare_GetIPDocumentTypes,
    _prepare_GetIWDocumentTypes,
    _prepare_GetTRPlusDocumentTypes,
    _prepare_GetTRMinusDocumentTypes,
    _prepare_GetDocumentSeries,
    _prepare_IssuePayment,
    _prepare_IssueTransferMinus,
    _prepare_IssueTransferPlus,
    _prepare_IssueTransferPlusByPaymentNumber,
    _prepare_IssueKP,
    _prepare_GetPagedDocument,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetById,
    OP_GetById_RAW,
    OP_GetByBufferNumber,
    OP_GetByBufferNumber_RAW,
    OP_GetList,
    OP_GetList_RAW,
    OP_GetListByContractor,
    OP_GetListByContractor_RAW,
    OP_GetListByContractorByContractorCodeDateFromDateTo,
    OP_GetListByContractorByContractorCodeDateFromDateTo_RAW,
    OP_GetListByPaymentRegistry,
    OP_GetListByPaymentRegistry_RAW,
    OP_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode,
    OP_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode_RAW,
    OP_GetListByReceivingPaymentRegistry,
    OP_GetListByReceivingPaymentRegistry_RAW,
    OP_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode,
    OP_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode_RAW,
    OP_GetPDF,
    OP_GetPDF_RAW,
    OP_GetPDFByBufferDocumentNumberPrintNote,
    OP_GetPDFByBufferDocumentNumberPrintNote_RAW,
    OP_GetNALDocumentTypes,
    OP_GetNALDocumentTypes_RAW,
    OP_GetZOBDocumentTypes,
    OP_GetZOBDocumentTypes_RAW,
    OP_GetKPDocumentTypes,
    OP_GetKPDocumentTypes_RAW,
    OP_GetKWDocumentTypes,
    OP_GetKWDocumentTypes_RAW,
    OP_GetBPDocumentTypes,
    OP_GetBPDocumentTypes_RAW,
    OP_GetBWDocumentTypes,
    OP_GetBWDocumentTypes_RAW,
    OP_GetIPDocumentTypes,
    OP_GetIPDocumentTypes_RAW,
    OP_GetIWDocumentTypes,
    OP_GetIWDocumentTypes_RAW,
    OP_GetTRPlusDocumentTypes,
    OP_GetTRPlusDocumentTypes_RAW,
    OP_GetTRMinusDocumentTypes,
    OP_GetTRMinusDocumentTypes_RAW,
    OP_GetDocumentSeries,
    OP_GetDocumentSeries_RAW,
    OP_IssuePayment,
    OP_IssuePayment_RAW,
    OP_IssueTransferMinus,
    OP_IssueTransferMinus_RAW,
    OP_IssueTransferPlus,
    OP_IssueTransferPlus_RAW,
    OP_IssueTransferPlusByPaymentNumber,
    OP_IssueTransferPlusByPaymentNumber_RAW,
    OP_IssueKP,
    OP_IssueKP_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
@overload
def Get(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
@overload
def Get(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
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
def GetList(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetList(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
def GetList(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetList(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetList if validate else OP_GetList_RAW, params=params, data=data)

@overload
def GetListByContractor(api: SyncInvokerProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByContractor(api: SyncRequestProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByContractor(api: SyncInvokerProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByContractor(api: SyncRequestProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
def GetListByContractor(api: object, contractorId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorId', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByContractor(): ambiguous overload for provided arguments")
        exact_match = 'GetListByContractor'
        exact_match_name = 'GetListByContractor'
    if provided_names == {'contractorCode', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByContractor(): ambiguous overload for provided arguments")
        exact_match = 'GetListByContractorByContractorCodeDateFromDateTo'
        exact_match_name = 'GetListByContractorByContractorCodeDateFromDateTo'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByContractor'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByContractorByContractorCodeDateFromDateTo'))
        if not candidates:
            raise TypeError("GetListByContractor(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByContractor(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByContractor':
        params, data = _prepare_GetListByContractor(contractorId=contractorId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByContractor if validate else OP_GetListByContractor_RAW, params=params, data=data)
    if selected == 'GetListByContractorByContractorCodeDateFromDateTo':
        params, data = _prepare_GetListByContractorByContractorCodeDateFromDateTo(contractorCode=contractorCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByContractorByContractorCodeDateFromDateTo if validate else OP_GetListByContractorByContractorCodeDateFromDateTo_RAW, params=params, data=data)
    raise TypeError("GetListByContractor(): internal overload dispatch failure")

@overload
def GetListByPaymentRegistry(api: SyncInvokerProtocol, paymentRegistryId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByPaymentRegistry(api: SyncRequestProtocol, paymentRegistryId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByPaymentRegistry(api: SyncInvokerProtocol, paymentRegistryCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByPaymentRegistry(api: SyncRequestProtocol, paymentRegistryCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
def GetListByPaymentRegistry(api: object, paymentRegistryId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, paymentRegistryCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'paymentRegistryId' if paymentRegistryId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'paymentRegistryCode' if paymentRegistryCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo', 'paymentRegistryId'}:
        if exact_match_name is not None:
            raise TypeError("GetListByPaymentRegistry(): ambiguous overload for provided arguments")
        exact_match = 'GetListByPaymentRegistry'
        exact_match_name = 'GetListByPaymentRegistry'
    if provided_names == {'dateFrom', 'dateTo', 'paymentRegistryCode'}:
        if exact_match_name is not None:
            raise TypeError("GetListByPaymentRegistry(): ambiguous overload for provided arguments")
        exact_match = 'GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode'
        exact_match_name = 'GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'paymentRegistryId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'paymentRegistryId'}):
            candidates.append((1, -3, 'GetListByPaymentRegistry'))
        if {'paymentRegistryCode'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'paymentRegistryCode'}):
            candidates.append((1, -3, 'GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode'))
        if not candidates:
            raise TypeError("GetListByPaymentRegistry(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByPaymentRegistry(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByPaymentRegistry':
        params, data = _prepare_GetListByPaymentRegistry(paymentRegistryId=paymentRegistryId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByPaymentRegistry if validate else OP_GetListByPaymentRegistry_RAW, params=params, data=data)
    if selected == 'GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode':
        params, data = _prepare_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode(paymentRegistryCode=paymentRegistryCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode if validate else OP_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode_RAW, params=params, data=data)
    raise TypeError("GetListByPaymentRegistry(): internal overload dispatch failure")

@overload
def GetListByReceivingPaymentRegistry(api: SyncInvokerProtocol, receivingPaymentRegistryId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByReceivingPaymentRegistry(api: SyncRequestProtocol, receivingPaymentRegistryId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByReceivingPaymentRegistry(api: SyncInvokerProtocol, receivingPaymentRegistryCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
@overload
def GetListByReceivingPaymentRegistry(api: SyncRequestProtocol, receivingPaymentRegistryCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PaymentListElement]]: ...
def GetListByReceivingPaymentRegistry(api: object, receivingPaymentRegistryId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, receivingPaymentRegistryCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'receivingPaymentRegistryId' if receivingPaymentRegistryId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'receivingPaymentRegistryCode' if receivingPaymentRegistryCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo', 'receivingPaymentRegistryId'}:
        if exact_match_name is not None:
            raise TypeError("GetListByReceivingPaymentRegistry(): ambiguous overload for provided arguments")
        exact_match = 'GetListByReceivingPaymentRegistry'
        exact_match_name = 'GetListByReceivingPaymentRegistry'
    if provided_names == {'dateFrom', 'dateTo', 'receivingPaymentRegistryCode'}:
        if exact_match_name is not None:
            raise TypeError("GetListByReceivingPaymentRegistry(): ambiguous overload for provided arguments")
        exact_match = 'GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode'
        exact_match_name = 'GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'receivingPaymentRegistryId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'receivingPaymentRegistryId'}):
            candidates.append((1, -3, 'GetListByReceivingPaymentRegistry'))
        if {'receivingPaymentRegistryCode'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'receivingPaymentRegistryCode'}):
            candidates.append((1, -3, 'GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode'))
        if not candidates:
            raise TypeError("GetListByReceivingPaymentRegistry(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByReceivingPaymentRegistry(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByReceivingPaymentRegistry':
        params, data = _prepare_GetListByReceivingPaymentRegistry(receivingPaymentRegistryId=receivingPaymentRegistryId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByReceivingPaymentRegistry if validate else OP_GetListByReceivingPaymentRegistry_RAW, params=params, data=data)
    if selected == 'GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode':
        params, data = _prepare_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode(receivingPaymentRegistryCode=receivingPaymentRegistryCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode if validate else OP_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode_RAW, params=params, data=data)
    raise TypeError("GetListByReceivingPaymentRegistry(): internal overload dispatch failure")

@overload
def GetPDF(api: SyncInvokerProtocol, documentId: int, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, documentId: int, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, documentNumber: str, buffer: bool, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
def GetPDF(api: object, documentId: object = _UNSET, printNote: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'printNote' if printNote is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'documentId', 'printNote'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDF'
        exact_match_name = 'GetPDF'
    if provided_names == {'buffer', 'documentNumber', 'printNote'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByBufferDocumentNumberPrintNote'
        exact_match_name = 'GetPDFByBufferDocumentNumberPrintNote'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId', 'printNote'}.issubset(provided_names) and provided_names.issubset({'documentId', 'printNote'}):
            candidates.append((2, -2, 'GetPDF'))
        if {'buffer', 'documentNumber', 'printNote'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber', 'printNote'}):
            candidates.append((3, -3, 'GetPDFByBufferDocumentNumberPrintNote'))
        if not candidates:
            raise TypeError("GetPDF(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetPDF':
        params, data = _prepare_GetPDF(documentId=documentId, printNote=printNote)
        return invoke_operation(api, OP_GetPDF if validate else OP_GetPDF_RAW, params=params, data=data)
    if selected == 'GetPDFByBufferDocumentNumberPrintNote':
        params, data = _prepare_GetPDFByBufferDocumentNumberPrintNote(documentNumber=documentNumber, buffer=buffer, printNote=printNote)
        return invoke_operation(api, OP_GetPDFByBufferDocumentNumberPrintNote if validate else OP_GetPDFByBufferDocumentNumberPrintNote_RAW, params=params, data=data)
    raise TypeError("GetPDF(): internal overload dispatch failure")

@overload
def GetNALDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetNALDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetNALDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetNALDocumentTypes()
    return invoke_operation(api, OP_GetNALDocumentTypes if validate else OP_GetNALDocumentTypes_RAW, params=params, data=data)

@overload
def GetZOBDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetZOBDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetZOBDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetZOBDocumentTypes()
    return invoke_operation(api, OP_GetZOBDocumentTypes if validate else OP_GetZOBDocumentTypes_RAW, params=params, data=data)

@overload
def GetKPDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetKPDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetKPDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetKPDocumentTypes()
    return invoke_operation(api, OP_GetKPDocumentTypes if validate else OP_GetKPDocumentTypes_RAW, params=params, data=data)

@overload
def GetKWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetKWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetKWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetKWDocumentTypes()
    return invoke_operation(api, OP_GetKWDocumentTypes if validate else OP_GetKWDocumentTypes_RAW, params=params, data=data)

@overload
def GetBPDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetBPDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetBPDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetBPDocumentTypes()
    return invoke_operation(api, OP_GetBPDocumentTypes if validate else OP_GetBPDocumentTypes_RAW, params=params, data=data)

@overload
def GetBWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetBWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetBWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetBWDocumentTypes()
    return invoke_operation(api, OP_GetBWDocumentTypes if validate else OP_GetBWDocumentTypes_RAW, params=params, data=data)

@overload
def GetIPDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetIPDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetIPDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetIPDocumentTypes()
    return invoke_operation(api, OP_GetIPDocumentTypes if validate else OP_GetIPDocumentTypes_RAW, params=params, data=data)

@overload
def GetIWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetIWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetIWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetIWDocumentTypes()
    return invoke_operation(api, OP_GetIWDocumentTypes if validate else OP_GetIWDocumentTypes_RAW, params=params, data=data)

@overload
def GetTRPlusDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetTRPlusDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetTRPlusDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetTRPlusDocumentTypes()
    return invoke_operation(api, OP_GetTRPlusDocumentTypes if validate else OP_GetTRPlusDocumentTypes_RAW, params=params, data=data)

@overload
def GetTRMinusDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetTRMinusDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetTRMinusDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetTRMinusDocumentTypes()
    return invoke_operation(api, OP_GetTRMinusDocumentTypes if validate else OP_GetTRMinusDocumentTypes_RAW, params=params, data=data)

@overload
def GetDocumentSeries(api: SyncInvokerProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
@overload
def GetDocumentSeries(api: SyncRequestProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
def GetDocumentSeries(api: object, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentSeries(documentTypeId=documentTypeId)
    return invoke_operation(api, OP_GetDocumentSeries if validate else OP_GetDocumentSeries_RAW, params=params, data=data)

@overload
def IssuePayment(api: SyncInvokerProtocol, payment: "PaymentIssue", *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
@overload
def IssuePayment(api: SyncRequestProtocol, payment: "PaymentIssue", *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
def IssuePayment(api: object, payment: "PaymentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IssuePayment(validate=validate, payment=payment)
    return invoke_operation(api, OP_IssuePayment if validate else OP_IssuePayment_RAW, params=params, data=data)

@overload
def IssueTransferMinus(api: SyncInvokerProtocol, payment: "PaymentIssue", *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
@overload
def IssueTransferMinus(api: SyncRequestProtocol, payment: "PaymentIssue", *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
def IssueTransferMinus(api: object, payment: "PaymentIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IssueTransferMinus(validate=validate, payment=payment)
    return invoke_operation(api, OP_IssueTransferMinus if validate else OP_IssueTransferMinus_RAW, params=params, data=data)

@overload
def IssueTransferPlus(api: SyncInvokerProtocol, paymentId: int, *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
@overload
def IssueTransferPlus(api: SyncRequestProtocol, paymentId: int, *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
@overload
def IssueTransferPlus(api: SyncInvokerProtocol, paymentNumber: str, *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
@overload
def IssueTransferPlus(api: SyncRequestProtocol, paymentNumber: str, *, validate: bool = True) -> ResponseEnvelope[Payment]: ...
def IssueTransferPlus(api: object, paymentId: object = _UNSET, paymentNumber: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'paymentId' if paymentId is not _UNSET else None,
        'paymentNumber' if paymentNumber is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'paymentId'}:
        if exact_match_name is not None:
            raise TypeError("IssueTransferPlus(): ambiguous overload for provided arguments")
        exact_match = 'IssueTransferPlus'
        exact_match_name = 'IssueTransferPlus'
    if provided_names == {'paymentNumber'}:
        if exact_match_name is not None:
            raise TypeError("IssueTransferPlus(): ambiguous overload for provided arguments")
        exact_match = 'IssueTransferPlusByPaymentNumber'
        exact_match_name = 'IssueTransferPlusByPaymentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'paymentId'}.issubset(provided_names) and provided_names.issubset({'paymentId'}):
            candidates.append((1, -1, 'IssueTransferPlus'))
        if {'paymentNumber'}.issubset(provided_names) and provided_names.issubset({'paymentNumber'}):
            candidates.append((1, -1, 'IssueTransferPlusByPaymentNumber'))
        if not candidates:
            raise TypeError("IssueTransferPlus(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("IssueTransferPlus(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'IssueTransferPlus':
        params, data = _prepare_IssueTransferPlus(paymentId=paymentId)
        return invoke_operation(api, OP_IssueTransferPlus if validate else OP_IssueTransferPlus_RAW, params=params, data=data)
    if selected == 'IssueTransferPlusByPaymentNumber':
        params, data = _prepare_IssueTransferPlusByPaymentNumber(paymentNumber=paymentNumber)
        return invoke_operation(api, OP_IssueTransferPlusByPaymentNumber if validate else OP_IssueTransferPlusByPaymentNumber_RAW, params=params, data=data)
    raise TypeError("IssueTransferPlus(): internal overload dispatch failure")

@overload
def IssueKP(api: SyncInvokerProtocol, payment: "PaymentKPIssue", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def IssueKP(api: SyncRequestProtocol, payment: "PaymentKPIssue", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def IssueKP(api: object, payment: "PaymentKPIssue", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IssueKP(validate=validate, payment=payment)
    return invoke_operation(api, OP_IssueKP if validate else OP_IssueKP_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

__all__ = ["Get", "GetList", "GetListByContractor", "GetListByPaymentRegistry", "GetListByReceivingPaymentRegistry", "GetPDF", "GetNALDocumentTypes", "GetZOBDocumentTypes", "GetKPDocumentTypes", "GetKWDocumentTypes", "GetBPDocumentTypes", "GetBWDocumentTypes", "GetIPDocumentTypes", "GetIWDocumentTypes", "GetTRPlusDocumentTypes", "GetTRMinusDocumentTypes", "GetDocumentSeries", "IssuePayment", "IssueTransferMinus", "IssueTransferPlus", "IssueKP", "GetPagedDocument"]
