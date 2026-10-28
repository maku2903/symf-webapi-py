from __future__ import annotations

from pydantic import BaseModel

from typing import Any, Dict
from SymfWebAPI.WebAPI.Interface.Enums import enumRepXPrintLocation, enumRepXReportText

class PrintData(BaseModel):
    Disclaimer: str
    Footer: str
    IssuedBy: str
    ReceivedBy: str
    ReportText: "enumRepXReportText"
    ReportParameters: Dict[str, Any]

class ReportDefinition(BaseModel):
    Id: int
    IsActive: bool
    Name: str
    Location: "enumRepXPrintLocation"
