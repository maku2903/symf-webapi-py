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
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDFSettings
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseCorrection
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocument
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentCorrection
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentListElement
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentPZ
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentStatus
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByBufferNumber,
    _prepare_GetCorrection,
    _prepare_GetCorrectionByBufferNumber,
    _prepare_GetList,
    _prepare_GetListBySeller,
    _prepare_GetListBySellerByDateFromDateToSellerCode,
    _prepare_GetListByDeliverer,
    _prepare_GetListByDelivererByDateFromDateToDelivererCode,
    _prepare_GetListByDimension,
    _prepare_GetPZ,
    _prepare_GetPZByBufferDocumentNumber,
    _prepare_GetZMW,
    _prepare_GetZMWByBufferDocumentNumber,
    _prepare_GetCorrectionSequence,
    _prepare_GetCorrectionSequenceByBufferDocumentNumber,
    _prepare_GetStatus,
    _prepare_GetStatusByBufferDocumentNumber,
    _prepare_GetMarkers,
    _prepare_GetKinds,
    _prepare_GetCatalogs,
    _prepare_GetPDF,
    _prepare_GetPDFByBufferDocumentNumberPrintNote,
    _prepare_GetDIMDocumentTypes,
    _prepare_GetFVMDocumentTypes,
    _prepare_GetFVRDocumentTypes,
    _prepare_GetFVZDocumentTypes,
    _prepare_GetFWZDocumentTypes,
    _prepare_GetRUZDocumentTypes,
    _prepare_GetWNTDocumentTypes,
    _prepare_GetZRZDocumentTypes,
    _prepare_GetDMKDocumentTypes,
    _prepare_GetFMKDocumentTypes,
    _prepare_GetFRKDocumentTypes,
    _prepare_GetFZKDocumentTypes,
    _prepare_GetFWZKDocumentTypes,
    _prepare_GetRKZDocumentTypes,
    _prepare_GetZRKDocumentTypes,
    _prepare_GetWNKDocumentTypes,
    _prepare_GetDocumentSeries,
    _prepare_GetPagedDocument,
    _prepare_GetPDFByDocumentIdSettings,
    _prepare_GetPDFByBufferDocumentNumberSettings,
    _prepare_GetDocumentTypesWithRange,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetById,
    OP_GetById_RAW,
    OP_GetByBufferNumber,
    OP_GetByBufferNumber_RAW,
    OP_GetCorrection,
    OP_GetCorrection_RAW,
    OP_GetCorrectionByBufferNumber,
    OP_GetCorrectionByBufferNumber_RAW,
    OP_GetList,
    OP_GetList_RAW,
    OP_GetListBySeller,
    OP_GetListBySeller_RAW,
    OP_GetListBySellerByDateFromDateToSellerCode,
    OP_GetListBySellerByDateFromDateToSellerCode_RAW,
    OP_GetListByDeliverer,
    OP_GetListByDeliverer_RAW,
    OP_GetListByDelivererByDateFromDateToDelivererCode,
    OP_GetListByDelivererByDateFromDateToDelivererCode_RAW,
    OP_GetListByDimension,
    OP_GetListByDimension_RAW,
    OP_GetPZ,
    OP_GetPZ_RAW,
    OP_GetPZByBufferDocumentNumber,
    OP_GetPZByBufferDocumentNumber_RAW,
    OP_GetZMW,
    OP_GetZMW_RAW,
    OP_GetZMWByBufferDocumentNumber,
    OP_GetZMWByBufferDocumentNumber_RAW,
    OP_GetCorrectionSequence,
    OP_GetCorrectionSequence_RAW,
    OP_GetCorrectionSequenceByBufferDocumentNumber,
    OP_GetCorrectionSequenceByBufferDocumentNumber_RAW,
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
    OP_GetPDF,
    OP_GetPDF_RAW,
    OP_GetPDFByBufferDocumentNumberPrintNote,
    OP_GetPDFByBufferDocumentNumberPrintNote_RAW,
    OP_GetDIMDocumentTypes,
    OP_GetDIMDocumentTypes_RAW,
    OP_GetFVMDocumentTypes,
    OP_GetFVMDocumentTypes_RAW,
    OP_GetFVRDocumentTypes,
    OP_GetFVRDocumentTypes_RAW,
    OP_GetFVZDocumentTypes,
    OP_GetFVZDocumentTypes_RAW,
    OP_GetFWZDocumentTypes,
    OP_GetFWZDocumentTypes_RAW,
    OP_GetRUZDocumentTypes,
    OP_GetRUZDocumentTypes_RAW,
    OP_GetWNTDocumentTypes,
    OP_GetWNTDocumentTypes_RAW,
    OP_GetZRZDocumentTypes,
    OP_GetZRZDocumentTypes_RAW,
    OP_GetDMKDocumentTypes,
    OP_GetDMKDocumentTypes_RAW,
    OP_GetFMKDocumentTypes,
    OP_GetFMKDocumentTypes_RAW,
    OP_GetFRKDocumentTypes,
    OP_GetFRKDocumentTypes_RAW,
    OP_GetFZKDocumentTypes,
    OP_GetFZKDocumentTypes_RAW,
    OP_GetFWZKDocumentTypes,
    OP_GetFWZKDocumentTypes_RAW,
    OP_GetRKZDocumentTypes,
    OP_GetRKZDocumentTypes_RAW,
    OP_GetZRKDocumentTypes,
    OP_GetZRKDocumentTypes_RAW,
    OP_GetWNKDocumentTypes,
    OP_GetWNKDocumentTypes_RAW,
    OP_GetDocumentSeries,
    OP_GetDocumentSeries_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
    OP_GetPDFByDocumentIdSettings,
    OP_GetPDFByDocumentIdSettings_RAW,
    OP_GetPDFByBufferDocumentNumberSettings,
    OP_GetPDFByBufferDocumentNumberSettings_RAW,
    OP_GetDocumentTypesWithRange,
    OP_GetDocumentTypesWithRange_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def Get(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
@overload
def Get(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocument]: ...
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
def GetCorrection(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[PurchaseCorrection]: ...
@overload
def GetCorrection(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[PurchaseCorrection]: ...
@overload
def GetCorrection(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[PurchaseCorrection]: ...
@overload
def GetCorrection(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[PurchaseCorrection]: ...
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
def GetList(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetList(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
def GetList(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetList(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetList if validate else OP_GetList_RAW, params=params, data=data)

@overload
def GetListBySeller(api: SyncInvokerProtocol, sellerId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetListBySeller(api: SyncRequestProtocol, sellerId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetListBySeller(api: SyncInvokerProtocol, sellerCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetListBySeller(api: SyncRequestProtocol, sellerCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
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
def GetListByDeliverer(api: SyncInvokerProtocol, delivererId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetListByDeliverer(api: SyncRequestProtocol, delivererId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetListByDeliverer(api: SyncInvokerProtocol, delivererCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetListByDeliverer(api: SyncRequestProtocol, delivererCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
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
def GetListByDimension(api: SyncInvokerProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetListByDimension(api: SyncRequestProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
def GetListByDimension(api: object, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetListByDimension(dimensionCode=dimensionCode, dictionaryValue=dictionaryValue, value=value)
    return invoke_operation(api, OP_GetListByDimension if validate else OP_GetListByDimension_RAW, params=params, data=data)

@overload
def GetPZ(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def GetPZ(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def GetPZ(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def GetPZ(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
def GetPZ(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("GetPZ(): ambiguous overload for provided arguments")
        exact_match = 'GetPZ'
        exact_match_name = 'GetPZ'
    if provided_names == {'buffer', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetPZ(): ambiguous overload for provided arguments")
        exact_match = 'GetPZByBufferDocumentNumber'
        exact_match_name = 'GetPZByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetPZ'))
        if {'buffer', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber'}):
            candidates.append((2, -2, 'GetPZByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetPZ(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetPZ(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetPZ':
        params, data = _prepare_GetPZ(documentId=documentId)
        return invoke_operation(api, OP_GetPZ if validate else OP_GetPZ_RAW, params=params, data=data)
    if selected == 'GetPZByBufferDocumentNumber':
        params, data = _prepare_GetPZByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetPZByBufferDocumentNumber if validate else OP_GetPZByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetPZ(): internal overload dispatch failure")

@overload
def GetZMW(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def GetZMW(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def GetZMW(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
@overload
def GetZMW(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentPZ]]: ...
def GetZMW(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("GetZMW(): ambiguous overload for provided arguments")
        exact_match = 'GetZMW'
        exact_match_name = 'GetZMW'
    if provided_names == {'buffer', 'documentNumber'}:
        if exact_match_name is not None:
            raise TypeError("GetZMW(): ambiguous overload for provided arguments")
        exact_match = 'GetZMWByBufferDocumentNumber'
        exact_match_name = 'GetZMWByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetZMW'))
        if {'buffer', 'documentNumber'}.issubset(provided_names) and provided_names.issubset({'buffer', 'documentNumber'}):
            candidates.append((2, -2, 'GetZMWByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetZMW(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetZMW(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetZMW':
        params, data = _prepare_GetZMW(documentId=documentId)
        return invoke_operation(api, OP_GetZMW if validate else OP_GetZMW_RAW, params=params, data=data)
    if selected == 'GetZMWByBufferDocumentNumber':
        params, data = _prepare_GetZMWByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetZMWByBufferDocumentNumber if validate else OP_GetZMWByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetZMW(): internal overload dispatch failure")

@overload
def GetCorrectionSequence(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentCorrection]]: ...
@overload
def GetCorrectionSequence(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentCorrection]]: ...
@overload
def GetCorrectionSequence(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentCorrection]]: ...
@overload
def GetCorrectionSequence(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentCorrection]]: ...
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
def GetStatus(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocumentStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocumentStatus]: ...
@overload
def GetStatus(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocumentStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[PurchaseDocumentStatus]: ...
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
def GetDIMDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetDIMDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetDIMDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDIMDocumentTypes()
    return invoke_operation(api, OP_GetDIMDocumentTypes if validate else OP_GetDIMDocumentTypes_RAW, params=params, data=data)

@overload
def GetFVMDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFVMDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFVMDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFVMDocumentTypes()
    return invoke_operation(api, OP_GetFVMDocumentTypes if validate else OP_GetFVMDocumentTypes_RAW, params=params, data=data)

@overload
def GetFVRDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFVRDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFVRDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFVRDocumentTypes()
    return invoke_operation(api, OP_GetFVRDocumentTypes if validate else OP_GetFVRDocumentTypes_RAW, params=params, data=data)

@overload
def GetFVZDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFVZDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFVZDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFVZDocumentTypes()
    return invoke_operation(api, OP_GetFVZDocumentTypes if validate else OP_GetFVZDocumentTypes_RAW, params=params, data=data)

@overload
def GetFWZDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFWZDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFWZDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFWZDocumentTypes()
    return invoke_operation(api, OP_GetFWZDocumentTypes if validate else OP_GetFWZDocumentTypes_RAW, params=params, data=data)

@overload
def GetRUZDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetRUZDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetRUZDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetRUZDocumentTypes()
    return invoke_operation(api, OP_GetRUZDocumentTypes if validate else OP_GetRUZDocumentTypes_RAW, params=params, data=data)

@overload
def GetWNTDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetWNTDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetWNTDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWNTDocumentTypes()
    return invoke_operation(api, OP_GetWNTDocumentTypes if validate else OP_GetWNTDocumentTypes_RAW, params=params, data=data)

@overload
def GetZRZDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetZRZDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetZRZDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetZRZDocumentTypes()
    return invoke_operation(api, OP_GetZRZDocumentTypes if validate else OP_GetZRZDocumentTypes_RAW, params=params, data=data)

@overload
def GetDMKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetDMKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetDMKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDMKDocumentTypes()
    return invoke_operation(api, OP_GetDMKDocumentTypes if validate else OP_GetDMKDocumentTypes_RAW, params=params, data=data)

@overload
def GetFMKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFMKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFMKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFMKDocumentTypes()
    return invoke_operation(api, OP_GetFMKDocumentTypes if validate else OP_GetFMKDocumentTypes_RAW, params=params, data=data)

@overload
def GetFRKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFRKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFRKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFRKDocumentTypes()
    return invoke_operation(api, OP_GetFRKDocumentTypes if validate else OP_GetFRKDocumentTypes_RAW, params=params, data=data)

@overload
def GetFZKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFZKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFZKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFZKDocumentTypes()
    return invoke_operation(api, OP_GetFZKDocumentTypes if validate else OP_GetFZKDocumentTypes_RAW, params=params, data=data)

@overload
def GetFWZKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetFWZKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetFWZKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFWZKDocumentTypes()
    return invoke_operation(api, OP_GetFWZKDocumentTypes if validate else OP_GetFWZKDocumentTypes_RAW, params=params, data=data)

@overload
def GetRKZDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetRKZDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetRKZDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetRKZDocumentTypes()
    return invoke_operation(api, OP_GetRKZDocumentTypes if validate else OP_GetRKZDocumentTypes_RAW, params=params, data=data)

@overload
def GetZRKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetZRKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetZRKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetZRKDocumentTypes()
    return invoke_operation(api, OP_GetZRKDocumentTypes if validate else OP_GetZRKDocumentTypes_RAW, params=params, data=data)

@overload
def GetWNKDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetWNKDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetWNKDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWNKDocumentTypes()
    return invoke_operation(api, OP_GetWNKDocumentTypes if validate else OP_GetWNKDocumentTypes_RAW, params=params, data=data)

@overload
def GetDocumentSeries(api: SyncInvokerProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
@overload
def GetDocumentSeries(api: SyncRequestProtocol, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentSeries]]: ...
def GetDocumentSeries(api: object, documentTypeId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentSeries(documentTypeId=documentTypeId)
    return invoke_operation(api, OP_GetDocumentSeries if validate else OP_GetDocumentSeries_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

@overload
def GetDocumentTypesWithRange(api: SyncInvokerProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
@overload
def GetDocumentTypesWithRange(api: SyncRequestProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[PurchaseDocumentListElement]]: ...
def GetDocumentTypesWithRange(api: object, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentTypesWithRange(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDocumentTypesWithRange if validate else OP_GetDocumentTypesWithRange_RAW, params=params, data=data)

__all__ = ["Get", "GetCorrection", "GetList", "GetListBySeller", "GetListByDeliverer", "GetListByDimension", "GetPZ", "GetZMW", "GetCorrectionSequence", "GetStatus", "GetMarkers", "GetKinds", "GetCatalogs", "GetPDF", "GetDIMDocumentTypes", "GetFVMDocumentTypes", "GetFVRDocumentTypes", "GetFVZDocumentTypes", "GetFWZDocumentTypes", "GetRUZDocumentTypes", "GetWNTDocumentTypes", "GetZRZDocumentTypes", "GetDMKDocumentTypes", "GetFMKDocumentTypes", "GetFRKDocumentTypes", "GetFZKDocumentTypes", "GetFWZKDocumentTypes", "GetRKZDocumentTypes", "GetZRKDocumentTypes", "GetWNKDocumentTypes", "GetDocumentSeries", "GetPagedDocument", "GetDocumentTypesWithRange"]
