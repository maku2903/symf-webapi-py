from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import FiscalPrinterStatus
from SymfWebAPI.WebAPI.Interface.Sales.ViewModels import FiscalizationResult

_ADAPTER_GetStatus = TypeAdapter(FiscalPrinterStatus)
OP_GetStatus = build_typed_operation(method='GET', path='/api/FiscalPrinter/Status', adapter=_ADAPTER_GetStatus)
OP_GetStatus_RAW = build_raw_operation(method='GET', path='/api/FiscalPrinter/Status')

_ADAPTER_Fiscalize = TypeAdapter(FiscalizationResult)
OP_Fiscalize = build_typed_operation(method='PATCH', path='/api/FiscalPrinter/Fiscalize', adapter=_ADAPTER_Fiscalize)
OP_Fiscalize_RAW = build_raw_operation(method='PATCH', path='/api/FiscalPrinter/Fiscalize')
