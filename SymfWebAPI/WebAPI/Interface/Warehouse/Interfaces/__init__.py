"""Auto-generated package (lazy imports)."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = ("IDeliveriesController", "IDeliveryDimensionsController", "IWarehouseDocumentDimensions2Controller", "IWarehouseDocumentDimensionsController", "IWarehouseDocumentsController", "IWarehouseDocumentsIssueController",)

def __getattr__(name: str):
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(__all__) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import IDeliveriesController as _IDeliveriesController
    from . import IDeliveryDimensionsController as _IDeliveryDimensionsController
    from . import IWarehouseDocumentDimensions2Controller as _IWarehouseDocumentDimensions2Controller
    from . import IWarehouseDocumentDimensionsController as _IWarehouseDocumentDimensionsController
    from . import IWarehouseDocumentsController as _IWarehouseDocumentsController
    from . import IWarehouseDocumentsIssueController as _IWarehouseDocumentsIssueController
