from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification

_ADAPTER_Get = TypeAdapter(List[Dimension])
OP_Get = build_typed_operation(method='GET', path='/api/ContractorDimensions', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/ContractorDimensions')

_ADAPTER_GetByContractorCode = TypeAdapter(List[Dimension])
OP_GetByContractorCode = build_typed_operation(method='GET', path='/api/ContractorDimensions', adapter=_ADAPTER_GetByContractorCode)
OP_GetByContractorCode_RAW = build_raw_operation(method='GET', path='/api/ContractorDimensions')

OP_Update = build_none_operation(method='PUT', path='/api/ContractorDimensions/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/ContractorDimensions/Update')

OP_UpdateByContractorCodeContractorDimension = build_none_operation(method='PUT', path='/api/ContractorDimensions/Update')
OP_UpdateByContractorCodeContractorDimension_RAW = build_raw_operation(method='PUT', path='/api/ContractorDimensions/Update')

OP_UpdateByContractorDimensionsContractorId = build_none_operation(method='PUT', path='/api/ContractorDimensions/UpdateList')
OP_UpdateByContractorDimensionsContractorId_RAW = build_raw_operation(method='PUT', path='/api/ContractorDimensions/UpdateList')

OP_UpdateByContractorCodeContractorDimensions = build_none_operation(method='PUT', path='/api/ContractorDimensions/UpdateList')
OP_UpdateByContractorCodeContractorDimensions_RAW = build_raw_operation(method='PUT', path='/api/ContractorDimensions/UpdateList')

_ADAPTER_GetClassification = TypeAdapter(List[DimensionClassification])
OP_GetClassification = build_typed_operation(method='GET', path='/api/ContractorDimensions/Classification', adapter=_ADAPTER_GetClassification)
OP_GetClassification_RAW = build_raw_operation(method='GET', path='/api/ContractorDimensions/Classification')
