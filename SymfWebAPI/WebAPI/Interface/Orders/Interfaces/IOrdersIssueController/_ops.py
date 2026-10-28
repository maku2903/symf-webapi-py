from __future__ import annotations

from typing import Any, List, Optional
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import Order
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderEdit
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderFV
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderIssue
from SymfWebAPI.WebAPI.Interface.Orders.ViewModels import OrderWZ

_ADAPTER_AddNew = TypeAdapter(Order)
OP_AddNew = build_typed_operation(method='POST', path='/api/OrdersIssue/New', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/OrdersIssue/New')

_ADAPTER_Edit = TypeAdapter(Order)
OP_Edit = build_typed_operation(method='PUT', path='/api/OrdersIssue/Edit', adapter=_ADAPTER_Edit)
OP_Edit_RAW = build_raw_operation(method='PUT', path='/api/OrdersIssue/Edit')

_ADAPTER_Issue = TypeAdapter(Order)
OP_Issue = build_typed_operation(method='PUT', path='/api/OrdersIssue/InBuffer', adapter=_ADAPTER_Issue)
OP_Issue_RAW = build_raw_operation(method='PUT', path='/api/OrdersIssue/InBuffer')

_ADAPTER_IssueByNumber = TypeAdapter(Order)
OP_IssueByNumber = build_typed_operation(method='PUT', path='/api/OrdersIssue/InBuffer', adapter=_ADAPTER_IssueByNumber)
OP_IssueByNumber_RAW = build_raw_operation(method='PUT', path='/api/OrdersIssue/InBuffer')

_ADAPTER_IssueWZ = TypeAdapter(List[OrderWZ])
OP_IssueWZ = build_typed_operation(method='PUT', path='/api/OrdersIssue/WZ', adapter=_ADAPTER_IssueWZ)
OP_IssueWZ_RAW = build_raw_operation(method='PUT', path='/api/OrdersIssue/WZ')

_ADAPTER_IssueWZByInBufferOrderNumber = TypeAdapter(List[OrderWZ])
OP_IssueWZByInBufferOrderNumber = build_typed_operation(method='PUT', path='/api/OrdersIssue/WZ', adapter=_ADAPTER_IssueWZByInBufferOrderNumber)
OP_IssueWZByInBufferOrderNumber_RAW = build_raw_operation(method='PUT', path='/api/OrdersIssue/WZ')

_ADAPTER_IssueFV = TypeAdapter(List[OrderFV])
OP_IssueFV = build_typed_operation(method='PUT', path='/api/OrdersIssue/FV', adapter=_ADAPTER_IssueFV)
OP_IssueFV_RAW = build_raw_operation(method='PUT', path='/api/OrdersIssue/FV')

_ADAPTER_IssueFVByOrderNumber = TypeAdapter(List[OrderFV])
OP_IssueFVByOrderNumber = build_typed_operation(method='PUT', path='/api/OrdersIssue/FV', adapter=_ADAPTER_IssueFVByOrderNumber)
OP_IssueFVByOrderNumber_RAW = build_raw_operation(method='PUT', path='/api/OrdersIssue/FV')

OP_Delete = build_none_operation(method='DELETE', path='/api/OrdersIssue/Delete')
OP_Delete_RAW = build_raw_operation(method='DELETE', path='/api/OrdersIssue/Delete')

OP_DeleteByBufferNumber = build_none_operation(method='DELETE', path='/api/OrdersIssue/Delete')
OP_DeleteByBufferNumber_RAW = build_raw_operation(method='DELETE', path='/api/OrdersIssue/Delete')

OP_ChangeDocumentNumber = build_none_operation(method='PATCH', path='/api/OrdersIssue/DocumentNumber')
OP_ChangeDocumentNumber_RAW = build_raw_operation(method='PATCH', path='/api/OrdersIssue/DocumentNumber')
