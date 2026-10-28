from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import UnitOfMeasurement
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import UnitOfMeasurementDefinition

_ADAPTER_Get = TypeAdapter(List[UnitOfMeasurement])
OP_Get = build_typed_operation(method='GET', path='/api/UnitsOfMeasurement', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/UnitsOfMeasurement')

_ADAPTER_GetDefinition = TypeAdapter(List[UnitOfMeasurementDefinition])
OP_GetDefinition = build_typed_operation(method='GET', path='/api/UnitsOfMeasurement/Definition', adapter=_ADAPTER_GetDefinition)
OP_GetDefinition_RAW = build_raw_operation(method='GET', path='/api/UnitsOfMeasurement/Definition')
