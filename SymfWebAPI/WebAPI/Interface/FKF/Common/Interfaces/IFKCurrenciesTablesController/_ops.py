from __future__ import annotations

from typing import Any, List, Optional
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import CurrencyTable

_ADAPTER_Get = TypeAdapter(List[CurrencyTable])
OP_Get = build_typed_operation(method='GET', path='/api/FKCurrenciesTables', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/FKCurrenciesTables')

_ADAPTER_GetByCurrencyIdDate = TypeAdapter(List[CurrencyTable])
OP_GetByCurrencyIdDate = build_typed_operation(method='GET', path='/api/FKCurrenciesTables', adapter=_ADAPTER_GetByCurrencyIdDate)
OP_GetByCurrencyIdDate_RAW = build_raw_operation(method='GET', path='/api/FKCurrenciesTables')

_ADAPTER_GetList = TypeAdapter(List[CurrencyTable])
OP_GetList = build_typed_operation(method='GET', path='/api/FKCurrenciesTables/Filter', adapter=_ADAPTER_GetList)
OP_GetList_RAW = build_raw_operation(method='GET', path='/api/FKCurrenciesTables/Filter')

_ADAPTER_GetListByCurrency = TypeAdapter(List[CurrencyTable])
OP_GetListByCurrency = build_typed_operation(method='GET', path='/api/FKCurrenciesTables/Filter', adapter=_ADAPTER_GetListByCurrency)
OP_GetListByCurrency_RAW = build_raw_operation(method='GET', path='/api/FKCurrenciesTables/Filter')
