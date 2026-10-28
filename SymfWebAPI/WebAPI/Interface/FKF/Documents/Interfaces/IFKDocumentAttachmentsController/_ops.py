from __future__ import annotations

from typing import Any
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Rdf import RdfDocumentAttachment

OP_AddNew = build_none_operation(method='POST', path='/api/FKDocumentAttachments/AddNew')
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/FKDocumentAttachments/AddNew')

OP_Update = build_none_operation(method='PUT', path='/api/FKDocumentAttachments/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/FKDocumentAttachments/Update')
