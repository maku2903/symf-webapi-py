from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumCurrencyRateType,
    enumFKSplitPaymentType,
    enumJPK_V7DocumentAttribute,
    enumJPK_V7ProductGroup,
    enumParallelType,
    enumRecordDecsriptionKind,
    enumSideType,
    enumTransactionInterestType,
    enumVatRegisterPeriodType,
    enumVatRegisterTypeABCD,
)
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Issue import DocumentRecordAccountIssue

class FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentIssue(BaseModel):
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
    Records: List["DocumentRecordIssue"]
    Settlements: List["DocumentSettlementIssue"]
    Transactions: List["DocumentTransactionIssue"]
    VatRegisters: List["DocumentVatRegisterIssue"]
    Features: List[int]
    IsSmeProcedure: bool
DocumentIssue = FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentIssue

class FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentRecordDimensionIssue(BaseModel):
    Index: int
    Value: Optional[str]
DocumentRecordDimensionIssue = FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentRecordDimensionIssue

class FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentRecordDimensionSplitIssue(BaseModel):
    SplitValue: Decimal
    Dimensions: List["DocumentRecordDimensionIssue"]
DocumentRecordDimensionSplitIssue = FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentRecordDimensionSplitIssue

class FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentRecordIssue(BaseModel):
    No: int
    SplitNo: int
    Account: "DocumentRecordAccountIssue"
    ParallelType: "enumParallelType"
    Side: "enumSideType"
    Description: str
    DescriptionKind: "enumRecordDecsriptionKind"
    Value: Decimal
    ValuePLN: Decimal
    Settlements: List["DocumentSettlementIssue"]
    Transactions: List["DocumentTransactionIssue"]
    Features: List[int]
    DimensionSplits: List["DocumentRecordDimensionSplitIssue"]
DocumentRecordIssue = FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentRecordIssue

class FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentSettlementIssue(BaseModel):
    TransactionId: Optional[int]
    SettledDocument: str
    Value: Decimal
    ValuePLN: Decimal
DocumentSettlementIssue = FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentSettlementIssue

class FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentTransactionIssue(BaseModel):
    MaturityDate: datetime
    Advance: bool
    Value: Decimal
    ValuePLN: Decimal
    InterestType: "enumTransactionInterestType"
    InterestRate: Decimal
    RKP: Decimal
DocumentTransactionIssue = FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentTransactionIssue

class FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentVatRegisterIssue(BaseModel):
    DefinitionId: int
    Type: "enumVatRegisterTypeABCD"
    Period: datetime
    PeriodType: "enumVatRegisterPeriodType"
    VatRate: Optional[str]
    GrossValuePLN: Decimal
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    Marker: int
    JPK_V7ProductGroups: Optional["enumJPK_V7ProductGroup"]
DocumentVatRegisterIssue = FKF_Documents_ViewModels_Issue_PurchaseInvoice_DocumentVatRegisterIssue
