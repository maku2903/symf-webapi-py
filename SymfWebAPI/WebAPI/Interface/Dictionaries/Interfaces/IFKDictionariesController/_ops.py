from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import BusinessDictionary
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import BusinessDictionaryElement
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import ContractorPosition
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import Dictionary
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import DictionaryElement
from SymfWebAPI.WebAPI.Interface.Dictionaries.ViewModels import DictionaryListElement

_ADAPTER_Get = TypeAdapter(List[DictionaryListElement])
OP_Get = build_typed_operation(method='GET', path='/api/FKDictionaries', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/FKDictionaries')

_ADAPTER_GetById = TypeAdapter(Dictionary)
OP_GetById = build_typed_operation(method='GET', path='/api/FKDictionaries', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/FKDictionaries')

OP_AddNew = build_none_operation(method='POST', path='/api/FKDictionaries/Create')
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/FKDictionaries/Create')

OP_Update = build_none_operation(method='PUT', path='/api/FKDictionaries/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/FKDictionaries/Update')

OP_SetElementPosition = build_none_operation(method='PATCH', path='/api/FKDictionaries/SetElementPosition')
OP_SetElementPosition_RAW = build_raw_operation(method='PATCH', path='/api/FKDictionaries/SetElementPosition')

OP_SetElementPositionByIdPosition = build_none_operation(method='PATCH', path='/api/FKDictionaries/SetElementPosition')
OP_SetElementPositionByIdPosition_RAW = build_raw_operation(method='PATCH', path='/api/FKDictionaries/SetElementPosition')

_ADAPTER_SetContractorPosition = TypeAdapter(ContractorPosition)
OP_SetContractorPosition = build_typed_operation(method='PATCH', path='/api/FKDictionaries/SetContractorPosition', adapter=_ADAPTER_SetContractorPosition)
OP_SetContractorPosition_RAW = build_raw_operation(method='PATCH', path='/api/FKDictionaries/SetContractorPosition')

_ADAPTER_SetContractorPositionByIdPosition = TypeAdapter(ContractorPosition)
OP_SetContractorPositionByIdPosition = build_typed_operation(method='PATCH', path='/api/FKDictionaries/SetContractorPosition', adapter=_ADAPTER_SetContractorPositionByIdPosition)
OP_SetContractorPositionByIdPosition_RAW = build_raw_operation(method='PATCH', path='/api/FKDictionaries/SetContractorPosition')

_ADAPTER_GetBusiness = TypeAdapter(BusinessDictionary)
OP_GetBusiness = build_typed_operation(method='GET', path='/api/FKDictionaries/Business', adapter=_ADAPTER_GetBusiness)
OP_GetBusiness_RAW = build_raw_operation(method='GET', path='/api/FKDictionaries/Business')

OP_AddNewBusiness = build_none_operation(method='POST', path='/api/FKDictionaries/CreateBusiness')
OP_AddNewBusiness_RAW = build_raw_operation(method='POST', path='/api/FKDictionaries/CreateBusiness')

OP_UpdateBusiness = build_none_operation(method='PUT', path='/api/FKDictionaries/UpdateBusiness')
OP_UpdateBusiness_RAW = build_raw_operation(method='PUT', path='/api/FKDictionaries/UpdateBusiness')
