from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Update(*, productId, prices = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = serialize_request_body(prices, prefer_model_dump=True, validate=validate, body_name='prices') if prices is not None else None
    return params or None, data

def _prepare_UpdateByPricesProductCode(*, productCode, prices = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = serialize_request_body(prices, prefer_model_dump=True, validate=validate, body_name='prices') if prices is not None else None
    return params or None, data

def _prepare_Recalculate(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_RecalculateByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data

def _prepare_GetSalePricesByProduct(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_GetSalePricesByProductByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data

def _prepare_GetSalePricesByProductKind(*, productKindId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productKindId"] = productKindId
    data = None
    return params or None, data

def _prepare_GetSalePrices() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetQuantitativeDiscountsByProduct(*, productId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productId"] = productId
    data = None
    return params or None, data

def _prepare_GetQuantitativeDiscountsByProductByProductCode(*, productCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productCode"] = productCode
    data = None
    return params or None, data

def _prepare_GetQuantitativeDiscountsByProductKind(*, productKindId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["productKindId"] = productKindId
    data = None
    return params or None, data

def _prepare_GetQuantitativeDiscounts() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetIndividualDiscountsByContractor(*, contractorId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    data = None
    return params or None, data

def _prepare_GetIndividualDiscountsByContractorByContractorCode(*, contractorCode) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    data = None
    return params or None, data

def _prepare_GetIndividualDiscountsByContractorKind(*, contractorKindId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorKindId"] = contractorKindId
    data = None
    return params or None, data

def _prepare_GetIndividualDiscounts() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetPriceFactors(*, criteria) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["criteria"] = criteria
    data = None
    return params or None, data

def _prepare_CalculatePrices(*, criteria = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteria, prefer_model_dump=True, validate=validate, body_name='criteria') if criteria is not None else None
    return params or None, data

def _prepare_OrderPrices(*, criteria = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(criteria, prefer_model_dump=True, validate=validate, body_name='criteria') if criteria is not None else None
    return params or None, data
