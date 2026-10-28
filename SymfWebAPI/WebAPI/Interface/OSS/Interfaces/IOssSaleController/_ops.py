from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Sales import OssDomesticSaleDocument
from SymfWebAPI.WebAPI.Interface.OSS.ViewModels.Sales import OssSaleDocument
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocument
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import SaleDocumentWZ

_ADAPTER_AddNew = TypeAdapter(SaleDocument)
OP_AddNew = build_typed_operation(method='POST', path='/api/OssSale/New', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/OssSale/New')

_ADAPTER_AddNewReceipt = TypeAdapter(SaleDocument)
OP_AddNewReceipt = build_typed_operation(method='POST', path='/api/OssSale/NewReceipt', adapter=_ADAPTER_AddNewReceipt)
OP_AddNewReceipt_RAW = build_raw_operation(method='POST', path='/api/OssSale/NewReceipt')

_ADAPTER_IssueWZ = TypeAdapter(List[SaleDocumentWZ])
OP_IssueWZ = build_typed_operation(method='PUT', path='/api/OssSale/WZ', adapter=_ADAPTER_IssueWZ)
OP_IssueWZ_RAW = build_raw_operation(method='PUT', path='/api/OssSale/WZ')
