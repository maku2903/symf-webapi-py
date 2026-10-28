from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.BankAccounts.ViewModels import BankAccount

_ADAPTER_Get = TypeAdapter(BankAccount)
OP_Get = build_typed_operation(method='GET', path='/api/BankAccounts', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/BankAccounts')

_ADAPTER_GetListByContractor = TypeAdapter(List[BankAccount])
OP_GetListByContractor = build_typed_operation(method='GET', path='/api/BankAccounts', adapter=_ADAPTER_GetListByContractor)
OP_GetListByContractor_RAW = build_raw_operation(method='GET', path='/api/BankAccounts')

_ADAPTER_GetListByContractorByContractorCode = TypeAdapter(List[BankAccount])
OP_GetListByContractorByContractorCode = build_typed_operation(method='GET', path='/api/BankAccounts', adapter=_ADAPTER_GetListByContractorByContractorCode)
OP_GetListByContractorByContractorCode_RAW = build_raw_operation(method='GET', path='/api/BankAccounts')

_ADAPTER_Insert = TypeAdapter(BankAccount)
OP_Insert = build_typed_operation(method='POST', path='/api/BankAccounts/Create', adapter=_ADAPTER_Insert)
OP_Insert_RAW = build_raw_operation(method='POST', path='/api/BankAccounts/Create')

_ADAPTER_InsertByBankAccountContractorCode = TypeAdapter(BankAccount)
OP_InsertByBankAccountContractorCode = build_typed_operation(method='POST', path='/api/BankAccounts/Create', adapter=_ADAPTER_InsertByBankAccountContractorCode)
OP_InsertByBankAccountContractorCode_RAW = build_raw_operation(method='POST', path='/api/BankAccounts/Create')

OP_Update = build_none_operation(method='PUT', path='/api/BankAccounts/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/BankAccounts/Update')

OP_SetAsMain = build_none_operation(method='PATCH', path='/api/BankAccounts/SetAsMain')
OP_SetAsMain_RAW = build_raw_operation(method='PATCH', path='/api/BankAccounts/SetAsMain')
