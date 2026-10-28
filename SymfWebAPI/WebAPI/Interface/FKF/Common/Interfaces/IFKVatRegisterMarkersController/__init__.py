from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import VatRegisterMarker
from ._common import (
    _prepare_Get,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[VatRegisterMarker]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[VatRegisterMarker]]: ...
def Get(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get()
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

__all__ = ["Get"]
