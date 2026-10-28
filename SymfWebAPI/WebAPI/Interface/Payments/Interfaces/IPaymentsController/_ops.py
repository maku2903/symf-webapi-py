from __future__ import annotations

from typing import Any, List, Optional
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentSeries
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import DocumentType
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import PDF
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels import Payment
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels.Issue import PaymentIssue
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels.IssueKP import PaymentKPIssue
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels import PaymentListElement
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

_ADAPTER_Get = TypeAdapter(List[PaymentListElement])
OP_Get = build_typed_operation(method='GET', path='/api/Payments', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Payments')

_ADAPTER_GetById = TypeAdapter(Payment)
OP_GetById = build_typed_operation(method='GET', path='/api/Payments', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/Payments')

_ADAPTER_GetByBufferNumber = TypeAdapter(Payment)
OP_GetByBufferNumber = build_typed_operation(method='GET', path='/api/Payments', adapter=_ADAPTER_GetByBufferNumber)
OP_GetByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/Payments')

_ADAPTER_GetList = TypeAdapter(List[PaymentListElement])
OP_GetList = build_typed_operation(method='GET', path='/api/Payments/Filter', adapter=_ADAPTER_GetList)
OP_GetList_RAW = build_raw_operation(method='GET', path='/api/Payments/Filter')

_ADAPTER_GetListByContractor = TypeAdapter(List[PaymentListElement])
OP_GetListByContractor = build_typed_operation(method='GET', path='/api/Payments/Filter', adapter=_ADAPTER_GetListByContractor)
OP_GetListByContractor_RAW = build_raw_operation(method='GET', path='/api/Payments/Filter')

_ADAPTER_GetListByContractorByContractorCodeDateFromDateTo = TypeAdapter(List[PaymentListElement])
OP_GetListByContractorByContractorCodeDateFromDateTo = build_typed_operation(method='GET', path='/api/Payments/Filter', adapter=_ADAPTER_GetListByContractorByContractorCodeDateFromDateTo)
OP_GetListByContractorByContractorCodeDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Payments/Filter')

_ADAPTER_GetListByPaymentRegistry = TypeAdapter(List[PaymentListElement])
OP_GetListByPaymentRegistry = build_typed_operation(method='GET', path='/api/Payments/Filter', adapter=_ADAPTER_GetListByPaymentRegistry)
OP_GetListByPaymentRegistry_RAW = build_raw_operation(method='GET', path='/api/Payments/Filter')

_ADAPTER_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode = TypeAdapter(List[PaymentListElement])
OP_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode = build_typed_operation(method='GET', path='/api/Payments/Filter', adapter=_ADAPTER_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode)
OP_GetListByPaymentRegistryByDateFromDateToPaymentRegistryCode_RAW = build_raw_operation(method='GET', path='/api/Payments/Filter')

_ADAPTER_GetListByReceivingPaymentRegistry = TypeAdapter(List[PaymentListElement])
OP_GetListByReceivingPaymentRegistry = build_typed_operation(method='GET', path='/api/Payments/Filter', adapter=_ADAPTER_GetListByReceivingPaymentRegistry)
OP_GetListByReceivingPaymentRegistry_RAW = build_raw_operation(method='GET', path='/api/Payments/Filter')

_ADAPTER_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode = TypeAdapter(List[PaymentListElement])
OP_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode = build_typed_operation(method='GET', path='/api/Payments/Filter', adapter=_ADAPTER_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode)
OP_GetListByReceivingPaymentRegistryByDateFromDateToReceivingPaymentRegistryCode_RAW = build_raw_operation(method='GET', path='/api/Payments/Filter')

_ADAPTER_GetPDF = TypeAdapter(PDF)
OP_GetPDF = build_typed_operation(method='GET', path='/api/Payments/PDF', adapter=_ADAPTER_GetPDF)
OP_GetPDF_RAW = build_raw_operation(method='GET', path='/api/Payments/PDF')

_ADAPTER_GetPDFByBufferDocumentNumberPrintNote = TypeAdapter(PDF)
OP_GetPDFByBufferDocumentNumberPrintNote = build_typed_operation(method='GET', path='/api/Payments/PDF', adapter=_ADAPTER_GetPDFByBufferDocumentNumberPrintNote)
OP_GetPDFByBufferDocumentNumberPrintNote_RAW = build_raw_operation(method='GET', path='/api/Payments/PDF')

_ADAPTER_GetNALDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetNALDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/NALDocumentTypes', adapter=_ADAPTER_GetNALDocumentTypes)
OP_GetNALDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/NALDocumentTypes')

_ADAPTER_GetZOBDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetZOBDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/ZOBDocumentTypes', adapter=_ADAPTER_GetZOBDocumentTypes)
OP_GetZOBDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/ZOBDocumentTypes')

_ADAPTER_GetKPDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetKPDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/KPDocumentTypes', adapter=_ADAPTER_GetKPDocumentTypes)
OP_GetKPDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/KPDocumentTypes')

_ADAPTER_GetKWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetKWDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/KWDocumentTypes', adapter=_ADAPTER_GetKWDocumentTypes)
OP_GetKWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/KWDocumentTypes')

_ADAPTER_GetBPDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetBPDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/BPDocumentTypes', adapter=_ADAPTER_GetBPDocumentTypes)
OP_GetBPDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/BPDocumentTypes')

_ADAPTER_GetBWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetBWDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/BWDocumentTypes', adapter=_ADAPTER_GetBWDocumentTypes)
OP_GetBWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/BWDocumentTypes')

_ADAPTER_GetIPDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetIPDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/IPDocumentTypes', adapter=_ADAPTER_GetIPDocumentTypes)
OP_GetIPDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/IPDocumentTypes')

_ADAPTER_GetIWDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetIWDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/IWDocumentTypes', adapter=_ADAPTER_GetIWDocumentTypes)
OP_GetIWDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/IWDocumentTypes')

_ADAPTER_GetTRPlusDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetTRPlusDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/TRPlusDocumentTypes', adapter=_ADAPTER_GetTRPlusDocumentTypes)
OP_GetTRPlusDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/TRPlusDocumentTypes')

_ADAPTER_GetTRMinusDocumentTypes = TypeAdapter(List[DocumentType])
OP_GetTRMinusDocumentTypes = build_typed_operation(method='GET', path='/api/Payments/TRMinusDocumentTypes', adapter=_ADAPTER_GetTRMinusDocumentTypes)
OP_GetTRMinusDocumentTypes_RAW = build_raw_operation(method='GET', path='/api/Payments/TRMinusDocumentTypes')

_ADAPTER_GetDocumentSeries = TypeAdapter(List[DocumentSeries])
OP_GetDocumentSeries = build_typed_operation(method='GET', path='/api/Payments/DocumentSeries', adapter=_ADAPTER_GetDocumentSeries)
OP_GetDocumentSeries_RAW = build_raw_operation(method='GET', path='/api/Payments/DocumentSeries')

_ADAPTER_IssuePayment = TypeAdapter(Payment)
OP_IssuePayment = build_typed_operation(method='POST', path='/api/Payments/Payment', adapter=_ADAPTER_IssuePayment)
OP_IssuePayment_RAW = build_raw_operation(method='POST', path='/api/Payments/Payment')

_ADAPTER_IssueTransferMinus = TypeAdapter(Payment)
OP_IssueTransferMinus = build_typed_operation(method='POST', path='/api/Payments/TransferMinus', adapter=_ADAPTER_IssueTransferMinus)
OP_IssueTransferMinus_RAW = build_raw_operation(method='POST', path='/api/Payments/TransferMinus')

_ADAPTER_IssueTransferPlus = TypeAdapter(Payment)
OP_IssueTransferPlus = build_typed_operation(method='PUT', path='/api/Payments/TransferPlus', adapter=_ADAPTER_IssueTransferPlus)
OP_IssueTransferPlus_RAW = build_raw_operation(method='PUT', path='/api/Payments/TransferPlus')

_ADAPTER_IssueTransferPlusByPaymentNumber = TypeAdapter(Payment)
OP_IssueTransferPlusByPaymentNumber = build_typed_operation(method='PUT', path='/api/Payments/TransferPlus', adapter=_ADAPTER_IssueTransferPlusByPaymentNumber)
OP_IssueTransferPlusByPaymentNumber_RAW = build_raw_operation(method='PUT', path='/api/Payments/TransferPlus')

OP_IssueKP = build_none_operation(method='POST', path='/api/Payments/IssueKP')
OP_IssueKP_RAW = build_raw_operation(method='POST', path='/api/Payments/IssueKP')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/Payments/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/Payments/Page')
