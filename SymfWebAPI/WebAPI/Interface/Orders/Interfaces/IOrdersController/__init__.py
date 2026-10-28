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
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import Order
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderFV
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderListElement
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderPositionRelation
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderStatus
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderWZ
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDFSettings
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByBufferNumber,
    _prepare_GetList,
    _prepare_GetListByRecipient,
    _prepare_GetListByRecipientByDateFromDateToRecipientCode,
    _prepare_GetListByBuyer,
    _prepare_GetListByBuyerByBuyerCodeDateFromDateTo,
    _prepare_GetListByDimension,
    _prepare_GetWZ,
    _prepare_GetWZByBufferOrderNumber,
    _prepare_GetFV,
    _prepare_GetFVByBufferOrderNumber,
    _prepare_GetPDF,
    _prepare_GetPDFByBufferOrderNumberPrintNote,
    _prepare_GetInvoicesPDF,
    _prepare_GetInvoicesPDFByBufferOrderNumberPrintNote,
    _prepare_GetZMODocumentTypes,
    _prepare_GetZWODocumentTypes,
    _prepare_GetDocumentSeries,
    _prepare_GetStatus,
    _prepare_GetStatusByBufferOrderNumber,
    _prepare_GetMarkers,
    _prepare_GetKinds,
    _prepare_GetCatalogs,
    _prepare_GetPositionRelations,
    _prepare_IncrementalSync,
    _prepare_GetPagedDocument,
    _prepare_GetPDFByOrderIdSettings,
    _prepare_GetPDFByBufferOrderNumberSettings,
    _prepare_GetDocumentTypesWithRange,
    _prepare_GetDocumentExternalMetadata,
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
    OP_GetListByRecipient,
    OP_GetListByRecipient_RAW,
    OP_GetListByRecipientByDateFromDateToRecipientCode,
    OP_GetListByRecipientByDateFromDateToRecipientCode_RAW,
    OP_GetListByBuyer,
    OP_GetListByBuyer_RAW,
    OP_GetListByBuyerByBuyerCodeDateFromDateTo,
    OP_GetListByBuyerByBuyerCodeDateFromDateTo_RAW,
    OP_GetListByDimension,
    OP_GetListByDimension_RAW,
    OP_GetWZ,
    OP_GetWZ_RAW,
    OP_GetWZByBufferOrderNumber,
    OP_GetWZByBufferOrderNumber_RAW,
    OP_GetFV,
    OP_GetFV_RAW,
    OP_GetFVByBufferOrderNumber,
    OP_GetFVByBufferOrderNumber_RAW,
    OP_GetPDF,
    OP_GetPDF_RAW,
    OP_GetPDFByBufferOrderNumberPrintNote,
    OP_GetPDFByBufferOrderNumberPrintNote_RAW,
    OP_GetInvoicesPDF,
    OP_GetInvoicesPDF_RAW,
    OP_GetInvoicesPDFByBufferOrderNumberPrintNote,
    OP_GetInvoicesPDFByBufferOrderNumberPrintNote_RAW,
    OP_GetZMODocumentTypes,
    OP_GetZMODocumentTypes_RAW,
    OP_GetZWODocumentTypes,
    OP_GetZWODocumentTypes_RAW,
    OP_GetDocumentSeries,
    OP_GetDocumentSeries_RAW,
    OP_GetStatus,
    OP_GetStatus_RAW,
    OP_GetStatusByBufferOrderNumber,
    OP_GetStatusByBufferOrderNumber_RAW,
    OP_GetMarkers,
    OP_GetMarkers_RAW,
    OP_GetKinds,
    OP_GetKinds_RAW,
    OP_GetCatalogs,
    OP_GetCatalogs_RAW,
    OP_GetPositionRelations,
    OP_GetPositionRelations_RAW,
    OP_IncrementalSync,
    OP_IncrementalSync_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
    OP_GetPDFByOrderIdSettings,
    OP_GetPDFByOrderIdSettings_RAW,
    OP_GetPDFByBufferOrderNumberSettings,
    OP_GetPDFByBufferOrderNumberSettings_RAW,
    OP_GetDocumentTypesWithRange,
    OP_GetDocumentTypesWithRange_RAW,
    OP_GetDocumentExternalMetadata,
    OP_GetDocumentExternalMetadata_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def Get(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Order]: ...
@overload
def Get(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[Order]: ...
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
def GetList(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetList(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
def GetList(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetList(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetList if validate else OP_GetList_RAW, params=params, data=data)

@overload
def GetListByRecipient(api: SyncInvokerProtocol, recipientId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetListByRecipient(api: SyncRequestProtocol, recipientId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetListByRecipient(api: SyncInvokerProtocol, recipientCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetListByRecipient(api: SyncRequestProtocol, recipientCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
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
    if provided_names == {'recipientId', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByRecipient(): ambiguous overload for provided arguments")
        exact_match = 'GetListByRecipient'
        exact_match_name = 'GetListByRecipient'
    if provided_names == {'dateFrom', 'recipientCode', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByRecipient(): ambiguous overload for provided arguments")
        exact_match = 'GetListByRecipientByDateFromDateToRecipientCode'
        exact_match_name = 'GetListByRecipientByDateFromDateToRecipientCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'recipientId'}.issubset(provided_names) and provided_names.issubset({'recipientId', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByRecipient'))
        if {'recipientCode'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'recipientCode', 'dateTo'}):
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
def GetListByBuyer(api: SyncInvokerProtocol, buyerId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetListByBuyer(api: SyncRequestProtocol, buyerId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetListByBuyer(api: SyncInvokerProtocol, buyerCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetListByBuyer(api: SyncRequestProtocol, buyerCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
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
def GetListByDimension(api: SyncInvokerProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetListByDimension(api: SyncRequestProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
def GetListByDimension(api: object, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetListByDimension(dimensionCode=dimensionCode, dictionaryValue=dictionaryValue, value=value)
    return invoke_operation(api, OP_GetListByDimension if validate else OP_GetListByDimension_RAW, params=params, data=data)

@overload
def GetWZ(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
@overload
def GetWZ(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
@overload
def GetWZ(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
@overload
def GetWZ(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OrderWZ]]: ...
def GetWZ(api: object, orderId: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId'}:
        if exact_match_name is not None:
            raise TypeError("GetWZ(): ambiguous overload for provided arguments")
        exact_match = 'GetWZ'
        exact_match_name = 'GetWZ'
    if provided_names == {'orderNumber', 'buffer'}:
        if exact_match_name is not None:
            raise TypeError("GetWZ(): ambiguous overload for provided arguments")
        exact_match = 'GetWZByBufferOrderNumber'
        exact_match_name = 'GetWZByBufferOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId'}):
            candidates.append((1, -1, 'GetWZ'))
        if {'orderNumber', 'buffer'}.issubset(provided_names) and provided_names.issubset({'orderNumber', 'buffer'}):
            candidates.append((2, -2, 'GetWZByBufferOrderNumber'))
        if not candidates:
            raise TypeError("GetWZ(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetWZ(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetWZ':
        params, data = _prepare_GetWZ(orderId=orderId)
        return invoke_operation(api, OP_GetWZ if validate else OP_GetWZ_RAW, params=params, data=data)
    if selected == 'GetWZByBufferOrderNumber':
        params, data = _prepare_GetWZByBufferOrderNumber(orderNumber=orderNumber, buffer=buffer)
        return invoke_operation(api, OP_GetWZByBufferOrderNumber if validate else OP_GetWZByBufferOrderNumber_RAW, params=params, data=data)
    raise TypeError("GetWZ(): internal overload dispatch failure")

@overload
def GetFV(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
@overload
def GetFV(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
@overload
def GetFV(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
@overload
def GetFV(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OrderFV]]: ...
def GetFV(api: object, orderId: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId'}:
        if exact_match_name is not None:
            raise TypeError("GetFV(): ambiguous overload for provided arguments")
        exact_match = 'GetFV'
        exact_match_name = 'GetFV'
    if provided_names == {'orderNumber', 'buffer'}:
        if exact_match_name is not None:
            raise TypeError("GetFV(): ambiguous overload for provided arguments")
        exact_match = 'GetFVByBufferOrderNumber'
        exact_match_name = 'GetFVByBufferOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId'}):
            candidates.append((1, -1, 'GetFV'))
        if {'orderNumber', 'buffer'}.issubset(provided_names) and provided_names.issubset({'orderNumber', 'buffer'}):
            candidates.append((2, -2, 'GetFVByBufferOrderNumber'))
        if not candidates:
            raise TypeError("GetFV(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetFV(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetFV':
        params, data = _prepare_GetFV(orderId=orderId)
        return invoke_operation(api, OP_GetFV if validate else OP_GetFV_RAW, params=params, data=data)
    if selected == 'GetFVByBufferOrderNumber':
        params, data = _prepare_GetFVByBufferOrderNumber(orderNumber=orderNumber, buffer=buffer)
        return invoke_operation(api, OP_GetFVByBufferOrderNumber if validate else OP_GetFVByBufferOrderNumber_RAW, params=params, data=data)
    raise TypeError("GetFV(): internal overload dispatch failure")

@overload
def GetPDF(api: SyncInvokerProtocol, orderId: int, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, orderId: int, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, orderNumber: str, buffer: bool, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncInvokerProtocol, orderId: int, settings: "PDFSettings", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, orderId: int, settings: "PDFSettings", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, settings: "PDFSettings", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def GetPDF(api: SyncRequestProtocol, orderNumber: str, buffer: bool, settings: "PDFSettings", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
def GetPDF(api: object, orderId: object = _UNSET, printNote: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, settings: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'printNote' if printNote is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
        'settings' if settings is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId', 'printNote'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDF'
        exact_match_name = 'GetPDF'
    if provided_names == {'orderNumber', 'buffer', 'printNote'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByBufferOrderNumberPrintNote'
        exact_match_name = 'GetPDFByBufferOrderNumberPrintNote'
    if provided_names == {'settings', 'orderId'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByOrderIdSettings'
        exact_match_name = 'GetPDFByOrderIdSettings'
    if provided_names == {'settings', 'orderNumber', 'buffer'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByBufferOrderNumberSettings'
        exact_match_name = 'GetPDFByBufferOrderNumberSettings'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId', 'printNote'}.issubset(provided_names) and provided_names.issubset({'orderId', 'printNote'}):
            candidates.append((2, -2, 'GetPDF'))
        if {'orderNumber', 'buffer', 'printNote'}.issubset(provided_names) and provided_names.issubset({'orderNumber', 'buffer', 'printNote'}):
            candidates.append((3, -3, 'GetPDFByBufferOrderNumberPrintNote'))
        if {'settings', 'orderId'}.issubset(provided_names) and provided_names.issubset({'settings', 'orderId'}):
            candidates.append((2, -2, 'GetPDFByOrderIdSettings'))
        if {'settings', 'orderNumber', 'buffer'}.issubset(provided_names) and provided_names.issubset({'settings', 'orderNumber', 'buffer'}):
            candidates.append((3, -3, 'GetPDFByBufferOrderNumberSettings'))
        if not candidates:
            raise TypeError("GetPDF(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetPDF':
        params, data = _prepare_GetPDF(orderId=orderId, printNote=printNote)
        return invoke_operation(api, OP_GetPDF if validate else OP_GetPDF_RAW, params=params, data=data)
    if selected == 'GetPDFByBufferOrderNumberPrintNote':
        params, data = _prepare_GetPDFByBufferOrderNumberPrintNote(orderNumber=orderNumber, buffer=buffer, printNote=printNote)
        return invoke_operation(api, OP_GetPDFByBufferOrderNumberPrintNote if validate else OP_GetPDFByBufferOrderNumberPrintNote_RAW, params=params, data=data)
    if selected == 'GetPDFByOrderIdSettings':
        params, data = _prepare_GetPDFByOrderIdSettings(validate=validate, orderId=orderId, settings=settings)
        return invoke_operation(api, OP_GetPDFByOrderIdSettings if validate else OP_GetPDFByOrderIdSettings_RAW, params=params, data=data)
    if selected == 'GetPDFByBufferOrderNumberSettings':
        params, data = _prepare_GetPDFByBufferOrderNumberSettings(validate=validate, orderNumber=orderNumber, buffer=buffer, settings=settings)
        return invoke_operation(api, OP_GetPDFByBufferOrderNumberSettings if validate else OP_GetPDFByBufferOrderNumberSettings_RAW, params=params, data=data)
    raise TypeError("GetPDF(): internal overload dispatch failure")

@overload
def GetInvoicesPDF(api: SyncInvokerProtocol, orderId: int, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[List[PDF]]: ...
@overload
def GetInvoicesPDF(api: SyncRequestProtocol, orderId: int, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[List[PDF]]: ...
@overload
def GetInvoicesPDF(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[List[PDF]]: ...
@overload
def GetInvoicesPDF(api: SyncRequestProtocol, orderNumber: str, buffer: bool, printNote: bool, *, validate: bool = True) -> ResponseEnvelope[List[PDF]]: ...
def GetInvoicesPDF(api: object, orderId: object = _UNSET, printNote: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'printNote' if printNote is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId', 'printNote'}:
        if exact_match_name is not None:
            raise TypeError("GetInvoicesPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetInvoicesPDF'
        exact_match_name = 'GetInvoicesPDF'
    if provided_names == {'orderNumber', 'buffer', 'printNote'}:
        if exact_match_name is not None:
            raise TypeError("GetInvoicesPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetInvoicesPDFByBufferOrderNumberPrintNote'
        exact_match_name = 'GetInvoicesPDFByBufferOrderNumberPrintNote'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId', 'printNote'}.issubset(provided_names) and provided_names.issubset({'orderId', 'printNote'}):
            candidates.append((2, -2, 'GetInvoicesPDF'))
        if {'orderNumber', 'buffer', 'printNote'}.issubset(provided_names) and provided_names.issubset({'orderNumber', 'buffer', 'printNote'}):
            candidates.append((3, -3, 'GetInvoicesPDFByBufferOrderNumberPrintNote'))
        if not candidates:
            raise TypeError("GetInvoicesPDF(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetInvoicesPDF(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetInvoicesPDF':
        params, data = _prepare_GetInvoicesPDF(orderId=orderId, printNote=printNote)
        return invoke_operation(api, OP_GetInvoicesPDF if validate else OP_GetInvoicesPDF_RAW, params=params, data=data)
    if selected == 'GetInvoicesPDFByBufferOrderNumberPrintNote':
        params, data = _prepare_GetInvoicesPDFByBufferOrderNumberPrintNote(orderNumber=orderNumber, buffer=buffer, printNote=printNote)
        return invoke_operation(api, OP_GetInvoicesPDFByBufferOrderNumberPrintNote if validate else OP_GetInvoicesPDFByBufferOrderNumberPrintNote_RAW, params=params, data=data)
    raise TypeError("GetInvoicesPDF(): internal overload dispatch failure")

@overload
def GetZMODocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetZMODocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetZMODocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetZMODocumentTypes()
    return invoke_operation(api, OP_GetZMODocumentTypes if validate else OP_GetZMODocumentTypes_RAW, params=params, data=data)

@overload
def GetZWODocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetZWODocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetZWODocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetZWODocumentTypes()
    return invoke_operation(api, OP_GetZWODocumentTypes if validate else OP_GetZWODocumentTypes_RAW, params=params, data=data)

@overload
def GetDocumentSeries(api: SyncInvokerProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
@overload
def GetDocumentSeries(api: SyncRequestProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
def GetDocumentSeries(api: object, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentSeries(documentTypeId=documentTypeId)
    return invoke_operation(api, OP_GetDocumentSeries if validate else OP_GetDocumentSeries_RAW, params=params, data=data)

@overload
def GetStatus(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[OrderStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[OrderStatus]: ...
@overload
def GetStatus(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[OrderStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[OrderStatus]: ...
def GetStatus(api: object, orderId: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'orderId' if orderId is not _UNSET else None,
        'orderNumber' if orderNumber is not _UNSET else None,
        'buffer' if buffer is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'orderId'}:
        if exact_match_name is not None:
            raise TypeError("GetStatus(): ambiguous overload for provided arguments")
        exact_match = 'GetStatus'
        exact_match_name = 'GetStatus'
    if provided_names == {'orderNumber', 'buffer'}:
        if exact_match_name is not None:
            raise TypeError("GetStatus(): ambiguous overload for provided arguments")
        exact_match = 'GetStatusByBufferOrderNumber'
        exact_match_name = 'GetStatusByBufferOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId'}):
            candidates.append((1, -1, 'GetStatus'))
        if {'orderNumber', 'buffer'}.issubset(provided_names) and provided_names.issubset({'orderNumber', 'buffer'}):
            candidates.append((2, -2, 'GetStatusByBufferOrderNumber'))
        if not candidates:
            raise TypeError("GetStatus(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetStatus(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetStatus':
        params, data = _prepare_GetStatus(orderId=orderId)
        return invoke_operation(api, OP_GetStatus if validate else OP_GetStatus_RAW, params=params, data=data)
    if selected == 'GetStatusByBufferOrderNumber':
        params, data = _prepare_GetStatusByBufferOrderNumber(orderNumber=orderNumber, buffer=buffer)
        return invoke_operation(api, OP_GetStatusByBufferOrderNumber if validate else OP_GetStatusByBufferOrderNumber_RAW, params=params, data=data)
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
def GetPositionRelations(api: SyncInvokerProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[OrderPositionRelation]: ...
@overload
def GetPositionRelations(api: SyncRequestProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[OrderPositionRelation]: ...
def GetPositionRelations(api: object, positionId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionRelations(positionId=positionId)
    return invoke_operation(api, OP_GetPositionRelations if validate else OP_GetPositionRelations_RAW, params=params, data=data)

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
def GetDocumentTypesWithRange(api: SyncInvokerProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
@overload
def GetDocumentTypesWithRange(api: SyncRequestProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OrderListElement]]: ...
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

__all__ = ["Get", "GetList", "GetListByRecipient", "GetListByBuyer", "GetListByDimension", "GetWZ", "GetFV", "GetPDF", "GetInvoicesPDF", "GetZMODocumentTypes", "GetZWODocumentTypes", "GetDocumentSeries", "GetStatus", "GetMarkers", "GetKinds", "GetCatalogs", "GetPositionRelations", "IncrementalSync", "GetPagedDocument", "GetDocumentTypesWithRange", "GetDocumentExternalMetadata"]
