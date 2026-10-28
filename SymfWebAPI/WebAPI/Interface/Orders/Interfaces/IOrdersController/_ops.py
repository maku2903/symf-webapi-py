from __future__ import annotations

from typing import Any, List, Optional
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
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

_ADAPTER_Get = TypeAdapter(List[OrderListElement])
OP_Get = build_typed_operation(method='GET', path='/api/Orders', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Orders')

_ADAPTER_GetById = TypeAdapter(Order)
OP_GetById = build_typed_operation(method='GET', path='/api/Orders', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/Orders')

_ADAPTER_GetByBufferNumber = TypeAdapter(Order)
OP_GetByBufferNumber = build_typed_operation(method='GET', path='/api/Orders', adapter=_ADAPTER_GetByBufferNumber)
OP_GetByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/Orders')

_ADAPTER_GetList = TypeAdapter(List[OrderListElement])
OP_GetList = build_typed_operation(method='GET', path='/api/Orders/Filter', adapter=_ADAPTER_GetList)
OP_GetList_RAW = build_raw_operation(method='GET', path='/api/Orders/Filter')

_ADAPTER_GetListByRecipient = TypeAdapter(List[OrderListElement])
OP_GetListByRecipient = build_typed_operation(method='GET', path='/api/Orders/Filter', adapter=_ADAPTER_GetListByRecipient)
OP_GetListByRecipient_RAW = build_raw_operation(method='GET', path='/api/Orders/Filter')

_ADAPTER_GetListByRecipientByDateFromDateToRecipientCode = TypeAdapter(List[OrderListElement])
OP_GetListByRecipientByDateFromDateToRecipientCode = build_typed_operation(method='GET', path='/api/Orders/Filter', adapter=_ADAPTER_GetListByRecipientByDateFromDateToRecipientCode)
OP_GetListByRecipientByDateFromDateToRecipientCode_RAW = build_raw_operation(method='GET', path='/api/Orders/Filter')

_ADAPTER_GetListByBuyer = TypeAdapter(List[OrderListElement])
OP_GetListByBuyer = build_typed_operation(method='GET', path='/api/Orders/Filter', adapter=_ADAPTER_GetListByBuyer)
OP_GetListByBuyer_RAW = build_raw_operation(method='GET', path='/api/Orders/Filter')

_ADAPTER_GetListByBuyerByBuyerCodeDateFromDateTo = TypeAdapter(List[OrderListElement])
OP_GetListByBuyerByBuyerCodeDateFromDateTo = build_typed_operation(method='GET', path='/api/Orders/Filter', adapter=_ADAPTER_GetListByBuyerByBuyerCodeDateFromDateTo)
OP_GetListByBuyerByBuyerCodeDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Orders/Filter')

_ADAPTER_GetListByDimension = TypeAdapter(List[OrderListElement])
OP_GetListByDimension = build_typed_operation(method='GET', path='/api/Orders/Filter', adapter=_ADAPTER_GetListByDimension)
OP_GetListByDimension_RAW = build_raw_operation(method='GET', path='/api/Orders/Filter')

_ADAPTER_GetWZ = TypeAdapter(List[OrderWZ])
OP_GetWZ = build_typed_operation(method='GET', path='/api/Orders/WZ', adapter=_ADAPTER_GetWZ)
OP_GetWZ_RAW = build_raw_operation(method='GET', path='/api/Orders/WZ')

_ADAPTER_GetWZByBufferOrderNumber = TypeAdapter(List[OrderWZ])
OP_GetWZByBufferOrderNumber = build_typed_operation(method='GET', path='/api/Orders/WZ', adapter=_ADAPTER_GetWZByBufferOrderNumber)
OP_GetWZByBufferOrderNumber_RAW = build_raw_operation(method='GET', path='/api/Orders/WZ')

_ADAPTER_GetFV = TypeAdapter(List[OrderFV])
OP_GetFV = build_typed_operation(method='GET', path='/api/Orders/FV', adapter=_ADAPTER_GetFV)
OP_GetFV_RAW = build_raw_operation(method='GET', path='/api/Orders/FV')

_ADAPTER_GetFVByBufferOrderNumber = TypeAdapter(List[OrderFV])
OP_GetFVByBufferOrderNumber = build_typed_operation(method='GET', path='/api/Orders/FV', adapter=_ADAPTER_GetFVByBufferOrderNumber)
OP_GetFVByBufferOrderNumber_RAW = build_raw_operation(method='GET', path='/api/Orders/FV')

_ADAPTER_GetPDF = TypeAdapter(PDF)
OP_GetPDF = build_typed_operation(method='GET', path='/api/Orders/PDF', adapter=_ADAPTER_GetPDF)
OP_GetPDF_RAW = build_raw_operation(method='GET', path='/api/Orders/PDF')

_ADAPTER_GetPDFByBufferOrderNumberPrintNote = TypeAdapter(PDF)
OP_GetPDFByBufferOrderNumberPrintNote = build_typed_operation(method='GET', path='/api/Orders/PDF', adapter=_ADAPTER_GetPDFByBufferOrderNumberPrintNote)
OP_GetPDFByBufferOrderNumberPrintNote_RAW = build_raw_operation(method='GET', path='/api/Orders/PDF')

_ADAPTER_GetInvoicesPDF = TypeAdapter(List[PDF])
OP_GetInvoicesPDF = build_typed_operation(method='GET', path='/api/Orders/InvoicesPDF', adapter=_ADAPTER_GetInvoicesPDF)
OP_GetInvoicesPDF_RAW = build_raw_operation(method='GET', path='/api/Orders/InvoicesPDF')

_ADAPTER_GetInvoicesPDFByBufferOrderNumberPrintNote = TypeAdapter(List[PDF])
OP_GetInvoicesPDFByBufferOrderNumberPrintNote = build_typed_operation(method='GET', path='/api/Orders/InvoicesPDF', adapter=_ADAPTER_GetInvoicesPDFByBufferOrderNumberPrintNote)
OP_GetInvoicesPDFByBufferOrderNumberPrintNote_RAW = build_raw_operation(method='GET', path='/api/Orders/InvoicesPDF')

_ADAPTER_GetZMODocumentTypes = TypeAdapter(List[DocumentType])
OP_GetZMODocumentTypes = build_typed_operation(method='GET', path='/api/Orders/ZMODocumentTypes', adapter=_ADAPTER_GetZMODocumentTypes)
OP_GetZMODocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Orders/ZMODocumentTypes')

_ADAPTER_GetZWODocumentTypes = TypeAdapter(List[DocumentType])
OP_GetZWODocumentTypes = build_typed_operation(method='GET', path='/api/Orders/ZWODocumentTypes', adapter=_ADAPTER_GetZWODocumentTypes)
OP_GetZWODocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Orders/ZWODocumentTypes')

_ADAPTER_GetDocumentSeries = TypeAdapter(List[DocumentSeries])
OP_GetDocumentSeries = build_typed_operation(method='GET', path='/api/Orders/DocumentSeries', adapter=_ADAPTER_GetDocumentSeries)
OP_GetDocumentSeries_RAW = build_raw_operation(method='GET', path='/api/Orders/DocumentSeries')

_ADAPTER_GetStatus = TypeAdapter(OrderStatus)
OP_GetStatus = build_typed_operation(method='GET', path='/api/Orders/Status', adapter=_ADAPTER_GetStatus)
OP_GetStatus_RAW = build_raw_operation(method='GET', path='/api/Orders/Status')

_ADAPTER_GetStatusByBufferOrderNumber = TypeAdapter(OrderStatus)
OP_GetStatusByBufferOrderNumber = build_typed_operation(method='GET', path='/api/Orders/Status', adapter=_ADAPTER_GetStatusByBufferOrderNumber)
OP_GetStatusByBufferOrderNumber_RAW = build_raw_operation(method='GET', path='/api/Orders/Status')

_ADAPTER_GetMarkers = TypeAdapter(List[Marker])
OP_GetMarkers = build_typed_operation(method='GET', path='/api/Orders/Markers', adapter=_ADAPTER_GetMarkers)
OP_GetMarkers_RAW = build_raw_operation(method='GET', path='/api/Orders/Markers')

_ADAPTER_GetKinds = TypeAdapter(List[Kind])
OP_GetKinds = build_typed_operation(method='GET', path='/api/Orders/Kinds', adapter=_ADAPTER_GetKinds)
OP_GetKinds_RAW = build_raw_operation(method='GET', path='/api/Orders/Kinds')

_ADAPTER_GetCatalogs = TypeAdapter(List[Catalog])
OP_GetCatalogs = build_typed_operation(method='GET', path='/api/Orders/Catalogs', adapter=_ADAPTER_GetCatalogs)
OP_GetCatalogs_RAW = build_raw_operation(method='GET', path='/api/Orders/Catalogs')

_ADAPTER_GetPositionRelations = TypeAdapter(OrderPositionRelation)
OP_GetPositionRelations = build_typed_operation(method='GET', path='/api/Orders/PositionRelations', adapter=_ADAPTER_GetPositionRelations)
OP_GetPositionRelations_RAW = build_raw_operation(method='GET', path='/api/Orders/PositionRelations')

_ADAPTER_IncrementalSync = TypeAdapter(List[IncrementalSyncListElement])
OP_IncrementalSync = build_typed_operation(method='GET', path='/api/Orders/IncrementalSync', adapter=_ADAPTER_IncrementalSync)
OP_IncrementalSync_RAW = build_raw_operation(method='GET', path='/api/Orders/IncrementalSync')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/Orders/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/Orders/Page')

_ADAPTER_GetPDFByOrderIdSettings = TypeAdapter(PDF)
OP_GetPDFByOrderIdSettings = build_typed_operation(method='PATCH', path='/api/Orders/PDF', adapter=_ADAPTER_GetPDFByOrderIdSettings)
OP_GetPDFByOrderIdSettings_RAW = build_raw_operation(method='PATCH', path='/api/Orders/PDF')

_ADAPTER_GetPDFByBufferOrderNumberSettings = TypeAdapter(PDF)
OP_GetPDFByBufferOrderNumberSettings = build_typed_operation(method='PATCH', path='/api/Orders/PDF', adapter=_ADAPTER_GetPDFByBufferOrderNumberSettings)
OP_GetPDFByBufferOrderNumberSettings_RAW = build_raw_operation(method='PATCH', path='/api/Orders/PDF')

_ADAPTER_GetDocumentTypesWithRange = TypeAdapter(List[OrderListElement])
OP_GetDocumentTypesWithRange = build_typed_operation(method='GET', path='/api/Orders/Filter/ByDocumentTypes', adapter=_ADAPTER_GetDocumentTypesWithRange)
OP_GetDocumentTypesWithRange_RAW = build_raw_operation(method='GET', path='/api/Orders/Filter/ByDocumentTypes')

_ADAPTER_GetDocumentExternalMetadata = TypeAdapter(List[DocumentExternalMetadataModel])
OP_GetDocumentExternalMetadata = build_typed_operation(method='GET', path='/api/Orders/ExternalMetadata', adapter=_ADAPTER_GetDocumentExternalMetadata)
OP_GetDocumentExternalMetadata_RAW = build_raw_operation(method='GET', path='/api/Orders/ExternalMetadata')
