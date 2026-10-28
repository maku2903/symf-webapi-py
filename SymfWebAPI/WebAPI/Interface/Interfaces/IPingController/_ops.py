from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.ViewModels import Ping

_ADAPTER_Get = TypeAdapter(Ping)
OP_Get = build_typed_operation(method='GET', path='/api/Ping', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Ping')
