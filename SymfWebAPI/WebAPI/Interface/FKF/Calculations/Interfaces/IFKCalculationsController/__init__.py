from __future__ import annotations

from typing import Any, List, Optional, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import CalculationFilterOptions
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import CalculationListElement
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import CalculationListElementGrouped
from ._common import (
    _prepare_Get,
    _prepare_Custom,
    _prepare_GetByContractor,
    _prepare_GetNotSettledByContractor,
    _prepare_GetBeforeMaturityTermByContractor,
    _prepare_GetAfterMaturityTermByContractor,
    _prepare_GetDueByContractor,
    _prepare_GetDueNotSettledByContractor,
    _prepare_GetDueBeforeMaturityTermByContractor,
    _prepare_GetDueAfterMaturityTermByContractor,
    _prepare_GetObligationByContractor,
    _prepare_GetObligationNotSettledByContractor,
    _prepare_GetObligationBeforeMaturityTermByContractor,
    _prepare_GetObligationAfterMaturityTermByContractor,
    _prepare_GetByEmployee,
    _prepare_GetNotSettledByEmployee,
    _prepare_GetBeforeMaturityTermByEmployee,
    _prepare_GetAfterMaturityTermByEmployee,
    _prepare_GetDueByEmployee,
    _prepare_GetDueNotSettledByEmployee,
    _prepare_GetDueBeforeMaturityTermByEmployee,
    _prepare_GetDueAfterMaturityTermByEmployee,
    _prepare_GetObligationByEmployee,
    _prepare_GetObligationNotSettledByEmployee,
    _prepare_GetObligationBeforeMaturityTermByEmployee,
    _prepare_GetObligationAfterMaturityTermByEmployee,
    _prepare_GetDueGroupedBySubject,
    _prepare_GetDueNotSettledGroupedBySubject,
    _prepare_GetDueBeforeMaturityTermGroupedBySubject,
    _prepare_GetDueAfterMaturityTermGroupedBySubject,
    _prepare_GetObligationGroupedBySubject,
    _prepare_GetObligationNotSettledGroupedBySubject,
    _prepare_GetObligationBeforeMaturityTermGroupedBySubject,
    _prepare_GetObligationAfterMaturityTermGroupedBySubject,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_Custom,
    OP_Custom_RAW,
    OP_GetByContractor,
    OP_GetByContractor_RAW,
    OP_GetNotSettledByContractor,
    OP_GetNotSettledByContractor_RAW,
    OP_GetBeforeMaturityTermByContractor,
    OP_GetBeforeMaturityTermByContractor_RAW,
    OP_GetAfterMaturityTermByContractor,
    OP_GetAfterMaturityTermByContractor_RAW,
    OP_GetDueByContractor,
    OP_GetDueByContractor_RAW,
    OP_GetDueNotSettledByContractor,
    OP_GetDueNotSettledByContractor_RAW,
    OP_GetDueBeforeMaturityTermByContractor,
    OP_GetDueBeforeMaturityTermByContractor_RAW,
    OP_GetDueAfterMaturityTermByContractor,
    OP_GetDueAfterMaturityTermByContractor_RAW,
    OP_GetObligationByContractor,
    OP_GetObligationByContractor_RAW,
    OP_GetObligationNotSettledByContractor,
    OP_GetObligationNotSettledByContractor_RAW,
    OP_GetObligationBeforeMaturityTermByContractor,
    OP_GetObligationBeforeMaturityTermByContractor_RAW,
    OP_GetObligationAfterMaturityTermByContractor,
    OP_GetObligationAfterMaturityTermByContractor_RAW,
    OP_GetByEmployee,
    OP_GetByEmployee_RAW,
    OP_GetNotSettledByEmployee,
    OP_GetNotSettledByEmployee_RAW,
    OP_GetBeforeMaturityTermByEmployee,
    OP_GetBeforeMaturityTermByEmployee_RAW,
    OP_GetAfterMaturityTermByEmployee,
    OP_GetAfterMaturityTermByEmployee_RAW,
    OP_GetDueByEmployee,
    OP_GetDueByEmployee_RAW,
    OP_GetDueNotSettledByEmployee,
    OP_GetDueNotSettledByEmployee_RAW,
    OP_GetDueBeforeMaturityTermByEmployee,
    OP_GetDueBeforeMaturityTermByEmployee_RAW,
    OP_GetDueAfterMaturityTermByEmployee,
    OP_GetDueAfterMaturityTermByEmployee_RAW,
    OP_GetObligationByEmployee,
    OP_GetObligationByEmployee_RAW,
    OP_GetObligationNotSettledByEmployee,
    OP_GetObligationNotSettledByEmployee_RAW,
    OP_GetObligationBeforeMaturityTermByEmployee,
    OP_GetObligationBeforeMaturityTermByEmployee_RAW,
    OP_GetObligationAfterMaturityTermByEmployee,
    OP_GetObligationAfterMaturityTermByEmployee_RAW,
    OP_GetDueGroupedBySubject,
    OP_GetDueGroupedBySubject_RAW,
    OP_GetDueNotSettledGroupedBySubject,
    OP_GetDueNotSettledGroupedBySubject_RAW,
    OP_GetDueBeforeMaturityTermGroupedBySubject,
    OP_GetDueBeforeMaturityTermGroupedBySubject_RAW,
    OP_GetDueAfterMaturityTermGroupedBySubject,
    OP_GetDueAfterMaturityTermGroupedBySubject_RAW,
    OP_GetObligationGroupedBySubject,
    OP_GetObligationGroupedBySubject_RAW,
    OP_GetObligationNotSettledGroupedBySubject,
    OP_GetObligationNotSettledGroupedBySubject_RAW,
    OP_GetObligationBeforeMaturityTermGroupedBySubject,
    OP_GetObligationBeforeMaturityTermGroupedBySubject_RAW,
    OP_GetObligationAfterMaturityTermGroupedBySubject,
    OP_GetObligationAfterMaturityTermGroupedBySubject_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def Get(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Get()
    return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)

@overload
def Custom(api: SyncInvokerProtocol, options: "CalculationFilterOptions", *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def Custom(api: SyncRequestProtocol, options: "CalculationFilterOptions", *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def Custom(api: object, options: "CalculationFilterOptions", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Custom(options=options)
    return invoke_operation(api, OP_Custom if validate else OP_Custom_RAW, params=params, data=data)

@overload
def GetByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetByContractor if validate else OP_GetByContractor_RAW, params=params, data=data)

@overload
def GetNotSettledByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetNotSettledByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetNotSettledByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetNotSettledByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetNotSettledByContractor if validate else OP_GetNotSettledByContractor_RAW, params=params, data=data)

@overload
def GetBeforeMaturityTermByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetBeforeMaturityTermByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetBeforeMaturityTermByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetBeforeMaturityTermByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetBeforeMaturityTermByContractor if validate else OP_GetBeforeMaturityTermByContractor_RAW, params=params, data=data)

@overload
def GetAfterMaturityTermByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetAfterMaturityTermByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetAfterMaturityTermByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetAfterMaturityTermByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetAfterMaturityTermByContractor if validate else OP_GetAfterMaturityTermByContractor_RAW, params=params, data=data)

@overload
def GetDueByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetDueByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetDueByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueByContractor if validate else OP_GetDueByContractor_RAW, params=params, data=data)

@overload
def GetDueNotSettledByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetDueNotSettledByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetDueNotSettledByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueNotSettledByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueNotSettledByContractor if validate else OP_GetDueNotSettledByContractor_RAW, params=params, data=data)

@overload
def GetDueBeforeMaturityTermByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetDueBeforeMaturityTermByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetDueBeforeMaturityTermByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueBeforeMaturityTermByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueBeforeMaturityTermByContractor if validate else OP_GetDueBeforeMaturityTermByContractor_RAW, params=params, data=data)

@overload
def GetDueAfterMaturityTermByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetDueAfterMaturityTermByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetDueAfterMaturityTermByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueAfterMaturityTermByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueAfterMaturityTermByContractor if validate else OP_GetDueAfterMaturityTermByContractor_RAW, params=params, data=data)

@overload
def GetObligationByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetObligationByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetObligationByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationByContractor if validate else OP_GetObligationByContractor_RAW, params=params, data=data)

@overload
def GetObligationNotSettledByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetObligationNotSettledByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetObligationNotSettledByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationNotSettledByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationNotSettledByContractor if validate else OP_GetObligationNotSettledByContractor_RAW, params=params, data=data)

@overload
def GetObligationBeforeMaturityTermByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetObligationBeforeMaturityTermByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetObligationBeforeMaturityTermByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationBeforeMaturityTermByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationBeforeMaturityTermByContractor if validate else OP_GetObligationBeforeMaturityTermByContractor_RAW, params=params, data=data)

@overload
def GetObligationAfterMaturityTermByContractor(api: SyncInvokerProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetObligationAfterMaturityTermByContractor(api: SyncRequestProtocol, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetObligationAfterMaturityTermByContractor(api: object, contractorPosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationAfterMaturityTermByContractor(contractorPosition=contractorPosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationAfterMaturityTermByContractor if validate else OP_GetObligationAfterMaturityTermByContractor_RAW, params=params, data=data)

@overload
def GetByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetByEmployee if validate else OP_GetByEmployee_RAW, params=params, data=data)

@overload
def GetNotSettledByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetNotSettledByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetNotSettledByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetNotSettledByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetNotSettledByEmployee if validate else OP_GetNotSettledByEmployee_RAW, params=params, data=data)

@overload
def GetBeforeMaturityTermByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetBeforeMaturityTermByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetBeforeMaturityTermByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetBeforeMaturityTermByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetBeforeMaturityTermByEmployee if validate else OP_GetBeforeMaturityTermByEmployee_RAW, params=params, data=data)

@overload
def GetAfterMaturityTermByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetAfterMaturityTermByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetAfterMaturityTermByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetAfterMaturityTermByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetAfterMaturityTermByEmployee if validate else OP_GetAfterMaturityTermByEmployee_RAW, params=params, data=data)

@overload
def GetDueByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetDueByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetDueByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueByEmployee if validate else OP_GetDueByEmployee_RAW, params=params, data=data)

@overload
def GetDueNotSettledByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetDueNotSettledByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetDueNotSettledByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueNotSettledByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueNotSettledByEmployee if validate else OP_GetDueNotSettledByEmployee_RAW, params=params, data=data)

@overload
def GetDueBeforeMaturityTermByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetDueBeforeMaturityTermByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetDueBeforeMaturityTermByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueBeforeMaturityTermByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueBeforeMaturityTermByEmployee if validate else OP_GetDueBeforeMaturityTermByEmployee_RAW, params=params, data=data)

@overload
def GetDueAfterMaturityTermByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetDueAfterMaturityTermByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetDueAfterMaturityTermByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueAfterMaturityTermByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueAfterMaturityTermByEmployee if validate else OP_GetDueAfterMaturityTermByEmployee_RAW, params=params, data=data)

@overload
def GetObligationByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetObligationByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetObligationByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationByEmployee if validate else OP_GetObligationByEmployee_RAW, params=params, data=data)

@overload
def GetObligationNotSettledByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetObligationNotSettledByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetObligationNotSettledByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationNotSettledByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationNotSettledByEmployee if validate else OP_GetObligationNotSettledByEmployee_RAW, params=params, data=data)

@overload
def GetObligationBeforeMaturityTermByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetObligationBeforeMaturityTermByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetObligationBeforeMaturityTermByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationBeforeMaturityTermByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationBeforeMaturityTermByEmployee if validate else OP_GetObligationBeforeMaturityTermByEmployee_RAW, params=params, data=data)

@overload
def GetObligationAfterMaturityTermByEmployee(api: SyncInvokerProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
@overload
def GetObligationAfterMaturityTermByEmployee(api: SyncRequestProtocol, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElement]]: ...
def GetObligationAfterMaturityTermByEmployee(api: object, employeePosition: int, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationAfterMaturityTermByEmployee(employeePosition=employeePosition, dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationAfterMaturityTermByEmployee if validate else OP_GetObligationAfterMaturityTermByEmployee_RAW, params=params, data=data)

@overload
def GetDueGroupedBySubject(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
@overload
def GetDueGroupedBySubject(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
def GetDueGroupedBySubject(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueGroupedBySubject(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueGroupedBySubject if validate else OP_GetDueGroupedBySubject_RAW, params=params, data=data)

@overload
def GetDueNotSettledGroupedBySubject(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
@overload
def GetDueNotSettledGroupedBySubject(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
def GetDueNotSettledGroupedBySubject(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueNotSettledGroupedBySubject(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueNotSettledGroupedBySubject if validate else OP_GetDueNotSettledGroupedBySubject_RAW, params=params, data=data)

@overload
def GetDueBeforeMaturityTermGroupedBySubject(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
@overload
def GetDueBeforeMaturityTermGroupedBySubject(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
def GetDueBeforeMaturityTermGroupedBySubject(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueBeforeMaturityTermGroupedBySubject(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueBeforeMaturityTermGroupedBySubject if validate else OP_GetDueBeforeMaturityTermGroupedBySubject_RAW, params=params, data=data)

@overload
def GetDueAfterMaturityTermGroupedBySubject(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
@overload
def GetDueAfterMaturityTermGroupedBySubject(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
def GetDueAfterMaturityTermGroupedBySubject(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetDueAfterMaturityTermGroupedBySubject(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetDueAfterMaturityTermGroupedBySubject if validate else OP_GetDueAfterMaturityTermGroupedBySubject_RAW, params=params, data=data)

@overload
def GetObligationGroupedBySubject(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
@overload
def GetObligationGroupedBySubject(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
def GetObligationGroupedBySubject(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationGroupedBySubject(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationGroupedBySubject if validate else OP_GetObligationGroupedBySubject_RAW, params=params, data=data)

@overload
def GetObligationNotSettledGroupedBySubject(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
@overload
def GetObligationNotSettledGroupedBySubject(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
def GetObligationNotSettledGroupedBySubject(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationNotSettledGroupedBySubject(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationNotSettledGroupedBySubject if validate else OP_GetObligationNotSettledGroupedBySubject_RAW, params=params, data=data)

@overload
def GetObligationBeforeMaturityTermGroupedBySubject(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
@overload
def GetObligationBeforeMaturityTermGroupedBySubject(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
def GetObligationBeforeMaturityTermGroupedBySubject(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationBeforeMaturityTermGroupedBySubject(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationBeforeMaturityTermGroupedBySubject if validate else OP_GetObligationBeforeMaturityTermGroupedBySubject_RAW, params=params, data=data)

@overload
def GetObligationAfterMaturityTermGroupedBySubject(api: SyncInvokerProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
@overload
def GetObligationAfterMaturityTermGroupedBySubject(api: SyncRequestProtocol, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[List[CalculationListElementGrouped]]: ...
def GetObligationAfterMaturityTermGroupedBySubject(api: object, dateFrom: Optional[datetime] = None, dateTo: Optional[datetime] = None, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetObligationAfterMaturityTermGroupedBySubject(dateFrom=dateFrom, dateTo=dateTo)
    return invoke_operation(api, OP_GetObligationAfterMaturityTermGroupedBySubject if validate else OP_GetObligationAfterMaturityTermGroupedBySubject_RAW, params=params, data=data)

__all__ = ["Get", "Custom", "GetByContractor", "GetNotSettledByContractor", "GetBeforeMaturityTermByContractor", "GetAfterMaturityTermByContractor", "GetDueByContractor", "GetDueNotSettledByContractor", "GetDueBeforeMaturityTermByContractor", "GetDueAfterMaturityTermByContractor", "GetObligationByContractor", "GetObligationNotSettledByContractor", "GetObligationBeforeMaturityTermByContractor", "GetObligationAfterMaturityTermByContractor", "GetByEmployee", "GetNotSettledByEmployee", "GetBeforeMaturityTermByEmployee", "GetAfterMaturityTermByEmployee", "GetDueByEmployee", "GetDueNotSettledByEmployee", "GetDueBeforeMaturityTermByEmployee", "GetDueAfterMaturityTermByEmployee", "GetObligationByEmployee", "GetObligationNotSettledByEmployee", "GetObligationBeforeMaturityTermByEmployee", "GetObligationAfterMaturityTermByEmployee", "GetDueGroupedBySubject", "GetDueNotSettledGroupedBySubject", "GetDueBeforeMaturityTermGroupedBySubject", "GetDueAfterMaturityTermGroupedBySubject", "GetObligationGroupedBySubject", "GetObligationNotSettledGroupedBySubject", "GetObligationBeforeMaturityTermGroupedBySubject", "GetObligationAfterMaturityTermGroupedBySubject"]
