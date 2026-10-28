from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from ._common import (
    _prepare_AddSendToKsefEventAsync,
    _prepare_ChangeKsefStatusAsync,
)
from ._ops import (
    OP_AddSendToKsefEventAsync,
    OP_AddSendToKsefEventAsync_RAW,
    OP_ChangeKsefStatusAsync,
    OP_ChangeKsefStatusAsync_RAW,
)

_UNSET = object()

@overload
def AddSendToKsefEventAsync(api: SyncInvokerProtocol, cancellationToken: int, docId: Any, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def AddSendToKsefEventAsync(api: SyncRequestProtocol, cancellationToken: int, docId: Any, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def AddSendToKsefEventAsync(api: object, cancellationToken: int, docId: Any, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddSendToKsefEventAsync(cancellationToken=cancellationToken, docId=docId)
    return invoke_operation(api, OP_AddSendToKsefEventAsync if validate else OP_AddSendToKsefEventAsync_RAW, params=params, data=data)

@overload
def ChangeKsefStatusAsync(api: SyncInvokerProtocol, id: int, ksefStatus: int, cancellationToken: Any, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def ChangeKsefStatusAsync(api: SyncRequestProtocol, id: int, ksefStatus: int, cancellationToken: Any, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def ChangeKsefStatusAsync(api: object, id: int, ksefStatus: int, cancellationToken: Any, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_ChangeKsefStatusAsync(id=id, ksefStatus=ksefStatus, cancellationToken=cancellationToken)
    return invoke_operation(api, OP_ChangeKsefStatusAsync if validate else OP_ChangeKsefStatusAsync_RAW, params=params, data=data)

__all__ = ["AddSendToKsefEventAsync", "ChangeKsefStatusAsync"]
