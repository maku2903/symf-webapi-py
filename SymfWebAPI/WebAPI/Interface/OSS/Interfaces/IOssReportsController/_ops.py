from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF

_ADAPTER_GetOrderPDF = TypeAdapter(PDF)
OP_GetOrderPDF = build_typed_operation(method='GET', path='/api/OssReports/Order', adapter=_ADAPTER_GetOrderPDF)
OP_GetOrderPDF_RAW = build_raw_operation(method='GET', path='/api/OssReports/Order')

_ADAPTER_GetSaleDocumentPDF = TypeAdapter(PDF)
OP_GetSaleDocumentPDF = build_typed_operation(method='GET', path='/api/OssReports/SaleDocument', adapter=_ADAPTER_GetSaleDocumentPDF)
OP_GetSaleDocumentPDF_RAW = build_raw_operation(method='GET', path='/api/OssReports/SaleDocument')

_ADAPTER_GetWarehouseDocumentPDF = TypeAdapter(PDF)
OP_GetWarehouseDocumentPDF = build_typed_operation(method='GET', path='/api/OssReports/WarehouseDocument', adapter=_ADAPTER_GetWarehouseDocumentPDF)
OP_GetWarehouseDocumentPDF_RAW = build_raw_operation(method='GET', path='/api/OssReports/WarehouseDocument')
