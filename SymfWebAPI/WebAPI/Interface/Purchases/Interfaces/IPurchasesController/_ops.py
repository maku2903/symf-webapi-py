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
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseCorrection
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocument
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentCorrection
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentListElement
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentPZ
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentStatus
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

_ADAPTER_Get = TypeAdapter(List[PurchaseDocumentListElement])
OP_Get = build_typed_operation(method='GET', path='/api/Purchases', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Purchases')

_ADAPTER_GetById = TypeAdapter(PurchaseDocument)
OP_GetById = build_typed_operation(method='GET', path='/api/Purchases', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/Purchases')

_ADAPTER_GetByBufferNumber = TypeAdapter(PurchaseDocument)
OP_GetByBufferNumber = build_typed_operation(method='GET', path='/api/Purchases', adapter=_ADAPTER_GetByBufferNumber)
OP_GetByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/Purchases')

_ADAPTER_GetCorrection = TypeAdapter(PurchaseCorrection)
OP_GetCorrection = build_typed_operation(method='GET', path='/api/Purchases/Correction', adapter=_ADAPTER_GetCorrection)
OP_GetCorrection_RAW = build_raw_operation(method='GET', path='/api/Purchases/Correction')

_ADAPTER_GetCorrectionByBufferNumber = TypeAdapter(PurchaseCorrection)
OP_GetCorrectionByBufferNumber = build_typed_operation(method='GET', path='/api/Purchases/Correction', adapter=_ADAPTER_GetCorrectionByBufferNumber)
OP_GetCorrectionByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/Purchases/Correction')

_ADAPTER_GetList = TypeAdapter(List[PurchaseDocumentListElement])
OP_GetList = build_typed_operation(method='GET', path='/api/Purchases/Filter', adapter=_ADAPTER_GetList)
OP_GetList_RAW = build_raw_operation(method='GET', path='/api/Purchases/Filter')

_ADAPTER_GetListBySeller = TypeAdapter(List[PurchaseDocumentListElement])
OP_GetListBySeller = build_typed_operation(method='GET', path='/api/Purchases/Filter', adapter=_ADAPTER_GetListBySeller)
OP_GetListBySeller_RAW = build_raw_operation(method='GET', path='/api/Purchases/Filter')

_ADAPTER_GetListBySellerByDateFromDateToSellerCode = TypeAdapter(List[PurchaseDocumentListElement])
OP_GetListBySellerByDateFromDateToSellerCode = build_typed_operation(method='GET', path='/api/Purchases/Filter', adapter=_ADAPTER_GetListBySellerByDateFromDateToSellerCode)
OP_GetListBySellerByDateFromDateToSellerCode_RAW = build_raw_operation(method='GET', path='/api/Purchases/Filter')

_ADAPTER_GetListByDeliverer = TypeAdapter(List[PurchaseDocumentListElement])
OP_GetListByDeliverer = build_typed_operation(method='GET', path='/api/Purchases/Filter', adapter=_ADAPTER_GetListByDeliverer)
OP_GetListByDeliverer_RAW = build_raw_operation(method='GET', path='/api/Purchases/Filter')

_ADAPTER_GetListByDelivererByDateFromDateToDelivererCode = TypeAdapter(List[PurchaseDocumentListElement])
OP_GetListByDelivererByDateFromDateToDelivererCode = build_typed_operation(method='GET', path='/api/Purchases/Filter', adapter=_ADAPTER_GetListByDelivererByDateFromDateToDelivererCode)
OP_GetListByDelivererByDateFromDateToDelivererCode_RAW = build_raw_operation(method='GET', path='/api/Purchases/Filter')

_ADAPTER_GetListByDimension = TypeAdapter(List[PurchaseDocumentListElement])
OP_GetListByDimension = build_typed_operation(method='GET', path='/api/Purchases/Filter', adapter=_ADAPTER_GetListByDimension)
OP_GetListByDimension_RAW = build_raw_operation(method='GET', path='/api/Purchases/Filter')

_ADAPTER_GetPZ = TypeAdapter(List[PurchaseDocumentPZ])
OP_GetPZ = build_typed_operation(method='GET', path='/api/Purchases/PZ', adapter=_ADAPTER_GetPZ)
OP_GetPZ_RAW = build_raw_operation(method='GET', path='/api/Purchases/PZ')

_ADAPTER_GetPZByBufferDocumentNumber = TypeAdapter(List[PurchaseDocumentPZ])
OP_GetPZByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Purchases/PZ', adapter=_ADAPTER_GetPZByBufferDocumentNumber)
OP_GetPZByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Purchases/PZ')

_ADAPTER_GetZMW = TypeAdapter(List[PurchaseDocumentPZ])
OP_GetZMW = build_typed_operation(method='GET', path='/api/Purchases/ZMW', adapter=_ADAPTER_GetZMW)
OP_GetZMW_RAW = build_raw_operation(method='GET', path='/api/Purchases/ZMW')

_ADAPTER_GetZMWByBufferDocumentNumber = TypeAdapter(List[PurchaseDocumentPZ])
OP_GetZMWByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Purchases/ZMW', adapter=_ADAPTER_GetZMWByBufferDocumentNumber)
OP_GetZMWByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Purchases/ZMW')

_ADAPTER_GetCorrectionSequence = TypeAdapter(List[PurchaseDocumentCorrection])
OP_GetCorrectionSequence = build_typed_operation(method='GET', path='/api/Purchases/CorrectionSequence', adapter=_ADAPTER_GetCorrectionSequence)
OP_GetCorrectionSequence_RAW = build_raw_operation(method='GET', path='/api/Purchases/CorrectionSequence')

_ADAPTER_GetCorrectionSequenceByBufferDocumentNumber = TypeAdapter(List[PurchaseDocumentCorrection])
OP_GetCorrectionSequenceByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Purchases/CorrectionSequence', adapter=_ADAPTER_GetCorrectionSequenceByBufferDocumentNumber)
OP_GetCorrectionSequenceByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Purchases/CorrectionSequence')

_ADAPTER_GetStatus = TypeAdapter(PurchaseDocumentStatus)
OP_GetStatus = build_typed_operation(method='GET', path='/api/Purchases/Status', adapter=_ADAPTER_GetStatus)
OP_GetStatus_RAW = build_raw_operation(method='GET', path='/api/Purchases/Status')

_ADAPTER_GetStatusByBufferDocumentNumber = TypeAdapter(PurchaseDocumentStatus)
OP_GetStatusByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Purchases/Status', adapter=_ADAPTER_GetStatusByBufferDocumentNumber)
OP_GetStatusByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Purchases/Status')

_ADAPTER_GetMarkers = TypeAdapter(List[Marker])
OP_GetMarkers = build_typed_operation(method='GET', path='/api/Purchases/Markers', adapter=_ADAPTER_GetMarkers)
OP_GetMarkers_RAW = build_raw_operation(method='GET', path='/api/Purchases/Markers')

_ADAPTER_GetKinds = TypeAdapter(List[Kind])
OP_GetKinds = build_typed_operation(method='GET', path='/api/Purchases/Kinds', adapter=_ADAPTER_GetKinds)
OP_GetKinds_RAW = build_raw_operation(method='GET', path='/api/Purchases/Kinds')

_ADAPTER_GetCatalogs = TypeAdapter(List[Catalog])
OP_GetCatalogs = build_typed_operation(method='GET', path='/api/Purchases/Catalogs', adapter=_ADAPTER_GetCatalogs)
OP_GetCatalogs_RAW = build_raw_operation(method='GET', path='/api/Purchases/Catalogs')

_ADAPTER_GetPDF = TypeAdapter(PDF)
OP_GetPDF = build_typed_operation(method='GET', path='/api/Purchases/PDF', adapter=_ADAPTER_GetPDF)
OP_GetPDF_RAW = build_raw_operation(method='GET', path='/api/Purchases/PDF')

_ADAPTER_GetPDFByBufferDocumentNumberPrintNote = TypeAdapter(PDF)
OP_GetPDFByBufferDocumentNumberPrintNote = build_typed_operation(method='GET', path='/api/Purchases/PDF', adapter=_ADAPTER_GetPDFByBufferDocumentNumberPrintNote)
OP_GetPDFByBufferDocumentNumberPrintNote_RAW = build_raw_operation(method='GET', path='/api/Purchases/PDF')

_ADAPTER_GetDIMDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetDIMDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/DIMDocumentTypes', adapter=_ADAPTER_GetDIMDocumentTypes)
OP_GetDIMDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/DIMDocumentTypes')

_ADAPTER_GetFVMDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFVMDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/FVMDocumentTypes', adapter=_ADAPTER_GetFVMDocumentTypes)
OP_GetFVMDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/FVMDocumentTypes')

_ADAPTER_GetFVRDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFVRDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/FVRDocumentTypes', adapter=_ADAPTER_GetFVRDocumentTypes)
OP_GetFVRDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/FVRDocumentTypes')

_ADAPTER_GetFVZDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFVZDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/FVZDocumentTypes', adapter=_ADAPTER_GetFVZDocumentTypes)
OP_GetFVZDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/FVZDocumentTypes')

_ADAPTER_GetFWZDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFWZDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/FWZDocumentTypes', adapter=_ADAPTER_GetFWZDocumentTypes)
OP_GetFWZDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/FWZDocumentTypes')

_ADAPTER_GetRUZDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetRUZDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/RUZDocumentTypes', adapter=_ADAPTER_GetRUZDocumentTypes)
OP_GetRUZDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/RUZDocumentTypes')

_ADAPTER_GetWNTDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetWNTDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/WNTDocumentTypes', adapter=_ADAPTER_GetWNTDocumentTypes)
OP_GetWNTDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/WNTDocumentTypes')

_ADAPTER_GetZRZDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetZRZDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/ZRZDocumentTypes', adapter=_ADAPTER_GetZRZDocumentTypes)
OP_GetZRZDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/ZRZDocumentTypes')

_ADAPTER_GetDMKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetDMKDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/DMKDocumentTypes', adapter=_ADAPTER_GetDMKDocumentTypes)
OP_GetDMKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/DMKDocumentTypes')

_ADAPTER_GetFMKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFMKDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/FMKDocumentTypes', adapter=_ADAPTER_GetFMKDocumentTypes)
OP_GetFMKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/FMKDocumentTypes')

_ADAPTER_GetFRKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFRKDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/FRKDocumentTypes', adapter=_ADAPTER_GetFRKDocumentTypes)
OP_GetFRKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/FRKDocumentTypes')

_ADAPTER_GetFZKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFZKDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/FZKDocumentTypes', adapter=_ADAPTER_GetFZKDocumentTypes)
OP_GetFZKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/FZKDocumentTypes')

_ADAPTER_GetFWZKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetFWZKDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/FWZKDocumentTypes', adapter=_ADAPTER_GetFWZKDocumentTypes)
OP_GetFWZKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/FWZKDocumentTypes')

_ADAPTER_GetRKZDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetRKZDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/RKZDocumentTypes', adapter=_ADAPTER_GetRKZDocumentTypes)
OP_GetRKZDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/RKZDocumentTypes')

_ADAPTER_GetZRKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetZRKDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/ZRKDocumentTypes', adapter=_ADAPTER_GetZRKDocumentTypes)
OP_GetZRKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/ZRKDocumentTypes')

_ADAPTER_GetWNKDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetWNKDocumentTypes = build_typed_operation(method='GET', path='/api/Purchases/WNKDocumentTypes', adapter=_ADAPTER_GetWNKDocumentTypes)
OP_GetWNKDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Purchases/WNKDocumentTypes')

_ADAPTER_GetDocumentSeries = TypeAdapter(List[DocumentSeries])
OP_GetDocumentSeries = build_typed_operation(method='GET', path='/api/Purchases/DocumentSeries', adapter=_ADAPTER_GetDocumentSeries)
OP_GetDocumentSeries_RAW = build_raw_operation(method='GET', path='/api/Purchases/DocumentSeries')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/Purchases/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/Purchases/Page')

_ADAPTER_GetPDFByDocumentIdSettings = TypeAdapter(PDF)
OP_GetPDFByDocumentIdSettings = build_typed_operation(method='PATCH', path='/api/Purchases/PDF', adapter=_ADAPTER_GetPDFByDocumentIdSettings)
OP_GetPDFByDocumentIdSettings_RAW = build_raw_operation(method='PATCH', path='/api/Purchases/PDF')

_ADAPTER_GetPDFByBufferDocumentNumberSettings = TypeAdapter(PDF)
OP_GetPDFByBufferDocumentNumberSettings = build_typed_operation(method='PATCH', path='/api/Purchases/PDF', adapter=_ADAPTER_GetPDFByBufferDocumentNumberSettings)
OP_GetPDFByBufferDocumentNumberSettings_RAW = build_raw_operation(method='PATCH', path='/api/Purchases/PDF')

_ADAPTER_GetDocumentTypesWithRange = TypeAdapter(List[PurchaseDocumentListElement])
OP_GetDocumentTypesWithRange = build_typed_operation(method='GET', path='/api/Purchases/Filter/ByDocumentTypes', adapter=_ADAPTER_GetDocumentTypesWithRange)
OP_GetDocumentTypesWithRange_RAW = build_raw_operation(method='GET', path='/api/Purchases/Filter/ByDocumentTypes')
