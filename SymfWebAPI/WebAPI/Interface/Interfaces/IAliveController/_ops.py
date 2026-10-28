from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation

OP_Get = build_none_operation(method='GET', path='/api/Alive')
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Alive')
