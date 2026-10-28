"""Auto-generated package (lazy imports)."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = ("IOssContractorsController", "IOssOrderController", "IOssProductController", "IOssProductMapsController", "IOssReportsController", "IOssSaleController",)

def __getattr__(name: str):
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(__all__) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import IOssContractorsController as _IOssContractorsController
    from . import IOssOrderController as _IOssOrderController
    from . import IOssProductController as _IOssProductController
    from . import IOssProductMapsController as _IOssProductMapsController
    from . import IOssReportsController as _IOssReportsController
    from . import IOssSaleController as _IOssSaleController
