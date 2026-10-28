from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseCorrection
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseCorrectionIssue
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocument
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentIssue
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentPZ

_ADAPTER_AddNew = TypeAdapter(PurchaseDocument)
OP_AddNew = build_typed_operation(method='POST', path='/api/PurchasesIssue/New', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/PurchasesIssue/New')

_ADAPTER_AddNewByCorrectionIssue = TypeAdapter(PurchaseCorrection)
OP_AddNewByCorrectionIssue = build_typed_operation(method='POST', path='/api/PurchasesIssue/NewCorrection', adapter=_ADAPTER_AddNewByCorrectionIssue)
OP_AddNewByCorrectionIssue_RAW = build_raw_operation(method='POST', path='/api/PurchasesIssue/NewCorrection')

_ADAPTER_Issue = TypeAdapter(PurchaseDocument)
OP_Issue = build_typed_operation(method='PUT', path='/api/PurchasesIssue/InBuffer', adapter=_ADAPTER_Issue)
OP_Issue_RAW = build_raw_operation(method='PUT', path='/api/PurchasesIssue/InBuffer')

_ADAPTER_IssueByNumber = TypeAdapter(PurchaseDocument)
OP_IssueByNumber = build_typed_operation(method='PUT', path='/api/PurchasesIssue/InBuffer', adapter=_ADAPTER_IssueByNumber)
OP_IssueByNumber_RAW = build_raw_operation(method='PUT', path='/api/PurchasesIssue/InBuffer')

_ADAPTER_IssuePZ = TypeAdapter(List[PurchaseDocumentPZ])
OP_IssuePZ = build_typed_operation(method='PUT', path='/api/PurchasesIssue/PZ', adapter=_ADAPTER_IssuePZ)
OP_IssuePZ_RAW = build_raw_operation(method='PUT', path='/api/PurchasesIssue/PZ')

_ADAPTER_IssuePZByDocumentNumber = TypeAdapter(List[PurchaseDocumentPZ])
OP_IssuePZByDocumentNumber = build_typed_operation(method='PUT', path='/api/PurchasesIssue/PZ', adapter=_ADAPTER_IssuePZByDocumentNumber)
OP_IssuePZByDocumentNumber_RAW = build_raw_operation(method='PUT', path='/api/PurchasesIssue/PZ')

_ADAPTER_IssuePZCorrection = TypeAdapter(List[PurchaseDocumentPZ])
OP_IssuePZCorrection = build_typed_operation(method='PUT', path='/api/PurchasesIssue/PZCorrection', adapter=_ADAPTER_IssuePZCorrection)
OP_IssuePZCorrection_RAW = build_raw_operation(method='PUT', path='/api/PurchasesIssue/PZCorrection')

_ADAPTER_IssuePZCorrectionByDocumentNumberIssue = TypeAdapter(List[PurchaseDocumentPZ])
OP_IssuePZCorrectionByDocumentNumberIssue = build_typed_operation(method='PUT', path='/api/PurchasesIssue/PZCorrection', adapter=_ADAPTER_IssuePZCorrectionByDocumentNumberIssue)
OP_IssuePZCorrectionByDocumentNumberIssue_RAW = build_raw_operation(method='PUT', path='/api/PurchasesIssue/PZCorrection')

OP_ChangeDocumentNumber = build_none_operation(method='PATCH', path='/api/PurchasesIssue/DocumentNumber')
OP_ChangeDocumentNumber_RAW = build_raw_operation(method='PATCH', path='/api/PurchasesIssue/DocumentNumber')
