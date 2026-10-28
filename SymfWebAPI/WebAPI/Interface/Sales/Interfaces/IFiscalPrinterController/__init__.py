from __future__ import annotations

from typing import Any, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import FiscalPrinterStatus
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import FiscalizationResult
from ._common import (
    _prepare_GetStatus,
    _prepare_Fiscalize,
)
from ._ops import (
    OP_GetStatus,
    OP_GetStatus_RAW,
    OP_Fiscalize,
    OP_Fiscalize_RAW,
)

_UNSET = object()

@overload
def GetStatus(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[FiscalPrinterStatus]: ...
@overload
def GetStatus(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[FiscalPrinterStatus]: ...
def GetStatus(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetStatus()
    return invoke_operation(api, OP_GetStatus if validate else OP_GetStatus_RAW, params=params, data=data)

@overload
def Fiscalize(api: SyncInvokerProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[FiscalizationResult]: ...
@overload
def Fiscalize(api: SyncRequestProtocol, documentId: int, *, validate: bool = True) -> ResponseEnvelope[FiscalizationResult]: ...
def Fiscalize(api: object, documentId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Fiscalize(documentId=documentId)
    return invoke_operation(api, OP_Fiscalize if validate else OP_Fiscalize_RAW, params=params, data=data)

__all__ = ["GetStatus", "Fiscalize"]
