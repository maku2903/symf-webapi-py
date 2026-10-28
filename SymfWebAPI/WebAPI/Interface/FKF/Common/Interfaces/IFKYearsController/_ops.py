from __future__ import annotations

from typing import Any, List
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Year

_ADAPTER_Get = TypeAdapter(List[Year])
OP_Get = build_typed_operation(method='GET', path='/api/FKYears', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/FKYears')

_ADAPTER_GetByDate = TypeAdapter(Year)
OP_GetByDate = build_typed_operation(method='GET', path='/api/FKYears', adapter=_ADAPTER_GetByDate)
OP_GetByDate_RAW = build_raw_operation(method='GET', path='/api/FKYears')
