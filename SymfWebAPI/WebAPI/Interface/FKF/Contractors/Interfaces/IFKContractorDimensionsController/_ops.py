from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import DimensionClassification

_ADAPTER_GetById = TypeAdapter(List[Dimension])
OP_GetById = build_typed_operation(method='GET', path='/api/FKContractorDimensions', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/FKContractorDimensions')

_ADAPTER_GetByPosition = TypeAdapter(List[Dimension])
OP_GetByPosition = build_typed_operation(method='GET', path='/api/FKContractorDimensions', adapter=_ADAPTER_GetByPosition)
OP_GetByPosition_RAW = build_raw_operation(method='GET', path='/api/FKContractorDimensions')

_ADAPTER_GetByCode = TypeAdapter(List[Dimension])
OP_GetByCode = build_typed_operation(method='GET', path='/api/FKContractorDimensions', adapter=_ADAPTER_GetByCode)
OP_GetByCode_RAW = build_raw_operation(method='GET', path='/api/FKContractorDimensions')

OP_UpdateById = build_none_operation(method='PUT', path='/api/FKContractorDimensions/Update')
OP_UpdateById_RAW = build_raw_operation(method='PUT', path='/api/FKContractorDimensions/Update')

OP_UpdateByPosition = build_none_operation(method='PUT', path='/api/FKContractorDimensions/Update')
OP_UpdateByPosition_RAW = build_raw_operation(method='PUT', path='/api/FKContractorDimensions/Update')

OP_UpdateByCode = build_none_operation(method='PUT', path='/api/FKContractorDimensions/Update')
OP_UpdateByCode_RAW = build_raw_operation(method='PUT', path='/api/FKContractorDimensions/Update')

OP_UpdateByIdByContractorDimensionsContractorId = build_none_operation(method='PUT', path='/api/FKContractorDimensions/UpdateList')
OP_UpdateByIdByContractorDimensionsContractorId_RAW = build_raw_operation(method='PUT', path='/api/FKContractorDimensions/UpdateList')

OP_UpdateByPositionByContractorDimensionsContractorPosition = build_none_operation(method='PUT', path='/api/FKContractorDimensions/UpdateList')
OP_UpdateByPositionByContractorDimensionsContractorPosition_RAW = build_raw_operation(method='PUT', path='/api/FKContractorDimensions/UpdateList')

OP_UpdateByCodeByContractorCodeContractorDimensions = build_none_operation(method='PUT', path='/api/FKContractorDimensions/UpdateList')
OP_UpdateByCodeByContractorCodeContractorDimensions_RAW = build_raw_operation(method='PUT', path='/api/FKContractorDimensions/UpdateList')

_ADAPTER_GetClassification = TypeAdapter(List[DimensionClassification])
OP_GetClassification = build_typed_operation(method='GET', path='/api/FKContractorDimensions/Classification', adapter=_ADAPTER_GetClassification)
OP_GetClassification_RAW = build_raw_operation(method='GET', path='/api/FKContractorDimensions/Classification')
