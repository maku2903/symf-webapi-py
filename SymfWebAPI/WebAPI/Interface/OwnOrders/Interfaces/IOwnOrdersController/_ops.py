from __future__ import annotations

from typing import Any, List, Optional
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
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

_ADAPTER_Get = TypeAdapter(List[OwnOrderListElement])
OP_Get = build_typed_operation(method='GET', path='/api/OwnOrders', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/OwnOrders')

_ADAPTER_GetById = TypeAdapter(OwnOrder)
OP_GetById = build_typed_operation(method='GET', path='/api/OwnOrders', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/OwnOrders')

_ADAPTER_GetByBufferNumber = TypeAdapter(OwnOrder)
OP_GetByBufferNumber = build_typed_operation(method='GET', path='/api/OwnOrders', adapter=_ADAPTER_GetByBufferNumber)
OP_GetByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/OwnOrders')

_ADAPTER_GetList = TypeAdapter(List[OwnOrderListElement])
OP_GetList = build_typed_operation(method='GET', path='/api/OwnOrders/Filter', adapter=_ADAPTER_GetList)
OP_GetList_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Filter')

_ADAPTER_GetListByDeliverer = TypeAdapter(List[OwnOrderListElement])
OP_GetListByDeliverer = build_typed_operation(method='GET', path='/api/OwnOrders/Filter', adapter=_ADAPTER_GetListByDeliverer)
OP_GetListByDeliverer_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Filter')

_ADAPTER_GetListByDelivererByDateFromDateToDelivererCode = TypeAdapter(List[OwnOrderListElement])
OP_GetListByDelivererByDateFromDateToDelivererCode = build_typed_operation(method='GET', path='/api/OwnOrders/Filter', adapter=_ADAPTER_GetListByDelivererByDateFromDateToDelivererCode)
OP_GetListByDelivererByDateFromDateToDelivererCode_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Filter')

_ADAPTER_GetListBySeller = TypeAdapter(List[OwnOrderListElement])
OP_GetListBySeller = build_typed_operation(method='GET', path='/api/OwnOrders/Filter', adapter=_ADAPTER_GetListBySeller)
OP_GetListBySeller_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Filter')

_ADAPTER_GetListBySellerByDateFromDateToSellerCode = TypeAdapter(List[OwnOrderListElement])
OP_GetListBySellerByDateFromDateToSellerCode = build_typed_operation(method='GET', path='/api/OwnOrders/Filter', adapter=_ADAPTER_GetListBySellerByDateFromDateToSellerCode)
OP_GetListBySellerByDateFromDateToSellerCode_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Filter')

_ADAPTER_GetListByDimension = TypeAdapter(List[OwnOrderListElement])
OP_GetListByDimension = build_typed_operation(method='GET', path='/api/OwnOrders/Filter', adapter=_ADAPTER_GetListByDimension)
OP_GetListByDimension_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Filter')

_ADAPTER_GetPZ = TypeAdapter(List[OwnOrderPZ])
OP_GetPZ = build_typed_operation(method='GET', path='/api/OwnOrders/PZ', adapter=_ADAPTER_GetPZ)
OP_GetPZ_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/PZ')

_ADAPTER_GetPZByBufferOrderNumber = TypeAdapter(List[OwnOrderPZ])
OP_GetPZByBufferOrderNumber = build_typed_operation(method='GET', path='/api/OwnOrders/PZ', adapter=_ADAPTER_GetPZByBufferOrderNumber)
OP_GetPZByBufferOrderNumber_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/PZ')

_ADAPTER_GetFV = TypeAdapter(List[OwnOrderFV])
OP_GetFV = build_typed_operation(method='GET', path='/api/OwnOrders/FV', adapter=_ADAPTER_GetFV)
OP_GetFV_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/FV')

_ADAPTER_GetFVByBufferOrderNumber = TypeAdapter(List[OwnOrderFV])
OP_GetFVByBufferOrderNumber = build_typed_operation(method='GET', path='/api/OwnOrders/FV', adapter=_ADAPTER_GetFVByBufferOrderNumber)
OP_GetFVByBufferOrderNumber_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/FV')

_ADAPTER_GetPDF = TypeAdapter(PDF)
OP_GetPDF = build_typed_operation(method='GET', path='/api/OwnOrders/PDF', adapter=_ADAPTER_GetPDF)
OP_GetPDF_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/PDF')

_ADAPTER_GetPDFByBufferOrderNumberPrintNote = TypeAdapter(PDF)
OP_GetPDFByBufferOrderNumberPrintNote = build_typed_operation(method='GET', path='/api/OwnOrders/PDF', adapter=_ADAPTER_GetPDFByBufferOrderNumberPrintNote)
OP_GetPDFByBufferOrderNumberPrintNote_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/PDF')

_ADAPTER_GetZMWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetZMWDocumentTypes = build_typed_operation(method='GET', path='/api/OwnOrders/ZMODocumentTypes', adapter=_ADAPTER_GetZMWDocumentTypes)
OP_GetZMWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/ZMODocumentTypes')

_ADAPTER_GetZWWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetZWWDocumentTypes = build_typed_operation(method='GET', path='/api/OwnOrders/ZWODocumentTypes', adapter=_ADAPTER_GetZWWDocumentTypes)
OP_GetZWWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/ZWODocumentTypes')

_ADAPTER_GetDocumentSeries = TypeAdapter(List[DocumentSeries])
OP_GetDocumentSeries = build_typed_operation(method='GET', path='/api/OwnOrders/DocumentSeries', adapter=_ADAPTER_GetDocumentSeries)
OP_GetDocumentSeries_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/DocumentSeries')

_ADAPTER_GetStatus = TypeAdapter(OwnOrderStatus)
OP_GetStatus = build_typed_operation(method='GET', path='/api/OwnOrders/Status', adapter=_ADAPTER_GetStatus)
OP_GetStatus_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Status')

_ADAPTER_GetStatusByBufferOrderNumber = TypeAdapter(OwnOrderStatus)
OP_GetStatusByBufferOrderNumber = build_typed_operation(method='GET', path='/api/OwnOrders/Status', adapter=_ADAPTER_GetStatusByBufferOrderNumber)
OP_GetStatusByBufferOrderNumber_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Status')

_ADAPTER_GetMarkers = TypeAdapter(List[Marker])
OP_GetMarkers = build_typed_operation(method='GET', path='/api/OwnOrders/Markers', adapter=_ADAPTER_GetMarkers)
OP_GetMarkers_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Markers')

_ADAPTER_GetKinds = TypeAdapter(List[Kind])
OP_GetKinds = build_typed_operation(method='GET', path='/api/OwnOrders/Kinds', adapter=_ADAPTER_GetKinds)
OP_GetKinds_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Kinds')

_ADAPTER_GetCatalogs = TypeAdapter(List[Catalog])
OP_GetCatalogs = build_typed_operation(method='GET', path='/api/OwnOrders/Catalogs', adapter=_ADAPTER_GetCatalogs)
OP_GetCatalogs_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Catalogs')

_ADAPTER_GetPositionRelations = TypeAdapter(OwnOrderPositionRelation)
OP_GetPositionRelations = build_typed_operation(method='GET', path='/api/OwnOrders/PositionRelations', adapter=_ADAPTER_GetPositionRelations)
OP_GetPositionRelations_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/PositionRelations')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/OwnOrders/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Page')

_ADAPTER_GetPDFByOrderIdSettings = TypeAdapter(PDF)
OP_GetPDFByOrderIdSettings = build_typed_operation(method='PATCH', path='/api/OwnOrders/PDF', adapter=_ADAPTER_GetPDFByOrderIdSettings)
OP_GetPDFByOrderIdSettings_RAW = build_raw_operation(method='PATCH', path='/api/OwnOrders/PDF')

_ADAPTER_GetPDFByBufferOrderNumberSettings = TypeAdapter(PDF)
OP_GetPDFByBufferOrderNumberSettings = build_typed_operation(method='PATCH', path='/api/OwnOrders/PDF', adapter=_ADAPTER_GetPDFByBufferOrderNumberSettings)
OP_GetPDFByBufferOrderNumberSettings_RAW = build_raw_operation(method='PATCH', path='/api/OwnOrders/PDF')

_ADAPTER_GetDocumentTypesWithRange = TypeAdapter(List[OwnOrderListElement])
OP_GetDocumentTypesWithRange = build_typed_operation(method='GET', path='/api/OwnOrders/Filter/ByDocumentTypes', adapter=_ADAPTER_GetDocumentTypesWithRange)
OP_GetDocumentTypesWithRange_RAW = build_raw_operation(method='GET', path='/api/OwnOrders/Filter/ByDocumentTypes')
