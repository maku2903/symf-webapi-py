from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import BalanceAndTurnoverFilterOptions
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import BalanceAndTurnoverListElement

_ADAPTER_BalanceAndTurnoverAsync = TypeAdapter(List[BalanceAndTurnoverListElement])
OP_BalanceAndTurnoverAsync = build_typed_operation(method='GET', path='/api/FKCalculationsBusiness/BalanceAndTurnover', adapter=_ADAPTER_BalanceAndTurnoverAsync)
OP_BalanceAndTurnoverAsync_RAW = build_raw_operation(method='GET', path='/api/FKCalculationsBusiness/BalanceAndTurnover')
