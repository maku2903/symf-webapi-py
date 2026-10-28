from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Contractors.ViewModels import Contractor
from SymfWebAPI.WebAPI.Interface.FKF.Contractors.ViewModels import ContractorCriteriaFilter
from SymfWebAPI.WebAPI.Interface.FKF.Contractors.ViewModels import ContractorListElement
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import FilterCriteria
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

_ADAPTER_Get = TypeAdapter(List[ContractorListElement])
OP_Get = build_typed_operation(method='GET', path='/api/FKContractors', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/FKContractors')

_ADAPTER_GetById = TypeAdapter(Contractor)
OP_GetById = build_typed_operation(method='GET', path='/api/FKContractors', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/FKContractors')

_ADAPTER_GetByPosition = TypeAdapter(Contractor)
OP_GetByPosition = build_typed_operation(method='GET', path='/api/FKContractors', adapter=_ADAPTER_GetByPosition)
OP_GetByPosition_RAW = build_raw_operation(method='GET', path='/api/FKContractors')

_ADAPTER_GetByCode = TypeAdapter(Contractor)
OP_GetByCode = build_typed_operation(method='GET', path='/api/FKContractors', adapter=_ADAPTER_GetByCode)
OP_GetByCode_RAW = build_raw_operation(method='GET', path='/api/FKContractors')

_ADAPTER_GetByNIP = TypeAdapter(List[Contractor])
OP_GetByNIP = build_typed_operation(method='GET', path='/api/FKContractors', adapter=_ADAPTER_GetByNIP)
OP_GetByNIP_RAW = build_raw_operation(method='GET', path='/api/FKContractors')

_ADAPTER_GetByPesel = TypeAdapter(List[Contractor])
OP_GetByPesel = build_typed_operation(method='GET', path='/api/FKContractors', adapter=_ADAPTER_GetByPesel)
OP_GetByPesel_RAW = build_raw_operation(method='GET', path='/api/FKContractors')

_ADAPTER_Filter = TypeAdapter(List[ContractorListElement])
OP_Filter = build_typed_operation(method='PATCH', path='/api/FKContractors/Filter', adapter=_ADAPTER_Filter)
OP_Filter_RAW = build_raw_operation(method='PATCH', path='/api/FKContractors/Filter')

_ADAPTER_AddNew = TypeAdapter(Contractor)
OP_AddNew = build_typed_operation(method='POST', path='/api/FKContractors/Create', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/FKContractors/Create')

OP_Update = build_none_operation(method='PUT', path='/api/FKContractors/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/FKContractors/Update')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/FKContractors/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/FKContractors/Page')

_ADAPTER_FilterSql = TypeAdapter(List[ContractorListElement])
OP_FilterSql = build_typed_operation(method='PATCH', path='/api/FKContractors/FilterSql', adapter=_ADAPTER_FilterSql)
OP_FilterSql_RAW = build_raw_operation(method='PATCH', path='/api/FKContractors/FilterSql')
