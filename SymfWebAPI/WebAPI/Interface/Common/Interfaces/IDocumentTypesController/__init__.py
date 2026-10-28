from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import CharacterRelation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentType
from ._common import (
    _prepare_Get,
    _prepare_GetByCharacter,
    _prepare_GetCharacterRelations,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByCharacter,
    OP_GetByCharacter_RAW,
    OP_GetCharacterRelations,
    OP_GetCharacterRelations_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[DocumentType]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[DocumentType]: ...
def Get(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get(id=id)
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetByCharacter(api: SyncInvokerProtocol, documentCharacter: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
@overload
def GetByCharacter(api: SyncRequestProtocol, documentCharacter: int, *, validate: bool = True) -> ResponseEnvelope[List[DocumentType]]: ...
def GetByCharacter(api: object, documentCharacter: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByCharacter(documentCharacter=documentCharacter)
    return invoke_operation(api, OP_GetByCharacter if validate else OP_GetByCharacter_RAW, params=params, data=data)

@overload
def GetCharacterRelations(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[CharacterRelation]]: ...
@overload
def GetCharacterRelations(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[CharacterRelation]]: ...
def GetCharacterRelations(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetCharacterRelations()
    return invoke_operation(api, OP_GetCharacterRelations if validate else OP_GetCharacterRelations_RAW, params=params, data=data)

__all__ = ["Get", "GetByCharacter", "GetCharacterRelations"]
