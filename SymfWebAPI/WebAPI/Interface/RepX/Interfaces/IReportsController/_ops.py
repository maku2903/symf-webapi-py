from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.RepX.ViewModels import PrintData
from SymfWebAPI.WebAPI.Interface.RepX.ViewModels import ReportDefinition

_ADAPTER_Get = TypeAdapter(PDF)
OP_Get = build_typed_operation(method='PATCH', path='/api/Reports', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='PATCH', path='/api/Reports')

_ADAPTER_GetDefinitions = TypeAdapter(List[ReportDefinition])
OP_GetDefinitions = build_typed_operation(method='GET', path='/api/Reports/Definitions', adapter=_ADAPTER_GetDefinitions)
OP_GetDefinitions_RAW = build_raw_operation(method='GET', path='/api/Reports/Definitions')
