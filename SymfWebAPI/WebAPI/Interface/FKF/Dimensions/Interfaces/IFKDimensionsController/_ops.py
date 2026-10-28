from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Dimension
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import DimensionClassification
from SymfWebAPI.WebAPI.Interface.FKF.Dimensions.ViewModels import Document

_ADAPTER_GetAccountChartByIdAndYear = TypeAdapter(List[Dimension])
OP_GetAccountChartByIdAndYear = build_typed_operation(method='GET', path='/api/FKDimensions/AccountChart', adapter=_ADAPTER_GetAccountChartByIdAndYear)
OP_GetAccountChartByIdAndYear_RAW = build_raw_operation(method='GET', path='/api/FKDimensions/AccountChart')

_ADAPTER_GetDocumentByIdAndYear = TypeAdapter(Document)
OP_GetDocumentByIdAndYear = build_typed_operation(method='GET', path='/api/FKDimensions/Document', adapter=_ADAPTER_GetDocumentByIdAndYear)
OP_GetDocumentByIdAndYear_RAW = build_raw_operation(method='GET', path='/api/FKDimensions/Document')

_ADAPTER_GetClassification = TypeAdapter(List[DimensionClassification])
OP_GetClassification = build_typed_operation(method='GET', path='/api/FKDimensions/Classification', adapter=_ADAPTER_GetClassification)
OP_GetClassification_RAW = build_raw_operation(method='GET', path='/api/FKDimensions/Classification')
