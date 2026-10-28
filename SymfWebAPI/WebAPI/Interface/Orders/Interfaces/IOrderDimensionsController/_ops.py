from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels.Aspects import AspectDocument
from SymfWebAPI.WebAPI.Interface.Common.ViewModels.Aspects import AspectPositionEdit
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PositionDimension

_ADAPTER_Get = TypeAdapter(List[Dimension])
OP_Get = build_typed_operation(method='GET', path='/api/OrderDimensions', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/OrderDimensions')

_ADAPTER_GetByBufferOrderNumber = TypeAdapter(List[Dimension])
OP_GetByBufferOrderNumber = build_typed_operation(method='GET', path='/api/OrderDimensions', adapter=_ADAPTER_GetByBufferOrderNumber)
OP_GetByBufferOrderNumber_RAW = build_raw_operation(method='GET', path='/api/OrderDimensions')

_ADAPTER_GetPositionsByOrderId = TypeAdapter(List[PositionDimension])
OP_GetPositionsByOrderId = build_typed_operation(method='GET', path='/api/OrderDimensions/Positions', adapter=_ADAPTER_GetPositionsByOrderId)
OP_GetPositionsByOrderId_RAW = build_raw_operation(method='GET', path='/api/OrderDimensions/Positions')

_ADAPTER_GetPositionsByOrderNumber = TypeAdapter(List[PositionDimension])
OP_GetPositionsByOrderNumber = build_typed_operation(method='GET', path='/api/OrderDimensions/Positions', adapter=_ADAPTER_GetPositionsByOrderNumber)
OP_GetPositionsByOrderNumber_RAW = build_raw_operation(method='GET', path='/api/OrderDimensions/Positions')

_ADAPTER_GetPosition = TypeAdapter(List[Dimension])
OP_GetPosition = build_typed_operation(method='GET', path='/api/OrderDimensions/Positions', adapter=_ADAPTER_GetPosition)
OP_GetPosition_RAW = build_raw_operation(method='GET', path='/api/OrderDimensions/Positions')

_ADAPTER_GetClassification = TypeAdapter(List[DimensionClassification])
OP_GetClassification = build_typed_operation(method='GET', path='/api/OrderDimensions/Classification', adapter=_ADAPTER_GetClassification)
OP_GetClassification_RAW = build_raw_operation(method='GET', path='/api/OrderDimensions/Classification')

_ADAPTER_GetPositionClassification = TypeAdapter(List[DimensionClassification])
OP_GetPositionClassification = build_typed_operation(method='GET', path='/api/OrderDimensions/PositionClassification', adapter=_ADAPTER_GetPositionClassification)
OP_GetPositionClassification_RAW = build_raw_operation(method='GET', path='/api/OrderDimensions/PositionClassification')

OP_Update = build_none_operation(method='PUT', path='/api/OrderDimensions/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/OrderDimensions/Update')

OP_UpdateByBufferOrderDimensionOrderNumber = build_none_operation(method='PUT', path='/api/OrderDimensions/Update')
OP_UpdateByBufferOrderDimensionOrderNumber_RAW = build_raw_operation(method='PUT', path='/api/OrderDimensions/Update')

OP_UpdateByOrderDimensionsOrderId = build_none_operation(method='PUT', path='/api/OrderDimensions/UpdateList')
OP_UpdateByOrderDimensionsOrderId_RAW = build_raw_operation(method='PUT', path='/api/OrderDimensions/UpdateList')

OP_UpdateByBufferOrderDimensionsOrderNumber = build_none_operation(method='PUT', path='/api/OrderDimensions/UpdateList')
OP_UpdateByBufferOrderDimensionsOrderNumber_RAW = build_raw_operation(method='PUT', path='/api/OrderDimensions/UpdateList')

OP_UpdatePosition = build_none_operation(method='PUT', path='/api/OrderDimensions/UpdatePosition')
OP_UpdatePosition_RAW = build_raw_operation(method='PUT', path='/api/OrderDimensions/UpdatePosition')

OP_UpdatePositionByPositionDimensionsPositionId = build_none_operation(method='PUT', path='/api/OrderDimensions/UpdatePositionList')
OP_UpdatePositionByPositionDimensionsPositionId_RAW = build_raw_operation(method='PUT', path='/api/OrderDimensions/UpdatePositionList')

OP_UpdatePositionByPositionDimension = build_none_operation(method='PUT', path='/api/OrderDimensions/UpdateMultiPositionsList')
OP_UpdatePositionByPositionDimension_RAW = build_raw_operation(method='PUT', path='/api/OrderDimensions/UpdateMultiPositionsList')

_ADAPTER_GetAspects = TypeAdapter(AspectDocument)
OP_GetAspects = build_typed_operation(method='GET', path='/api/OwnOrderDimensions/Aspects', adapter=_ADAPTER_GetAspects)
OP_GetAspects_RAW = build_raw_operation(method='GET', path='/api/OwnOrderDimensions/Aspects')

_ADAPTER_GetAspectsByBufferOrderNumber = TypeAdapter(AspectDocument)
OP_GetAspectsByBufferOrderNumber = build_typed_operation(method='GET', path='/api/OwnOrderDimensions/Aspects', adapter=_ADAPTER_GetAspectsByBufferOrderNumber)
OP_GetAspectsByBufferOrderNumber_RAW = build_raw_operation(method='GET', path='/api/OwnOrderDimensions/Aspects')

OP_UpdateAspect = build_none_operation(method='PUT', path='/api/OwnOrderDimensions/Aspects')
OP_UpdateAspect_RAW = build_raw_operation(method='PUT', path='/api/OwnOrderDimensions/Aspects')
