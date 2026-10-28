from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension

_ADAPTER_Get = TypeAdapter(List[Dimension])
OP_Get = build_typed_operation(method='GET', path='/api/v2/ProductDimensions', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/v2/ProductDimensions')

_ADAPTER_GetByProductCode = TypeAdapter(List[Dimension])
OP_GetByProductCode = build_typed_operation(method='GET', path='/api/v2/ProductDimensions', adapter=_ADAPTER_GetByProductCode)
OP_GetByProductCode_RAW = build_raw_operation(method='GET', path='/api/v2/ProductDimensions')
