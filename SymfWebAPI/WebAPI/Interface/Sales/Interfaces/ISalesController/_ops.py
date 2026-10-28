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

_ADAPTER_Get = TypeAdapter(List[SaleDocumentListElement])
OP_Get = build_typed_operation(method='GET', path='/api/Sales', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Sales')

_ADAPTER_GetById = TypeAdapter(SaleDocument)
OP_GetById = build_typed_operation(method='GET', path='/api/Sales', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/Sales')

_ADAPTER_GetByBufferNumber = TypeAdapter(SaleDocument)
OP_GetByBufferNumber = build_typed_operation(method='GET', path='/api/Sales', adapter=_ADAPTER_GetByBufferNumber)
OP_GetByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/Sales')

_ADAPTER_GetList = TypeAdapter(List[SaleDocumentListElement])
OP_GetList = build_typed_operation(method='GET', path='/api/Sales/Filter', adapter=_ADAPTER_GetList)
OP_GetList_RAW = build_raw_operation(method='GET', path='/api/Sales/Filter')

_ADAPTER_GetListByBuyer = TypeAdapter(List[SaleDocumentListElement])
OP_GetListByBuyer = build_typed_operation(method='GET', path='/api/Sales/Filter', adapter=_ADAPTER_GetListByBuyer)
OP_GetListByBuyer_RAW = build_raw_operation(method='GET', path='/api/Sales/Filter')

_ADAPTER_GetListByBuyerByBuyerCodeDateFromDateTo = TypeAdapter(List[SaleDocumentListElement])
OP_GetListByBuyerByBuyerCodeDateFromDateTo = build_typed_operation(method='GET', path='/api/Sales/Filter', adapter=_ADAPTER_GetListByBuyerByBuyerCodeDateFromDateTo)
OP_GetListByBuyerByBuyerCodeDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Sales/Filter')

_ADAPTER_GetListByRecipient = TypeAdapter(List[SaleDocumentListElement])
OP_GetListByRecipient = build_typed_operation(method='GET', path='/api/Sales/Filter', adapter=_ADAPTER_GetListByRecipient)
OP_GetListByRecipient_RAW = build_raw_operation(method='GET', path='/api/Sales/Filter')

_ADAPTER_GetListByRecipientByDateFromDateToRecipientCode = TypeAdapter(List[SaleDocumentListElement])
OP_GetListByRecipientByDateFromDateToRecipientCode = build_typed_operation(method='GET', path='/api/Sales/Filter', adapter=_ADAPTER_GetListByRecipientByDateFromDateToRecipientCode)
OP_GetListByRecipientByDateFromDateToRecipientCode_RAW = build_raw_operation(method='GET', path='/api/Sales/Filter')

_ADAPTER_GetListByDimension = TypeAdapter(List[SaleDocumentListElement])
OP_GetListByDimension = build_typed_operation(method='GET', path='/api/Sales/Filter', adapter=_ADAPTER_GetListByDimension)
OP_GetListByDimension_RAW = build_raw_operation(method='GET', path='/api/Sales/Filter')

_ADAPTER_GetWZ = TypeAdapter(List[SaleDocumentWZ])
OP_GetWZ = build_typed_operation(method='GET', path='/api/Sales/WZ', adapter=_ADAPTER_GetWZ)
OP_GetWZ_RAW = build_raw_operation(method='GET', path='/api/Sales/WZ')

_ADAPTER_GetWZByBufferDocumentNumber = TypeAdapter(List[SaleDocumentWZ])
OP_GetWZByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Sales/WZ', adapter=_ADAPTER_GetWZByBufferDocumentNumber)
OP_GetWZByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Sales/WZ')

_ADAPTER_GetZMO = TypeAdapter(List[SaleDocumentZMO])
OP_GetZMO = build_typed_operation(method='GET', path='/api/Sales/ZMO', adapter=_ADAPTER_GetZMO)
OP_GetZMO_RAW = build_raw_operation(method='GET', path='/api/Sales/ZMO')

_ADAPTER_GetZMOByBufferDocumentNumber = TypeAdapter(List[SaleDocumentZMO])
OP_GetZMOByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Sales/ZMO', adapter=_ADAPTER_GetZMOByBufferDocumentNumber)
OP_GetZMOByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Sales/ZMO')

_ADAPTER_GetStatus = TypeAdapter(SaleDocumentStatus)
OP_GetStatus = build_typed_operation(method='GET', path='/api/Sales/Status', adapter=_ADAPTER_GetStatus)
OP_GetStatus_RAW = build_raw_operation(method='GET', path='/api/Sales/Status')

_ADAPTER_GetStatusByBufferDocumentNumber = TypeAdapter(SaleDocumentStatus)
OP_GetStatusByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Sales/Status', adapter=_ADAPTER_GetStatusByBufferDocumentNumber)
OP_GetStatusByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Sales/Status')

_ADAPTER_GetMarkers = TypeAdapter(List[Marker])
OP_GetMarkers = build_typed_operation(method='GET', path='/api/Sales/Markers', adapter=_ADAPTER_GetMarkers)
OP_GetMarkers_RAW = build_raw_operation(method='GET', path='/api/Sales/Markers')

_ADAPTER_GetKinds = TypeAdapter(List[Kind])
OP_GetKinds = build_typed_operation(method='GET', path='/api/Sales/Kinds', adapter=_ADAPTER_GetKinds)
OP_GetKinds_RAW = build_raw_operation(method='GET', path='/api/Sales/Kinds')

_ADAPTER_GetCatalogs = TypeAdapter(List[Catalog])
OP_GetCatalogs = build_typed_operation(method='GET', path='/api/Sales/Catalogs', adapter=_ADAPTER_GetCatalogs)
OP_GetCatalogs_RAW = build_raw_operation(method='GET', path='/api/Sales/Catalogs')

_ADAPTER_GetDEXDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetDEXDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/DEXDocumentTypes', adapter=_ADAPTER_GetDEXDocumentTypes)
OP_GetDEXDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/DEXDocumentTypes')

_ADAPTER_GetFVSMDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFVSMDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/FVSMDocumentTypes', adapter=_ADAPTER_GetFVSMDocumentTypes)
OP_GetFVSMDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/FVSMDocumentTypes')

_ADAPTER_GetFVSDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFVSDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/FVSDocumentTypes', adapter=_ADAPTER_GetFVSDocumentTypes)
OP_GetFVSDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/FVSDocumentTypes')

_ADAPTER_GetFVWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFVWDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/FVWDocumentTypes', adapter=_ADAPTER_GetFVWDocumentTypes)
OP_GetFVWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/FVWDocumentTypes')

_ADAPTER_GetSKODocumentTypes = TypeAdapter(List[DocumentType])
OP_GetSKODocumentTypes = build_typed_operation(method='GET', path='/api/Sales/SKODocumentTypes', adapter=_ADAPTER_GetSKODocumentTypes)
OP_GetSKODocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/SKODocumentTypes')

_ADAPTER_GetSKWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetSKWDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/SKWDocumentTypes', adapter=_ADAPTER_GetSKWDocumentTypes)
OP_GetSKWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/SKWDocumentTypes')

_ADAPTER_GetPARDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetPARDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/PARDocumentTypes', adapter=_ADAPTER_GetPARDocumentTypes)
OP_GetPARDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/PARDocumentTypes')

_ADAPTER_GetSRSDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetSRSDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/SRSDocumentTypes', adapter=_ADAPTER_GetSRSDocumentTypes)
OP_GetSRSDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/SRSDocumentTypes')

_ADAPTER_GetREXDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetREXDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/REXDocumentTypes', adapter=_ADAPTER_GetREXDocumentTypes)
OP_GetREXDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/REXDocumentTypes')

_ADAPTER_GetRUSDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetRUSDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/RUSDocumentTypes', adapter=_ADAPTER_GetRUSDocumentTypes)
OP_GetRUSDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/RUSDocumentTypes')

_ADAPTER_GetWDTDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetWDTDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/WDTDocumentTypes', adapter=_ADAPTER_GetWDTDocumentTypes)
OP_GetWDTDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/WDTDocumentTypes')

_ADAPTER_GetDXKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetDXKDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/DXKDocumentTypes', adapter=_ADAPTER_GetDXKDocumentTypes)
OP_GetDXKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/DXKDocumentTypes')

_ADAPTER_GetPRKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetPRKDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/PRKDocumentTypes', adapter=_ADAPTER_GetPRKDocumentTypes)
OP_GetPRKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/PRKDocumentTypes')

_ADAPTER_GetSRKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetSRKDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/SRKDocumentTypes', adapter=_ADAPTER_GetSRKDocumentTypes)
OP_GetSRKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/SRKDocumentTypes')

_ADAPTER_GetRKSDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetRKSDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/RKSDocumentTypes', adapter=_ADAPTER_GetRKSDocumentTypes)
OP_GetRKSDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/RKSDocumentTypes')

_ADAPTER_GetRXKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetRXKDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/RXKDocumentTypes', adapter=_ADAPTER_GetRXKDocumentTypes)
OP_GetRXKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/RXKDocumentTypes')

_ADAPTER_GetFVMKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFVMKDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/FVMKDocumentTypes', adapter=_ADAPTER_GetFVMKDocumentTypes)
OP_GetFVMKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/FVMKDocumentTypes')

_ADAPTER_GetFKSDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFKSDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/FKSDocumentTypes', adapter=_ADAPTER_GetFKSDocumentTypes)
OP_GetFKSDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/FKSDocumentTypes')

_ADAPTER_GetFKWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFKWDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/FKWDocumentTypes', adapter=_ADAPTER_GetFKWDocumentTypes)
OP_GetFKWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/FKWDocumentTypes')

_ADAPTER_GetSKKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetSKKDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/SKKDocumentTypes', adapter=_ADAPTER_GetSKKDocumentTypes)
OP_GetSKKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/SKKDocumentTypes')

_ADAPTER_GetSKWKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetSKWKDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/SKWKDocumentTypes', adapter=_ADAPTER_GetSKWKDocumentTypes)
OP_GetSKWKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/SKWKDocumentTypes')

_ADAPTER_GetWKSDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetWKSDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/WKSDocumentTypes', adapter=_ADAPTER_GetWKSDocumentTypes)
OP_GetWKSDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/WKSDocumentTypes')

_ADAPTER_GetWDTKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetWDTKDocumentTypes = build_typed_operation(method='GET', path='/api/Sales/WDTKDocumentTypes', adapter=_ADAPTER_GetWDTKDocumentTypes)
OP_GetWDTKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Sales/WDTKDocumentTypes')

_ADAPTER_GetDocumentSeries = TypeAdapter(List[DocumentSeries])
OP_GetDocumentSeries = build_typed_operation(method='GET', path='/api/Sales/DocumentSeries', adapter=_ADAPTER_GetDocumentSeries)
OP_GetDocumentSeries_RAW = build_raw_operation(method='GET', path='/api/Sales/DocumentSeries')

_ADAPTER_GetPDF = TypeAdapter(PDF)
OP_GetPDF = build_typed_operation(method='GET', path='/api/Sales/PDF', adapter=_ADAPTER_GetPDF)
OP_GetPDF_RAW = build_raw_operation(method='GET', path='/api/Sales/PDF')

_ADAPTER_GetPDFByBufferDocumentNumberPrintNote = TypeAdapter(PDF)
OP_GetPDFByBufferDocumentNumberPrintNote = build_typed_operation(method='GET', path='/api/Sales/PDF', adapter=_ADAPTER_GetPDFByBufferDocumentNumberPrintNote)
OP_GetPDFByBufferDocumentNumberPrintNote_RAW = build_raw_operation(method='GET', path='/api/Sales/PDF')

_ADAPTER_GetCorrection = TypeAdapter(SaleCorrection)
OP_GetCorrection = build_typed_operation(method='GET', path='/api/Sales/Correction', adapter=_ADAPTER_GetCorrection)
OP_GetCorrection_RAW = build_raw_operation(method='GET', path='/api/Sales/Correction')

_ADAPTER_GetCorrectionByBufferNumber = TypeAdapter(SaleCorrection)
OP_GetCorrectionByBufferNumber = build_typed_operation(method='GET', path='/api/Sales/Correction', adapter=_ADAPTER_GetCorrectionByBufferNumber)
OP_GetCorrectionByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/Sales/Correction')

_ADAPTER_GetCorrectionSequence = TypeAdapter(List[SaleDocumentCorrection])
OP_GetCorrectionSequence = build_typed_operation(method='GET', path='/api/Sales/CorrectionSequence', adapter=_ADAPTER_GetCorrectionSequence)
OP_GetCorrectionSequence_RAW = build_raw_operation(method='GET', path='/api/Sales/CorrectionSequence')

_ADAPTER_GetCorrectionSequenceByBufferDocumentNumber = TypeAdapter(List[SaleDocumentCorrection])
OP_GetCorrectionSequenceByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Sales/CorrectionSequence', adapter=_ADAPTER_GetCorrectionSequenceByBufferDocumentNumber)
OP_GetCorrectionSequenceByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Sales/CorrectionSequence')

_ADAPTER_IncrementalSync = TypeAdapter(List[IncrementalSyncListElement])
OP_IncrementalSync = build_typed_operation(method='GET', path='/api/Sales/IncrementalSync', adapter=_ADAPTER_IncrementalSync)
OP_IncrementalSync_RAW = build_raw_operation(method='GET', path='/api/Sales/IncrementalSync')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/Sales/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/Sales/Page')

_ADAPTER_GetPDFByDocumentIdSettings = TypeAdapter(PDF)
OP_GetPDFByDocumentIdSettings = build_typed_operation(method='PATCH', path='/api/Sales/PDF', adapter=_ADAPTER_GetPDFByDocumentIdSettings)
OP_GetPDFByDocumentIdSettings_RAW = build_raw_operation(method='PATCH', path='/api/Sales/PDF')

_ADAPTER_GetPDFByBufferDocumentNumberSettings = TypeAdapter(PDF)
OP_GetPDFByBufferDocumentNumberSettings = build_typed_operation(method='PATCH', path='/api/Sales/PDF', adapter=_ADAPTER_GetPDFByBufferDocumentNumberSettings)
OP_GetPDFByBufferDocumentNumberSettings_RAW = build_raw_operation(method='PATCH', path='/api/Sales/PDF')

_ADAPTER_GetDocumentTypesWithRange = TypeAdapter(List[SaleDocumentListElement])
OP_GetDocumentTypesWithRange = build_typed_operation(method='GET', path='/api/Sales/Filter/ByDocumentTypes', adapter=_ADAPTER_GetDocumentTypesWithRange)
OP_GetDocumentTypesWithRange_RAW = build_raw_operation(method='GET', path='/api/Sales/Filter/ByDocumentTypes')

_ADAPTER_GetDocumentExternalMetadata = TypeAdapter(List[DocumentExternalMetadataModel])
OP_GetDocumentExternalMetadata = build_typed_operation(method='GET', path='/api/Sales/ExternalMetadata', adapter=_ADAPTER_GetDocumentExternalMetadata)
OP_GetDocumentExternalMetadata_RAW = build_raw_operation(method='GET', path='/api/Sales/ExternalMetadata')

OP_RefreshKsefStatusAsync = build_none_operation(method='GET', path='/api/v2026.2/Sales/Status/Refresh/{id:int}')
OP_RefreshKsefStatusAsync_RAW = build_raw_operation(method='GET', path='/api/v2026.2/Sales/Status/Refresh/{id:int}')

OP_RefreshKsefStatusAsyncGet = build_none_operation(method='GET', path='/api/v2026.2/Sales/Status/Refresh/Batch')
OP_RefreshKsefStatusAsyncGet_RAW = build_raw_operation(method='GET', path='/api/v2026.2/Sales/Status/Refresh/Batch')
