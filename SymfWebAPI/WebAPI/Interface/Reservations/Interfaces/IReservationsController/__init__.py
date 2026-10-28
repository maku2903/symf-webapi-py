from __future__ import annotations

from typing import Any, List, overload
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.Reservations.ViewModels import AdvancedReservationNew
from SymfWebAPI.WebAPI.Interface.Reservations.ViewModels import Reservation
from SymfWebAPI.WebAPI.Interface.Reservations.ViewModels import ReservationListElement
from SymfWebAPI.WebAPI.Interface.Reservations.ViewModels import ReservationNew
from ._common import (
    _prepare_Get,
    _prepare_GetById,
    _prepare_GetListByContractor,
    _prepare_GetListByContractorByContractorCode,
    _prepare_GetListByProduct,
    _prepare_GetListByProductByProductCode,
    _prepare_AddNew,
    _prepare_AdvancedAddNew,
    _prepare_Delete,
    _prepare_AdvancedDelete,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetById,
    OP_GetById_RAW,
    OP_GetListByContractor,
    OP_GetListByContractor_RAW,
    OP_GetListByContractorByContractorCode,
    OP_GetListByContractorByContractorCode_RAW,
    OP_GetListByProduct,
    OP_GetListByProduct_RAW,
    OP_GetListByProductByProductCode,
    OP_GetListByProductByProductCode_RAW,
    OP_AddNew,
    OP_AddNew_RAW,
    OP_AdvancedAddNew,
    OP_AdvancedAddNew_RAW,
    OP_Delete,
    OP_Delete_RAW,
    OP_AdvancedDelete,
    OP_AdvancedDelete_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Reservation]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Reservation]: ...
def Get(api: object, id: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetById'
        exact_match_name = 'GetById'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'Get'))
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'GetById'))
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
    if selected == 'GetById':
        params, data = _prepare_GetById(id=id)
        return invoke_operation(api, OP_GetById if validate else OP_GetById_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetListByContractor(api: SyncInvokerProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
@overload
def GetListByContractor(api: SyncRequestProtocol, contractorId: int, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
@overload
def GetListByContractor(api: SyncInvokerProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
@overload
def GetListByContractor(api: SyncRequestProtocol, contractorCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
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
def GetListByProduct(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
@overload
def GetListByProduct(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
@overload
def GetListByProduct(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
@overload
def GetListByProduct(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ReservationListElement]]: ...
def GetListByProduct(api: object, productId: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId'}:
        if exact_match_name is not None:
            raise TypeError("GetListByProduct(): ambiguous overload for provided arguments")
        exact_match = 'GetListByProduct'
        exact_match_name = 'GetListByProduct'
    if provided_names == {'productCode'}:
        if exact_match_name is not None:
            raise TypeError("GetListByProduct(): ambiguous overload for provided arguments")
        exact_match = 'GetListByProductByProductCode'
        exact_match_name = 'GetListByProductByProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'GetListByProduct'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'GetListByProductByProductCode'))
        if not candidates:
            raise TypeError("GetListByProduct(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetListByProduct(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetListByProduct':
        params, data = _prepare_GetListByProduct(productId=productId)
        return invoke_operation(api, OP_GetListByProduct if validate else OP_GetListByProduct_RAW, params=params, data=data)
    if selected == 'GetListByProductByProductCode':
        params, data = _prepare_GetListByProductByProductCode(productCode=productCode)
        return invoke_operation(api, OP_GetListByProductByProductCode if validate else OP_GetListByProductByProductCode_RAW, params=params, data=data)
    raise TypeError("GetListByProduct(): internal overload dispatch failure")

@overload
def AddNew(api: SyncInvokerProtocol, reservation: "ReservationNew", *, validate: bool = True) -> ResponseEnvelope[Reservation]: ...
@overload
def AddNew(api: SyncRequestProtocol, reservation: "ReservationNew", *, validate: bool = True) -> ResponseEnvelope[Reservation]: ...
def AddNew(api: object, reservation: "ReservationNew", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, reservation=reservation)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def AdvancedAddNew(api: SyncInvokerProtocol, reservation: "AdvancedReservationNew", *, validate: bool = True) -> ResponseEnvelope[Reservation]: ...
@overload
def AdvancedAddNew(api: SyncRequestProtocol, reservation: "AdvancedReservationNew", *, validate: bool = True) -> ResponseEnvelope[Reservation]: ...
def AdvancedAddNew(api: object, reservation: "AdvancedReservationNew", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AdvancedAddNew(validate=validate, reservation=reservation)
    return invoke_operation(api, OP_AdvancedAddNew if validate else OP_AdvancedAddNew_RAW, params=params, data=data)

@overload
def Delete(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Delete(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Delete(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Delete(id=id)
    return invoke_operation(api, OP_Delete if validate else OP_Delete_RAW, params=params, data=data)

@overload
def AdvancedDelete(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def AdvancedDelete(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def AdvancedDelete(api: object, id: int, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AdvancedDelete(id=id)
    return invoke_operation(api, OP_AdvancedDelete if validate else OP_AdvancedDelete_RAW, params=params, data=data)

__all__ = ["Get", "GetListByContractor", "GetListByProduct", "AddNew", "AdvancedAddNew", "Delete", "AdvancedDelete"]
