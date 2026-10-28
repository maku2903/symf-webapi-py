from __future__ import annotations

import warnings

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.errors import SessionManagementBypassWarning
from SymfWebAPI.WebAPI.Interface.ViewModels import SessionInformation
from ._common import (
    _prepare_CloseSession,
    _prepare_OpenNewSession,
    _prepare_SessionInformationAsync,
)
from ._ops import (
    OP_CloseSession,
    OP_CloseSession_RAW,
    OP_OpenNewSession,
    OP_OpenNewSession_RAW,
    OP_SessionInformationAsync,
    OP_SessionInformationAsync_RAW,
)

_UNSET = object()

@overload
def CloseSession(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def CloseSession(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def CloseSession(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    warnings.warn(
        "Manual call to session endpoint bypasses SessionManager; " "prefer api.open()/api.close() unless you intentionally manage sessions manually.",
        SessionManagementBypassWarning,
        stacklevel=2,
    )
    params, data = _prepare_CloseSession()
    return invoke_operation(api, OP_CloseSession if validate else OP_CloseSession_RAW, params=params, data=data)

@overload
def OpenNewSession(api: SyncInvokerProtocol, deviceName: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def OpenNewSession(api: SyncRequestProtocol, deviceName: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def OpenNewSession(api: object, deviceName: str, *, validate: bool = True) -> ResponseEnvelope[Any]:
    warnings.warn(
        "Manual call to session endpoint bypasses SessionManager; " "prefer api.open()/api.close() unless you intentionally manage sessions manually.",
        SessionManagementBypassWarning,
        stacklevel=2,
    )
    params, data = _prepare_OpenNewSession(deviceName=deviceName)
    return invoke_operation(api, OP_OpenNewSession if validate else OP_OpenNewSession_RAW, params=params, data=data)

@overload
def SessionInformationAsync(api: SyncInvokerProtocol, cancellationToken: Any, *, validate: bool = True) -> ResponseEnvelope[SessionInformation]: ...
@overload
def SessionInformationAsync(api: SyncRequestProtocol, cancellationToken: Any, *, validate: bool = True) -> ResponseEnvelope[SessionInformation]: ...
def SessionInformationAsync(api: object, cancellationToken: Any, *, validate: bool = True) -> ResponseEnvelope[Any]:
    warnings.warn(
        "Manual call to session endpoint bypasses SessionManager; " "prefer api.open()/api.close() unless you intentionally manage sessions manually.",
        SessionManagementBypassWarning,
        stacklevel=2,
    )
    params, data = _prepare_SessionInformationAsync(cancellationToken=cancellationToken)
    return invoke_operation(api, OP_SessionInformationAsync if validate else OP_SessionInformationAsync_RAW, params=params, data=data)

__all__ = ["CloseSession", "OpenNewSession", "SessionInformationAsync"]
