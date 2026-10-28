from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorDeliveryAddress
from ._common import (
    _prepare_Get,
    _prepare_GetByContractorCode,
    _prepare_AddNew,
    _prepare_AddNewByContractorCodeContractorDeliveryAddress,
    _prepare_Update,
    _prepare_UpdateByContractorCodeContractorDeliveryAddress,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByContractorCode,
    OP_GetByContractorCode_RAW,
    OP_AddNew,
    OP_AddNew_RAW,
    OP_AddNewByContractorCodeContractorDeliveryAddress,
    OP_AddNewByContractorCodeContractorDeliveryAddress_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_UpdateByContractorCodeContractorDeliveryAddress,
    OP_UpdateByContractorCodeContractorDeliveryAddress_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[ContractorDeliveryAddress]]: ...
@overload
def Get(api: SyncRequestProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[ContractorDeliveryAddress]]: ...
@overload
def Get(api: SyncInvokerProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ContractorDeliveryAddress]]: ...
@overload
def Get(api: SyncRequestProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ContractorDeliveryAddress]]: ...
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

@overload
def AddNew(api: SyncInvokerProtocol, contractorId: int, contractorDeliveryAddress: "ContractorDeliveryAddress", *, validate: bool = True) -> ResponseEnvelope[List[ContractorDeliveryAddress]]: ...
@overload
def AddNew(api: SyncRequestProtocol, contractorId: int, contractorDeliveryAddress: "ContractorDeliveryAddress", *, validate: bool = True) -> ResponseEnvelope[List[ContractorDeliveryAddress]]: ...
@overload
def AddNew(api: SyncInvokerProtocol, contractorCode: str, contractorDeliveryAddress: "ContractorDeliveryAddress", *, validate: bool = True) -> ResponseEnvelope[List[ContractorDeliveryAddress]]: ...
@overload
def AddNew(api: SyncRequestProtocol, contractorCode: str, contractorDeliveryAddress: "ContractorDeliveryAddress", *, validate: bool = True) -> ResponseEnvelope[List[ContractorDeliveryAddress]]: ...
def AddNew(api: object, contractorId: object = _UNSET, contractorDeliveryAddress: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'contractorDeliveryAddress' if contractorDeliveryAddress is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorDeliveryAddress', 'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("AddNew(): ambiguous overload for provided arguments")
        exact_match = 'AddNew'
        exact_match_name = 'AddNew'
    if provided_names == {'contractorCode', 'contractorDeliveryAddress'}:
        if exact_match_name is not None:
            raise TypeError("AddNew(): ambiguous overload for provided arguments")
        exact_match = 'AddNewByContractorCodeContractorDeliveryAddress'
        exact_match_name = 'AddNewByContractorCodeContractorDeliveryAddress'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorDeliveryAddress', 'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorDeliveryAddress', 'contractorId'}):
            candidates.append((2, -2, 'AddNew'))
        if {'contractorCode', 'contractorDeliveryAddress'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'contractorDeliveryAddress'}):
            candidates.append((2, -2, 'AddNewByContractorCodeContractorDeliveryAddress'))
        if not candidates:
            raise TypeError("AddNew(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("AddNew(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'AddNew':
        params, data = _prepare_AddNew(validate=validate, contractorId=contractorId, contractorDeliveryAddress=contractorDeliveryAddress)
        return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)
    if selected == 'AddNewByContractorCodeContractorDeliveryAddress':
        params, data = _prepare_AddNewByContractorCodeContractorDeliveryAddress(validate=validate, contractorCode=contractorCode, contractorDeliveryAddress=contractorDeliveryAddress)
        return invoke_operation(api, OP_AddNewByContractorCodeContractorDeliveryAddress if validate else OP_AddNewByContractorCodeContractorDeliveryAddress_RAW, params=params, data=data)
    raise TypeError("AddNew(): internal overload dispatch failure")

@overload
def Update(api: SyncInvokerProtocol, contractorId: int, contractorDeliveryAddress: "ContractorDeliveryAddress", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, contractorId: int, contractorDeliveryAddress: "ContractorDeliveryAddress", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncInvokerProtocol, contractorCode: str, contractorDeliveryAddress: "ContractorDeliveryAddress", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, contractorCode: str, contractorDeliveryAddress: "ContractorDeliveryAddress", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, contractorId: object = _UNSET, contractorDeliveryAddress: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'contractorDeliveryAddress' if contractorDeliveryAddress is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorDeliveryAddress', 'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'Update'
        exact_match_name = 'Update'
    if provided_names == {'contractorCode', 'contractorDeliveryAddress'}:
        if exact_match_name is not None:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        exact_match = 'UpdateByContractorCodeContractorDeliveryAddress'
        exact_match_name = 'UpdateByContractorCodeContractorDeliveryAddress'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorDeliveryAddress', 'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorDeliveryAddress', 'contractorId'}):
            candidates.append((2, -2, 'Update'))
        if {'contractorCode', 'contractorDeliveryAddress'}.issubset(provided_names) and provided_names.issubset({'contractorCode', 'contractorDeliveryAddress'}):
            candidates.append((2, -2, 'UpdateByContractorCodeContractorDeliveryAddress'))
        if not candidates:
            raise TypeError("Update(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Update(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Update':
        params, data = _prepare_Update(validate=validate, contractorId=contractorId, contractorDeliveryAddress=contractorDeliveryAddress)
        return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)
    if selected == 'UpdateByContractorCodeContractorDeliveryAddress':
        params, data = _prepare_UpdateByContractorCodeContractorDeliveryAddress(validate=validate, contractorCode=contractorCode, contractorDeliveryAddress=contractorDeliveryAddress)
        return invoke_operation(api, OP_UpdateByContractorCodeContractorDeliveryAddress if validate else OP_UpdateByContractorCodeContractorDeliveryAddress_RAW, params=params, data=data)
    raise TypeError("Update(): internal overload dispatch failure")

__all__ = ["Get", "AddNew", "Update"]
