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
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDFSettings
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocument
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentFV
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentListElement
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentStatus
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseRegistry
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

_ADAPTER_Get = TypeAdapter(List[WarehouseDocumentListElement])
OP_Get = build_typed_operation(method='GET', path='/api/WarehouseDocuments', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments')

_ADAPTER_GetById = TypeAdapter(WarehouseDocument)
OP_GetById = build_typed_operation(method='GET', path='/api/WarehouseDocuments', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments')

_ADAPTER_GetByBufferNumber = TypeAdapter(WarehouseDocument)
OP_GetByBufferNumber = build_typed_operation(method='GET', path='/api/WarehouseDocuments', adapter=_ADAPTER_GetByBufferNumber)
OP_GetByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments')

_ADAPTER_GetList = TypeAdapter(List[WarehouseDocumentListElement])
OP_GetList = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Filter', adapter=_ADAPTER_GetList)
OP_GetList_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Filter')

_ADAPTER_GetListByContractor = TypeAdapter(List[WarehouseDocumentListElement])
OP_GetListByContractor = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Filter', adapter=_ADAPTER_GetListByContractor)
OP_GetListByContractor_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Filter')

_ADAPTER_GetListByContractorByContractorCodeDateFromDateTo = TypeAdapter(List[WarehouseDocumentListElement])
OP_GetListByContractorByContractorCodeDateFromDateTo = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Filter', adapter=_ADAPTER_GetListByContractorByContractorCodeDateFromDateTo)
OP_GetListByContractorByContractorCodeDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Filter')

_ADAPTER_GetListByWarehouse = TypeAdapter(List[WarehouseDocumentListElement])
OP_GetListByWarehouse = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Filter', adapter=_ADAPTER_GetListByWarehouse)
OP_GetListByWarehouse_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Filter')

_ADAPTER_GetListByWarehouseByDateFromDateToWarehouseCode = TypeAdapter(List[WarehouseDocumentListElement])
OP_GetListByWarehouseByDateFromDateToWarehouseCode = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Filter', adapter=_ADAPTER_GetListByWarehouseByDateFromDateToWarehouseCode)
OP_GetListByWarehouseByDateFromDateToWarehouseCode_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Filter')

_ADAPTER_GetListByDimension = TypeAdapter(List[WarehouseDocumentListElement])
OP_GetListByDimension = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Filter', adapter=_ADAPTER_GetListByDimension)
OP_GetListByDimension_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Filter')

_ADAPTER_GetFV = TypeAdapter(List[WarehouseDocumentFV])
OP_GetFV = build_typed_operation(method='GET', path='/api/WarehouseDocuments/FV', adapter=_ADAPTER_GetFV)
OP_GetFV_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/FV')

_ADAPTER_GetFVByBufferDocumentNumber = TypeAdapter(List[WarehouseDocumentFV])
OP_GetFVByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/WarehouseDocuments/FV', adapter=_ADAPTER_GetFVByBufferDocumentNumber)
OP_GetFVByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/FV')

_ADAPTER_GetStatus = TypeAdapter(WarehouseDocumentStatus)
OP_GetStatus = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Status', adapter=_ADAPTER_GetStatus)
OP_GetStatus_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Status')

_ADAPTER_GetStatusByBufferDocumentNumber = TypeAdapter(WarehouseDocumentStatus)
OP_GetStatusByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Status', adapter=_ADAPTER_GetStatusByBufferDocumentNumber)
OP_GetStatusByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Status')

_ADAPTER_GetMarkers = TypeAdapter(List[Marker])
OP_GetMarkers = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Markers', adapter=_ADAPTER_GetMarkers)
OP_GetMarkers_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Markers')

_ADAPTER_GetKinds = TypeAdapter(List[Kind])
OP_GetKinds = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Kinds', adapter=_ADAPTER_GetKinds)
OP_GetKinds_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Kinds')

_ADAPTER_GetCatalogs = TypeAdapter(List[Catalog])
OP_GetCatalogs = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Catalogs', adapter=_ADAPTER_GetCatalogs)
OP_GetCatalogs_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Catalogs')

_ADAPTER_GetWarehouseRegistries = TypeAdapter(List[WarehouseRegistry])
OP_GetWarehouseRegistries = build_typed_operation(method='GET', path='/api/WarehouseDocuments/WarehouseRegistries', adapter=_ADAPTER_GetWarehouseRegistries)
OP_GetWarehouseRegistries_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/WarehouseRegistries')

_ADAPTER_GetPWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetPWDocumentTypes = build_typed_operation(method='GET', path='/api/WarehouseDocuments/PWDocumentTypes', adapter=_ADAPTER_GetPWDocumentTypes)
OP_GetPWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/PWDocumentTypes')

_ADAPTER_GetRWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetRWDocumentTypes = build_typed_operation(method='GET', path='/api/WarehouseDocuments/RWDocumentTypes', adapter=_ADAPTER_GetRWDocumentTypes)
OP_GetRWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/RWDocumentTypes')

_ADAPTER_GetWZODocumentTypes = TypeAdapter(List[DocumentType])
OP_GetWZODocumentTypes = build_typed_operation(method='GET', path='/api/WarehouseDocuments/WZDocumentTypes', adapter=_ADAPTER_GetWZODocumentTypes)
OP_GetWZODocumentTypes_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/WZDocumentTypes')

_ADAPTER_GetPZODocumentTypes = TypeAdapter(List[DocumentType])
OP_GetPZODocumentTypes = build_typed_operation(method='GET', path='/api/WarehouseDocuments/PZDocumentTypes', adapter=_ADAPTER_GetPZODocumentTypes)
OP_GetPZODocumentTypes_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/PZDocumentTypes')

_ADAPTER_GetMMMinusDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetMMMinusDocumentTypes = build_typed_operation(method='GET', path='/api/WarehouseDocuments/MMMinusDocumentTypes', adapter=_ADAPTER_GetMMMinusDocumentTypes)
OP_GetMMMinusDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/MMMinusDocumentTypes')

_ADAPTER_GetDocumentSeries = TypeAdapter(List[DocumentSeries])
OP_GetDocumentSeries = build_typed_operation(method='GET', path='/api/WarehouseDocuments/DocumentSeries', adapter=_ADAPTER_GetDocumentSeries)
OP_GetDocumentSeries_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/DocumentSeries')

_ADAPTER_GetPDF = TypeAdapter(PDF)
OP_GetPDF = build_typed_operation(method='GET', path='/api/WarehouseDocuments/PDF', adapter=_ADAPTER_GetPDF)
OP_GetPDF_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/PDF')

_ADAPTER_GetPDFByBufferDocumentNumberPrintNote = TypeAdapter(PDF)
OP_GetPDFByBufferDocumentNumberPrintNote = build_typed_operation(method='GET', path='/api/WarehouseDocuments/PDF', adapter=_ADAPTER_GetPDFByBufferDocumentNumberPrintNote)
OP_GetPDFByBufferDocumentNumberPrintNote_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/PDF')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Page')

_ADAPTER_GetPDFByDocumentIdSettings = TypeAdapter(PDF)
OP_GetPDFByDocumentIdSettings = build_typed_operation(method='PATCH', path='/api/WarehouseDocuments/PDF', adapter=_ADAPTER_GetPDFByDocumentIdSettings)
OP_GetPDFByDocumentIdSettings_RAW = build_raw_operation(method='PATCH', path='/api/WarehouseDocuments/PDF')

_ADAPTER_GetPDFByBufferDocumentNumberSettings = TypeAdapter(PDF)
OP_GetPDFByBufferDocumentNumberSettings = build_typed_operation(method='PATCH', path='/api/WarehouseDocuments/PDF', adapter=_ADAPTER_GetPDFByBufferDocumentNumberSettings)
OP_GetPDFByBufferDocumentNumberSettings_RAW = build_raw_operation(method='PATCH', path='/api/WarehouseDocuments/PDF')

_ADAPTER_GetDocumentTypesWithRange = TypeAdapter(List[WarehouseDocumentListElement])
OP_GetDocumentTypesWithRange = build_typed_operation(method='GET', path='/api/WarehouseDocuments/Filter/ByDocumentTypes', adapter=_ADAPTER_GetDocumentTypesWithRange)
OP_GetDocumentTypesWithRange_RAW = build_raw_operation(method='GET', path='/api/WarehouseDocuments/Filter/ByDocumentTypes')
