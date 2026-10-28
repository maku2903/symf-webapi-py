from __future__ import annotations

from typing import Any, TypedDict

class AccountJSON(TypedDict):
    Synthetic: int
    Analytic1: int
    Analytic2: int
    Analytic3: int
    Analytic4: int
    Analytic5: int

class DocumentMessageJSON(TypedDict):
    Type: Any
    Message: str

class DocumentRelationJSON(TypedDict):
    DocumentNumber: str
    DocumentDate: str
    DocumentId: int
    YearId: int

class DocumentSettlementJSON(TypedDict):
    Id: int
    TransactionId: int
    SettledDocument: str
    Side: Any
    Account: str
    Account_Full: AccountJSON
    Value: float | int
    ValuePLN: float | int
    Currency: str
    CurrencyRate: float | int
    CurrencyForeign: str
    CurrencyRateForeign: float | int
    ValueForeign: float | int

class DocumentTransactionJSON(TypedDict):
    Id: int
    Side: Any
    Account: str
    Account_Full: AccountJSON
    MaturityDate: str
    Advance: bool
    Value: float | int
    ValuePLN: float | int
    Currency: str
    CurrencyRate: float | int
    InterestType: Any
    InterestRate: float | int
    RKP: float | int
    BankAccountId: int | None

class DocumentVatRegisterJSON(TypedDict):
    Id: int
    DefinitionId: int
    Type: Any
    Period: str
    PeriodType: Any
    Service: bool
    UE: bool
    Chargable: bool
    VatRate: str | None
    GrossValue: float | int
    GrossValuePLN: float | int
    NetValue: float | int
    NetValuePLN: float | int
    VatValue: float | int
    VatValuePLN: float | int
    ToPay: float | int
    Marker: int
    CorrectionNumber: str
    CorrectionDate: str
    JPK_V7ProductGroups: Any
    ContractorPosition: int
    SplitNo: int
    DocumentDate: str
    ReceiptDate: str

class DocumentVatRegisterCurrencyJSON(TypedDict):
    Currency: str
    CurrencyRate: float | int | None
    CurrencyRateTableId: int | None
    CurrencyRateTableDate: str | None

class DocumentJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Source: Any
    YearId: int
    SettlementId: int
    IssueDate: str
    DocumentDate: str
    PeriodDate: str
    OperationDate: str
    ReceiptDate: str
    TypeCode: str
    NumberInSeries: int
    Content: str
    ContractorPosition: int
    TrilateralContractorPosition: int
    Value: float | int
    ValuePLN: float | int
    ValueParallel: float | int
    ValueOffVatRegistry: float | int
    OpeningBalance: float | int
    RecordsBalance: float | int
    Currency: str
    CurrencyRate: float | int
    CurrencyRateTableId: int
    CurrencyRateType: Any
    CorrectionNumber: str
    CorrectionDate: str
    Marker: int
    SplitPaymentType: Any
    JPK_V7Attributes: Any
    ClearenceDate: str | None
    StatusKSeF: Any
    eArchiveId: str | None
    NumberKSeF: str | None
    MaturityDate: str | None
    PaymentDate: str | None
    Origin: str
    IssueDateKSeF: str | None
    Records: list[DocumentRecordJSON]
    Settlements: list[DocumentSettlementJSON]
    Transactions: list[DocumentTransactionJSON]
    VatRegisters: list[DocumentVatRegisterJSON]
    CurrencyVAT: DocumentVatRegisterCurrencyJSON
    CurrencyCIT_PIT: DocumentVatRegisterCurrencyJSON
    Features: list[int]
    FKMessages: list[DocumentMessageJSON]
    Relations: list[DocumentRelationJSON]

class DocumentRecordJSON(TypedDict):
    Id: int
    No: int
    SplitNo: int
    Account: str
    Account_Full: AccountJSON
    SplitType: Any
    SplitOpposingAccountType: Any
    ParallelType: Any
    Side: Any
    RecordVat: bool
    Description: str
    DescriptionKind: Any
    Currency: str
    CurrencyRate: float | int
    CurrencyRateTableId: int
    CurrencyRateType: Any
    DocumentNumber: str
    Value: float | int
    ValuePLN: float | int
    ReportAccount: bool
    KPKWDate: str
    Settlements: list[DocumentSettlementJSON]
    Transactions: list[DocumentTransactionJSON]
    Features: list[int]
