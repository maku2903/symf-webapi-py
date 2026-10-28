"""Auto-generated package (lazy imports)."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = ("BankAccounts", "Common", "Contractors", "Dictionaries", "Enums", "FKF", "HMF", "Interfaces", "InventoryStates", "OSS", "Orders", "OwnOrders", "Payments", "Products", "Purchases", "RepX", "Reservations", "Sales", "ViewModels", "Warehouse",)

def __getattr__(name: str):
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(__all__) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import BankAccounts as _BankAccounts
    from . import Common as _Common
    from . import Contractors as _Contractors
    from . import Dictionaries as _Dictionaries
    from . import Enums as _Enums
    from . import FKF as _FKF
    from . import HMF as _HMF
    from . import Interfaces as _Interfaces
    from . import InventoryStates as _InventoryStates
    from . import OSS as _OSS
    from . import Orders as _Orders
    from . import OwnOrders as _OwnOrders
    from . import Payments as _Payments
    from . import Products as _Products
    from . import Purchases as _Purchases
    from . import RepX as _RepX
    from . import Reservations as _Reservations
    from . import Sales as _Sales
    from . import ViewModels as _ViewModels
    from . import Warehouse as _Warehouse
