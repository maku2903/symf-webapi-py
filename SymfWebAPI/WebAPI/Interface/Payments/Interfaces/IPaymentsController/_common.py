from __future__ import annotations

from typing import Any

from SymfWebAPI.operations import serialize_request_body

def _prepare_Get() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetById(*, id) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["id"] = id
    data = None
    return params or None, data

def _prepare_GetByBufferNumber(*, number, buffer) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["number"] = number
    params["buffer"] = buffer
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

def _prepare_GetListByContractor(*, contractorId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorId"] = contractorId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByContractorByContractorCodeDateFromDateTo(*, contractorCode, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["contractorCode"] = contractorCode
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByPaymentRegistry(*, paymentRegistryId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["paymentRegistryId"] = paymentRegistryId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode(*, paymentRegistryCode, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["paymentRegistryCode"] = paymentRegistryCode
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByReceivingPaymentRegistry(*, receivingPaymentRegistryId, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["receivingPaymentRegistryId"] = receivingPaymentRegistryId
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode(*, receivingPaymentRegistryCode, dateFrom = None, dateTo = None) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["receivingPaymentRegistryCode"] = receivingPaymentRegistryCode
    if dateFrom is not None:
        params["dateFrom"] = dateFrom
    if dateTo is not None:
        params["dateTo"] = dateTo
    data = None
    return params or None, data

def _prepare_GetPDF(*, documentId, printNote) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentId"] = documentId
    params["printNote"] = printNote
    data = None
    return params or None, data

def _prepare_GetPDFByBufferDocumentNumberPrintNote(*, documentNumber, buffer, printNote) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentNumber"] = documentNumber
    params["buffer"] = buffer
    params["printNote"] = printNote
    data = None
    return params or None, data

def _prepare_GetNALDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetZOBDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetKPDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetKWDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetBPDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetBWDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetIPDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetIWDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetTRPlusDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetTRMinusDocumentTypes() -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = None
    return params or None, data

def _prepare_GetDocumentSeries(*, documentTypeId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["documentTypeId"] = documentTypeId
    data = None
    return params or None, data

def _prepare_IssuePayment(*, payment = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(payment, prefer_model_dump=True, validate=validate, body_name='payment') if payment is not None else None
    return params or None, data

def _prepare_IssueTransferMinus(*, payment = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(payment, prefer_model_dump=True, validate=validate, body_name='payment') if payment is not None else None
    return params or None, data

def _prepare_IssueTransferPlus(*, paymentId) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["paymentId"] = paymentId
    data = None
    return params or None, data

def _prepare_IssueTransferPlusByPaymentNumber(*, paymentNumber) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["paymentNumber"] = paymentNumber
    data = None
    return params or None, data

def _prepare_IssueKP(*, payment = None, validate: bool = True) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    data = serialize_request_body(payment, prefer_model_dump=True, validate=validate, body_name='payment') if payment is not None else None
    return params or None, data

def _prepare_GetPagedDocument(*, page, size, orderBy) -> tuple[dict[str, Any] | None, Any]:
    params: dict[str, Any] = {}
    params["page"] = page
    params["size"] = size
    params["orderBy"] = orderBy.value
    data = None
    return params or None, data
