from __future__ import annotations

from pydantic import BaseModel

from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from SymfWebAPI.WebAPI.Interface.Enums import enumDocumentSource, enumSideType

class DocumentRecordDimension(BaseModel):
    Index: int
    Value: Optional[str]

class DocumentRecordDimensionSplit(BaseModel):
    SplitValue: Decimal
    Percent: Decimal
    Dimensions: List["DocumentRecordDimension"]

class FKF_Dimensions_ViewModels_Document(BaseModel):
    Id: int
    DocumentNumber: str
    Source: "enumDocumentSource"
    YearId: int
    DocumentDate: datetime
    ContractorPosition: int
    Records: List["DocumentRecord"]
Document = FKF_Dimensions_ViewModels_Document

class FKF_Dimensions_ViewModels_DocumentRecord(BaseModel):
    Id: int
    No: int
    SplitNo: int
    Side: "enumSideType"
    Account: str
    Value: Decimal
    ValuePLN: Decimal
    Currency: str
    DimensionSplits: List["DocumentRecordDimensionSplit"]
DocumentRecord = FKF_Dimensions_ViewModels_DocumentRecord
