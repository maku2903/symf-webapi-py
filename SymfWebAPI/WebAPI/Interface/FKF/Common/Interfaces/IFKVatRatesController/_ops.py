from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import VatRate

_ADAPTER_Get = TypeAdapter(List[VatRate])
OP_Get = build_typed_operation(method='GET', path='/api/FKVatRates', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/FKVatRates')
