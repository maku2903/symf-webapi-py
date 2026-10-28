from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PriceType
from ._common import (
    _prepare_GetSalePriceTypes,
)
from ._ops import (
    OP_GetSalePriceTypes,
    OP_GetSalePriceTypes_RAW,
)

_UNSET = object()

@overload
def GetSalePriceTypes(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PriceType]]: ...
@overload
def GetSalePriceTypes(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PriceType]]: ...
def GetSalePriceTypes(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetSalePriceTypes()
    return invoke_operation(api, OP_GetSalePriceTypes if validate else OP_GetSalePriceTypes_RAW, params=params, data=data)

__all__ = ["GetSalePriceTypes"]
