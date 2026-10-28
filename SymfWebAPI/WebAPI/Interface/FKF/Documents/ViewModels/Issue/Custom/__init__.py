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
    enumOssDeliveryKind,
    enumParallelType,
    enumRecordDecsriptionKind,
    enumSideType,
    enumTransactionInterestType,
    enumVatRegisterPeriodType,
    enumVatRegisterTypeABCD,
)
from SymfWebAPI.WebAPI.Interface.FKF.Documents.ViewModels.Issue import DocumentRecordAccountIssue

class DocumentRelationIssue(BaseModel):
    DocumentNumber: str
    DocumentDate: datetime
    ContractorPosition: int

class DocumentVatRegisterCurrencyIssue(BaseModel):
    Currency: str
    CurrencyRate: Optional[Decimal]
    CurrencyRateTableId: Optional[int]
    CurrencyRateTableDate: Optional[datetime]

class FKF_Documents_ViewModels_Issue_Custom_DocumentIssue(BaseModel):
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
    NumberKSeF: Optional[str]
    IssueDateKSeF: Optional[datetime]
    Records: List["DocumentRecordIssue"]
    Settlements: List["DocumentSettlementIssue"]
    Transactions: List["DocumentTransactionIssue"]
    VatRegisters: List["DocumentVatRegisterIssue"]
    CurrencyVAT: "DocumentVatRegisterCurrencyIssue"
    CurrencyCIT_PIT: "DocumentVatRegisterCurrencyIssue"
    Relations: List["DocumentRelationIssue"]
    Features: List[int]
    IsSmeProcedure: bool
DocumentIssue = FKF_Documents_ViewModels_Issue_Custom_DocumentIssue

class FKF_Documents_ViewModels_Issue_Custom_DocumentRecordDimensionIssue(BaseModel):
    Index: int
    Value: Optional[str]
DocumentRecordDimensionIssue = FKF_Documents_ViewModels_Issue_Custom_DocumentRecordDimensionIssue

class FKF_Documents_ViewModels_Issue_Custom_DocumentRecordDimensionSplitIssue(BaseModel):
    SplitValue: Decimal
    Dimensions: List["DocumentRecordDimensionIssue"]
DocumentRecordDimensionSplitIssue = FKF_Documents_ViewModels_Issue_Custom_DocumentRecordDimensionSplitIssue

class FKF_Documents_ViewModels_Issue_Custom_DocumentRecordIssue(BaseModel):
    No: int
    SplitNo: int
    Account: "DocumentRecordAccountIssue"
    ParallelType: Optional["enumParallelType"]
    Side: "enumSideType"
    Description: str
    DescriptionKind: Optional["enumRecordDecsriptionKind"]
    Currency: str
    CurrencyRate: Optional[Decimal]
    CurrencyRateTableId: Optional[int]
    CurrencyRateType: Optional["enumCurrencyRateType"]
    DocumentNumber: str
    Value: Optional[Decimal]
    ValuePLN: Optional[Decimal]
    ReportAccount: Optional[bool]
    KPKWDate: Optional[datetime]
    Transactions: List["DocumentTransactionIssue"]
    Settlements: List["DocumentSettlementIssue"]
    Features: List[int]
    DimensionSplits: List["DocumentRecordDimensionSplitIssue"]
DocumentRecordIssue = FKF_Documents_ViewModels_Issue_Custom_DocumentRecordIssue

class FKF_Documents_ViewModels_Issue_Custom_DocumentSettlementIssue(BaseModel):
    TransactionId: Optional[int]
    SettledDocument: str
    Value: Optional[Decimal]
    ValuePLN: Optional[Decimal]
    Currency: str
    CurrencyRate: Optional[Decimal]
    CurrencyForeign: str
    CurrencyRateForeign: Optional[Decimal]
    ValueForeign: Optional[Decimal]
DocumentSettlementIssue = FKF_Documents_ViewModels_Issue_Custom_DocumentSettlementIssue

class FKF_Documents_ViewModels_Issue_Custom_DocumentTransactionIssue(BaseModel):
    MaturityDate: Optional[datetime]
    Advance: Optional[bool]
    Value: Optional[Decimal]
    ValuePLN: Optional[Decimal]
    TransactionId: Optional[int]
    Currency: str
    CurrencyRate: Optional[Decimal]
    InterestType: Optional["enumTransactionInterestType"]
    InterestRate: Optional[Decimal]
    RKP: Optional[Decimal]
    BankAccountId: Optional[int]
    Marker: Optional[int]
DocumentTransactionIssue = FKF_Documents_ViewModels_Issue_Custom_DocumentTransactionIssue

class FKF_Documents_ViewModels_Issue_Custom_DocumentVatRegisterIssue(BaseModel):
    DefinitionId: int
    Type: Optional["enumVatRegisterTypeABCD"]
    Period: Optional[datetime]
    PeriodType: Optional["enumVatRegisterPeriodType"]
    Service: Optional[bool]
    UE: Optional[bool]
    Chargable: Optional[bool]
    VatRate: Optional[str]
    GrossValuePLN: Optional[Decimal]
    NetValuePLN: Optional[Decimal]
    VatValuePLN: Optional[Decimal]
    GrossValue: Optional[Decimal]
    NetValue: Optional[Decimal]
    VatValue: Optional[Decimal]
    Marker: Optional[int]
    JPK_V7ProductGroups: Optional["enumJPK_V7ProductGroup"]
    ContractorPosition: Optional[int]
    SplitNo: Optional[int]
    DocumentDate: Optional[datetime]
    ReceiptDate: Optional[datetime]
    OssShippingCountry: str
    OssDeliveryCountry: str
    OssDeliveryKind: Optional["enumOssDeliveryKind"]
    OssCorrectionDate: Optional[datetime]
DocumentVatRegisterIssue = FKF_Documents_ViewModels_Issue_Custom_DocumentVatRegisterIssue
