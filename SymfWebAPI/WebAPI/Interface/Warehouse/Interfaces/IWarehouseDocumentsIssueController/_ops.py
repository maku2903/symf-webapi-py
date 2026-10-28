from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocument
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentEdit
from SymfWebAPI.WebAPI.Interface.Warehouse.ViewModels import WarehouseDocumentIssue

_ADAPTER_AddNew = TypeAdapter(WarehouseDocument)
OP_AddNew = build_typed_operation(method='POST', path='/api/WarehouseDocumentsIssue/New', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/WarehouseDocumentsIssue/New')

_ADAPTER_Edit = TypeAdapter(WarehouseDocument)
OP_Edit = build_typed_operation(method='PUT', path='/api/WarehouseDocumentsIssue/Edit', adapter=_ADAPTER_Edit)
OP_Edit_RAW = build_raw_operation(method='PUT', path='/api/WarehouseDocumentsIssue/Edit')

_ADAPTER_Issue = TypeAdapter(WarehouseDocument)
OP_Issue = build_typed_operation(method='PUT', path='/api/WarehouseDocumentsIssue/InBuffer', adapter=_ADAPTER_Issue)
OP_Issue_RAW = build_raw_operation(method='PUT', path='/api/WarehouseDocumentsIssue/InBuffer')

_ADAPTER_IssueByNumber = TypeAdapter(WarehouseDocument)
OP_IssueByNumber = build_typed_operation(method='PUT', path='/api/WarehouseDocumentsIssue/InBuffer', adapter=_ADAPTER_IssueByNumber)
OP_IssueByNumber_RAW = build_raw_operation(method='PUT', path='/api/WarehouseDocumentsIssue/InBuffer')

OP_IssueMMPlus = build_none_operation(method='PUT', path='/api/WarehouseDocumentsIssue/MMPlus')
OP_IssueMMPlus_RAW = build_raw_operation(method='PUT', path='/api/WarehouseDocumentsIssue/MMPlus')

OP_IssueMMPlusByDocumentNumber = build_none_operation(method='PUT', path='/api/WarehouseDocumentsIssue/MMPlus')
OP_IssueMMPlusByDocumentNumber_RAW = build_raw_operation(method='PUT', path='/api/WarehouseDocumentsIssue/MMPlus')

OP_ChangeDocumentNumber = build_none_operation(method='PATCH', path='/api/WarehouseDocumentsIssue/DocumentNumber')
OP_ChangeDocumentNumber_RAW = build_raw_operation(method='PATCH', path='/api/WarehouseDocumentsIssue/DocumentNumber')
