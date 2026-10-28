from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PriceType

_ADAPTER_GetSalePriceTypes = TypeAdapter(List[PriceType])
OP_GetSalePriceTypes = build_typed_operation(method='GET', path='/api/Prices/SalePriceTypes', adapter=_ADAPTER_GetSalePriceTypes)
OP_GetSalePriceTypes_RAW = build_raw_operation(method='GET', path='/api/Prices/SalePriceTypes')
