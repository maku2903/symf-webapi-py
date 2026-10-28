from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation

OP_AddSendToKsefEventAsync = build_none_operation(method='POST', path='/api/Ksef/AddSendToKsefEvent')
OP_AddSendToKsefEventAsync_RAW = build_raw_operation(method='POST', path='/api/Ksef/AddSendToKsefEvent')

OP_ChangeKsefStatusAsync = build_none_operation(method='POST', path='/api/Ksef/ChangeKsefStatusAsync')
OP_ChangeKsefStatusAsync_RAW = build_raw_operation(method='POST', path='/api/Ksef/ChangeKsefStatusAsync')
