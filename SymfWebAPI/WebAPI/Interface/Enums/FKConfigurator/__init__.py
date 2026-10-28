from __future__ import annotations

from SymfWebAPI.enums import ForwardCompatibleEnum

class AccountBalanceTurnoverType(ForwardCompatibleEnum):
    Balance = 0
    TurnoverDebit = 1
    TurnoverCredit = 2

class DictionaryElementType(ForwardCompatibleEnum):
    Record = 0
    RecordOrDimension = 1
    Dimension = 2

class DictionaryType(ForwardCompatibleEnum):
    ProductType = 1
    Product = 2
    ContractorType = 3
    Contractor = 4
    Department = 5
    CostType = 6
    A01 = 101
    A02 = 102
    A03 = 103
    A04 = 104
    A05 = 105
    A06 = 106
    A07 = 107
    A08 = 108
    A09 = 109
    A10 = 110
    A11 = 111
    A12 = 112
    A13 = 113
    A14 = 114
    A15 = 115
    A16 = 116
    A17 = 117
    A18 = 118
    A19 = 119
    A20 = 120
