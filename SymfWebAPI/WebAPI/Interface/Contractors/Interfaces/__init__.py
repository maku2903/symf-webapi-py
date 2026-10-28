"""Auto-generated package (lazy imports)."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = ("IContractorCardIndexController", "IContractorDeliveryAddressesController", "IContractorDimensions2Controller", "IContractorDimensionsController", "IContractorsController",)

def __getattr__(name: str):
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(__all__) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import IContractorCardIndexController as _IContractorCardIndexController
    from . import IContractorDeliveryAddressesController as _IContractorDeliveryAddressesController
    from . import IContractorDimensions2Controller as _IContractorDimensions2Controller
    from . import IContractorDimensionsController as _IContractorDimensionsController
    from . import IContractorsController as _IContractorsController
