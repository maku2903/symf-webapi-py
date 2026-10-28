from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import Document
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Issue.Custom import DocumentIssue
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import DocumentMessage

_ADAPTER_AddNew = TypeAdapter(Document)
OP_AddNew = build_typed_operation(method='POST', path='/api/FKDocumentsIssue/NewCustom', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/FKDocumentsIssue/NewCustom')

_ADAPTER_Validate = TypeAdapter(List[DocumentMessage])
OP_Validate = build_typed_operation(method='PATCH', path='/api/FKDocumentsIssue/NewCustom', adapter=_ADAPTER_Validate)
OP_Validate_RAW = build_raw_operation(method='PATCH', path='/api/FKDocumentsIssue/NewCustom')
