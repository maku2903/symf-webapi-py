from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PositionDimension

_ADAPTER_Get = TypeAdapter(List[Dimension])
OP_Get = build_typed_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions')

_ADAPTER_GetByBufferDocumentNumber = TypeAdapter(List[Dimension])
OP_GetByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions', adapter=_ADAPTER_GetByBufferDocumentNumber)
OP_GetByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions')

_ADAPTER_GetPositionsByOrderId = TypeAdapter(List[PositionDimension])
OP_GetPositionsByOrderId = build_typed_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions/Positions', adapter=_ADAPTER_GetPositionsByOrderId)
OP_GetPositionsByOrderId_RAW = build_raw_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions/Positions')

_ADAPTER_GetPositionsByOrderNumber = TypeAdapter(List[PositionDimension])
OP_GetPositionsByOrderNumber = build_typed_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions/Positions', adapter=_ADAPTER_GetPositionsByOrderNumber)
OP_GetPositionsByOrderNumber_RAW = build_raw_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions/Positions')

_ADAPTER_GetPosition = TypeAdapter(List[Dimension])
OP_GetPosition = build_typed_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions/Positions', adapter=_ADAPTER_GetPosition)
OP_GetPosition_RAW = build_raw_operation(method='GET', path='/api/v2/WarehouseDocumentDimensions/Positions')
