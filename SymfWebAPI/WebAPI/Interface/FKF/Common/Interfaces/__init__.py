"""Auto-generated package (lazy imports)."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = ("IFKCountriesController", "IFKCurrenciesController", "IFKCurrenciesTablesController", "IFKRegionsController", "IFKTaxOfficesController", "IFKVatRatesController", "IFKVatRegisterMarkersController", "IFKVatRegistersController", "IFKYearsController",)

def __getattr__(name: str):
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(__all__) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import IFKCountriesController as _IFKCountriesController
    from . import IFKCurrenciesController as _IFKCurrenciesController
    from . import IFKCurrenciesTablesController as _IFKCurrenciesTablesController
    from . import IFKRegionsController as _IFKRegionsController
    from . import IFKTaxOfficesController as _IFKTaxOfficesController
    from . import IFKVatRatesController as _IFKVatRatesController
    from . import IFKVatRegisterMarkersController as _IFKVatRegisterMarkersController
    from . import IFKVatRegistersController as _IFKVatRegistersController
    from . import IFKYearsController as _IFKYearsController
