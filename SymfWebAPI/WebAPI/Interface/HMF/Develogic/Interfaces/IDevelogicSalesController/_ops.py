from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.HMF.Develogic.ViewModels import DevelogicAdvancePayment
from SymfWebAPI.WebAPI.Interface.HMF.Develogic.ViewModels import DevelogicContractInvoiceIssue
from SymfWebAPI.WebAPI.Interface.HMF.Develogic.ViewModels import DevelogicDocumentIssue
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocument

_ADAPTER_AddNew = TypeAdapter(SaleDocument)
OP_AddNew = build_typed_operation(method='POST', path='/api/DevelogicSales/Invoice', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/DevelogicSales/Invoice')

_ADAPTER_IssueAdvancePayment = TypeAdapter(SaleDocument)
OP_IssueAdvancePayment = build_typed_operation(method='POST', path='/api/DevelogicSales/AdvancePayment', adapter=_ADAPTER_IssueAdvancePayment)
OP_IssueAdvancePayment_RAW = build_raw_operation(method='POST', path='/api/DevelogicSales/AdvancePayment')

_ADAPTER_IssueContractInvoice = TypeAdapter(SaleDocument)
OP_IssueContractInvoice = build_typed_operation(method='POST', path='/api/DevelogicSales/ContractInvoice', adapter=_ADAPTER_IssueContractInvoice)
OP_IssueContractInvoice_RAW = build_raw_operation(method='POST', path='/api/DevelogicSales/ContractInvoice')
