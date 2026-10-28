from __future__ import annotations

from typing import Any, List, Optional
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import AdvancePaymentOptions
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleCorrection
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleCorrectionIssue
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocument
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentIssue
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentWZ

_ADAPTER_AddNew = TypeAdapter(SaleDocument)
OP_AddNew = build_typed_operation(method='POST', path='/api/SalesIssue/New', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/SalesIssue/New')

_ADAPTER_AddNewByCorrectionIssue = TypeAdapter(SaleCorrection)
OP_AddNewByCorrectionIssue = build_typed_operation(method='POST', path='/api/SalesIssue/NewCorrection', adapter=_ADAPTER_AddNewByCorrectionIssue)
OP_AddNewByCorrectionIssue_RAW = build_raw_operation(method='POST', path='/api/SalesIssue/NewCorrection')

_ADAPTER_Issue = TypeAdapter(SaleDocument)
OP_Issue = build_typed_operation(method='PUT', path='/api/SalesIssue/InBuffer', adapter=_ADAPTER_Issue)
OP_Issue_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/InBuffer')

_ADAPTER_IssueByNumber = TypeAdapter(SaleDocument)
OP_IssueByNumber = build_typed_operation(method='PUT', path='/api/SalesIssue/InBuffer', adapter=_ADAPTER_IssueByNumber)
OP_IssueByNumber_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/InBuffer')

_ADAPTER_IssueAdvancePayment = TypeAdapter(SaleDocument)
OP_IssueAdvancePayment = build_typed_operation(method='PUT', path='/api/SalesIssue/AdvancePayment', adapter=_ADAPTER_IssueAdvancePayment)
OP_IssueAdvancePayment_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/AdvancePayment')

_ADAPTER_IssueAdvancePaymentByDocumentNumberOptions = TypeAdapter(SaleDocument)
OP_IssueAdvancePaymentByDocumentNumberOptions = build_typed_operation(method='PUT', path='/api/SalesIssue/AdvancePayment', adapter=_ADAPTER_IssueAdvancePaymentByDocumentNumberOptions)
OP_IssueAdvancePaymentByDocumentNumberOptions_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/AdvancePayment')

_ADAPTER_IssueWZ = TypeAdapter(List[SaleDocumentWZ])
OP_IssueWZ = build_typed_operation(method='PUT', path='/api/SalesIssue/WZ', adapter=_ADAPTER_IssueWZ)
OP_IssueWZ_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/WZ')

_ADAPTER_IssueWZByDocumentNumberInBuffer = TypeAdapter(List[SaleDocumentWZ])
OP_IssueWZByDocumentNumberInBuffer = build_typed_operation(method='PUT', path='/api/SalesIssue/WZ', adapter=_ADAPTER_IssueWZByDocumentNumberInBuffer)
OP_IssueWZByDocumentNumberInBuffer_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/WZ')

_ADAPTER_IssueWZCorrection = TypeAdapter(List[SaleDocumentWZ])
OP_IssueWZCorrection = build_typed_operation(method='PUT', path='/api/SalesIssue/IssueWZCorrection', adapter=_ADAPTER_IssueWZCorrection)
OP_IssueWZCorrection_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/IssueWZCorrection')

_ADAPTER_IssueWZCorrectionByDocumentNumberIssue = TypeAdapter(List[SaleDocumentWZ])
OP_IssueWZCorrectionByDocumentNumberIssue = build_typed_operation(method='PUT', path='/api/SalesIssue/IssueWZCorrection', adapter=_ADAPTER_IssueWZCorrectionByDocumentNumberIssue)
OP_IssueWZCorrectionByDocumentNumberIssue_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/IssueWZCorrection')

OP_ChangeDocumentNumber = build_none_operation(method='PATCH', path='/api/SalesIssue/DocumentNumber')
OP_ChangeDocumentNumber_RAW = build_raw_operation(method='PATCH', path='/api/SalesIssue/DocumentNumber')

OP_IssuePN = build_none_operation(method='PUT', path='/api/SalesIssue/IssuePayment')
OP_IssuePN_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/IssuePayment')

OP_IssuePNByDocumentNumber = build_none_operation(method='PUT', path='/api/SalesIssue/IssuePayment')
OP_IssuePNByDocumentNumber_RAW = build_raw_operation(method='PUT', path='/api/SalesIssue/IssuePayment')

OP_ChangeFiscalStatus = build_none_operation(method='PATCH', path='/api/SalesIssue/FiscalStatus')
OP_ChangeFiscalStatus_RAW = build_raw_operation(method='PATCH', path='/api/SalesIssue/FiscalStatus')

OP_ChangeFiscalStatusByDocumentNumber = build_none_operation(method='PATCH', path='/api/SalesIssue/FiscalStatus')
OP_ChangeFiscalStatusByDocumentNumber_RAW = build_raw_operation(method='PATCH', path='/api/SalesIssue/FiscalStatus')
