from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocument
from SymfWebAPI.WebAPI.Interface.Purchases.ViewModels import PurchaseDocumentIssue

_ADAPTER_AddNew = TypeAdapter(PurchaseDocument)
OP_AddNew = build_typed_operation(method='POST', path='/api/DevelogicPurchases/Invoice', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/DevelogicPurchases/Invoice')
