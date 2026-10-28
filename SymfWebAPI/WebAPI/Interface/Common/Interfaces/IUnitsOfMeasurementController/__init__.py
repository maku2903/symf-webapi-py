from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import UnitOfMeasurement
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import UnitOfMeasurementDefinition
from ._common import (
    _prepare_Get,
    _prepare_GetDefinition,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetDefinition,
    OP_GetDefinition_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[UnitOfMeasurement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[UnitOfMeasurement]]: ...
def Get(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get()
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetDefinition(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[UnitOfMeasurementDefinition]]: ...
@overload
def GetDefinition(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[UnitOfMeasurementDefinition]]: ...
def GetDefinition(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDefinition()
    return invoke_operation(api, OP_GetDefinition if validate else OP_GetDefinition_RAW, params=params, data=data)

__all__ = ["Get", "GetDefinition"]
