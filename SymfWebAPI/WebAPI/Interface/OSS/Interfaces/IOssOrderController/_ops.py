from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import Order
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderFV
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderWZ
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Orders import OssOrder

_ADAPTER_AddNew = TypeAdapter(Order)
OP_AddNew = build_typed_operation(method='POST', path='/api/OssOrder/New', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/OssOrder/New')

_ADAPTER_IssueFV = TypeAdapter(List[OrderFV])
OP_IssueFV = build_typed_operation(method='PUT', path='/api/OssOrder/FV', adapter=_ADAPTER_IssueFV)
OP_IssueFV_RAW = build_raw_operation(method='PUT', path='/api/OssOrder/FV')

_ADAPTER_IssueWZ = TypeAdapter(List[OrderWZ])
OP_IssueWZ = build_typed_operation(method='PUT', path='/api/OssOrder/WZ', adapter=_ADAPTER_IssueWZ)
OP_IssueWZ_RAW = build_raw_operation(method='PUT', path='/api/OssOrder/WZ')
