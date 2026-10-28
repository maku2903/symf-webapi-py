from __future__ import annotations

from typing import Any, List, Literal, overload
from SymfWebAPI.client import SyncAPI
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import BalanceAndTurnoverFilterOptions
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import BalanceAndTurnoverListElement
from .json_types import BalanceAndTurnoverListElementJSON

@overload
def BalanceAndTurnoverAsync(api: SyncAPI, options: "BalanceAndTurnoverFilterOptions", *, validate: Literal[True] = True) -> ResponseEnvelope[List[BalanceAndTurnoverListElement]]: ...
@overload
def BalanceAndTurnoverAsync(api: SyncAPI, options: "BalanceAndTurnoverFilterOptions", *, validate: Literal[False]) -> ResponseEnvelope[list[BalanceAndTurnoverListElementJSON]]: ...
@overload
def BalanceAndTurnoverAsync(api: SyncInvokerProtocol, options: "BalanceAndTurnoverFilterOptions", *, validate: Literal[True] = True) -> ResponseEnvelope[List[BalanceAndTurnoverListElement]]: ...
@overload
def BalanceAndTurnoverAsync(api: SyncInvokerProtocol, options: "BalanceAndTurnoverFilterOptions", *, validate: Literal[False]) -> ResponseEnvelope[list[BalanceAndTurnoverListElementJSON]]: ...
@overload
def BalanceAndTurnoverAsync(api: SyncRequestProtocol, options: "BalanceAndTurnoverFilterOptions", *, validate: Literal[True] = True) -> ResponseEnvelope[List[BalanceAndTurnoverListElement]]: ...
@overload
def BalanceAndTurnoverAsync(api: SyncRequestProtocol, options: "BalanceAndTurnoverFilterOptions", *, validate: Literal[False]) -> ResponseEnvelope[list[BalanceAndTurnoverListElementJSON]]: ...
