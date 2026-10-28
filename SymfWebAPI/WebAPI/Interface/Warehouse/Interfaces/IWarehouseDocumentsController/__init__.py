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
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocument
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentFV
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentListElement
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentStatus
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseRegistry
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetByBufferNumber,
    _prepare_GetList,
    _prepare_GetListByContractor,
    _prepare_GetListByContractorByContractorCodeDateFromDateTo,
    _prepare_GetListByWarehouse,
    _prepare_GetListByWarehouseByDateFromDateToWarehouseCode,
    _prepare_GetListByDimension,
    _prepare_GetFV,
    _prepare_GetFVByBufferDocumentNumber,
    _prepare_GetStatus,
    _prepare_GetStatusByBufferDocumentNumber,
    _prepare_GetMarkers,
    _prepare_GetKinds,
    _prepare_GetCatalogs,
    _prepare_GetWarehouseRegistries,
    _prepare_GetPWDocumentTypes,
    _prepare_GetRWDocumentTypes,
    _prepare_GetWZODocumentTypes,
    _prepare_GetPZODocumentTypes,
    _prepare_GetMMMinusDocumentTypes,
    _prepare_GetDocumentSeries,
    _prepare_GetPDF,
    _prepare_GetPDFByBufferDocumentNumberPrintNote,
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
    OP_GetList,
    OP_GetList_RAW,
    OP_GetListByContractor,
    OP_GetListByContractor_RAW,
    OP_GetListByContractorByContractorCodeDateFromDateTo,
    OP_GetListByContractorByContractorCodeDateFromDateTo_RAW,
    OP_GetListByWarehouse,
    OP_GetListByWarehouse_RAW,
    OP_GetListByWarehouseByDateFromDateToWarehouseCode,
    OP_GetListByWarehouseByDateFromDateToWarehouseCode_RAW,
    OP_GetListByDimension,
    OP_GetListByDimension_RAW,
    OP_GetFV,
    OP_GetFV_RAW,
    OP_GetFVByBufferDocumentNumber,
    OP_GetFVByBufferDocumentNumber_RAW,
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
    OP_GetWarehouseRegistries,
    OP_GetWarehouseRegistries_RAW,
    OP_GetPWDocumentTypes,
    OP_GetPWDocumentTypes_RAW,
    OP_GetRWDocumentTypes,
    OP_GetRWDocumentTypes_RAW,
    OP_GetWZODocumentTypes,
    OP_GetWZODocumentTypes_RAW,
    OP_GetPZODocumentTypes,
    OP_GetPZODocumentTypes_RAW,
    OP_GetMMMinusDocumentTypes,
    OP_GetMMMinusDocumentTypes_RAW,
    OP_GetDocumentSeries,
    OP_GetDocumentSeries_RAW,
    OP_GetPDF,
    OP_GetPDF_RAW,
    OP_GetPDFByBufferDocumentNumberPrintNote,
    OP_GetPDFByBufferDocumentNumberPrintNote_RAW,
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
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
@overload
def Get(api: SyncInvokerProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
@overload
def Get(api: SyncRequestProtocol, number: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocument]: ...
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
def GetList(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetList(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
def GetList(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetList(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetList if validate else OP_GetList_RAW, params=params, data=data)

@overload
def GetListByContractor(api: SyncInvokerProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetListByContractor(api: SyncRequestProtocol, contractorId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetListByContractor(api: SyncInvokerProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetListByContractor(api: SyncRequestProtocol, contractorCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
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
def GetListByWarehouse(api: SyncInvokerProtocol, warehouseId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetListByWarehouse(api: SyncRequestProtocol, warehouseId: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetListByWarehouse(api: SyncInvokerProtocol, warehouseCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetListByWarehouse(api: SyncRequestProtocol, warehouseCode: str, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
def GetListByWarehouse(api: object, warehouseId: object = _UNSET, dateFrom: object = _UNSET, dateTo: object = _UNSET, warehouseCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'warehouseId' if warehouseId is not _UNSET else None,
        'dateFrom' if dateFrom is not _UNSET else None,
        'dateTo' if dateTo is not _UNSET else None,
        'warehouseCode' if warehouseCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'dateFrom', 'warehouseId', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByWarehouse(): ambiguous overload for provided arguments")
        exact_match = 'GetListByWarehouse'
        exact_match_name = 'GetListByWarehouse'
    if provided_names == {'warehouseCode', 'dateFrom', 'dateTo'}:
        if exact_match_name is not None:
            raise TypeError("GetListByWarehouse(): ambiguous overload for provided arguments")
        exact_match = 'GetListByWarehouseByDateFromDateToWarehouseCode'
        exact_match_name = 'GetListByWarehouseByDateFromDateToWarehouseCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'warehouseId'}.issubset(provided_names) and provided_names.issubset({'dateFrom', 'warehouseId', 'dateTo'}):
            candidates.append((1, -3, 'GetListByWarehouse'))
        if {'warehouseCode'}.issubset(provided_names) and provided_names.issubset({'warehouseCode', 'dateFrom', 'dateTo'}):
            candidates.append((1, -3, 'GetListByWarehouseByDateFromDateToWarehouseCode'))
        if not candidates:
            raise TypeError("GetListByWarehouse(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByWarehouse(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByWarehouse':
        params, data = _prepare_GetListByWarehouse(warehouseId=warehouseId, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByWarehouse if validate else OP_GetListByWarehouse_RAW, params=params, data=data)
    if selected == 'GetListByWarehouseByDateFromDateToWarehouseCode':
        params, data = _prepare_GetListByWarehouseByDateFromDateToWarehouseCode(warehouseCode=warehouseCode, dateFrom=dateFrom, dateTo=dateTo)
        return invoke_operation(api, OP_GetListByWarehouseByDateFromDateToWarehouseCode if validate else OP_GetListByWarehouseByDateFromDateToWarehouseCode_RAW, params=params, data=data)
    raise TypeError("GetListByWarehouse(): internal overload dispatch failure")

@overload
def GetListByDimension(api: SyncInvokerProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetListByDimension(api: SyncRequestProtocol, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
def GetListByDimension(api: object, dimensionCode: str, dictionaryValue: str, value: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetListByDimension(dimensionCode=dimensionCode, dictionaryValue=dictionaryValue, value=value)
    return invoke_operation(api, OP_GetListByDimension if validate else OP_GetListByDimension_RAW, params=params, data=data)

@overload
def GetFV(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentFV]]: ...
@overload
def GetFV(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentFV]]: ...
@overload
def GetFV(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentFV]]: ...
@overload
def GetFV(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentFV]]: ...
def GetFV(api: object, documentId: object = _UNSET, documentNumber: object = _UNSET, buffer: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
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
            raise TypeError("GetFV(): ambiguous overload for provided arguments")
        exact_match = 'GetFV'
        exact_match_name = 'GetFV'
    if provided_names == {'documentNumber', 'buffer'}:
        if exact_match_name is not None:
            raise TypeError("GetFV(): ambiguous overload for provided arguments")
        exact_match = 'GetFVByBufferDocumentNumber'
        exact_match_name = 'GetFVByBufferDocumentNumber'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'documentId'}.issubset(provided_names) and provided_names.issubset({'documentId'}):
            candidates.append((1, -1, 'GetFV'))
        if {'documentNumber', 'buffer'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'buffer'}):
            candidates.append((2, -2, 'GetFVByBufferDocumentNumber'))
        if not candidates:
            raise TypeError("GetFV(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetFV(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetFV':
        params, data = _prepare_GetFV(documentId=documentId)
        return invoke_operation(api, OP_GetFV if validate else OP_GetFV_RAW, params=params, data=data)
    if selected == 'GetFVByBufferDocumentNumber':
        params, data = _prepare_GetFVByBufferDocumentNumber(documentNumber=documentNumber, buffer=buffer)
        return invoke_operation(api, OP_GetFVByBufferDocumentNumber if validate else OP_GetFVByBufferDocumentNumber_RAW, params=params, data=data)
    raise TypeError("GetFV(): internal overload dispatch failure")

@overload
def GetStatus(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocumentStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocumentStatus]: ...
@overload
def GetStatus(api: SyncInvokerProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocumentStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, documentNumber: str, buffer: bool, *, validate: bool = True) -> ResponseEnvelope[WarehouseDocumentStatus]: ...
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
    if provided_names == {'documentNumber', 'buffer'}:
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
        if {'documentNumber', 'buffer'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'buffer'}):
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
def GetWarehouseRegistries(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseRegistry]]: ...
@overload
def GetWarehouseRegistries(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseRegistry]]: ...
def GetWarehouseRegistries(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWarehouseRegistries()
    return invoke_operation(api, OP_GetWarehouseRegistries if validate else OP_GetWarehouseRegistries_RAW, params=params, data=data)

@overload
def GetPWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetPWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetPWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPWDocumentTypes()
    return invoke_operation(api, OP_GetPWDocumentTypes if validate else OP_GetPWDocumentTypes_RAW, params=params, data=data)

@overload
def GetRWDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetRWDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetRWDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetRWDocumentTypes()
    return invoke_operation(api, OP_GetRWDocumentTypes if validate else OP_GetRWDocumentTypes_RAW, params=params, data=data)

@overload
def GetWZODocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetWZODocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetWZODocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWZODocumentTypes()
    return invoke_operation(api, OP_GetWZODocumentTypes if validate else OP_GetWZODocumentTypes_RAW, params=params, data=data)

@overload
def GetPZODocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetPZODocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetPZODocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPZODocumentTypes()
    return invoke_operation(api, OP_GetPZODocumentTypes if validate else OP_GetPZODocumentTypes_RAW, params=params, data=data)

@overload
def GetMMMinusDocumentTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetMMMinusDocumentTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetMMMinusDocumentTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetMMMinusDocumentTypes()
    return invoke_operation(api, OP_GetMMMinusDocumentTypes if validate else OP_GetMMMinusDocumentTypes_RAW, params=params, data=data)

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
    if provided_names == {'documentNumber', 'buffer', 'printNote'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByBufferDocumentNumberPrintNote'
        exact_match_name = 'GetPDFByBufferDocumentNumberPrintNote'
    if provided_names == {'settings', 'documentId'}:
        if exact_match_name is not None:
            raise TypeError("GetPDF(): ambiguous overload for provided arguments")
        exact_match = 'GetPDFByDocumentIdSettings'
        exact_match_name = 'GetPDFByDocumentIdSettings'
    if provided_names == {'documentNumber', 'settings', 'buffer'}:
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
        if {'documentNumber', 'buffer', 'printNote'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'buffer', 'printNote'}):
            candidates.append((3, -3, 'GetPDFByBufferDocumentNumberPrintNote'))
        if {'settings', 'documentId'}.issubset(provided_names) and provided_names.issubset({'settings', 'documentId'}):
            candidates.append((2, -2, 'GetPDFByDocumentIdSettings'))
        if {'documentNumber', 'settings', 'buffer'}.issubset(provided_names) and provided_names.issubset({'documentNumber', 'settings', 'buffer'}):
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
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

@overload
def GetDocumentTypesWithRange(api: SyncInvokerProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
@overload
def GetDocumentTypesWithRange(api: SyncRequestProtocol, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[WarehouseDocumentListElement]]: ...
def GetDocumentTypesWithRange(api: object, dateFrom: "FilterDocumentType", dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDocumentTypesWithRange(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDocumentTypesWithRange if validate else OP_GetDocumentTypesWithRange_RAW, params=params, data=data)

__all__ = ["Get", "GetList", "GetListByContractor", "GetListByWarehouse", "GetListByDimension", "GetFV", "GetStatus", "GetMarkers", "GetKinds", "GetCatalogs", "GetWarehouseRegistries", "GetPWDocumentTypes", "GetRWDocumentTypes", "GetWZODocumentTypes", "GetPZODocumentTypes", "GetMMMinusDocumentTypes", "GetDocumentSeries", "GetPDF", "GetPagedDocument", "GetDocumentTypesWithRange"]
