from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCurrencyRateType,
    enumDocumentSource,
    enumFKSplitPaymentType,
    enumJPK_V7DocumentAttribute,
    enumKSeFInvoiceStatus,
)
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels import (
    DocumentMessage,
    DocumentRecord,
    DocumentRelation,
    DocumentSettlement,
    DocumentTransaction,
    DocumentVatRegister,
    DocumentVatRegisterCurrency,
)
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Issue.Custom import (
    DocumentRelationIssue,
    DocumentVatRegisterCurrencyIssue,
)

class CustomDocumentIssueV2026_1Request(BaseModel):
    BuyerOrSellerContractorPosition: Optional[int]
    DocumentNumber: str
    YearId: int
    TypeCode: str
    Content: str
    IssueDate: datetime
    DocumentDate: Optional[datetime]
    PeriodDate: Optional[datetime]
    OperationDate: Optional[datetime]
    ReceiptDate: Optional[datetime]
    ClearanceDate: Optional[datetime]
    ContractorPosition: Optional[int]
    Currency: str
    CurrencyRate: Optional[Decimal]
    CurrencyRateTableId: Optional[int]
    CurrencyRateType: Optional["enumCurrencyRateType"]
    Marker: Optional[int]
    SplitPaymentType: Optional["enumFKSplitPaymentType"]
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Value: Optional[Decimal]
    ValuePLN: Optional[Decimal]
    ValueParallel: Optional[Decimal]
    ValueOffVatRegistry: Optional[Decimal]
    OpeningBalance: Optional[Decimal]
    RecordsBalance: Optional[Decimal]
    eArchiveId: Optional[str]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    Records: List["FKF_Documents_ViewModels_Issue_Simple_DocumentRecordIssue"]
    Settlements: List["FKF_Documents_ViewModels_Issue_Simple_DocumentSettlementIssue"]
    Transactions: List["FKF_Documents_ViewModels_Issue_Simple_DocumentTransactionIssue"]
    VatRegisters: List["FKF_Documents_ViewModels_Issue_SaleInvoice_DocumentVatRegisterIssue"]
    CurrencyVAT: "DocumentVatRegisterCurrencyIssue"
    CurrencyCIT_PIT: "DocumentVatRegisterCurrencyIssue"
    Relations: List["DocumentRelationIssue"]
    Features: List[int]
    IsSmeProcedure: bool

class DocumentV2026_1Response(BaseModel):
    BuyerOrSellerContractorPosition: Optional[int]
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
    NumberKSeF: str
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

class PurchaseDocumentIssueV2026_1Request(BaseModel):
    BuyerOrSellerContractorPosition: Optional[int]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    DocumentNumber: str
    YearId: int
    TypeCode: str
    Content: str
    IssueDate: datetime
    DocumentDate: Optional[datetime]
    PeriodDate: Optional[datetime]
    OperationDate: Optional[datetime]
    ReceiptDate: Optional[datetime]
    ContractorPosition: int
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateTableId: int
    CurrencyRateType: "enumCurrencyRateType"
    Marker: int
    SplitPaymentType: "enumFKSplitPaymentType"
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Records: List["FKF_Documents_ViewModels_Issue_Simple_DocumentRecordIssue"]
    Settlements: List["FKF_Documents_ViewModels_Issue_Simple_DocumentSettlementIssue"]
    Transactions: List["FKF_Documents_ViewModels_Issue_Simple_DocumentTransactionIssue"]
    VatRegisters: List["FKF_Documents_ViewModels_Issue_SaleInvoice_DocumentVatRegisterIssue"]
    Features: List[int]
    IsSmeProcedure: bool

class SaleDocumentIssueV2026_1Request(BaseModel):
    BuyerOrSellerContractorPosition: Optional[int]
    NumberKSeF: str
    IssueDateKSeF: Optional[datetime]
    DocumentNumber: str
    YearId: int
    TypeCode: str
    Content: str
    IssueDate: datetime
    DocumentDate: Optional[datetime]
    PeriodDate: Optional[datetime]
    OperationDate: Optional[datetime]
    ReceiptDate: Optional[datetime]
    ContractorPosition: int
    Currency: str
    CurrencyRate: Decimal
    CurrencyRateTableId: int
    CurrencyRateType: "enumCurrencyRateType"
    Marker: int
    SplitPaymentType: "enumFKSplitPaymentType"
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Records: List["FKF_Documents_ViewModels_Issue_Simple_DocumentRecordIssue"]
    Settlements: List["FKF_Documents_ViewModels_Issue_Simple_DocumentSettlementIssue"]
    Transactions: List["FKF_Documents_ViewModels_Issue_Simple_DocumentTransactionIssue"]
    VatRegisters: List["FKF_Documents_ViewModels_Issue_SaleInvoice_DocumentVatRegisterIssue"]
    Features: List[int]
    IsSmeProcedure: bool
