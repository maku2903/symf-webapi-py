from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.AccountsChart.ViewModels import AccountChartElement
from SymfWebAPI.WebAPI.Interface.FKF.AccountsChart.ViewModels import AccountChartElementSimple

_ADAPTER_GetFlatList = TypeAdapter(List[AccountChartElementSimple])
OP_GetFlatList = build_typed_operation(method='GET', path='/api/FKAccountsChart/FlatList', adapter=_ADAPTER_GetFlatList)
OP_GetFlatList_RAW = build_raw_operation(method='GET', path='/api/FKAccountsChart/FlatList')

_ADAPTER_GetTreeList = TypeAdapter(List[AccountChartElement])
OP_GetTreeList = build_typed_operation(method='GET', path='/api/FKAccountsChart/FlatList', adapter=_ADAPTER_GetTreeList)
OP_GetTreeList_RAW = build_raw_operation(method='GET', path='/api/FKAccountsChart/FlatList')
