from __future__ import annotations

from typing import Any

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_Custom(*, options) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["options"] = options
    data = None
    return params or None, data

def _prepare_GetByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetNotSettledByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetBeforeMaturityTermByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetAfterMaturityTermByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueNotSettledByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueBeforeMaturityTermByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueAfterMaturityTermByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationNotSettledByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationBeforeMaturityTermByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationAfterMaturityTermByContractor(*, contractorPosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorPosition"] = contractorPosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetNotSettledByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetBeforeMaturityTermByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetAfterMaturityTermByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueNotSettledByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueBeforeMaturityTermByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueAfterMaturityTermByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationNotSettledByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationBeforeMaturityTermByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationAfterMaturityTermByEmployee(*, employeePosition, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["employeePosition"] = employeePosition
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueGroupedBySubject(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueNotSettledGroupedBySubject(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueBeforeMaturityTermGroupedBySubject(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetDueAfterMaturityTermGroupedBySubject(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationGroupedBySubject(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationNotSettledGroupedBySubject(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationBeforeMaturityTermGroupedBySubject(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetObligationAfterMaturityTermGroupedBySubject(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data
