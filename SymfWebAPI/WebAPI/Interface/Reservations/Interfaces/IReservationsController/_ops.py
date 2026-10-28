from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Reservations.ViewModels import AdvancedReservationNew
from SymfWebAPI.WebAPI.Interface.Reservations.ViewModels import Reservation
from SymfWebAPI.WebAPI.Interface.Reservations.ViewModels import ReservationListElement
from SymfWebAPI.WebAPI.Interface.Reservations.ViewModels import ReservationNew

_ADAPTER_Get = TypeAdapter(List[ReservationListElement])
OP_Get = build_typed_operation(method='GET', path='/api/Reservations', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Reservations')

_ADAPTER_GetById = TypeAdapter(Reservation)
OP_GetById = build_typed_operation(method='GET', path='/api/Reservations', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/Reservations')

_ADAPTER_GetListByContractor = TypeAdapter(List[ReservationListElement])
OP_GetListByContractor = build_typed_operation(method='GET', path='/api/Reservations/Filter', adapter=_ADAPTER_GetListByContractor)
OP_GetListByContractor_RAW = build_raw_operation(method='GET', path='/api/Reservations/Filter')

_ADAPTER_GetListByContractorByContractorCode = TypeAdapter(List[ReservationListElement])
OP_GetListByContractorByContractorCode = build_typed_operation(method='GET', path='/api/Reservations/Filter', adapter=_ADAPTER_GetListByContractorByContractorCode)
OP_GetListByContractorByContractorCode_RAW = build_raw_operation(method='GET', path='/api/Reservations/Filter')

_ADAPTER_GetListByProduct = TypeAdapter(List[ReservationListElement])
OP_GetListByProduct = build_typed_operation(method='GET', path='/api/Reservations/Filter', adapter=_ADAPTER_GetListByProduct)
OP_GetListByProduct_RAW = build_raw_operation(method='GET', path='/api/Reservations/Filter')

_ADAPTER_GetListByProductByProductCode = TypeAdapter(List[ReservationListElement])
OP_GetListByProductByProductCode = build_typed_operation(method='GET', path='/api/Reservations/Filter', adapter=_ADAPTER_GetListByProductByProductCode)
OP_GetListByProductByProductCode_RAW = build_raw_operation(method='GET', path='/api/Reservations/Filter')

_ADAPTER_AddNew = TypeAdapter(Reservation)
OP_AddNew = build_typed_operation(method='POST', path='/api/Reservations/Create', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/Reservations/Create')

_ADAPTER_AdvancedAddNew = TypeAdapter(Reservation)
OP_AdvancedAddNew = build_typed_operation(method='POST', path='/api/Reservations/AdvancedCreate', adapter=_ADAPTER_AdvancedAddNew)
OP_AdvancedAddNew_RAW = build_raw_operation(method='POST', path='/api/Reservations/AdvancedCreate')

OP_Delete = build_none_operation(method='DELETE', path='/api/Reservations/Delete')
OP_Delete_RAW = build_raw_operation(method='DELETE', path='/api/Reservations/Delete')

OP_AdvancedDelete = build_none_operation(method='DELETE', path='/api/Reservations/AdvancedDelete')
OP_AdvancedDelete_RAW = build_raw_operation(method='DELETE', path='/api/Reservations/AdvancedDelete')
