from __future__ import annotations

from typing import Any, TypedDict

class FiscalPrinterStatusJSON(TypedDict):
    IsConnected: bool
    ChargerConnected: bool | None
    CommandQueueEmpty: bool | None
    PaperRunningOut: bool | None
    CommunicationInterfaceStatus: Any | None
    DeviceStatus: Any | None

class FiscalizationResultJSON(TypedDict):
    Success: bool
    ReceiptNumber: int | None
    FiscalDeviceNo: str
    ErrorMessage: str
