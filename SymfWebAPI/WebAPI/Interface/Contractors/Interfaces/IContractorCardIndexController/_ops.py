from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation

OP_GetByIdAsync = build_none_operation(method='GET', path='/api/Contractors')
OP_GetByIdAsync_RAW = build_raw_operation(method='GET', path='/api/Contractors')

OP_GetByCodeAsync = build_none_operation(method='GET', path='/api/Contractors')
OP_GetByCodeAsync_RAW = build_raw_operation(method='GET', path='/api/Contractors')

OP_GetByNIPAsync = build_none_operation(method='GET', path='/api/Contractors')
OP_GetByNIPAsync_RAW = build_raw_operation(method='GET', path='/api/Contractors')
