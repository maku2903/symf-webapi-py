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
OP_Get = build_typed_operation(method='GET', path='/api/SalesDimensions', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions')

_ADAPTER_GetByBufferDocumentNumber = TypeAdapter(List[Dimension])
OP_GetByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/SalesDimensions', adapter=_ADAPTER_GetByBufferDocumentNumber)
OP_GetByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions')

_ADAPTER_GetPositionsByDocumentId = TypeAdapter(List[PositionDimension])
OP_GetPositionsByDocumentId = build_typed_operation(method='GET', path='/api/SalesDimensions/Positions', adapter=_ADAPTER_GetPositionsByDocumentId)
OP_GetPositionsByDocumentId_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions/Positions')

_ADAPTER_GetPositionsByDocumentNumber = TypeAdapter(List[PositionDimension])
OP_GetPositionsByDocumentNumber = build_typed_operation(method='GET', path='/api/SalesDimensions/Positions', adapter=_ADAPTER_GetPositionsByDocumentNumber)
OP_GetPositionsByDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions/Positions')

_ADAPTER_GetPosition = TypeAdapter(List[Dimension])
OP_GetPosition = build_typed_operation(method='GET', path='/api/SalesDimensions/Positions', adapter=_ADAPTER_GetPosition)
OP_GetPosition_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions/Positions')

_ADAPTER_GetClassification = TypeAdapter(List[DimensionClassification])
OP_GetClassification = build_typed_operation(method='GET', path='/api/SalesDimensions/Classification', adapter=_ADAPTER_GetClassification)
OP_GetClassification_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions/Classification')

_ADAPTER_GetPositionClassification = TypeAdapter(List[DimensionClassification])
OP_GetPositionClassification = build_typed_operation(method='GET', path='/api/SalesDimensions/PositionClassification', adapter=_ADAPTER_GetPositionClassification)
OP_GetPositionClassification_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions/PositionClassification')

OP_Update = build_none_operation(method='PUT', path='/api/SalesDimensions/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/SalesDimensions/Update')

OP_UpdateByBufferDocumentDimensionDocumentNumber = build_none_operation(method='PUT', path='/api/SalesDimensions/Update')
OP_UpdateByBufferDocumentDimensionDocumentNumber_RAW = build_raw_operation(method='PUT', path='/api/SalesDimensions/Update')

OP_UpdateByDocumentDimensionsDocumentId = build_none_operation(method='PUT', path='/api/SalesDimensions/UpdateList')
OP_UpdateByDocumentDimensionsDocumentId_RAW = build_raw_operation(method='PUT', path='/api/SalesDimensions/UpdateList')

OP_UpdateByBufferDocumentDimensionsDocumentNumber = build_none_operation(method='PUT', path='/api/SalesDimensions/UpdateList')
OP_UpdateByBufferDocumentDimensionsDocumentNumber_RAW = build_raw_operation(method='PUT', path='/api/SalesDimensions/UpdateList')

OP_UpdatePosition = build_none_operation(method='PUT', path='/api/SalesDimensions/UpdatePosition')
OP_UpdatePosition_RAW = build_raw_operation(method='PUT', path='/api/SalesDimensions/UpdatePosition')

OP_UpdatePositionByPositionDimensionsPositionId = build_none_operation(method='PUT', path='/api/SalesDimensions/UpdatePositionList')
OP_UpdatePositionByPositionDimensionsPositionId_RAW = build_raw_operation(method='PUT', path='/api/SalesDimensions/UpdatePositionList')

OP_UpdatePositionByPositionDimension = build_none_operation(method='PUT', path='/api/SalesDimensions/UpdateMultiPositionsList')
OP_UpdatePositionByPositionDimension_RAW = build_raw_operation(method='PUT', path='/api/SalesDimensions/UpdateMultiPositionsList')

_ADAPTER_GetAspects = TypeAdapter(AspectDocument)
OP_GetAspects = build_typed_operation(method='GET', path='/api/SalesDimensions/Aspects', adapter=_ADAPTER_GetAspects)
OP_GetAspects_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions/Aspects')

_ADAPTER_GetAspectsByBufferDocumentNumber = TypeAdapter(AspectDocument)
OP_GetAspectsByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/SalesDimensions/Aspects', adapter=_ADAPTER_GetAspectsByBufferDocumentNumber)
OP_GetAspectsByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/SalesDimensions/Aspects')

OP_UpdateAspect = build_none_operation(method='PUT', path='/api/SalesDimensions/Aspects')
OP_UpdateAspect_RAW = build_raw_operation(method='PUT', path='/api/SalesDimensions/Aspects')
