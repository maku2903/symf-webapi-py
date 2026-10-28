from __future__ import annotations

from typing import Any, List, Optional
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import CurrencyRate

_ADAPTER_Get = TypeAdapter(List[CurrencyRate])
OP_Get = build_typed_operation(method='GET', path='/api/CurrencyRates', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/CurrencyRates')

_ADAPTER_GetByCurrencyIdDate = TypeAdapter(List[CurrencyRate])
OP_GetByCurrencyIdDate = build_typed_operation(method='GET', path='/api/CurrencyRates', adapter=_ADAPTER_GetByCurrencyIdDate)
OP_GetByCurrencyIdDate_RAW = build_raw_operation(method='GET', path='/api/CurrencyRates')

_ADAPTER_GetList = TypeAdapter(List[CurrencyRate])
OP_GetList = build_typed_operation(method='GET', path='/api/CurrencyRates/Filter', adapter=_ADAPTER_GetList)
OP_GetList_RAW = build_raw_operation(method='GET', path='/api/CurrencyRates/Filter')

_ADAPTER_GetListByCurrency = TypeAdapter(List[CurrencyRate])
OP_GetListByCurrency = build_typed_operation(method='GET', path='/api/CurrencyRates/Filter', adapter=_ADAPTER_GetListByCurrency)
OP_GetListByCurrency_RAW = build_raw_operation(method='GET', path='/api/CurrencyRates/Filter')
