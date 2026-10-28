from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Issue.Business import BusinessDocumentIssue
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import Document

_ADAPTER_NewPurchaseInvoice = TypeAdapter(Document)
OP_NewPurchaseInvoice = build_typed_operation(method='POST', path='/api/FKDocumentsBusinessIssue/NewPurchaseInvoice', adapter=_ADAPTER_NewPurchaseInvoice)
OP_NewPurchaseInvoice_RAW = build_raw_operation(method='POST', path='/api/FKDocumentsBusinessIssue/NewPurchaseInvoice')

_ADAPTER_NewPurchaseInvoiceCorrection = TypeAdapter(Document)
OP_NewPurchaseInvoiceCorrection = build_typed_operation(method='POST', path='/api/FKDocumentsBusinessIssue/NewPurchaseInvoiceCorrection', adapter=_ADAPTER_NewPurchaseInvoiceCorrection)
OP_NewPurchaseInvoiceCorrection_RAW = build_raw_operation(method='POST', path='/api/FKDocumentsBusinessIssue/NewPurchaseInvoiceCorrection')

_ADAPTER_NewSaleInvoice = TypeAdapter(Document)
OP_NewSaleInvoice = build_typed_operation(method='POST', path='/api/FKDocumentsBusinessIssue/NewSaleInvoice', adapter=_ADAPTER_NewSaleInvoice)
OP_NewSaleInvoice_RAW = build_raw_operation(method='POST', path='/api/FKDocumentsBusinessIssue/NewSaleInvoice')

_ADAPTER_NewSaleInvoiceCorrection = TypeAdapter(Document)
OP_NewSaleInvoiceCorrection = build_typed_operation(method='POST', path='/api/FKDocumentsBusinessIssue/NewSaleInvoiceCorrection', adapter=_ADAPTER_NewSaleInvoiceCorrection)
OP_NewSaleInvoiceCorrection_RAW = build_raw_operation(method='POST', path='/api/FKDocumentsBusinessIssue/NewSaleInvoiceCorrection')
