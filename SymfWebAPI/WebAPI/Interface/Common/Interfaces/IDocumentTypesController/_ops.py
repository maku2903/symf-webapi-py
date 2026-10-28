from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import CharacterRelation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentType

_ADAPTER_Get = TypeAdapter(DocumentType)
OP_Get = build_typed_operation(method='GET', path='/api/DocumentTypes', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/DocumentTypes')

_ADAPTER_GetByCharacter = TypeAdapter(List[DocumentType])
OP_GetByCharacter = build_typed_operation(method='GET', path='/api/DocumentTypes', adapter=_ADAPTER_GetByCharacter)
OP_GetByCharacter_RAW = build_raw_operation(method='GET', path='/api/DocumentTypes')

_ADAPTER_GetCharacterRelations = TypeAdapter(List[CharacterRelation])
OP_GetCharacterRelations = build_typed_operation(method='GET', path='/api/DocumentTypes/CharacterRelations', adapter=_ADAPTER_GetCharacterRelations)
OP_GetCharacterRelations_RAW = build_raw_operation(method='GET', path='/api/DocumentTypes/CharacterRelations')
