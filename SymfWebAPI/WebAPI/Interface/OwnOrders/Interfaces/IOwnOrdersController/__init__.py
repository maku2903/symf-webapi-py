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
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Kind
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Marker
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrder
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrderFV
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrderListElement
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrderPZ
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrderPositionRelation
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrderStatus
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDFSettings
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByBufferNumber,
    _prepare_GetList,
    _prepare_GetListByDeliverer,
    _prepare_GetListByDelivererByDateFromDateToDelivererCode,
    _prepare_GetListBySeller,
    _prepare_GetListBySellerByDateFromDateToSellerCode,
    _prepare_GetListByDimension,
    _prepare_GetPZ,
    _prepare_GetPZByBufferOrderNumber,
    _prepare_GetFV,
    _prepare_GetFVByBufferOrderNumber,
    _prepare_GetPDF,
    _prepare_GetPDFByBufferOrderNumberPrintNote,
    _prepare_GetZMWDocumentTypes,
    _prepare_GetZWWDocumentTypes,
    _prepare_GetDocumentSeries,
    _prepare_GetStatus,
    _prepare_GetStatusByBufferOrderNumber,
    _prepare_GetMarkers,
    _prepare_GetKinds,
    _prepare_GetCatalogs,
    _prepare_GetPositionRelations,
    _prepare_GetPagedDocument,
    _prepare_GetPDFByOrderIdSettings,
    _prepare_GetPDFByBufferOrderNumberSettings,
    _prepare_GetDocumentTypesWithRange,
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
    OP_GetListByDeliverer,
    OP_GetListByDeliverer_RAW,
    OP_GetListByDelivererByDateFromDateToDelivererCode,
    OP_GetListByDelivererByDateFromDateToDelivererCode_RAW,
    OP_GetListBySeller,
    OP_GetListBySeller_RAW,
    OP_GetListBySellerByDateFromDateToSellerCode,
    OP_GetListBySellerByDateFromDateToSellerCode_RAW,
    OP_GetListByDimension,
    OP_GetListByDimension_RAW,
    OP_GetPZ,
    OP_GetPZ_RAW,
    OP_GetPZByBufferOrderNumber,
    OP_GetPZByBufferOrderNumber_RAW,
    OP_GetFV,
    OP_GetFV_RAW,
    OP_GetFVByBufferOrderNumber,
    OP_GetFVByBufferOrderNumber_RAW,
    OP_GetPDF,
    OP_GetPDF_RAW,
    OP_GetPDFByBufferOrderNumberPrintNote,
    OP_GetPDFByBufferOrderNumberPrintNote_RAW,
    OP_GetZMWDocumentTypes,
    OP_GetZMWDocumentTypes_RAW,
    OP_GetZWWDocumentTypes,
    OP_GetZWWDocumentTypes_RAW,
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
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
    OP_GetPDFByOrderIdSettings,
    OP_GetPDFByOrderIdSettings_RAW,
    OP_GetPDFByBufferOrderNumberSettings,
    OP_GetPDFByBufferOrderNumberSettings_RAW,
    OP_GetDocumentTypesWithRange,
    OP_GetDocumentTypesWithRange_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[OwnOrder]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[OwnOrder]: ...
@overload
def Get(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[OwnOrder]: ...
@overload
def Get(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[OwnOrder]: ...
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
def GetList(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetList(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
def GetList(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetList(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetList if validate else OP_GetList_RAW, params=params, data=data)

@overload
def GetListByDeliverer(api: SyncInvokerProtocol, delivererId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetListByDeliverer(api: SyncRequestProtocol, delivererId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetListByDeliverer(api: SyncInvokerProtocol, delivererCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetListByDeliverer(api: SyncRequestProtocol, delivererCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
def GetListByDeliverer(api: object, delivererId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, delivererCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'delivererId' if delivererId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'delivererCode' if delivererCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo', 'delivererId'}:
        if exact_match_name is not None:
            raise TypeError("GetListByDeliverer(): ambiguous overload for provided arguments")
        exact_match = 'GetListByDeliverer'
        exact_match_name = 'GetListByDeliverer'
    if provided_names == {'dateFrom', 'dateTo', 'delivererCode'}:
        if exact_match_name is not None:
            raise TypeError("GetListByDeliverer(): ambiguous overload for provided arguments")
        exact_match = 'GetListByDelivererByDateFromDateToDelivererCode'
        exact_match_name = 'GetListByDelivererByDateFromDateToDelivererCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'delivererId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'delivererId'}):
            candidates.append((1, -3, 'GetListByDeliverer'))
        if {'delivererCode'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'delivererCode'}):
            candidates.append((1, -3, 'GetListByDelivererByDateFromDateToDelivererCode'))
        if not candidates:
            raise TypeError("GetListByDeliverer(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByDeliverer(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByDeliverer':
        params, data = _prepare_GetListByDeliverer(delivererId=delivererId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByDeliverer if validate else OP_GetListByDeliverer_RAW, params=params, data=data)
    if selected == 'GetListByDelivererByDateFromDateToDelivererCode':
        params, data = _prepare_GetListByDelivererByDateFromDateToDelivererCode(delivererCode=delivererCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByDelivererByDateFromDateToDelivererCode if validate else OP_GetListByDelivererByDateFromDateToDelivererCode_RAW, params=params, data=data)
    raise TypeError("GetListByDeliverer(): internal overload dispatch failure")

@overload
def GetListBySeller(api: SyncInvokerProtocol, sellerId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetListBySeller(api: SyncRequestProtocol, sellerId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetListBySeller(api: SyncInvokerProtocol, sellerCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetListBySeller(api: SyncRequestProtocol, sellerCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
def GetListBySeller(api: object, sellerId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, sellerCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'sellerId' if sellerId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'sellerCode' if sellerCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'dateTo', 'sellerId'}:
        if exact_match_name is not None:
            raise TypeError("GetListBySeller(): ambiguous overload for provided arguments")
        exact_match = 'GetListBySeller'
        exact_match_name = 'GetListBySeller'
    if provided_names == {'dateFrom', 'dateTo', 'sellerCode'}:
        if exact_match_name is not None:
            raise TypeError("GetListBySeller(): ambiguous overload for provided arguments")
        exact_match = 'GetListBySellerByDateFromDateToSellerCode'
        exact_match_name = 'GetListBySellerByDateFromDateToSellerCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'sellerId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'sellerId'}):
            candidates.append((1, -3, 'GetListBySeller'))
        if {'sellerCode'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'dateTo', 'sellerCode'}):
            candidates.append((1, -3, 'GetListBySellerByDateFromDateToSellerCode'))
        if not candidates:
            raise TypeError("GetListBySeller(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListBySeller(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListBySeller':
        params, data = _prepare_GetListBySeller(sellerId=sellerId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListBySeller if validate else OP_GetListBySeller_RAW, params=params, data=data)
    if selected == 'GetListBySellerByDateFromDateToSellerCode':
        params, data = _prepare_GetListBySellerByDateFromDateToSellerCode(sellerCode=sellerCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListBySellerByDateFromDateToSellerCode if validate else OP_GetListBySellerByDateFromDateToSellerCode_RAW, params=params, data=data)
    raise TypeError("GetListBySeller(): internal overload dispatch failure")

@overload
def GetListByDimension(api: SyncInvokerProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetListByDimension(api: SyncRequestProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
def GetListByDimension(api: object, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetListByDimension(dimensionCode=dimensionCode, dictionaryValue=dictionaryValue, value=value)
    return invoke_operation(api, OP_GetListByDimension if validate else OP_GetListByDimension_RAW, params=params, data=data)

@overload
def GetPZ(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderPZ]]: ...
@overload
def GetPZ(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderPZ]]: ...
@overload
def GetPZ(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderPZ]]: ...
@overload
def GetPZ(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderPZ]]: ...
def GetPZ(api: object, orderId: object = _UNSET, orderNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("GetPZ(): ambiguous overload for provided arguments")
        exact_match = 'GetPZ'
        exact_match_name = 'GetPZ'
    if provided_names == {'buffer', 'orderNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetPZ(): ambiguous overload for provided arguments")
        exact_match = 'GetPZByBufferOrderNumber'
        exact_match_name = 'GetPZByBufferOrderNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'orderId'}.issubset(provided_names) and provided_names.issubset({'orderId'}):
            candidates.append((1, -1, 'GetPZ'))
        if {'buffer', 'orderNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderNumber'}):
            candidates.append((2, -2, 'GetPZByBufferOrderNumber'))
        if not candidates:
            raise TypeError("GetPZ(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetPZ(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetPZ':
        params, data = _prepare_GetPZ(orderId=orderId)
        return invoke_operation(api, OP_GetPZ if validate else OP_GetPZ_RAW, params=params, data=data)
    if selected == 'GetPZByBufferOrderNumber':
        params, data = _prepare_GetPZByBufferOrderNumber(orderNumber=orderNumber, buffer=buffer)
        return invoke_operation(api, OP_GetPZByBufferOrderNumber if validate else OP_GetPZByBufferOrderNumber_RAW, params=params, data=data)
    raise TypeError("GetPZ(): internal overload dispatch failure")

@overload
def GetFV(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderFV]]: ...
@overload
def GetFV(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderFV]]: ...
@overload
def GetFV(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderFV]]: ...
@overload
def GetFV(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderFV]]: ...
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
    if provided_names == {'buffer', 'orderNumber'}:
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
        if {'buffer', 'orderNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderNumber'}):
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
    if provided_names == {'buffer', 'orderNumber', 'printNote'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByBufferOrderNumberPrintNote'
        exact_match_name = 'GetPDFByBufferOrderNumberPrintNote'
    if provided_names == {'orderId', 'settings'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByOrderIdSettings'
        exact_match_name = 'GetPDFByOrderIdSettings'
    if provided_names == {'buffer', 'orderNumber', 'settings'}:
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
        if {'buffer', 'orderNumber', 'printNote'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderNumber', 'printNote'}):
            candidates.append((3, -3, 'GetPDFByBufferOrderNumberPrintNote'))
        if {'orderId', 'settings'}.issubset(provided_names) and provided_names.issubset({'orderId', 'settings'}):
            candidates.append((2, -2, 'GetPDFByOrderIdSettings'))
        if {'buffer', 'orderNumber', 'settings'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderNumber', 'settings'}):
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
def GetZMWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetZMWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetZMWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetZMWDocumentTypes()
    return invoke_operation(api, OP_GetZMWDocumentTypes if validate else OP_GetZMWDocumentTypes_RAW, params=params, data=data)

@overload
def GetZWWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetZWWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetZWWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetZWWDocumentTypes()
    return invoke_operation(api, OP_GetZWWDocumentTypes if validate else OP_GetZWWDocumentTypes_RAW, params=params, data=data)

@overload
def GetDocumentSeries(api: SyncInvokerProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
@overload
def GetDocumentSeries(api: SyncRequestProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
def GetDocumentSeries(api: object, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentSeries(documentTypeId=documentTypeId)
    return invoke_operation(api, OP_GetDocumentSeries if validate else OP_GetDocumentSeries_RAW, params=params, data=data)

@overload
def GetStatus(api: SyncInvokerProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[OwnOrderStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, orderId: int, *, validate: bool = True) -> ResponseEnvelope[OwnOrderStatus]: ...
@overload
def GetStatus(api: SyncInvokerProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[OwnOrderStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, orderNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[OwnOrderStatus]: ...
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
    if provided_names == {'buffer', 'orderNumber'}:
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
        if {'buffer', 'orderNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'orderNumber'}):
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
def GetPositionRelations(api: SyncInvokerProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[OwnOrderPositionRelation]: ...
@overload
def GetPositionRelations(api: SyncRequestProtocol, positionId: int, *, validate: bool = True) -> ResponseEnvelope[OwnOrderPositionRelation]: ...
def GetPositionRelations(api: object, positionId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPositionRelations(positionId=positionId)
    return invoke_operation(api, OP_GetPositionRelations if validate else OP_GetPositionRelations_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

@overload
def GetDocumentTypesWithRange(api: SyncInvokerProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
@overload
def GetDocumentTypesWithRange(api: SyncRequestProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[OwnOrderListElement]]: ...
def GetDocumentTypesWithRange(api: object, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentTypesWithRange(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDocumentTypesWithRange if validate else OP_GetDocumentTypesWithRange_RAW, params=params, data=data)

__all__ = ["Get", "GetList", "GetListByDeliverer", "GetListBySeller", "GetListByDimension", "GetPZ", "GetFV", "GetPDF", "GetZMWDocumentTypes", "GetZWWDocumentTypes", "GetDocumentSeries", "GetStatus", "GetMarkers", "GetKinds", "GetCatalogs", "GetPositionRelations", "GetPagedDocument", "GetDocumentTypesWithRange"]
