from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PaymentForm
from ._common import (
    _prepare_Get,
    _prepare_GetByRegistryId,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByRegistryId,
    OP_GetByRegistryId_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PaymentForm]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[PaymentForm]]: ...
@overload
def Get(api: SyncInvokerProtocol, registryId: int, *, validate: bool = True) -> ResponseEnvelope[List[PaymentForm]]: ...
@overload
def Get(api: SyncRequestProtocol, registryId: int, *, validate: bool = True) -> ResponseEnvelope[List[PaymentForm]]: ...
def Get(api: object, registryId: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'registryId' if registryId is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'registryId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByRegistryId'
        exact_match_name = 'GetByRegistryId'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'Get'))
        if {'registryId'}.issubset(provided_names) and provided_names.issubset({'registryId'}):
            candidates.append((1, -1, 'GetByRegistryId'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get()
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByRegistryId':
        params, data = _prepare_GetByRegistryId(registryId=registryId)
        return invoke_operation(api, OP_GetByRegistryId if validate else OP_GetByRegistryId_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

__all__ = ["Get"]
