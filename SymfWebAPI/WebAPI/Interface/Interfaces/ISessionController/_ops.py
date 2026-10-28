from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.ViewModels import SessionInformation

OP_CloseSession = build_none_operation(method='GET', path='/api/Sessions/CloseSession')
OP_CloseSession_RAW = build_raw_operation(method='GET', path='/api/Sessions/CloseSession')

OP_OpenNewSession = build_none_operation(method='GET', path='/api/Sessions/OpenNewSession')
OP_OpenNewSession_RAW = build_raw_operation(method='GET', path='/api/Sessions/OpenNewSession')

_ADAPTER_SessionInformationAsync = TypeAdapter(SessionInformation)
OP_SessionInformationAsync = build_typed_operation(method='GET', path='/api/Sessions/SessionInformation', adapter=_ADAPTER_SessionInformationAsync)
OP_SessionInformationAsync_RAW = build_raw_operation(method='GET', path='/api/Sessions/SessionInformation')
