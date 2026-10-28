"""Auto-generated package (lazy imports)."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = ("AccountsChart", "Calculations", "Common", "Contractors", "Dimensions", "Documents", "Employees",)

def __getattr__(name: str):
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(__all__) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import AccountsChart as _AccountsChart
    from . import Calculations as _Calculations
    from . import Common as _Common
    from . import Contractors as _Contractors
    from . import Dimensions as _Dimensions
    from . import Documents as _Documents
    from . import Employees as _Employees
