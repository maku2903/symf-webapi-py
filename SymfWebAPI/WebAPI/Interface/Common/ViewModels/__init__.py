from __future__ import annotations

from pydantic import BaseModel

from typing import Any, List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import (
    enumDocumentCharacter,
    enumIncrementalSyncModifyType,
    enumJPKDocumentKind,
    enumJPK_V7DocumentAttribute,
    enumPaymentRegistryType,
    enumPriceKind,
    enumPriceType,
    enumPrintParameterDocumentStatus,
    enumPrintParameterNotSettledDocuments,
    enumPrintParameterOperationDateFormat,
    enumVatRateType,
)

class AgriculturalPromotionFund(BaseModel):
    Code: str
    Active: bool
    Rate: Decimal
    AccountFK: str

class CNCode(BaseModel):
    Id: int
    Name: str
    Description: str
    Active: bool

class CharacterRelation(BaseModel):
    Character: "enumDocumentCharacter"
    Corrections: List["enumDocumentCharacter"]
    Related: List["enumDocumentCharacter"]

class Common_ViewModels_Catalog(BaseModel):
    Id: int
    ParentId: int
    Name: str
    FullPath: str
Catalog = Common_ViewModels_Catalog

class Common_ViewModels_Country(BaseModel):
    Id: int
    Name: str
    Code: str
    Active: bool
Country = Common_ViewModels_Country

class Common_ViewModels_Currency(BaseModel):
    Id: int
    Shortcut: str
    Name: str
    Active: bool
Currency = Common_ViewModels_Currency

class Common_ViewModels_Dimension(BaseModel):
    Name: str
    Code: str
    Value: Optional[str]
    DictionaryValue: Optional[str]
    Type: str
Dimension = Common_ViewModels_Dimension

class Common_ViewModels_DimensionClassification(BaseModel):
    Id: int
    Name: str
    Code: str
    Type: str
    DictionaryId: Optional[int]
    Index: Optional[int]
DimensionClassification = Common_ViewModels_DimensionClassification

class Common_ViewModels_DocumentType(BaseModel):
    Id: int
    Code: str
    Name: str
    Active: bool
    JPKDocumentKind: "enumJPKDocumentKind"
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    Character: "enumDocumentCharacter"
    CorrectionTypeId: Optional[int]
    CorrectionSerieId: Optional[int]
    RelatedTypeId: Optional[int]
    RelatedSerieId: Optional[int]
    DefaultDateRegister: Optional[int]
    IsIssuedByBuyer: bool
    IsThirdPartyContractorEnabled: bool
    SelfTaxation: int
    IdRejestr: int
DocumentType = Common_ViewModels_DocumentType

class Common_ViewModels_Marker(BaseModel):
    Subtype: int
    Name: str
    Active: bool
Marker = Common_ViewModels_Marker

class Common_ViewModels_Region(BaseModel):
    Id: int
    Name: str
    Description: str
    Active: bool
Region = Common_ViewModels_Region

class Common_ViewModels_VatRate(BaseModel):
    Description: str
    Value: Decimal
    Active: bool
    DateTo: Optional[datetime]
    DateFrom: Optional[datetime]
    Type: "enumVatRateType"
    Fiscal: bool
    RR: bool
    Id: Optional[int]
    Code: str
VatRate = Common_ViewModels_VatRate

class CurrencyRate(BaseModel):
    CurrencyId: int
    Date: datetime
    Rate: Decimal

class Department(BaseModel):
    Id: int
    Name: str
    Code: str

class DocumentAddress(BaseModel):
    Name: Optional[str]
    NIP: Optional[str]
    City: Optional[str]
    PostCode: Optional[str]
    Street: Optional[str]
    HouseNo: Optional[str]
    ApartmentNo: Optional[str]
    CountryId: Optional[int]

class DocumentSeries(BaseModel):
    Id: int
    Code: str

class FilterDimensionCriteria(BaseModel):
    Id: Optional[int]
    Code: str
    Value: Optional[str]
    DictionaryValue: str

class FilterDocumentType(BaseModel):
    DocumentTypes: List[str]

class IncrementalSyncListElement_1(BaseModel):
    Id: int
    ModifyType: "enumIncrementalSyncModifyType"
    ModifiedAt: datetime
    Object: Any
IncrementalSyncListElement = IncrementalSyncListElement_1

class Kind(BaseModel):
    Id: Optional[int]
    Code: str
    Active: bool

class PDF(BaseModel):
    Hash_SHA1: str
    ContentFile_Base64: str
    CreateDate: datetime

class PDFDimensionSetting(BaseModel):
    Code: str
    PrintLabel: bool

class PDFSettings(BaseModel):
    PrintNote: bool
    PrintRemarks: bool
    PrintFooter: bool
    PrintExecutiveSubject: bool
    OperationDateFormat: "enumPrintParameterOperationDateFormat"
    DocumentStatus: "enumPrintParameterDocumentStatus"
    NotSettledDocuments: "enumPrintParameterNotSettledDocuments"
    DocumentStatusText: str
    IncludedDimensions: List["PDFDimensionSetting"]
    PrintLeftToPay: bool
    PrintReceiptNumber: bool
    PrintDiscountColumns: bool
    MainSubjectAddressDimensionCode: str
    MainSubjectNameDimensionCode: str
    ExecutiveSubjectAddressDimensionCode: str
    ExecutiveSubjectNameDimensionCode: str
    PositionDescriptionDimensionCode: str

class PKWiUCode(BaseModel):
    Id: int
    Name: str
    Description: str
    Active: bool

class PaymentForm(BaseModel):
    Name: str
    Days: int
    Type: "enumPaymentRegistryType"
    Active: bool
    Id: Optional[int]
    Client: int

class PaymentFormBase(BaseModel):
    Id: Optional[int]
    Client: int

class PaymentRegistry(BaseModel):
    Name: str
    Type: "enumPaymentRegistryType"
    DefaultPaymentFormId: Optional[int]
    BankName: Optional[str]
    BankAccountId: int
    Id: Optional[int]
    Code: str
    AccountNumber: Optional[str]

class PaymentRegistryBase(BaseModel):
    Id: Optional[int]
    Code: str
    AccountNumber: Optional[str]

class PositionDimension(BaseModel):
    PositionId: int
    Dimensions: List["Dimension"]

class PriceType(BaseModel):
    Type: "enumPriceType"
    Code: str
    Name: str
    Kind: "enumPriceKind"
    Active: bool

class RelatedDocumentPosition(BaseModel):
    Id: int
    No: int
    Quantity: Decimal
    NetValuePLN: Decimal
    DocumentId: int
    DocumentNumber: str
    QuantityCorrected: Decimal
    NetValuePLNCorrected: Decimal

class UnitOfMeasurement(BaseModel):
    Id: int
    Name: str
    Description: str
    Active: bool

class UnitOfMeasurementDefinition(BaseModel):
    Guid: str
    Name: str
    No: int

class VatRateBase(BaseModel):
    Id: Optional[int]
    Code: str

class Warehouse(BaseModel):
    Id: int
    Name: str
    Code: str
