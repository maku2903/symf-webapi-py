"""Auto-generated package (lazy imports)."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = ("IPurchasesController", "IPurchasesDimensions2Controller", "IPurchasesDimensionsController", "IPurchasesIssueController",)

def __getattr__(name: str):
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(__all__) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import IPurchasesController as _IPurchasesController
    from . import IPurchasesDimensions2Controller as _IPurchasesDimensions2Controller
    from . import IPurchasesDimensionsController as _IPurchasesDimensionsController
    from . import IPurchasesIssueController as _IPurchasesIssueController
