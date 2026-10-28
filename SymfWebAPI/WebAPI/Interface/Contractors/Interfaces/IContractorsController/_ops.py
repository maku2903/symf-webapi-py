from __future__ import annotations

from typing import Any, List
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Catalog
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import Contractor
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorCriteriaFilter
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorFilterCriteria
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorListElement
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorListElementWithDimensions
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import IncrementalSyncListElement
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Kind
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Marker
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

_ADAPTER_Get = TypeAdapter(Contractor)
OP_Get = build_typed_operation(method='GET', path='/api/Contractors', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Contractors')

_ADAPTER_GetByCode = TypeAdapter(Contractor)
OP_GetByCode = build_typed_operation(method='GET', path='/api/Contractors', adapter=_ADAPTER_GetByCode)
OP_GetByCode_RAW = build_raw_operation(method='GET', path='/api/Contractors')

_ADAPTER_GetByNIP = TypeAdapter(List[Contractor])
OP_GetByNIP = build_typed_operation(method='GET', path='/api/Contractors', adapter=_ADAPTER_GetByNIP)
OP_GetByNIP_RAW = build_raw_operation(method='GET', path='/api/Contractors')

_ADAPTER_GetByPesel = TypeAdapter(List[Contractor])
OP_GetByPesel = build_typed_operation(method='GET', path='/api/Contractors', adapter=_ADAPTER_GetByPesel)
OP_GetByPesel_RAW = build_raw_operation(method='GET', path='/api/Contractors')

_ADAPTER_GetByPosition = TypeAdapter(List[Contractor])
OP_GetByPosition = build_typed_operation(method='GET', path='/api/Contractors', adapter=_ADAPTER_GetByPosition)
OP_GetByPosition_RAW = build_raw_operation(method='GET', path='/api/Contractors')

_ADAPTER_GetByNIPAndPosition = TypeAdapter(List[Contractor])
OP_GetByNIPAndPosition = build_typed_operation(method='GET', path='/api/Contractors', adapter=_ADAPTER_GetByNIPAndPosition)
OP_GetByNIPAndPosition_RAW = build_raw_operation(method='GET', path='/api/Contractors')

_ADAPTER_GetGet = TypeAdapter(List[ContractorListElement])
OP_GetGet = build_typed_operation(method='GET', path='/api/Contractors', adapter=_ADAPTER_GetGet)
OP_GetGet_RAW = build_raw_operation(method='GET', path='/api/Contractors')

_ADAPTER_GetWithDimensions = TypeAdapter(List[ContractorListElementWithDimensions])
OP_GetWithDimensions = build_typed_operation(method='GET', path='/api/Contractors/WithDimensions', adapter=_ADAPTER_GetWithDimensions)
OP_GetWithDimensions_RAW = build_raw_operation(method='GET', path='/api/Contractors/WithDimensions')

_ADAPTER_Filter = TypeAdapter(List[ContractorListElement])
OP_Filter = build_typed_operation(method='PATCH', path='/api/Contractors/Filter', adapter=_ADAPTER_Filter)
OP_Filter_RAW = build_raw_operation(method='PATCH', path='/api/Contractors/Filter')

_ADAPTER_FilterWithDimensions = TypeAdapter(List[ContractorListElementWithDimensions])
OP_FilterWithDimensions = build_typed_operation(method='PATCH', path='/api/Contractors/Filter/WithDimensions', adapter=_ADAPTER_FilterWithDimensions)
OP_FilterWithDimensions_RAW = build_raw_operation(method='PATCH', path='/api/Contractors/Filter/WithDimensions')

_ADAPTER_AddNew = TypeAdapter(Contractor)
OP_AddNew = build_typed_operation(method='POST', path='/api/Contractors/Create', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/Contractors/Create')

OP_Update = build_none_operation(method='PUT', path='/api/Contractors/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/Contractors/Update')

_ADAPTER_GetMarkers = TypeAdapter(List[Marker])
OP_GetMarkers = build_typed_operation(method='GET', path='/api/Contractors/Markers', adapter=_ADAPTER_GetMarkers)
OP_GetMarkers_RAW = build_raw_operation(method='GET', path='/api/Contractors/Markers')

_ADAPTER_GetKinds = TypeAdapter(List[Kind])
OP_GetKinds = build_typed_operation(method='GET', path='/api/Contractors/Kinds', adapter=_ADAPTER_GetKinds)
OP_GetKinds_RAW = build_raw_operation(method='GET', path='/api/Contractors/Kinds')

_ADAPTER_GetCatalogs = TypeAdapter(List[Catalog])
OP_GetCatalogs = build_typed_operation(method='GET', path='/api/Contractors/Catalogs', adapter=_ADAPTER_GetCatalogs)
OP_GetCatalogs_RAW = build_raw_operation(method='GET', path='/api/Contractors/Catalogs')

OP_SyncFK = build_none_operation(method='PATCH', path='/api/Contractors/SyncFK')
OP_SyncFK_RAW = build_raw_operation(method='PATCH', path='/api/Contractors/SyncFK')

OP_SyncFKByContractorCodeIsNew = build_none_operation(method='PATCH', path='/api/Contractors/SyncFK')
OP_SyncFKByContractorCodeIsNew_RAW = build_raw_operation(method='PATCH', path='/api/Contractors/SyncFK')

_ADAPTER_IncrementalSync = TypeAdapter(List[IncrementalSyncListElement])
OP_IncrementalSync = build_typed_operation(method='GET', path='/api/Contractors/IncrementalSync', adapter=_ADAPTER_IncrementalSync)
OP_IncrementalSync_RAW = build_raw_operation(method='GET', path='/api/Contractors/IncrementalSync')

_ADAPTER_FilterSql = TypeAdapter(List[ContractorListElement])
OP_FilterSql = build_typed_operation(method='PATCH', path='/api/Contractors/FilterSql', adapter=_ADAPTER_FilterSql)
OP_FilterSql_RAW = build_raw_operation(method='PATCH', path='/api/Contractors/FilterSql')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/Contractors/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/Contractors/Page')

_ADAPTER_GetPagedDocumentWithDimensions = TypeAdapter(Page)
OP_GetPagedDocumentWithDimensions = build_typed_operation(method='GET', path='/api/Contractors/PageWithDimensions', adapter=_ADAPTER_GetPagedDocumentWithDimensions)
OP_GetPagedDocumentWithDimensions_RAW = build_raw_operation(method='GET', path='/api/Contractors/PageWithDimensions')

_ADAPTER_FilterSqlWithDimensions = TypeAdapter(List[ContractorListElementWithDimensions])
OP_FilterSqlWithDimensions = build_typed_operation(method='PATCH', path='/api/Contractors/FilterSql/WithDimensions', adapter=_ADAPTER_FilterSqlWithDimensions)
OP_FilterSqlWithDimensions_RAW = build_raw_operation(method='PATCH', path='/api/Contractors/FilterSql/WithDimensions')
