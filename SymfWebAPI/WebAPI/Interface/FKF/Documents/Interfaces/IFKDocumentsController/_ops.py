from __future__ import annotations

from typing import Any, List, Optional
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import Document
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import DocumentListElement
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import DocumentType
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import DocumentV2
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import Feature
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Marker
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Transactions import TransactionDocument
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

_ADAPTER_Get = TypeAdapter(List[DocumentListElement])
OP_Get = build_typed_operation(method='GET', path='/api/FKDocuments', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/FKDocuments')

_ADAPTER_GetByIdYearId = TypeAdapter(Document)
OP_GetByIdYearId = build_typed_operation(method='GET', path='/api/FKDocuments', adapter=_ADAPTER_GetByIdYearId)
OP_GetByIdYearId_RAW = build_raw_operation(method='GET', path='/api/FKDocuments')

_ADAPTER_GetV2 = TypeAdapter(DocumentV2)
OP_GetV2 = build_typed_operation(method='GET', path='/api/FKDocuments', adapter=_ADAPTER_GetV2)
OP_GetV2_RAW = build_raw_operation(method='GET', path='/api/FKDocuments')

_ADAPTER_GetFromBuffer = TypeAdapter(List[DocumentListElement])
OP_GetFromBuffer = build_typed_operation(method='GET', path='/api/FKDocuments/Buffer', adapter=_ADAPTER_GetFromBuffer)
OP_GetFromBuffer_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/Buffer')

_ADAPTER_GetFromAccountingBooks = TypeAdapter(List[DocumentListElement])
OP_GetFromAccountingBooks = build_typed_operation(method='GET', path='/api/FKDocuments/AccountingBooks', adapter=_ADAPTER_GetFromAccountingBooks)
OP_GetFromAccountingBooks_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/AccountingBooks')

_ADAPTER_GetFromSchemes = TypeAdapter(List[DocumentListElement])
OP_GetFromSchemes = build_typed_operation(method='GET', path='/api/FKDocuments/Schemes', adapter=_ADAPTER_GetFromSchemes)
OP_GetFromSchemes_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/Schemes')

_ADAPTER_GetFromBufferByContractorPositionDateFromDateToYearId = TypeAdapter(List[DocumentListElement])
OP_GetFromBufferByContractorPositionDateFromDateToYearId = build_typed_operation(method='GET', path='/api/FKDocuments/Buffer', adapter=_ADAPTER_GetFromBufferByContractorPositionDateFromDateToYearId)
OP_GetFromBufferByContractorPositionDateFromDateToYearId_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/Buffer')

_ADAPTER_GetFromAccountingBooksByContractorPositionDateFromDateToYearId = TypeAdapter(List[DocumentListElement])
OP_GetFromAccountingBooksByContractorPositionDateFromDateToYearId = build_typed_operation(method='GET', path='/api/FKDocuments/Buffer', adapter=_ADAPTER_GetFromAccountingBooksByContractorPositionDateFromDateToYearId)
OP_GetFromAccountingBooksByContractorPositionDateFromDateToYearId_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/Buffer')

_ADAPTER_GetFromSchemesByContractorPositionDateFromDateToYearId = TypeAdapter(List[DocumentListElement])
OP_GetFromSchemesByContractorPositionDateFromDateToYearId = build_typed_operation(method='GET', path='/api/FKDocuments/Buffer', adapter=_ADAPTER_GetFromSchemesByContractorPositionDateFromDateToYearId)
OP_GetFromSchemesByContractorPositionDateFromDateToYearId_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/Buffer')

_ADAPTER_GetDocumentFeatures = TypeAdapter(List[Feature])
OP_GetDocumentFeatures = build_typed_operation(method='GET', path='/api/FKDocuments/DocumentFeatures', adapter=_ADAPTER_GetDocumentFeatures)
OP_GetDocumentFeatures_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/DocumentFeatures')

_ADAPTER_GetDocumentFeaturesByYearId = TypeAdapter(List[Feature])
OP_GetDocumentFeaturesByYearId = build_typed_operation(method='GET', path='/api/FKDocuments/DocumentFeatures', adapter=_ADAPTER_GetDocumentFeaturesByYearId)
OP_GetDocumentFeaturesByYearId_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/DocumentFeatures')

_ADAPTER_GetDocumentRecordFeatures = TypeAdapter(List[Feature])
OP_GetDocumentRecordFeatures = build_typed_operation(method='GET', path='/api/FKDocuments/DocumentRecordFeatures', adapter=_ADAPTER_GetDocumentRecordFeatures)
OP_GetDocumentRecordFeatures_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/DocumentRecordFeatures')

_ADAPTER_GetDocumentRecordFeaturesByYearId = TypeAdapter(List[Feature])
OP_GetDocumentRecordFeaturesByYearId = build_typed_operation(method='GET', path='/api/FKDocuments/DocumentRecordFeatures', adapter=_ADAPTER_GetDocumentRecordFeaturesByYearId)
OP_GetDocumentRecordFeaturesByYearId_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/DocumentRecordFeatures')

_ADAPTER_GetDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetDocumentTypes = build_typed_operation(method='GET', path='/api/FKDocuments/DocumentTypes', adapter=_ADAPTER_GetDocumentTypes)
OP_GetDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/DocumentTypes')

_ADAPTER_GetDocumentTypesByYearId = TypeAdapter(List[DocumentType])
OP_GetDocumentTypesByYearId = build_typed_operation(method='GET', path='/api/FKDocuments/DocumentTypes', adapter=_ADAPTER_GetDocumentTypesByYearId)
OP_GetDocumentTypesByYearId_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/DocumentTypes')

_ADAPTER_GetMarkers = TypeAdapter(List[Marker])
OP_GetMarkers = build_typed_operation(method='GET', path='/api/FKDocuments/Markers', adapter=_ADAPTER_GetMarkers)
OP_GetMarkers_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/Markers')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/FKDocuments/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/Page')

_ADAPTER_GetDocumentTransactions = TypeAdapter(List[TransactionDocument])
OP_GetDocumentTransactions = build_typed_operation(method='GET', path='/api/FKDocuments/Transactions', adapter=_ADAPTER_GetDocumentTransactions)
OP_GetDocumentTransactions_RAW = build_raw_operation(method='GET', path='/api/FKDocuments/Transactions')
