from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PositionDimension

_ADAPTER_Get = TypeAdapter(List[Dimension])
OP_Get = build_typed_operation(method='GET', path='/api/v2/SalesDimensions', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/v2/SalesDimensions')

_ADAPTER_GetByBufferDocumentNumber = TypeAdapter(List[Dimension])
OP_GetByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/v2/SalesDimensions', adapter=_ADAPTER_GetByBufferDocumentNumber)
OP_GetByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/v2/SalesDimensions')

_ADAPTER_GetPositionsByDocumentId = TypeAdapter(List[PositionDimension])
OP_GetPositionsByDocumentId = build_typed_operation(method='GET', path='/api/v2/SalesDimensions/Positions', adapter=_ADAPTER_GetPositionsByDocumentId)
OP_GetPositionsByDocumentId_RAW = build_raw_operation(method='GET', path='/api/v2/SalesDimensions/Positions')

_ADAPTER_GetPositionsByDocumentNumber = TypeAdapter(List[PositionDimension])
OP_GetPositionsByDocumentNumber = build_typed_operation(method='GET', path='/api/v2/SalesDimensions/Positions', adapter=_ADAPTER_GetPositionsByDocumentNumber)
OP_GetPositionsByDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/v2/SalesDimensions/Positions')

_ADAPTER_GetPosition = TypeAdapter(List[Dimension])
OP_GetPosition = build_typed_operation(method='GET', path='/api/v2/SalesDimensions/Positions', adapter=_ADAPTER_GetPosition)
OP_GetPosition_RAW = build_raw_operation(method='GET', path='/api/v2/SalesDimensions/Positions')
