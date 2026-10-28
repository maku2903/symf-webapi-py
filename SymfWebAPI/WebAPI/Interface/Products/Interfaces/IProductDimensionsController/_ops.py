from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification

_ADAPTER_Get = TypeAdapter(List[Dimension])
OP_Get = build_typed_operation(method='GET', path='/api/ProductDimensions', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/ProductDimensions')

_ADAPTER_GetByProductCode = TypeAdapter(List[Dimension])
OP_GetByProductCode = build_typed_operation(method='GET', path='/api/ProductDimensions', adapter=_ADAPTER_GetByProductCode)
OP_GetByProductCode_RAW = build_raw_operation(method='GET', path='/api/ProductDimensions')

OP_Update = build_none_operation(method='PUT', path='/api/ProductDimensions/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/ProductDimensions/Update')

OP_UpdateByProductCodeProductDimension = build_none_operation(method='PUT', path='/api/ProductDimensions/Update')
OP_UpdateByProductCodeProductDimension_RAW = build_raw_operation(method='PUT', path='/api/ProductDimensions/Update')

OP_UpdateByProductDimensionsProductId = build_none_operation(method='PUT', path='/api/ProductDimensions/UpdateList')
OP_UpdateByProductDimensionsProductId_RAW = build_raw_operation(method='PUT', path='/api/ProductDimensions/UpdateList')

OP_UpdateByProductCodeProductDimensions = build_none_operation(method='PUT', path='/api/ProductDimensions/UpdateList')
OP_UpdateByProductCodeProductDimensions_RAW = build_raw_operation(method='PUT', path='/api/ProductDimensions/UpdateList')

_ADAPTER_GetClassification = TypeAdapter(List[DimensionClassification])
OP_GetClassification = build_typed_operation(method='GET', path='/api/ProductDimensions/Classification', adapter=_ADAPTER_GetClassification)
OP_GetClassification_RAW = build_raw_operation(method='GET', path='/api/ProductDimensions/Classification')
