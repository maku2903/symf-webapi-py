from __future__ import annotations

from typing import Any, List, Optional, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Catalog
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentSeries
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentType
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import FilterDocumentType
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import IncrementalSyncListElement
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Kind
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Marker
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDFSettings
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleCorrection
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocument
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentCorrection
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentListElement
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentStatus
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentWZ
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentZMO
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByBufferNumber,
    _prepare_GetList,
    _prepare_GetListByBuyer,
    _prepare_GetListByBuyerByBuyerCodeDateFromDateTo,
    _prepare_GetListByRecipient,
    _prepare_GetListByRecipientByDateFromDateToRecipientCode,
    _prepare_GetListByDimension,
    _prepare_GetWZ,
    _prepare_GetWZByBufferDocumentNumber,
    _prepare_GetZMO,
    _prepare_GetZMOByBufferDocumentNumber,
    _prepare_GetStatus,
    _prepare_GetStatusByBufferDocumentNumber,
    _prepare_GetMarkers,
    _prepare_GetKinds,
    _prepare_GetCatalogs,
    _prepare_GetDEXDocumentTypes,
    _prepare_GetFVSMDocumentTypes,
    _prepare_GetFVSDocumentTypes,
    _prepare_GetFVWDocumentTypes,
    _prepare_GetSKODocumentTypes,
    _prepare_GetSKWDocumentTypes,
    _prepare_GetPARDocumentTypes,
    _prepare_GetSRSDocumentTypes,
    _prepare_GetREXDocumentTypes,
    _prepare_GetRUSDocumentTypes,
    _prepare_GetWDTDocumentTypes,
    _prepare_GetDXKDocumentTypes,
    _prepare_GetPRKDocumentTypes,
    _prepare_GetSRKDocumentTypes,
    _prepare_GetRKSDocumentTypes,
    _prepare_GetRXKDocumentTypes,
    _prepare_GetFVMKDocumentTypes,
    _prepare_GetFKSDocumentTypes,
    _prepare_GetFKWDocumentTypes,
    _prepare_GetSKKDocumentTypes,
    _prepare_GetSKWKDocumentTypes,
    _prepare_GetWKSDocumentTypes,
    _prepare_GetWDTKDocumentTypes,
    _prepare_GetDocumentSeries,
    _prepare_GetPDF,
    _prepare_GetPDFByBufferDocumentNumberPrintNote,
    _prepare_GetCorrection,
    _prepare_GetCorrectionByBufferNumber,
    _prepare_GetCorrectionSequence,
    _prepare_GetCorrectionSequenceByBufferDocumentNumber,
    _prepare_IncrementalSync,
    _prepare_GetPagedDocument,
    _prepare_GetPDFByDocumentIdSettings,
    _prepare_GetPDFByBufferDocumentNumberSettings,
    _prepare_GetDocumentTypesWithRange,
    _prepare_GetDocumentExternalMetadata,
    _prepare_RefreshKsefStatusAsync,
    _prepare_RefreshKsefStatusAsyncGet,
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
    OP_GetListByBuyer,
    OP_GetListByBuyer_RAW,
    OP_GetListByBuyerByBuyerCodeDateFromDateTo,
    OP_GetListByBuyerByBuyerCodeDateFromDateTo_RAW,
    OP_GetListByRecipient,
    OP_GetListByRecipient_RAW,
    OP_GetListByRecipientByDateFromDateToRecipientCode,
    OP_GetListByRecipientByDateFromDateToRecipientCode_RAW,
    OP_GetListByDimension,
    OP_GetListByDimension_RAW,
    OP_GetWZ,
    OP_GetWZ_RAW,
    OP_GetWZByBufferDocumentNumber,
    OP_GetWZByBufferDocumentNumber_RAW,
    OP_GetZMO,
    OP_GetZMO_RAW,
    OP_GetZMOByBufferDocumentNumber,
    OP_GetZMOByBufferDocumentNumber_RAW,
    OP_GetStatus,
    OP_GetStatus_RAW,
    OP_GetStatusByBufferDocumentNumber,
    OP_GetStatusByBufferDocumentNumber_RAW,
    OP_GetMarkers,
    OP_GetMarkers_RAW,
    OP_GetKinds,
    OP_GetKinds_RAW,
    OP_GetCatalogs,
    OP_GetCatalogs_RAW,
    OP_GetDEXDocumentTypes,
    OP_GetDEXDocumentTypes_RAW,
    OP_GetFVSMDocumentTypes,
    OP_GetFVSMDocumentTypes_RAW,
    OP_GetFVSDocumentTypes,
    OP_GetFVSDocumentTypes_RAW,
    OP_GetFVWDocumentTypes,
    OP_GetFVWDocumentTypes_RAW,
    OP_GetSKODocumentTypes,
    OP_GetSKODocumentTypes_RAW,
    OP_GetSKWDocumentTypes,
    OP_GetSKWDocumentTypes_RAW,
    OP_GetPARDocumentTypes,
    OP_GetPARDocumentTypes_RAW,
    OP_GetSRSDocumentTypes,
    OP_GetSRSDocumentTypes_RAW,
    OP_GetREXDocumentTypes,
    OP_GetREXDocumentTypes_RAW,
    OP_GetRUSDocumentTypes,
    OP_GetRUSDocumentTypes_RAW,
    OP_GetWDTDocumentTypes,
    OP_GetWDTDocumentTypes_RAW,
    OP_GetDXKDocumentTypes,
    OP_GetDXKDocumentTypes_RAW,
    OP_GetPRKDocumentTypes,
    OP_GetPRKDocumentTypes_RAW,
    OP_GetSRKDocumentTypes,
    OP_GetSRKDocumentTypes_RAW,
    OP_GetRKSDocumentTypes,
    OP_GetRKSDocumentTypes_RAW,
    OP_GetRXKDocumentTypes,
    OP_GetRXKDocumentTypes_RAW,
    OP_GetFVMKDocumentTypes,
    OP_GetFVMKDocumentTypes_RAW,
    OP_GetFKSDocumentTypes,
    OP_GetFKSDocumentTypes_RAW,
    OP_GetFKWDocumentTypes,
    OP_GetFKWDocumentTypes_RAW,
    OP_GetSKKDocumentTypes,
    OP_GetSKKDocumentTypes_RAW,
    OP_GetSKWKDocumentTypes,
    OP_GetSKWKDocumentTypes_RAW,
    OP_GetWKSDocumentTypes,
    OP_GetWKSDocumentTypes_RAW,
    OP_GetWDTKDocumentTypes,
    OP_GetWDTKDocumentTypes_RAW,
    OP_GetDocumentSeries,
    OP_GetDocumentSeries_RAW,
    OP_GetPDF,
    OP_GetPDF_RAW,
    OP_GetPDFByBufferDocumentNumberPrintNote,
    OP_GetPDFByBufferDocumentNumberPrintNote_RAW,
    OP_GetCorrection,
    OP_GetCorrection_RAW,
    OP_GetCorrectionByBufferNumber,
    OP_GetCorrectionByBufferNumber_RAW,
    OP_GetCorrectionSequence,
    OP_GetCorrectionSequence_RAW,
    OP_GetCorrectionSequenceByBufferDocumentNumber,
    OP_GetCorrectionSequenceByBufferDocumentNumber_RAW,
    OP_IncrementalSync,
    OP_IncrementalSync_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
    OP_GetPDFByDocumentIdSettings,
    OP_GetPDFByDocumentIdSettings_RAW,
    OP_GetPDFByBufferDocumentNumberSettings,
    OP_GetPDFByBufferDocumentNumberSettings_RAW,
    OP_GetDocumentTypesWithRange,
    OP_GetDocumentTypesWithRange_RAW,
    OP_GetDocumentExternalMetadata,
    OP_GetDocumentExternalMetadata_RAW,
    OP_RefreshKsefStatusAsync,
    OP_RefreshKsefStatusAsync_RAW,
    OP_RefreshKsefStatusAsyncGet,
    OP_RefreshKsefStatusAsyncGet_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def Get(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
@overload
def Get(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[SaleDocument]: ...
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
def GetList(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetList(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
def GetList(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetList(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetList if validate else OP_GetList_RAW, params=params, data=data)

@overload
def GetListByBuyer(api: SyncInvokerProtocol, buyerId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetListByBuyer(api: SyncRequestProtocol, buyerId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetListByBuyer(api: SyncInvokerProtocol, buyerCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetListByBuyer(api: SyncRequestProtocol, buyerCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
def GetListByBuyer(api: object, buyerId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, buyerCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'buyerId' if buyerId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'buyerCode' if buyerCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'buyerId', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByBuyer(): ambiguous overload for provided arguments")
        exact_match = 'GetListByBuyer'
        exact_match_name = 'GetListByBuyer'
    if provided_names == {'buyerCode', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByBuyer(): ambiguous overload for provided arguments")
        exact_match = 'GetListByBuyerByBuyerCodeDateFromDateTo'
        exact_match_name = 'GetListByBuyerByBuyerCodeDateFromDateTo'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'buyerId'}.issubset(provided_names) and provided_names.issubset({'buyerId', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByBuyer'))
        if {'buyerCode'}.issubset(provided_names) and provided_names.issubset({'buyerCode', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByBuyerByBuyerCodeDateFromDateTo'))
        if not candidates:
            raise TypeError("GetListByBuyer(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByBuyer(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByBuyer':
        params, data = _prepare_GetListByBuyer(buyerId=buyerId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByBuyer if validate else OP_GetListByBuyer_RAW, params=params, data=data)
    if selected == 'GetListByBuyerByBuyerCodeDateFromDateTo':
        params, data = _prepare_GetListByBuyerByBuyerCodeDateFromDateTo(buyerCode=buyerCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByBuyerByBuyerCodeDateFromDateTo if validate else OP_GetListByBuyerByBuyerCodeDateFromDateTo_RAW, params=params, data=data)
    raise TypeError("GetListByBuyer(): internal overload dispatch failure")

@overload
def GetListByRecipient(api: SyncInvokerProtocol, recipientId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetListByRecipient(api: SyncRequestProtocol, recipientId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetListByRecipient(api: SyncInvokerProtocol, recipientCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetListByRecipient(api: SyncRequestProtocol, recipientCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
def GetListByRecipient(api: object, recipientId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, recipientCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'recipientId' if recipientId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'recipientCode' if recipientCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo', 'recipientId'}:
        if exact_match_name is not None:
            raise TypeError("GetListByRecipient(): ambiguous overload for provided arguments")
        exact_match = 'GetListByRecipient'
        exact_match_name = 'GetListByRecipient'
    if provided_names == {'dateFrom', 'dateTo', 'recipientCode'}:
        if exact_match_name is not None:
            raise TypeError("GetListByRecipient(): ambiguous overload for provided arguments")
        exact_match = 'GetListByRecipientByDateFromDateToRecipientCode'
        exact_match_name = 'GetListByRecipientByDateFromDateToRecipientCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'recipientId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'recipientId'}):
            candidates.append((1, -3, 'GetListByRecipient'))
        if {'recipientCode'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'recipientCode'}):
            candidates.append((1, -3, 'GetListByRecipientByDateFromDateToRecipientCode'))
        if not candidates:
            raise TypeError("GetListByRecipient(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByRecipient(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByRecipient':
        params, data = _prepare_GetListByRecipient(recipientId=recipientId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByRecipient if validate else OP_GetListByRecipient_RAW, params=params, data=data)
    if selected == 'GetListByRecipientByDateFromDateToRecipientCode':
        params, data = _prepare_GetListByRecipientByDateFromDateToRecipientCode(recipientCode=recipientCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByRecipientByDateFromDateToRecipientCode if validate else OP_GetListByRecipientByDateFromDateToRecipientCode_RAW, params=params, data=data)
    raise TypeError("GetListByRecipient(): internal overload dispatch failure")

@overload
def GetListByDimension(api: SyncInvokerProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetListByDimension(api: SyncRequestProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
def GetListByDimension(api: object, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetListByDimension(dimensionCode=dimensionCode, dictionaryValue=dictionaryValue, value=value)
    return invoke_operation(api, OP_GetListByDimension if validate else OP_GetListByDimension_RAW, params=params, data=data)

@overload
def GetWZ(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def GetWZ(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def GetWZ(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
@overload
def GetWZ(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentWZ]]: ...
def GetWZ(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("GetWZ(): ambiguous overload for provided arguments")
        exact_match = 'GetWZ'
        exact_match_name = 'GetWZ'
    if provided_names == {'buffer', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetWZ(): ambiguous overload for provided arguments")
        exact_match = 'GetWZByBufferDocumentNumber'
        exact_match_name = 'GetWZByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetWZ'))
        if {'buffer', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber'}):
            candidates.append((2, -2, 'GetWZByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetWZ(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetWZ(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetWZ':
        params, data = _prepare_GetWZ(documentId=documentId)
        return invoke_operation(api, OP_GetWZ if validate else OP_GetWZ_RAW, params=params, data=data)
    if selected == 'GetWZByBufferDocumentNumber':
        params, data = _prepare_GetWZByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetWZByBufferDocumentNumber if validate else OP_GetWZByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetWZ(): internal overload dispatch failure")

@overload
def GetZMO(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentZMO]]: ...
@overload
def GetZMO(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentZMO]]: ...
@overload
def GetZMO(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentZMO]]: ...
@overload
def GetZMO(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentZMO]]: ...
def GetZMO(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("GetZMO(): ambiguous overload for provided arguments")
        exact_match = 'GetZMO'
        exact_match_name = 'GetZMO'
    if provided_names == {'buffer', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetZMO(): ambiguous overload for provided arguments")
        exact_match = 'GetZMOByBufferDocumentNumber'
        exact_match_name = 'GetZMOByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetZMO'))
        if {'buffer', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber'}):
            candidates.append((2, -2, 'GetZMOByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetZMO(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetZMO(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetZMO':
        params, data = _prepare_GetZMO(documentId=documentId)
        return invoke_operation(api, OP_GetZMO if validate else OP_GetZMO_RAW, params=params, data=data)
    if selected == 'GetZMOByBufferDocumentNumber':
        params, data = _prepare_GetZMOByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetZMOByBufferDocumentNumber if validate else OP_GetZMOByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetZMO(): internal overload dispatch failure")

@overload
def GetStatus(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocumentStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[SaleDocumentStatus]: ...
@overload
def GetStatus(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[SaleDocumentStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[SaleDocumentStatus]: ...
def GetStatus(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("GetStatus(): ambiguous overload for provided arguments")
        exact_match = 'GetStatus'
        exact_match_name = 'GetStatus'
    if provided_names == {'buffer', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetStatus(): ambiguous overload for provided arguments")
        exact_match = 'GetStatusByBufferDocumentNumber'
        exact_match_name = 'GetStatusByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetStatus'))
        if {'buffer', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber'}):
            candidates.append((2, -2, 'GetStatusByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetStatus(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetStatus(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetStatus':
        params, data = _prepare_GetStatus(documentId=documentId)
        return invoke_operation(api, OP_GetStatus if validate else OP_GetStatus_RAW, params=params, data=data)
    if selected == 'GetStatusByBufferDocumentNumber':
        params, data = _prepare_GetStatusByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetStatusByBufferDocumentNumber if validate else OP_GetStatusByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetStatus(): internal overload dispatch failure")

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
def GetDEXDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetDEXDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetDEXDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDEXDocumentTypes()
    return invoke_operation(api, OP_GetDEXDocumentTypes if validate else OP_GetDEXDocumentTypes_RAW, params=params, data=data)

@overload
def GetFVSMDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFVSMDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFVSMDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFVSMDocumentTypes()
    return invoke_operation(api, OP_GetFVSMDocumentTypes if validate else OP_GetFVSMDocumentTypes_RAW, params=params, data=data)

@overload
def GetFVSDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFVSDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFVSDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFVSDocumentTypes()
    return invoke_operation(api, OP_GetFVSDocumentTypes if validate else OP_GetFVSDocumentTypes_RAW, params=params, data=data)

@overload
def GetFVWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFVWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFVWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFVWDocumentTypes()
    return invoke_operation(api, OP_GetFVWDocumentTypes if validate else OP_GetFVWDocumentTypes_RAW, params=params, data=data)

@overload
def GetSKODocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetSKODocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetSKODocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSKODocumentTypes()
    return invoke_operation(api, OP_GetSKODocumentTypes if validate else OP_GetSKODocumentTypes_RAW, params=params, data=data)

@overload
def GetSKWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetSKWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetSKWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSKWDocumentTypes()
    return invoke_operation(api, OP_GetSKWDocumentTypes if validate else OP_GetSKWDocumentTypes_RAW, params=params, data=data)

@overload
def GetPARDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetPARDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetPARDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPARDocumentTypes()
    return invoke_operation(api, OP_GetPARDocumentTypes if validate else OP_GetPARDocumentTypes_RAW, params=params, data=data)

@overload
def GetSRSDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetSRSDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetSRSDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSRSDocumentTypes()
    return invoke_operation(api, OP_GetSRSDocumentTypes if validate else OP_GetSRSDocumentTypes_RAW, params=params, data=data)

@overload
def GetREXDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetREXDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetREXDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetREXDocumentTypes()
    return invoke_operation(api, OP_GetREXDocumentTypes if validate else OP_GetREXDocumentTypes_RAW, params=params, data=data)

@overload
def GetRUSDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetRUSDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetRUSDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetRUSDocumentTypes()
    return invoke_operation(api, OP_GetRUSDocumentTypes if validate else OP_GetRUSDocumentTypes_RAW, params=params, data=data)

@overload
def GetWDTDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetWDTDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetWDTDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWDTDocumentTypes()
    return invoke_operation(api, OP_GetWDTDocumentTypes if validate else OP_GetWDTDocumentTypes_RAW, params=params, data=data)

@overload
def GetDXKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetDXKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetDXKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDXKDocumentTypes()
    return invoke_operation(api, OP_GetDXKDocumentTypes if validate else OP_GetDXKDocumentTypes_RAW, params=params, data=data)

@overload
def GetPRKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetPRKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetPRKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPRKDocumentTypes()
    return invoke_operation(api, OP_GetPRKDocumentTypes if validate else OP_GetPRKDocumentTypes_RAW, params=params, data=data)

@overload
def GetSRKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetSRKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetSRKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSRKDocumentTypes()
    return invoke_operation(api, OP_GetSRKDocumentTypes if validate else OP_GetSRKDocumentTypes_RAW, params=params, data=data)

@overload
def GetRKSDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetRKSDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetRKSDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetRKSDocumentTypes()
    return invoke_operation(api, OP_GetRKSDocumentTypes if validate else OP_GetRKSDocumentTypes_RAW, params=params, data=data)

@overload
def GetRXKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetRXKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetRXKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetRXKDocumentTypes()
    return invoke_operation(api, OP_GetRXKDocumentTypes if validate else OP_GetRXKDocumentTypes_RAW, params=params, data=data)

@overload
def GetFVMKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFVMKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFVMKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFVMKDocumentTypes()
    return invoke_operation(api, OP_GetFVMKDocumentTypes if validate else OP_GetFVMKDocumentTypes_RAW, params=params, data=data)

@overload
def GetFKSDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFKSDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFKSDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFKSDocumentTypes()
    return invoke_operation(api, OP_GetFKSDocumentTypes if validate else OP_GetFKSDocumentTypes_RAW, params=params, data=data)

@overload
def GetFKWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFKWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFKWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFKWDocumentTypes()
    return invoke_operation(api, OP_GetFKWDocumentTypes if validate else OP_GetFKWDocumentTypes_RAW, params=params, data=data)

@overload
def GetSKKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetSKKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetSKKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSKKDocumentTypes()
    return invoke_operation(api, OP_GetSKKDocumentTypes if validate else OP_GetSKKDocumentTypes_RAW, params=params, data=data)

@overload
def GetSKWKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetSKWKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetSKWKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSKWKDocumentTypes()
    return invoke_operation(api, OP_GetSKWKDocumentTypes if validate else OP_GetSKWKDocumentTypes_RAW, params=params, data=data)

@overload
def GetWKSDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetWKSDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetWKSDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWKSDocumentTypes()
    return invoke_operation(api, OP_GetWKSDocumentTypes if validate else OP_GetWKSDocumentTypes_RAW, params=params, data=data)

@overload
def GetWDTKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetWDTKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetWDTKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWDTKDocumentTypes()
    return invoke_operation(api, OP_GetWDTKDocumentTypes if validate else OP_GetWDTKDocumentTypes_RAW, params=params, data=data)

@overload
def GetDocumentSeries(api: SyncInvokerProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
@overload
def GetDocumentSeries(api: SyncRequestProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
def GetDocumentSeries(api: object, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentSeries(documentTypeId=documentTypeId)
    return invoke_operation(api, OP_GetDocumentSeries if validate else OP_GetDocumentSeries_RAW, params=params, data=data)

@overload
def GetPDF(api: SyncInvokerProtocol, documentId: int, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, documentId: int, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, documentNumber: str, buffer: bool, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncInvokerProtocol, documentId: int, settings: "PDFSettings", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, documentId: int, settings: "PDFSettings", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, settings: "PDFSettings", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, documentNumber: str, buffer: bool, settings: "PDFSettings", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
def GetPDF(api: object, documentId: object = _UNSET, printNote: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, settings: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'documentId' if documentId is not _UNSET else None,
        'printNote' if printNote is not _UNSET else None,
        'documentNumber' if documentNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
        'settings' if settings is not _UNSET else None,
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
    if provided_names == {'documentId', 'settings'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByDocumentIdSettings'
        exact_match_name = 'GetPDFByDocumentIdSettings'
    if provided_names == {'buffer', 'documentNumber', 'settings'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByBufferDocumentNumberSettings'
        exact_match_name = 'GetPDFByBufferDocumentNumberSettings'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId', 'printNote'}.issubset(provided_names) and provided_names.issubset({'documentId', 'printNote'}):
            candidates.append((2, -2, 'GetPDF'))
        if {'buffer', 'documentNumber', 'printNote'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber', 'printNote'}):
            candidates.append((3, -3, 'GetPDFByBufferDocumentNumberPrintNote'))
        if {'documentId', 'settings'}.issubset(provided_names) and provided_names.issubset({'documentId', 'settings'}):
            candidates.append((2, -2, 'GetPDFByDocumentIdSettings'))
        if {'buffer', 'documentNumber', 'settings'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber', 'settings'}):
            candidates.append((3, -3, 'GetPDFByBufferDocumentNumberSettings'))
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
    if selected == 'GetPDFByDocumentIdSettings':
        params, data = _prepare_GetPDFByDocumentIdSettings(validate=validate, documentId=documentId, settings=settings)
        return invoke_operation(api, OP_GetPDFByDocumentIdSettings if validate else OP_GetPDFByDocumentIdSettings_RAW, params=params, data=data)
    if selected == 'GetPDFByBufferDocumentNumberSettings':
        params, data = _prepare_GetPDFByBufferDocumentNumberSettings(validate=validate, documentNumber=documentNumber, buffer=buffer, settings=settings)
        return invoke_operation(api, OP_GetPDFByBufferDocumentNumberSettings if validate else OP_GetPDFByBufferDocumentNumberSettings_RAW, params=params, data=data)
    raise TypeError("GetPDF(): internal overload dispatch failure")

@overload
def GetCorrection(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[SaleCorrection]: ...
@overload
def GetCorrection(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[SaleCorrection]: ...
@overload
def GetCorrection(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[SaleCorrection]: ...
@overload
def GetCorrection(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[SaleCorrection]: ...
def GetCorrection(api: object, id: object = _UNSET, number: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'number' if number is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("GetCorrection(): ambiguous overload for provided arguments")
        exact_match = 'GetCorrection'
        exact_match_name = 'GetCorrection'
    if provided_names == {'buffer', 'number'}:
        if exact_match_name is not None:
            raise TypeError("GetCorrection(): ambiguous overload for provided arguments")
        exact_match = 'GetCorrectionByBufferNumber'
        exact_match_name = 'GetCorrectionByBufferNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'GetCorrection'))
        if {'buffer', 'number'}.issubset(provided_names) and provided_names.issubset({'buffer', 'number'}):
            candidates.append((2, -2, 'GetCorrectionByBufferNumber'))
        if not candidates:
            raise TypeError("GetCorrection(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetCorrection(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetCorrection':
        params, data = _prepare_GetCorrection(id=id)
        return invoke_operation(api, OP_GetCorrection if validate else OP_GetCorrection_RAW, params=params, data=data)
    if selected == 'GetCorrectionByBufferNumber':
        params, data = _prepare_GetCorrectionByBufferNumber(number=number, buffer=buffer)
        return invoke_operation(api, OP_GetCorrectionByBufferNumber if validate else OP_GetCorrectionByBufferNumber_RAW, params=params, data=data)
    raise TypeError("GetCorrection(): internal overload dispatch failure")

@overload
def GetCorrectionSequence(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentCorrection]]: ...
@overload
def GetCorrectionSequence(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentCorrection]]: ...
@overload
def GetCorrectionSequence(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentCorrection]]: ...
@overload
def GetCorrectionSequence(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentCorrection]]: ...
def GetCorrectionSequence(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("GetCorrectionSequence(): ambiguous overload for provided arguments")
        exact_match = 'GetCorrectionSequence'
        exact_match_name = 'GetCorrectionSequence'
    if provided_names == {'buffer', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetCorrectionSequence(): ambiguous overload for provided arguments")
        exact_match = 'GetCorrectionSequenceByBufferDocumentNumber'
        exact_match_name = 'GetCorrectionSequenceByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetCorrectionSequence'))
        if {'buffer', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber'}):
            candidates.append((2, -2, 'GetCorrectionSequenceByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetCorrectionSequence(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetCorrectionSequence(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetCorrectionSequence':
        params, data = _prepare_GetCorrectionSequence(documentId=documentId)
        return invoke_operation(api, OP_GetCorrectionSequence if validate else OP_GetCorrectionSequence_RAW, params=params, data=data)
    if selected == 'GetCorrectionSequenceByBufferDocumentNumber':
        params, data = _prepare_GetCorrectionSequenceByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetCorrectionSequenceByBufferDocumentNumber if validate else OP_GetCorrectionSequenceByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetCorrectionSequence(): internal overload dispatch failure")

@overload
def IncrementalSync(api: SyncInvokerProtocol, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[List[IncrementalSyncListElement]]: ...
@overload
def IncrementalSync(api: SyncRequestProtocol, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[List[IncrementalSyncListElement]]: ...
def IncrementalSync(api: object, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IncrementalSync(dateFrom=dateFrom)
    return invoke_operation(api, OP_IncrementalSync if validate else OP_IncrementalSync_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

@overload
def GetDocumentTypesWithRange(api: SyncInvokerProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
@overload
def GetDocumentTypesWithRange(api: SyncRequestProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[SaleDocumentListElement]]: ...
def GetDocumentTypesWithRange(api: object, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentTypesWithRange(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDocumentTypesWithRange if validate else OP_GetDocumentTypesWithRange_RAW, params=params, data=data)

@overload
def GetDocumentExternalMetadata(api: SyncInvokerProtocol, page: Optional[int] = None, size: Optional[int] = None, orderBy: Optional["enumOrderByType"] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentExternalMetadataModel]]: ...
@overload
def GetDocumentExternalMetadata(api: SyncRequestProtocol, page: Optional[int] = None, size: Optional[int] = None, orderBy: Optional["enumOrderByType"] = None, *, validate: bool = True) -> ResponseEnvelope[List[DocumentExternalMetadataModel]]: ...
def GetDocumentExternalMetadata(api: object, page: Optional[int] = None, size: Optional[int] = None, orderBy: Optional["enumOrderByType"] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentExternalMetadata(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetDocumentExternalMetadata if validate else OP_GetDocumentExternalMetadata_RAW, params=params, data=data)

@overload
def RefreshKsefStatusAsync(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def RefreshKsefStatusAsync(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def RefreshKsefStatusAsync(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def RefreshKsefStatusAsync(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def RefreshKsefStatusAsync(api: object, id: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("RefreshKsefStatusAsync(): ambiguous overload for provided arguments")
        exact_match = 'RefreshKsefStatusAsync'
        exact_match_name = 'RefreshKsefStatusAsync'
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("RefreshKsefStatusAsync(): ambiguous overload for provided arguments")
        exact_match = 'RefreshKsefStatusAsyncGet'
        exact_match_name = 'RefreshKsefStatusAsyncGet'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'RefreshKsefStatusAsync'))
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'RefreshKsefStatusAsyncGet'))
        if not candidates:
            raise TypeError("RefreshKsefStatusAsync(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("RefreshKsefStatusAsync(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'RefreshKsefStatusAsync':
        params, data = _prepare_RefreshKsefStatusAsync(id=id)
        return invoke_operation(api, OP_RefreshKsefStatusAsync if validate else OP_RefreshKsefStatusAsync_RAW, params=params, data=data)
    if selected == 'RefreshKsefStatusAsyncGet':
        params, data = _prepare_RefreshKsefStatusAsyncGet()
        return invoke_operation(api, OP_RefreshKsefStatusAsyncGet if validate else OP_RefreshKsefStatusAsyncGet_RAW, params=params, data=data)
    raise TypeError("RefreshKsefStatusAsync(): internal overload dispatch failure")

__all__ = ["Get", "GetList", "GetListByBuyer", "GetListByRecipient", "GetListByDimension", "GetWZ", "GetZMO", "GetStatus", "GetMarkers", "GetKinds", "GetCatalogs", "GetDEXDocumentTypes", "GetFVSMDocumentTypes", "GetFVSDocumentTypes", "GetFVWDocumentTypes", "GetSKODocumentTypes", "GetSKWDocumentTypes", "GetPARDocumentTypes", "GetSRSDocumentTypes", "GetREXDocumentTypes", "GetRUSDocumentTypes", "GetWDTDocumentTypes", "GetDXKDocumentTypes", "GetPRKDocumentTypes", "GetSRKDocumentTypes", "GetRKSDocumentTypes", "GetRXKDocumentTypes", "GetFVMKDocumentTypes", "GetFKSDocumentTypes", "GetFKWDocumentTypes", "GetSKKDocumentTypes", "GetSKWKDocumentTypes", "GetWKSDocumentTypes", "GetWDTKDocumentTypes", "GetDocumentSeries", "GetPDF", "GetCorrection", "GetCorrectionSequence", "IncrementalSync", "GetPagedDocument", "GetDocumentTypesWithRange", "GetDocumentExternalMetadata", "RefreshKsefStatusAsync"]
