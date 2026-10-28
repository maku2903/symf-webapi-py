from __future__ import annotations

from SymfWebAPI.enums import ForwardCompatibleEnum

class FiscalCommunicationInterfaceStatus(ForwardCompatibleEnum):
    TransactionResourcesFree = 0
    TransactionResourcesBusyByPC1 = 1
    TransactionResourcesBusyByPC2 = 2
    TransactionResourcesBusyBySystem = 3

class FiscalDeviceStatus(ForwardCompatibleEnum):
    Ready = 0
    InMenu = 1
    WaitingForKey = 2
    WaitingForUser = 3

class enumAccountingSchemePositionType(ForwardCompatibleEnum):
    Basic = 0
    Additional01 = 1
    Additional02 = 2
    Additional03 = 3
    Additional04 = 4
    Additional05 = 5
    Additional06 = 6
    Additional07 = 7
    Additional08 = 8
    Additional09 = 9
    Additional10 = 10

class enumCalculationState(ForwardCompatibleEnum):
    All = 0
    Settled = 1
    NotSettled = 2
    NotSettledBeforeMaturityTerm = 3
    NotSettledAfterMaturityTerm = 4
    NotSettledWithoutMaturityTerm = 5

class enumCalculationType(ForwardCompatibleEnum):
    Due = 0
    Obligation = 1
    All = 3

class enumCancelationType(ForwardCompatibleEnum):
    Other = 0
    Standard = 1
    ImportedFromArchive = 2
    CanceledReceipt = 3

class enumContractorSplitPayment(ForwardCompatibleEnum):
    VALUE_0 = 0
    Blocked = 1
    Required = 2

class enumContractorType(ForwardCompatibleEnum):
    Firm = 0
    PersonFirm = 1
    Person = 2

class enumCurrencyRateType(ForwardCompatibleEnum):
    WithoutCurrency = 0
    Purchase = 1
    Sale = 2
    Mean = 3

class enumDefaultUnitOfMeasurementKind(ForwardCompatibleEnum):
    VALUE_0 = 0
    Record = 1
    Additional1 = 2
    Additional2 = 3

class enumDocumentCharacter(ForwardCompatibleEnum):
    ZMO = 86
    ZWO = 103
    ZMW = 87
    ZWW = 104
    NAL = 58
    ZOB = 59
    KP = 60
    KW = 61
    BP = 62
    BW = 63
    IP = 64
    IW = 65
    TRPlus = 66
    TRMinus = 67
    RK = 110
    FVZ = 68
    RUZ = 70
    DIM = 72
    ZRZ = 97
    FVR = 99
    FVM = 106
    WNT = 115
    FWZ = 138
    FZK = 69
    FWZK = 139
    RKZ = 71
    DMK = 73
    ZRK = 98
    FRK = 100
    FMK = 107
    WNK = 121
    DEX = 46
    PAR = 50
    SRS = 79
    RUS = 42
    REX = 126
    FVSM = 124
    FVS = 40
    FVW = 101
    SKO = 134
    SKW = 150
    WDT = 114
    RO = 154
    RKO = 155
    SZA = 136
    SZW = 152
    NZZ = 159
    NZZK = 160
    NZW = 157
    NZWK = 158
    DXK = 45
    PRK = 51
    SRK = 80
    RKS = 43
    RXK = 127
    FVMK = 125
    FKS = 41
    FKW = 102
    SKK = 135
    SKWK = 151
    WKS = 118
    WDTK = 120
    PWM = 91
    PW = 74
    RW = 76
    WZ = 78
    PZ = 89
    MMPlus = 82
    MMMinus = 84
    PWK = 75
    RWK = 77
    WZK = 88
    MKPlus = 83
    MKMinus = 85
    PZK = 81
    KWM = 90
    FZS = 108
    ZKS = 112
    FZZ = 128
    ZKZ = 113
    KZS = 109
    ZSK = 122
    KZZ = 111
    ZZK = 123
    FWS = 116
    FWEZ = 117
    WKZ = 119
    WDP = 129
    WPK = 130
    PZP = 131
    PPK = 132
    LP = 156

class enumDocumentReservationType(ForwardCompatibleEnum):
    VALUE_0 = 0
    Qunatity = 1
    IndicationDelivery = 2

class enumDocumentSource(ForwardCompatibleEnum):
    AccountingBooks = 0
    Buffer = 1
    Schemes = 2

class enumDocumentStatus(ForwardCompatibleEnum):
    Other = 0
    New = 4
    Partial = 8
    Realized = 16
    Closed = 32

class enumFKDocumentCharacter(ForwardCompatibleEnum):
    DP = 1
    FVZ = 2
    FVS = 3
    RUZ = 4
    RUS = 5
    RK = 6
    RK_Old = 7
    DEX = 8
    DIM = 9
    FKZ = 10
    FKS = 11
    RKZ = 12
    RKS = 13
    WB = 14
    RZL = 15
    FWN = 16
    WNT = 17
    WDT = 18
    PWN = 19
    FWV = 20
    RKW = 21
    FWZ = 22
    FWS = 23
    KFWZ = 24
    KFWS = 25
    DS = 26
    WBW = 27

class enumFKDocumentMessageType(ForwardCompatibleEnum):
    Comments = 0
    Warning = 1
    Error = 2

class enumFKSplitPaymentType(ForwardCompatibleEnum):
    VALUE_0 = 0
    SplitPayment = 1
    VoluntarySplitPayment = 3
    TaxPayerRegister = 4
    TaxPayerRegister_SplitPayment = 5
    TaxPayerRegister_VoluntarySplitPayment = 7

class enumFilterCriteriaMode(ForwardCompatibleEnum):
    Within = 0
    StartsWith = 1

class enumFilterSqlCriteriaMode(ForwardCompatibleEnum):
    Within = 0
    Equals = 1
    Like = 2

class enumFiscalizationStatus(ForwardCompatibleEnum):
    NonFiscal = 0
    ToFiscalization = 1
    Fiscializated = 2

class enumIncrementalSyncModifyType(ForwardCompatibleEnum):
    InsertOrUpdate = 1
    Delete = 2

class enumIndividualDiscountSubjectType(ForwardCompatibleEnum):
    Contractor = 0
    ContractorKind = 1
    Product = 2
    ProductKind = 3

class enumJPKDocumentKind(ForwardCompatibleEnum):
    VALUE_0 = 0
    VAT = 1
    KOREKTA = 2
    ZAL = 3
    PZ = 21
    WZ = 22
    RW = 23
    MM = 24

class enumJPK_V7DocumentAttribute(ForwardCompatibleEnum):
    VALUE_0 = 0
    RO = 1
    WEW = 2
    FP = 4
    MK = 8
    VAT_RR = 16
    SW = 32
    EE = 64
    TP = 128
    TT_WNT = 256
    TT_D = 512
    MR_T = 1024
    MR_UZ = 2048
    I_42 = 4096
    I_63 = 8192
    B_SPV = 16384
    B_SPV_DOSTAWA = 32768
    B_MPV_PROWIZJA = 65536
    MPP = 131072
    IMP = 262144
    IED = 524288
    WSTO_EE = 1048576
    BFK = 2097152
    DI = 4194304
    OFF = 8388608

class enumJPK_V7ProductGroup(ForwardCompatibleEnum):
    VALUE_0 = 0
    GTU_01 = 1
    GTU_02 = 2
    GTU_03 = 4
    GTU_04 = 8
    GTU_05 = 16
    GTU_06 = 32
    GTU_07 = 64
    GTU_08 = 128
    GTU_09 = 256
    GTU_10 = 512
    GTU_11 = 1024
    GTU_12 = 2048
    GTU_13 = 4096

class enumKSeFInvoiceStatus(ForwardCompatibleEnum):
    NOT_KSEF_FORMAT = 0
    WAITING_TO_BE_SENT_TO_KSEF_MODULE = 10
    ERROR_SENDING_TO_KSEF_MODULE = 20
    SENDING = 25
    NOT_SENT_TO_KSEF = 30
    ERROR = 40
    PENDING_FOR_VALIDATION_BY_KSEF = 50
    APPROVED_BY_KSEF = 60
    REJECTED_BY_KSEF = 70

class enumManualSettledState(ForwardCompatibleEnum):
    Automatic = 0
    Manual_NotSettled = 1
    Manual_Settled = 2

class enumOrderByType(ForwardCompatibleEnum):
    Desc = 0
    Asc = 1

class enumOssDeliveryKind(ForwardCompatibleEnum):
    Product = 1
    Service = 2

class enumParallelType(ForwardCompatibleEnum):
    Undefined = 0
    Parallel = 1
    StandardWithOnRequestParallel = 2
    StandardWithAutomaticParallel = 4
    ParallelOnDebit = 8
    ParallelOnCredit = 16
    OnRequestParallel = 32
    StuckParallel = 64

class enumPaymentRegistryType(ForwardCompatibleEnum):
    Cash = 0
    Bank = 1
    Other = 2

class enumPaymentSubjectType(ForwardCompatibleEnum):
    Contractor = 0
    PaymentRegistry = 104
    Employee = 106
    Office = 107

class enumPaymentType(ForwardCompatibleEnum):
    Income = 0
    Expenditure = 1

class enumPhotoQuality(ForwardCompatibleEnum):
    Original = 0
    Medium = 1
    Low = 2

class enumPriceCalculationMethod(ForwardCompatibleEnum):
    Handel = 0
    Algorithm = 1

class enumPriceFactorType(ForwardCompatibleEnum):
    Discount = 0
    Price = 1

class enumPriceKind(ForwardCompatibleEnum):
    Undefined = 0
    Gross = 1
    Net = 2

class enumPriceListConnectionType(ForwardCompatibleEnum):
    Individual = 1
    LinkedWithCardIndexAndIndividualDiscounts = 2
    LinkedWithCardIndexAndIndividualDiscountsAndOtherPriceLists = 3

class enumPriceParameter(ForwardCompatibleEnum):
    Profit = 1
    Markup = 2

class enumPriceRecalculateType(ForwardCompatibleEnum):
    PurchasePriceAndBasePriceAreNotAgreed = 0
    AutomaticallyAtEveryPurchasePriceChange = 1
    AutomaticallyWhenPurchasePriceIsHigherThanBasePrice = 2
    ManuallyAtEveryPurchasePriceChange = 3
    ManuallyWhenPurchasePriceIsHigherThanBasePrice = 4

class enumPriceRounding(ForwardCompatibleEnum):
    _0_0001 = 6
    _0_001 = 5
    _0_01 = 0
    _0_10 = 1
    _1_00 = 2
    _10_00 = 3
    _100_00 = 4

class enumPriceType(ForwardCompatibleEnum):
    Undefined = 0
    PriceA = 1
    PriceB = 2
    PriceC = 3
    PriceD = 4
    Price_Individual = 5
    Price_Purchase = 6
    Price_Purchase_In_Currency = 7
    Price_Base = 8
    Other = 9
    Duty = 10
    Excise = 11
    Quantitative_Discount = 12
    Sale_Currency_Exchange_Rate = 13
    Purchase_Currency_Exchange_Rate = 14
    Contractor_Discount = 15
    PriceE = 16
    PriceF = 17
    PriceG = 18
    PriceH = 19
    PriceI = 20
    PriceJ = 21
    PriceK = 22
    PriceL = 23
    PriceM = 24
    PriceN = 25
    PriceO = 26
    PriceP = 27
    PriceQ = 28
    PriceR = 29
    PriceS = 30
    PriceT = 31

class enumPrintParameterDocumentStatus(ForwardCompatibleEnum):
    Automatic = 0
    Original = 1
    Copy = 2
    Original_Copy = 3
    Empty = 4
    Custom = 5

class enumPrintParameterNotSettledDocuments(ForwardCompatibleEnum):
    DoNotPrint = 0
    PrintForIssueDate = 1
    PrintForPrintDate = 2

class enumPrintParameterOperationDateFormat(ForwardCompatibleEnum):
    OperationDate = 0
    OperationPeriod = 1

class enumProductType(ForwardCompatibleEnum):
    Article = 0
    Service = 1
    Kit = 2
    Set = 3
    ServiceProfit = 4

class enumRDFStatus(ForwardCompatibleEnum):
    NoInvoice = 0
    InvoiceNotPrinted = 1
    InvoicePrinted = 2

class enumRecordDecsriptionKind(ForwardCompatibleEnum):
    FromDocument = 0
    FromRecord = 1
    FromFirstRecord = 2

class enumRepXPrintLocation(ForwardCompatibleEnum):
    Document = 1
    CardIndex = 2

class enumRepXReportText(ForwardCompatibleEnum):
    Empty = 0
    Original = 1
    Copy = 2
    Original_Copy = 3
    Duplicate = 4

class enumReservationDocumentType(ForwardCompatibleEnum):
    Unknown = 0
    SaleDocument = 16
    WarehouseDocument = 33
    ForeignOrder = 45

class enumReservationKind(ForwardCompatibleEnum):
    FIFO_IndicationDelivery = 0
    FIFO_Quantity = 1
    LIFO_IndicationDelivery = 2
    LIFO_Quantity = 3

class enumReservationMode(ForwardCompatibleEnum):
    MadeByUser = 1
    MadeByProgram = 2

class enumReservationPositionType(ForwardCompatibleEnum):
    Unknown = 0
    SaleDocument = 18
    WarehouseDocument = 37
    ForeignOrder = 30

class enumReservationType(ForwardCompatibleEnum):
    Manual = 1
    Automatic = 2

class enumSalePriceType(ForwardCompatibleEnum):
    Undefined = 0
    PriceA = 1
    PriceB = 2
    PriceC = 3
    PriceD = 4
    PriceE = 16
    PriceF = 17
    PriceG = 18
    PriceH = 19
    PriceI = 20
    PriceJ = 21
    PriceK = 22
    PriceL = 23
    PriceM = 24
    PriceN = 25
    PriceO = 26
    PriceP = 27
    PriceQ = 28
    PriceR = 29
    PriceS = 30
    PriceT = 31

class enumSettlementMethod(ForwardCompatibleEnum):
    FIFO = 0
    LIFO = 1

class enumSettlementType(ForwardCompatibleEnum):
    Due = 0
    Obligation = 1

class enumSideType(ForwardCompatibleEnum):
    Debit = 0
    Credit = 1

class enumSplitOpposingAccountType(ForwardCompatibleEnum):
    Debit_SplitInCreaditWithMultipleOpposingAccounts = 99
    Debit_SplitInDebitWithSingleOpposingAccount = 101
    Debit_WithoutSplitWithSingleOpposingAccount = 103
    Credit_SplitInDebitWithMultipleOpposingAccounts = 199
    Credit_SplitInCreditWithSingleOpposingAccount = 201
    Credit_WithoutSplitWithSingleOpposingAccount = 203

class enumSplitType(ForwardCompatibleEnum):
    VALUE_0 = 0
    SplitInDebit = 1
    SplitInCredit = 2

class enumSplitValueType(ForwardCompatibleEnum):
    Value = 0
    Percent = 1

class enumSubjectType(ForwardCompatibleEnum):
    Empty_Null = -1
    Other = 0
    Employees = 1
    Contractors = 2
    Accounts = 3
    Offices = 4
    Currencies = 5
    IncidentalContractors = 8
    Countries = 9
    Dictionaries = 99

class enumTransactionInterestType(ForwardCompatibleEnum):
    VALUE_0 = 0
    Statutory = 1
    FixedRate = 2

class enumVatRateType(ForwardCompatibleEnum):
    Unknown = -1
    Other = 0
    Zero = 3
    Exempt = 4
    NoSubjectTo = 5
    Basic = 10
    Reduced11 = 11
    Reduced12 = 12
    SuperReduced = 13
    Intermediate = 14

class enumVatRegisterKind(ForwardCompatibleEnum):
    Purchase_Standard = 100
    Purchase_FixedAssets = 101
    Purchase_Special1 = 102
    Purchase_Special2 = 103
    Purchase_NonDeductibleVat = 104
    Purchase_LowerVat = 106
    Purchase_HigherVat = 107
    Sale_Standard = 200
    Sale_WithCustomizablePeriod = 210
    Sale_ProductDeliveryWhereBuyerIsTaxPayer = 203
    Sale_NonDeductibleVat = 204
    Sale_ProductDeliveryAndServiceOutsideOfCountry = 205
    Sale_LowerVat = 206
    Sale_HigherVat = 207
    Import_Standard = 300
    Import_FixedAssets = 301
    Import_Service = 302
    Import_ProductDeliveryWhereBuyerIsTaxPayer = 303
    Import_ProductDeliveryWithSimplifiedCustomProcedure = 304
    Export_Standard = 400
    Export_NonDeductibleVat = 404
    Export_ProductDeliveryAndServiceOutsideOfCountry = 405

class enumVatRegisterPeriodType(ForwardCompatibleEnum):
    SpecificPeriod = 0
    Pending = 1
    PeriodSetByPayment = 2
    PeriodSetByMaturityTerm = 3

class enumVatRegisterType(ForwardCompatibleEnum):
    Purchase = 1
    Sale = 2
    Import = 3
    Export = 4

class enumVatRegisterTypeABCD(ForwardCompatibleEnum):
    A = 1
    B = 2
    C = 3
    D = 4

class enumYearClosingStatus(ForwardCompatibleEnum):
    Active = 0
    Closed = 1
    Aprroved = 2
