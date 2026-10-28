from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import Contractor

_ADAPTER_Get = TypeAdapter(Contractor)
OP_Get = build_typed_operation(method='GET', path='/api/OssContractors', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/OssContractors')

_ADAPTER_AddNew = TypeAdapter(Contractor)
OP_AddNew = build_typed_operation(method='POST', path='/api/OssContractors/Create', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/OssContractors/Create')

OP_Update = build_none_operation(method='PUT', path='/api/OssContractors/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/OssContractors/Update')
