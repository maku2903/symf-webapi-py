from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Dimension

_ADAPTER_GetById = TypeAdapter(List[Dimension])
OP_GetById = build_typed_operation(method='GET', path='/api/v2/FKContractorDimensions', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/v2/FKContractorDimensions')

_ADAPTER_GetByPosition = TypeAdapter(List[Dimension])
OP_GetByPosition = build_typed_operation(method='GET', path='/api/v2/FKContractorDimensions', adapter=_ADAPTER_GetByPosition)
OP_GetByPosition_RAW = build_raw_operation(method='GET', path='/api/v2/FKContractorDimensions')

_ADAPTER_GetByCode = TypeAdapter(List[Dimension])
OP_GetByCode = build_typed_operation(method='GET', path='/api/v2/FKContractorDimensions', adapter=_ADAPTER_GetByCode)
OP_GetByCode_RAW = build_raw_operation(method='GET', path='/api/v2/FKContractorDimensions')
