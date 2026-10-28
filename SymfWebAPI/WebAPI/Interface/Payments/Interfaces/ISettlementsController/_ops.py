from __future__ import annotations

from typing import Any, List, Optional
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels import Settlement
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels.Issue import SettlementIssue
from SymfWebAPI.WebAPI.Interface.Payments.ViewModels import SettlementListElement

_ADAPTER_Get = TypeAdapter(List[SettlementListElement])
OP_Get = build_typed_operation(method='GET', path='/api/Settlements', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Settlements')

_ADAPTER_GetById = TypeAdapter(Settlement)
OP_GetById = build_typed_operation(method='GET', path='/api/Settlements', adapter=_ADAPTER_GetById)
OP_GetById_RAW = build_raw_operation(method='GET', path='/api/Settlements')

_ADAPTER_GetByBufferNumber = TypeAdapter(Settlement)
OP_GetByBufferNumber = build_typed_operation(method='GET', path='/api/Settlements', adapter=_ADAPTER_GetByBufferNumber)
OP_GetByBufferNumber_RAW = build_raw_operation(method='GET', path='/api/Settlements')

_ADAPTER_GetByDocument = TypeAdapter(Settlement)
OP_GetByDocument = build_typed_operation(method='GET', path='/api/Settlements', adapter=_ADAPTER_GetByDocument)
OP_GetByDocument_RAW = build_raw_operation(method='GET', path='/api/Settlements')

_ADAPTER_GetByDocumentByBufferDocumentNumber = TypeAdapter(Settlement)
OP_GetByDocumentByBufferDocumentNumber = build_typed_operation(method='GET', path='/api/Settlements', adapter=_ADAPTER_GetByDocumentByBufferDocumentNumber)
OP_GetByDocumentByBufferDocumentNumber_RAW = build_raw_operation(method='GET', path='/api/Settlements')

_ADAPTER_GetListByIssueDate = TypeAdapter(List[SettlementListElement])
OP_GetListByIssueDate = build_typed_operation(method='GET', path='/api/Settlements/Filter/ByIssueDate', adapter=_ADAPTER_GetListByIssueDate)
OP_GetListByIssueDate_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/ByIssueDate')

OP_GetListByIssueDateByContractorIdDateFromDateTo = build_none_operation(method='GET', path='/api/Settlements/Filter/ByIssueDate')
OP_GetListByIssueDateByContractorIdDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/ByIssueDate')

OP_GetListByIssueDateByContractorCodeDateFromDateTo = build_none_operation(method='GET', path='/api/Settlements/Filter/ByIssueDate')
OP_GetListByIssueDateByContractorCodeDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/ByIssueDate')

_ADAPTER_GetListByMaturityDate = TypeAdapter(List[SettlementListElement])
OP_GetListByMaturityDate = build_typed_operation(method='GET', path='/api/Settlements/Filter/ByMaturityDate', adapter=_ADAPTER_GetListByMaturityDate)
OP_GetListByMaturityDate_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/ByMaturityDate')

_ADAPTER_GetListByMaturityDateByContractorIdDateFromDateTo = TypeAdapter(List[SettlementListElement])
OP_GetListByMaturityDateByContractorIdDateFromDateTo = build_typed_operation(method='GET', path='/api/Settlements/Filter/ByMaturityDate', adapter=_ADAPTER_GetListByMaturityDateByContractorIdDateFromDateTo)
OP_GetListByMaturityDateByContractorIdDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/ByMaturityDate')

_ADAPTER_GetListByMaturityDateByContractorCodeDateFromDateTo = TypeAdapter(List[SettlementListElement])
OP_GetListByMaturityDateByContractorCodeDateFromDateTo = build_typed_operation(method='GET', path='/api/Settlements/Filter/ByMaturityDate', adapter=_ADAPTER_GetListByMaturityDateByContractorCodeDateFromDateTo)
OP_GetListByMaturityDateByContractorCodeDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/ByMaturityDate')

_ADAPTER_GetNotSettled = TypeAdapter(List[SettlementListElement])
OP_GetNotSettled = build_typed_operation(method='GET', path='/api/Settlements/Filter/NotSettled', adapter=_ADAPTER_GetNotSettled)
OP_GetNotSettled_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/NotSettled')

_ADAPTER_GetNotSettledByIssueDate = TypeAdapter(List[SettlementListElement])
OP_GetNotSettledByIssueDate = build_typed_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByIssueDate', adapter=_ADAPTER_GetNotSettledByIssueDate)
OP_GetNotSettledByIssueDate_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByIssueDate')

OP_GetNotSettledByIssueDateByContractorIdDateFromDateTo = build_none_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByIssueDate')
OP_GetNotSettledByIssueDateByContractorIdDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByIssueDate')

OP_GetNotSettledByIssueDateByContractorCodeDateFromDateTo = build_none_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByIssueDate')
OP_GetNotSettledByIssueDateByContractorCodeDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByIssueDate')

_ADAPTER_GetNotSettledByMaturityDate = TypeAdapter(List[SettlementListElement])
OP_GetNotSettledByMaturityDate = build_typed_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByMaturityDate', adapter=_ADAPTER_GetNotSettledByMaturityDate)
OP_GetNotSettledByMaturityDate_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByMaturityDate')

_ADAPTER_GetNotSettledByMaturityDateByContractorIdDateFromDateTo = TypeAdapter(List[SettlementListElement])
OP_GetNotSettledByMaturityDateByContractorIdDateFromDateTo = build_typed_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByMaturityDate', adapter=_ADAPTER_GetNotSettledByMaturityDateByContractorIdDateFromDateTo)
OP_GetNotSettledByMaturityDateByContractorIdDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByMaturityDate')

_ADAPTER_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo = TypeAdapter(List[SettlementListElement])
OP_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo = build_typed_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByMaturityDate', adapter=_ADAPTER_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo)
OP_GetNotSettledByMaturityDateByContractorCodeDateFromDateTo_RAW = build_raw_operation(method='GET', path='/api/Settlements/Filter/NotSettled/ByMaturityDate')

_ADAPTER_Issue = TypeAdapter(Settlement)
OP_Issue = build_typed_operation(method='POST', path='/api/Settlements/Issue', adapter=_ADAPTER_Issue)
OP_Issue_RAW = build_raw_operation(method='POST', path='/api/Settlements/Issue')
