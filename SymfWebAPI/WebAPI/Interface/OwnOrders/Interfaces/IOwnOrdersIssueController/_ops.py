from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrder
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrderIssue
from SymfWebAPI.WebAPI.Interface.OwnOrders.ViewModels import OwnOrderPZ

_ADAPTER_AddNew = TypeAdapter(OwnOrder)
OP_AddNew = build_typed_operation(method='POST', path='/api/OwnOrdersIssue/New', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/OwnOrdersIssue/New')

OP_Delete = build_none_operation(method='DELETE', path='/api/OwnOrdersIssue/Delete')
OP_Delete_RAW = build_raw_operation(method='DELETE', path='/api/OwnOrdersIssue/Delete')

OP_DeleteByBufferNumber = build_none_operation(method='DELETE', path='/api/OwnOrdersIssue/Delete')
OP_DeleteByBufferNumber_RAW = build_raw_operation(method='DELETE', path='/api/OwnOrdersIssue/Delete')

_ADAPTER_Issue = TypeAdapter(OwnOrder)
OP_Issue = build_typed_operation(method='PUT', path='/api/OwnOrdersIssue/InBuffer', adapter=_ADAPTER_Issue)
OP_Issue_RAW = build_raw_operation(method='PUT', path='/api/OwnOrdersIssue/InBuffer')

_ADAPTER_IssueByNumber = TypeAdapter(OwnOrder)
OP_IssueByNumber = build_typed_operation(method='PUT', path='/api/OwnOrdersIssue/InBuffer', adapter=_ADAPTER_IssueByNumber)
OP_IssueByNumber_RAW = build_raw_operation(method='PUT', path='/api/OwnOrdersIssue/InBuffer')

_ADAPTER_IssuePZ = TypeAdapter(List[OwnOrderPZ])
OP_IssuePZ = build_typed_operation(method='PUT', path='/api/OwnOrdersIssue/PZ', adapter=_ADAPTER_IssuePZ)
OP_IssuePZ_RAW = build_raw_operation(method='PUT', path='/api/OwnOrdersIssue/PZ')

_ADAPTER_IssuePZByOrderNumber = TypeAdapter(List[OwnOrderPZ])
OP_IssuePZByOrderNumber = build_typed_operation(method='PUT', path='/api/OwnOrdersIssue/PZ', adapter=_ADAPTER_IssuePZByOrderNumber)
OP_IssuePZByOrderNumber_RAW = build_raw_operation(method='PUT', path='/api/OwnOrdersIssue/PZ')

OP_ChangeDocumentNumber = build_none_operation(method='PATCH', path='/api/OwnOrdersIssue/DocumentNumber')
OP_ChangeDocumentNumber_RAW = build_raw_operation(method='PATCH', path='/api/OwnOrdersIssue/DocumentNumber')

OP_IssueFV = build_none_operation(method='PUT', path='/api/OwnOrdersIssue/FV')
OP_IssueFV_RAW = build_raw_operation(method='PUT', path='/api/OwnOrdersIssue/FV')

OP_IssueFVByOrderNumber = build_none_operation(method='PUT', path='/api/OwnOrdersIssue/FV')
OP_IssueFVByOrderNumber_RAW = build_raw_operation(method='PUT', path='/api/OwnOrdersIssue/FV')
