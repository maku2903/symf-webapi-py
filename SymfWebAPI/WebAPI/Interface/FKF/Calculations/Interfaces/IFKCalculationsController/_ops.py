from __future__ import annotations

from typing import Any, List, Optional
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import CalculationFilterOptions
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import CalculationListElement
from SymfWebAPI.WebAPI.Interface.FKF.Calculations.ViewModels import CalculationListElementGrouped

_ADAPTER_Get = TypeAdapter(List[CalculationListElement])
OP_Get = build_typed_operation(method='GET', path='/api/FKCalculations', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/FKCalculations')

_ADAPTER_Custom = TypeAdapter(List[CalculationListElement])
OP_Custom = build_typed_operation(method='GET', path='/api/FKCalculations/CustomFilter', adapter=_ADAPTER_Custom)
OP_Custom_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/CustomFilter')

_ADAPTER_GetByContractor = TypeAdapter(List[CalculationListElement])
OP_GetByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter', adapter=_ADAPTER_GetByContractor)
OP_GetByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter')

_ADAPTER_GetNotSettledByContractor = TypeAdapter(List[CalculationListElement])
OP_GetNotSettledByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/NotSettled', adapter=_ADAPTER_GetNotSettledByContractor)
OP_GetNotSettledByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/NotSettled')

_ADAPTER_GetBeforeMaturityTermByContractor = TypeAdapter(List[CalculationListElement])
OP_GetBeforeMaturityTermByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/BeforeMaturityTerm', adapter=_ADAPTER_GetBeforeMaturityTermByContractor)
OP_GetBeforeMaturityTermByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/BeforeMaturityTerm')

_ADAPTER_GetAfterMaturityTermByContractor = TypeAdapter(List[CalculationListElement])
OP_GetAfterMaturityTermByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/AfterMaturityTerm', adapter=_ADAPTER_GetAfterMaturityTermByContractor)
OP_GetAfterMaturityTermByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/AfterMaturityTerm')

_ADAPTER_GetDueByContractor = TypeAdapter(List[CalculationListElement])
OP_GetDueByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Due', adapter=_ADAPTER_GetDueByContractor)
OP_GetDueByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Due')

_ADAPTER_GetDueNotSettledByContractor = TypeAdapter(List[CalculationListElement])
OP_GetDueNotSettledByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Due/NotSettled', adapter=_ADAPTER_GetDueNotSettledByContractor)
OP_GetDueNotSettledByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Due/NotSettled')

_ADAPTER_GetDueBeforeMaturityTermByContractor = TypeAdapter(List[CalculationListElement])
OP_GetDueBeforeMaturityTermByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Due/BeforeMaturityTerm', adapter=_ADAPTER_GetDueBeforeMaturityTermByContractor)
OP_GetDueBeforeMaturityTermByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Due/BeforeMaturityTerm')

_ADAPTER_GetDueAfterMaturityTermByContractor = TypeAdapter(List[CalculationListElement])
OP_GetDueAfterMaturityTermByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Due/AfterMaturityTerm', adapter=_ADAPTER_GetDueAfterMaturityTermByContractor)
OP_GetDueAfterMaturityTermByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Due/AfterMaturityTerm')

_ADAPTER_GetObligationByContractor = TypeAdapter(List[CalculationListElement])
OP_GetObligationByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Obligation', adapter=_ADAPTER_GetObligationByContractor)
OP_GetObligationByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Obligation')

_ADAPTER_GetObligationNotSettledByContractor = TypeAdapter(List[CalculationListElement])
OP_GetObligationNotSettledByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/NotSettled', adapter=_ADAPTER_GetObligationNotSettledByContractor)
OP_GetObligationNotSettledByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/NotSettled')

_ADAPTER_GetObligationBeforeMaturityTermByContractor = TypeAdapter(List[CalculationListElement])
OP_GetObligationBeforeMaturityTermByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/BeforeMaturityTerm', adapter=_ADAPTER_GetObligationBeforeMaturityTermByContractor)
OP_GetObligationBeforeMaturityTermByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/BeforeMaturityTerm')

_ADAPTER_GetObligationAfterMaturityTermByContractor = TypeAdapter(List[CalculationListElement])
OP_GetObligationAfterMaturityTermByContractor = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/AfterMaturityTerm', adapter=_ADAPTER_GetObligationAfterMaturityTermByContractor)
OP_GetObligationAfterMaturityTermByContractor_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/AfterMaturityTerm')

_ADAPTER_GetByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter', adapter=_ADAPTER_GetByEmployee)
OP_GetByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter')

_ADAPTER_GetNotSettledByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetNotSettledByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/NotSettled', adapter=_ADAPTER_GetNotSettledByEmployee)
OP_GetNotSettledByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/NotSettled')

_ADAPTER_GetBeforeMaturityTermByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetBeforeMaturityTermByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/BeforeMaturityTerm', adapter=_ADAPTER_GetBeforeMaturityTermByEmployee)
OP_GetBeforeMaturityTermByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/BeforeMaturityTerm')

_ADAPTER_GetAfterMaturityTermByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetAfterMaturityTermByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/AfterMaturityTerm', adapter=_ADAPTER_GetAfterMaturityTermByEmployee)
OP_GetAfterMaturityTermByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/AfterMaturityTerm')

_ADAPTER_GetDueByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetDueByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Due', adapter=_ADAPTER_GetDueByEmployee)
OP_GetDueByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Due')

_ADAPTER_GetDueNotSettledByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetDueNotSettledByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Due/NotSettled', adapter=_ADAPTER_GetDueNotSettledByEmployee)
OP_GetDueNotSettledByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Due/NotSettled')

_ADAPTER_GetDueBeforeMaturityTermByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetDueBeforeMaturityTermByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Due/BeforeMaturityTerm', adapter=_ADAPTER_GetDueBeforeMaturityTermByEmployee)
OP_GetDueBeforeMaturityTermByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Due/BeforeMaturityTerm')

_ADAPTER_GetDueAfterMaturityTermByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetDueAfterMaturityTermByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Due/AfterMaturityTerm', adapter=_ADAPTER_GetDueAfterMaturityTermByEmployee)
OP_GetDueAfterMaturityTermByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Due/AfterMaturityTerm')

_ADAPTER_GetObligationByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetObligationByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Obligation', adapter=_ADAPTER_GetObligationByEmployee)
OP_GetObligationByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Obligation')

_ADAPTER_GetObligationNotSettledByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetObligationNotSettledByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/NotSettled', adapter=_ADAPTER_GetObligationNotSettledByEmployee)
OP_GetObligationNotSettledByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/NotSettled')

_ADAPTER_GetObligationBeforeMaturityTermByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetObligationBeforeMaturityTermByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/BeforeMaturityTerm', adapter=_ADAPTER_GetObligationBeforeMaturityTermByEmployee)
OP_GetObligationBeforeMaturityTermByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/BeforeMaturityTerm')

_ADAPTER_GetObligationAfterMaturityTermByEmployee = TypeAdapter(List[CalculationListElement])
OP_GetObligationAfterMaturityTermByEmployee = build_typed_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/AfterMaturityTerm', adapter=_ADAPTER_GetObligationAfterMaturityTermByEmployee)
OP_GetObligationAfterMaturityTermByEmployee_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Filter/Obligation/AfterMaturityTerm')

_ADAPTER_GetDueGroupedBySubject = TypeAdapter(List[CalculationListElementGrouped])
OP_GetDueGroupedBySubject = build_typed_operation(method='GET', path='/api/FKCalculations/Grouped/Due', adapter=_ADAPTER_GetDueGroupedBySubject)
OP_GetDueGroupedBySubject_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Grouped/Due')

_ADAPTER_GetDueNotSettledGroupedBySubject = TypeAdapter(List[CalculationListElementGrouped])
OP_GetDueNotSettledGroupedBySubject = build_typed_operation(method='GET', path='/api/FKCalculations/Grouped/Due/NotSettled', adapter=_ADAPTER_GetDueNotSettledGroupedBySubject)
OP_GetDueNotSettledGroupedBySubject_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Grouped/Due/NotSettled')

_ADAPTER_GetDueBeforeMaturityTermGroupedBySubject = TypeAdapter(List[CalculationListElementGrouped])
OP_GetDueBeforeMaturityTermGroupedBySubject = build_typed_operation(method='GET', path='/api/FKCalculations/Grouped/Due/BeforeMaturityTerm', adapter=_ADAPTER_GetDueBeforeMaturityTermGroupedBySubject)
OP_GetDueBeforeMaturityTermGroupedBySubject_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Grouped/Due/BeforeMaturityTerm')

_ADAPTER_GetDueAfterMaturityTermGroupedBySubject = TypeAdapter(List[CalculationListElementGrouped])
OP_GetDueAfterMaturityTermGroupedBySubject = build_typed_operation(method='GET', path='/api/FKCalculations/Grouped/Due/AfterMaturityTerm', adapter=_ADAPTER_GetDueAfterMaturityTermGroupedBySubject)
OP_GetDueAfterMaturityTermGroupedBySubject_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Grouped/Due/AfterMaturityTerm')

_ADAPTER_GetObligationGroupedBySubject = TypeAdapter(List[CalculationListElementGrouped])
OP_GetObligationGroupedBySubject = build_typed_operation(method='GET', path='/api/FKCalculations/Grouped/Obligation', adapter=_ADAPTER_GetObligationGroupedBySubject)
OP_GetObligationGroupedBySubject_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Grouped/Obligation')

_ADAPTER_GetObligationNotSettledGroupedBySubject = TypeAdapter(List[CalculationListElementGrouped])
OP_GetObligationNotSettledGroupedBySubject = build_typed_operation(method='GET', path='/api/FKCalculations/Grouped/Obligation/NotSettled', adapter=_ADAPTER_GetObligationNotSettledGroupedBySubject)
OP_GetObligationNotSettledGroupedBySubject_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Grouped/Obligation/NotSettled')

_ADAPTER_GetObligationBeforeMaturityTermGroupedBySubject = TypeAdapter(List[CalculationListElementGrouped])
OP_GetObligationBeforeMaturityTermGroupedBySubject = build_typed_operation(method='GET', path='/api/FKCalculations/Grouped/Obligation/BeforeMaturityTerm', adapter=_ADAPTER_GetObligationBeforeMaturityTermGroupedBySubject)
OP_GetObligationBeforeMaturityTermGroupedBySubject_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Grouped/Obligation/BeforeMaturityTerm')

_ADAPTER_GetObligationAfterMaturityTermGroupedBySubject = TypeAdapter(List[CalculationListElementGrouped])
OP_GetObligationAfterMaturityTermGroupedBySubject = build_typed_operation(method='GET', path='/api/FKCalculations/Grouped/Obligation/AfterMaturityTerm', adapter=_ADAPTER_GetObligationAfterMaturityTermGroupedBySubject)
OP_GetObligationAfterMaturityTermGroupedBySubject_RAW = build_raw_operation(method='GET', path='/api/FKCalculations/Grouped/Obligation/AfterMaturityTerm')
