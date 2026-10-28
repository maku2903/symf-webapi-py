from __future__ import annotations

from typing import Any

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetByCurrencyIdDate(*, currencyId, date = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["currencyId"] = currencyId
    if date is not None:
        params["date"] = date
    data = None
    return params or None, data

def _prepare_GetList(*, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByCurrency(*, currencyId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["currencyId"] = currencyId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data
