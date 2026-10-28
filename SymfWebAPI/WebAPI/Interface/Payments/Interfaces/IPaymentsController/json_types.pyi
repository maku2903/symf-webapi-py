from __future__ import annotations

from typing import Any, TypedDict

class DocumentTypeJSON(TypedDict):
    Id: int
    Code: str
    Name: str
    Active: bool
    JPKDocumentKind: Any
    JPK_V7Attributes: Any
    Character: Any
    CorrectionTypeId: int | None
    CorrectionSerieId: int | None
    RelatedTypeId: int | None
    RelatedSerieId: int | None
    DefaultDateRegister: int | None
    IsIssuedByBuyer: bool
    IsThirdPartyContractorEnabled: bool
    SelfTaxation: int
    IdRejestr: int

class DocumentSeriesJSON(TypedDict):
    Id: int
    Code: str

class PDFJSON(TypedDict):
    Hash_SHA1: str
    ContentFile_Base64: str
    CreateDate: str

class PageJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[Any]

class PaymentJSON(TypedDict):
    Id: int
    DocumentNumber: str
    Active: bool
    Canceled: Any
    Buffer: bool
    Settled: bool
    IssueDate: str | None
    MaturityDate: str | None
    SettlementDate: str | None
    TypeCode: str
    Series: str
    NumberInSeries: int
    IssuerId: int
    SubjectId: int | None
    ReceivingPaymentRegistryId: int | None
    Description: str
    Currency: str
    CurrencyRate: float | int
    TotalValue: float | int
    SettledValue: float | int
    SettledValuePLN: float | int
    PaymentRegistryId: int
    PaymentType: Any
    SubjectType: Any
    Positions: list[PaymentPositionJSON]

class PaymentListElementJSON(TypedDict):
    Id: int
    DocumentNumber: str
    SubjectId: int | None
    ReceivingPaymentRegistryId: int | None
    PaymentRegistryId: int | None
    IssueDate: str | None
    MaturityDate: str | None
    SettlementDate: str | None
    PaymentType: Any
    SubjectType: Any
    Currency: str
    CurrencyRate: float | int
    TotalValue: float | int
    SettledValue: float | int
    SettledValuePLN: float | int

class PaymentPositionJSON(TypedDict):
    Id: int
    DocumentNumber: str
    ValuePLN: float | int
    ValueSettlement: float | int
    ValuePayment: float | int
    CurrencyRateSettlement: float | int
    CurrencyRatePayment: float | int

class GetPagedDocumentJSON(TypedDict):
    NextPage: str | None
    PreviousPage: str | None
    PageNumber: int
    LimitPerPage: int
    TotalItems: int
    OrderBy: Any
    Data: list[PaymentListElementJSON]
