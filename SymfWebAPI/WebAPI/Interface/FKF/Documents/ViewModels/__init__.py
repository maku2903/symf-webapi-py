from __future__ import annotations

from pydantic import BaseModel

import importlib
from typing import TYPE_CHECKING
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCurrencyRateType,
    enumDocumentSource,
    enumFKDocumentCharacter,
    enumFKDocumentMessageType,
    enumFKSplitPaymentType,
    enumJPK_V7DocumentAttribute,
    enumJPK_V7ProductGroup,
    enumKSeFInvoiceStatus,
    enumParallelType,
    enumRecordDecsriptionKind,
    enumSideType,
    enumSplitOpposingAccountType,
    enumSplitType,
    enumTransactionInterestType,
    enumVatRegisterPeriodType,
    enumVatRegisterTypeABCD,
)
from SymfWebAPI.WebAPI.Interface.FKF.Common.ViewModels import Account

class DocumentListElement(BaseModel):
    Id: int
    DocumentNumber: str
    Source: "enumDocumentSource"
    YearId: int
    DocumentDate: Optional[datetime]
    PeriodDate: Optional[datetime]
    OperationDate: Optional[datetime]
    IssueDate: Optional[datetime]
    ReceiptDate: Optional[datetime]
    TypeCode: str
    NumberInSeries: int
    Content: str
    ContractorPosition: Optional[int]
    Value: Decimal
    ValuePLN: Decimal
    Currency: str

class DocumentMessage(BaseModel):
    Type: "enumFKDocumentMessageType"
    Message: str

class DocumentRelation(BaseModel):
    DocumentNumber: str
    DocumentDate: datetime
    DocumentId: int
    YearId: int

class DocumentSettlement(BaseModel):
    Id: int
    TransactionId: int
    SettledDocument: str
    Side: "enumSideType"
    Account: str
    Account_Full: "Account"
    Value: Decimal
    ValuePLN: Decimal
    Currency: str
    CurrencyRate: Decimal
    CurrencyForeign: str
    CurrencyRateForeign: Decimal
    ValueForeign: Decimal

class DocumentTransaction(BaseModel):
    Id: int
    Side: "enumSideType"
    Account: str
    Account_Full: "Account"
    MaturityDate: datetime
    Advance: bool
    Value: Decimal
    ValuePLN: Decimal
    Currency: str
    CurrencyRate: Decimal
    InterestType: "enumTransactionInterestType"
    InterestRate: Decimal
    RKP: Decimal
    BankAccountId: Optional[int]

class DocumentV2(BaseModel):
    Id: int
    DocumentNumber: str
    Source: "enumDocumentSource"
    YearId: int
    SettlementId: int
    IssueDate: datetime
    DocumentDate: datetime
    PeriodDate: datetime
    OperationDate: datetime
    ReceiptDate: datetime
    TypeCode: str
    NumberInSeries: int
    Content: str
    ContractorPosition: int
    TrilateralContractorPosition: int
    Value: Decimal
    ValuePLN: Decimal
    ValueParallel: Decimal
    ValueOffVatRegistry: Decimal
    OpeningBalance: Decimal
    RecordsBalance: Decimal
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateTableId: int
    CurrencyRateType: "enumCurrencyRateType"
    CorrectionNumber: str
    CorrectionDate: datetime
    Marker: int
    SplitPaymentType: "enumFKSplitPaymentType"
    JpkV7Attributes: "enumJPK_V7DocumentAttribute"
    ClearanceDate: Optional[datetime]
    StatusKSeF: "enumKSeFInvoiceStatus"
    EArchiveId: Optional[str]
    NumberKSeF: Optional[str]
    MaturityDate: Optional[datetime]
    PaymentDate: Optional[datetime]
    Origin: str
    IssueDateKSeF: Optional[datetime]
    Records: List["DocumentRecord"]
    Settlements: List["DocumentSettlement"]
    Transactions: List["DocumentTransaction"]
    VatRegisters: List["DocumentVatRegister"]
    CurrencyVAT: "DocumentVatRegisterCurrency"
    CurrencyCIT_PIT: "DocumentVatRegisterCurrency"
    Features: List[int]
    FKMessages: List["DocumentMessage"]
    Relations: List["DocumentRelation"]

class DocumentVatRegister(BaseModel):
    Id: int
    DefinitionId: int
    Type: "enumVatRegisterTypeABCD"
    Period: datetime
    PeriodType: "enumVatRegisterPeriodType"
    Service: bool
    UE: bool
    Chargable: bool
    VatRate: Optional[str]
    GrossValue: Decimal
    GrossValuePLN: Decimal
    NetValue: Decimal
    NetValuePLN: Decimal
    VatValue: Decimal
    VatValuePLN: Decimal
    ToPay: Decimal
    Marker: int
    CorrectionNumber: str
    CorrectionDate: datetime
    JPK_V7ProductGroups: "enumJPK_V7ProductGroup"
    ContractorPosition: int
    SplitNo: int
    DocumentDate: datetime
    ReceiptDate: datetime

class DocumentVatRegisterCurrency(BaseModel):
    Currency: str
    CurrencyRate: Optional[Decimal]
    CurrencyRateTableId: Optional[int]
    CurrencyRateTableDate: Optional[datetime]

class FKF_Documents_ViewModels_Document(BaseModel):
    Id: int
    DocumentNumber: str
    Source: "enumDocumentSource"
    YearId: int
    SettlementId: int
    IssueDate: datetime
    DocumentDate: datetime
    PeriodDate: datetime
    OperationDate: datetime
    ReceiptDate: datetime
    TypeCode: str
    NumberInSeries: int
    Content: str
    ContractorPosition: int
    TrilateralContractorPosition: int
    Value: Decimal
    ValuePLN: Decimal
    ValueParallel: Decimal
    ValueOffVatRegistry: Decimal
    OpeningBalance: Decimal
    RecordsBalance: Decimal
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateTableId: int
    CurrencyRateType: "enumCurrencyRateType"
    CorrectionNumber: str
    CorrectionDate: datetime
    Marker: int
    SplitPaymentType: "enumFKSplitPaymentType"
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    ClearenceDate: Optional[datetime]
    StatusKSeF: "enumKSeFInvoiceStatus"
    eArchiveId: Optional[str]
    NumberKSeF: Optional[str]
    MaturityDate: Optional[datetime]
    PaymentDate: Optional[datetime]
    Origin: str
    IssueDateKSeF: Optional[datetime]
    Records: List["DocumentRecord"]
    Settlements: List["DocumentSettlement"]
    Transactions: List["DocumentTransaction"]
    VatRegisters: List["DocumentVatRegister"]
    CurrencyVAT: "DocumentVatRegisterCurrency"
    CurrencyCIT_PIT: "DocumentVatRegisterCurrency"
    Features: List[int]
    FKMessages: List["DocumentMessage"]
    Relations: List["DocumentRelation"]
Document = FKF_Documents_ViewModels_Document

class FKF_Documents_ViewModels_DocumentRecord(BaseModel):
    Id: int
    No: int
    SplitNo: int
    Account: str
    Account_Full: "Account"
    SplitType: "enumSplitType"
    SplitOpposingAccountType: "enumSplitOpposingAccountType"
    ParallelType: "enumParallelType"
    Side: "enumSideType"
    RecordVat: bool
    Description: str
    DescriptionKind: "enumRecordDecsriptionKind"
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateTableId: int
    CurrencyRateType: "enumCurrencyRateType"
    DocumentNumber: str
    Value: Decimal
    ValuePLN: Decimal
    ReportAccount: bool
    KPKWDate: datetime
    Settlements: List["DocumentSettlement"]
    Transactions: List["DocumentTransaction"]
    Features: List[int]
DocumentRecord = FKF_Documents_ViewModels_DocumentRecord

class FKF_Documents_ViewModels_DocumentType(BaseModel):
    Id: int
    Code: str
    Name: str
    YearId: int
    Character: "enumFKDocumentCharacter"
DocumentType = FKF_Documents_ViewModels_DocumentType

class Feature(BaseModel):
    Id: int
    Name: str
    Description: str
    YearId: int
    BufferOnly: bool

_VERSIONED_CHILDREN = ['V2026_1', 'V2026_2']

_VERSIONED_EXPORTS = {
    'BusinessDocumentIssueV2026_2Request': 'V2026_2',
    'CustomDocumentIssueV2026_1Request': 'V2026_1',
    'DocumentV2026_1Response': 'V2026_1',
    'PurchaseDocumentIssueV2026_1Request': 'V2026_1',
    'SaleDocumentIssueV2026_1Request': 'V2026_1',
}

def __getattr__(name: str):
    if name in _VERSIONED_CHILDREN:
        value = importlib.import_module(f".{name}", __name__)
        globals()[name] = value
        return value
    child_name = _VERSIONED_EXPORTS.get(name)
    if child_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(f".{child_name}", __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value

def __dir__():
    return sorted(set(_VERSIONED_CHILDREN) | set(_VERSIONED_EXPORTS) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import V2026_1
    from . import V2026_2
    from .V2026_1 import CustomDocumentIssueV2026_1Request, DocumentV2026_1Response, PurchaseDocumentIssueV2026_1Request, SaleDocumentIssueV2026_1Request
    from .V2026_2 import BusinessDocumentIssueV2026_2Request
