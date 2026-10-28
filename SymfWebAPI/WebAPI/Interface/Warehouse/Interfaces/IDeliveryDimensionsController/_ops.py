from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DimensionClassification

_ADAPTER_Get = TypeAdapter(List[Dimension])
OP_Get = build_typed_operation(method='GET', path='/api/DeliveryDimensions', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/DeliveryDimensions')

_ADAPTER_GetClassification = TypeAdapter(List[DimensionClassification])
OP_GetClassification = build_typed_operation(method='GET', path='/api/DeliveryDimensions/Classification', adapter=_ADAPTER_GetClassification)
OP_GetClassification_RAW = build_raw_operation(method='GET', path='/api/DeliveryDimensions/Classification')

OP_Update = build_none_operation(method='PUT', path='/api/DeliveryDimensions/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/DeliveryDimensions/Update')

OP_UpdateByDeliveryDimensionsDeliveryId = build_none_operation(method='PUT', path='/api/DeliveryDimensions/UpdateList')
OP_UpdateByDeliveryDimensionsDeliveryId_RAW = build_raw_operation(method='PUT', path='/api/DeliveryDimensions/UpdateList')
