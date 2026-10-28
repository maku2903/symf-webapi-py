from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.RepX.ViewModels import PrintData
from SymfWebAPI.WebAPI.Interface.RepX.ViewModels import ReportDefinition
from ._common import (
    _prepare_Get,
    _prepare_GetDefinitions,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetDefinitions,
    OP_GetDefinitions_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, reportId: int, objectId: int, data: "PrintData", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
@overload
def Get(api: SyncRequestProtocol, reportId: int, objectId: int, data: "PrintData", *, validate: bool = True) -> ResponseEnvelope[PDF]: ...
def Get(api: object, reportId: int, objectId: int, data: "PrintData", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get(validate=validate, reportId=reportId, objectId=objectId, data=data)
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetDefinitions(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ReportDefinition]]: ...
@overload
def GetDefinitions(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ReportDefinition]]: ...
def GetDefinitions(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDefinitions()
    return invoke_operation(api, OP_GetDefinitions if validate else OP_GetDefinitions_RAW, params=params, data=data)

__all__ = ["Get", "GetDefinitions"]
