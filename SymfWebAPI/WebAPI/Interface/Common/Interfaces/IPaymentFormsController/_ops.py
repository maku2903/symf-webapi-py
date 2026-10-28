from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentForm

_ADAPTER_Get = TypeAdapter(List[PaymentForm])
OP_Get = build_typed_operation(method='GET', path='/api/PaymentForms', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/PaymentForms')

_ADAPTER_GetByRegistryId = TypeAdapter(List[PaymentForm])
OP_GetByRegistryId = build_typed_operation(method='GET', path='/api/PaymentForms', adapter=_ADAPTER_GetByRegistryId)
OP_GetByRegistryId_RAW = build_raw_operation(method='GET', path='/api/PaymentForms')
