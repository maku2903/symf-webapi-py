from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import BalanceAndTurnoverFilterOptions
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import BalanceAndTurnoverListElement
from ._common import (
    _prepare_BalanceAndTurnoverAsync,
)
from ._ops import (
    OP_BalanceAndTurnoverAsync,
    OP_BalanceAndTurnoverAsync_RAW,
)

_UNSET = object()

@overload
def BalanceAndTurnoverAsync(api: SyncInvokerProtocol, options: "BalanceAndTurnoverFilterOptions", *, validate: bool = True) -> ResponseEnvelope[List[BalanceAndTurnoverListElement]]: ...
@overload
def BalanceAndTurnoverAsync(api: SyncRequestProtocol, options: "BalanceAndTurnoverFilterOptions", *, validate: bool = True) -> ResponseEnvelope[List[BalanceAndTurnoverListElement]]: ...
def BalanceAndTurnoverAsync(api: object, options: "BalanceAndTurnoverFilterOptions", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_BalanceAndTurnoverAsync(options=options)
    return invoke_operation(api, OP_BalanceAndTurnoverAsync if validate else OP_BalanceAndTurnoverAsync_RAW, params=params, data=data)

__all__ = ["BalanceAndTurnoverAsync"]
