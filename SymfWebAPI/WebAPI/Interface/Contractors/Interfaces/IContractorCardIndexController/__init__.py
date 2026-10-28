from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from ._common import (
    _prepare_GetByIdAsync,
    _prepare_GetByCodeAsync,
    _prepare_GetByNIPAsync,
)
from ._ops import (
    OP_GetByIdAsync,
    OP_GetByIdAsync_RAW,
    OP_GetByCodeAsync,
    OP_GetByCodeAsync_RAW,
    OP_GetByNIPAsync,
    OP_GetByNIPAsync_RAW,
)

_UNSET = object()

@overload
def GetByIdAsync(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetByIdAsync(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def GetByIdAsync(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByIdAsync(id=id)
    return invoke_operation(api, OP_GetByIdAsync if validate else OP_GetByIdAsync_RAW, params=params, data=data)

@overload
def GetByCodeAsync(api: SyncInvokerProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetByCodeAsync(api: SyncRequestProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def GetByCodeAsync(api: object, code: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByCodeAsync(code=code)
    return invoke_operation(api, OP_GetByCodeAsync if validate else OP_GetByCodeAsync_RAW, params=params, data=data)

@overload
def GetByNIPAsync(api: SyncInvokerProtocol, nip: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def GetByNIPAsync(api: SyncRequestProtocol, nip: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def GetByNIPAsync(api: object, nip: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByNIPAsync(nip=nip)
    return invoke_operation(api, OP_GetByNIPAsync if validate else OP_GetByNIPAsync_RAW, params=params, data=data)

__all__ = ["GetByIdAsync", "GetByCodeAsync", "GetByNIPAsync"]
