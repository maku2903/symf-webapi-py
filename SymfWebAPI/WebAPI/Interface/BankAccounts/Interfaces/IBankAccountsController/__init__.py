from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.BankAccounts.ViewModels import BankAccount
from ._common import (
    _prepare_Get,
    _prepare_GetListByContractor,
    _prepare_GetListByContractorByContractorCode,
    _prepare_Insert,
    _prepare_InsertByBankAccountContractorCode,
    _prepare_Update,
    _prepare_SetAsMain,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetListByContractor,
    OP_GetListByContractor_RAW,
    OP_GetListByContractorByContractorCode,
    OP_GetListByContractorByContractorCode_RAW,
    OP_Insert,
    OP_Insert_RAW,
    OP_InsertByBankAccountContractorCode,
    OP_InsertByBankAccountContractorCode_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_SetAsMain,
    OP_SetAsMain_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[BankAccount]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[BankAccount]: ...
def Get(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get(id=id)
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def GetListByContractor(api: SyncInvokerProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[BankAccount]]: ...
@overload
def GetListByContractor(api: SyncRequestProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[BankAccount]]: ...
@overload
def GetListByContractor(api: SyncInvokerProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[BankAccount]]: ...
@overload
def GetListByContractor(api: SyncRequestProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[BankAccount]]: ...
def GetListByContractor(api: object, contractorId: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("GetListByContractor(): ambiguous overload for provided arguments")
        exact_match = 'GetListByContractor'
        exact_match_name = 'GetListByContractor'
    if provided_names == {'contractorCode'}:
        if exact_match_name is not None:
            raise TypeError("GetListByContractor(): ambiguous overload for provided arguments")
        exact_match = 'GetListByContractorByContractorCode'
        exact_match_name = 'GetListByContractorByContractorCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'contractorId'}.issubset(provided_names) and provided_names.issubset({'contractorId'}):
            candidates.append((1, -1, 'GetListByContractor'))
        if {'contractorCode'}.issubset(provided_names) and provided_names.issubset({'contractorCode'}):
            candidates.append((1, -1, 'GetListByContractorByContractorCode'))
        if not candidates:
            raise TypeError("GetListByContractor(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByContractor(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByContractor':
        params, data = _prepare_GetListByContractor(contractorId=contractorId)
        return invoke_operation(api, OP_GetListByContractor if validate else OP_GetListByContractor_RAW, params=params, data=data)
    if selected == 'GetListByContractorByContractorCode':
        params, data = _prepare_GetListByContractorByContractorCode(contractorCode=contractorCode)
        return invoke_operation(api, OP_GetListByContractorByContractorCode if validate else OP_GetListByContractorByContractorCode_RAW, params=params, data=data)
    raise TypeError("GetListByContractor(): internal overload dispatch failure")

@overload
def Insert(api: SyncInvokerProtocol, contractorId: int, bankAccount: "BankAccount", *, validate: bool = True) -> ResponseEnvelope[BankAccount]: ...
@overload
def Insert(api: SyncRequestProtocol, contractorId: int, bankAccount: "BankAccount", *, validate: bool = True) -> ResponseEnvelope[BankAccount]: ...
@overload
def Insert(api: SyncInvokerProtocol, contractorCode: str, bankAccount: "BankAccount", *, validate: bool = True) -> ResponseEnvelope[BankAccount]: ...
@overload
def Insert(api: SyncRequestProtocol, contractorCode: str, bankAccount: "BankAccount", *, validate: bool = True) -> ResponseEnvelope[BankAccount]: ...
def Insert(api: object, contractorId: object = _UNSET, bankAccount: object = _UNSET, contractorCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'contractorId' if contractorId is not _UNSET else None,
        'bankAccount' if bankAccount is not _UNSET else None,
        'contractorCode' if contractorCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'bankAccount', 'contractorId'}:
        if exact_match_name is not None:
            raise TypeError("Insert(): ambiguous overload for provided arguments")
        exact_match = 'Insert'
        exact_match_name = 'Insert'
    if provided_names == {'bankAccount', 'contractorCode'}:
        if exact_match_name is not None:
            raise TypeError("Insert(): ambiguous overload for provided arguments")
        exact_match = 'InsertByBankAccountContractorCode'
        exact_match_name = 'InsertByBankAccountContractorCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'bankAccount', 'contractorId'}.issubset(provided_names) and provided_names.issubset({'bankAccount', 'contractorId'}):
            candidates.append((2, -2, 'Insert'))
        if {'bankAccount', 'contractorCode'}.issubset(provided_names) and provided_names.issubset({'bankAccount', 'contractorCode'}):
            candidates.append((2, -2, 'InsertByBankAccountContractorCode'))
        if not candidates:
            raise TypeError("Insert(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Insert(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Insert':
        params, data = _prepare_Insert(validate=validate, contractorId=contractorId, bankAccount=bankAccount)
        return invoke_operation(api, OP_Insert if validate else OP_Insert_RAW, params=params, data=data)
    if selected == 'InsertByBankAccountContractorCode':
        params, data = _prepare_InsertByBankAccountContractorCode(validate=validate, contractorCode=contractorCode, bankAccount=bankAccount)
        return invoke_operation(api, OP_InsertByBankAccountContractorCode if validate else OP_InsertByBankAccountContractorCode_RAW, params=params, data=data)
    raise TypeError("Insert(): internal overload dispatch failure")

@overload
def Update(api: SyncInvokerProtocol, bankAccount: "BankAccount", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, bankAccount: "BankAccount", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, bankAccount: "BankAccount", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Update(validate=validate, bankAccount=bankAccount)
    return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)

@overload
def SetAsMain(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def SetAsMain(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def SetAsMain(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_SetAsMain(id=id)
    return invoke_operation(api, OP_SetAsMain if validate else OP_SetAsMain_RAW, params=params, data=data)

__all__ = ["Get", "GetListByContractor", "Insert", "Update", "SetAsMain"]
