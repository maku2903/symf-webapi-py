from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Dimension
from ._common import (
    _prepare_Get,
    _prepare_GetByContractorCode,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByContractorCode,
    OP_GetByContractorCode_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncInvokerProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
@overload
def Get(api: SyncRequestProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[Dimension]]: ...
def Get(api: object, contractorId: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'contractorCode'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByContractorCode'
        exact_match_name = 'GetByContractorCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId'}):
            candidates.append((1, -1, 'Get'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode'}):
            candidates.append((1, -1, 'GetByContractorCode'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(contractorId=contractorId)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByContractorCode':
        params, data = _prepare_GetByContractorCode(contractorCode=contractorCode)
        return invoke_operation(api, OP_GetByContractorCode if validate else OP_GetByContractorCode_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

__all__ = ["Get"]
