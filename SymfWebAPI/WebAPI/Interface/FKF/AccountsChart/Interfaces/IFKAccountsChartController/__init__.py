from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.AccountsChart.ViewModels import AccountChartElement
from SymfWebAPI.WebAPI.Interface.FKF.AccountsChart.ViewModels import AccountChartElementSimple
from ._common import (
    _prepare_GetFlatList,
    _prepare_GetTreeList,
)
from ._ops import (
    OP_GetFlatList,
    OP_GetFlatList_RAW,
    OP_GetTreeList,
    OP_GetTreeList_RAW,
)

_UNSET = object()

@overload
def GetFlatList(api: SyncInvokerProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[AccountChartElementSimple]]: ...
@overload
def GetFlatList(api: SyncRequestProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[AccountChartElementSimple]]: ...
def GetFlatList(api: object, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetFlatList(yearId=yearId)
    return invoke_operation(api, OP_GetFlatList if validate else OP_GetFlatList_RAW, params=params, data=data)

@overload
def GetTreeList(api: SyncInvokerProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[AccountChartElement]]: ...
@overload
def GetTreeList(api: SyncRequestProtocol, yearId: int, *, validate: bool = True) -> ResponseEnvelope[List[AccountChartElement]]: ...
def GetTreeList(api: object, yearId: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetTreeList(yearId=yearId)
    return invoke_operation(api, OP_GetTreeList if validate else OP_GetTreeList_RAW, params=params, data=data)

__all__ = ["GetFlatList", "GetTreeList"]
