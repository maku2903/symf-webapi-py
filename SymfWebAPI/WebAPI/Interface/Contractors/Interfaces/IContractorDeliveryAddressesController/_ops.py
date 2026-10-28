from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Contractors.ViewModels import ContractorDeliveryAddress

_ADAPTER_Get = TypeAdapter(List[ContractorDeliveryAddress])
OP_Get = build_typed_operation(method='GET', path='/api/ContractorDeliveryAddresses', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/ContractorDeliveryAddresses')

_ADAPTER_GetByContractorCode = TypeAdapter(List[ContractorDeliveryAddress])
OP_GetByContractorCode = build_typed_operation(method='GET', path='/api/ContractorDeliveryAddresses', adapter=_ADAPTER_GetByContractorCode)
OP_GetByContractorCode_RAW = build_raw_operation(method='GET', path='/api/ContractorDeliveryAddresses')

_ADAPTER_AddNew = TypeAdapter(List[ContractorDeliveryAddress])
OP_AddNew = build_typed_operation(method='POST', path='/api/ContractorDeliveryAddresses/Create', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/ContractorDeliveryAddresses/Create')

_ADAPTER_AddNewByContractorCodeContractorDeliveryAddress = TypeAdapter(List[ContractorDeliveryAddress])
OP_AddNewByContractorCodeContractorDeliveryAddress = build_typed_operation(method='POST', path='/api/ContractorDeliveryAddresses/Create', adapter=_ADAPTER_AddNewByContractorCodeContractorDeliveryAddress)
OP_AddNewByContractorCodeContractorDeliveryAddress_RAW = build_raw_operation(method='POST', path='/api/ContractorDeliveryAddresses/Create')

OP_Update = build_none_operation(method='PUT', path='/api/ContractorDeliveryAddresses/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/ContractorDeliveryAddresses/Update')

OP_UpdateByContractorCodeContractorDeliveryAddress = build_none_operation(method='PUT', path='/api/ContractorDeliveryAddresses/Update')
OP_UpdateByContractorCodeContractorDeliveryAddress_RAW = build_raw_operation(method='PUT', path='/api/ContractorDeliveryAddresses/Update')
