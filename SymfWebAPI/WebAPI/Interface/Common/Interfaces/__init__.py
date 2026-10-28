"""Auto-generated package (lazy imports)."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = ("IAgriculturalPromotionFundsController", "IAspectsClassificationController", "ICNCodesController", "ICountriesController", "ICurrenciesController", "ICurrencyRatesController", "IDepartmentsController", "IDocumentSeriesController", "IDocumentTypesController", "IKsefController", "IPKWiUCodesController", "IPaymentFormsController", "IPaymentRegistriesController", "IPricesController", "IRegionsController", "IUnitsOfMeasurementController", "IVatRatesController", "IWarehousesController",)

def __getattr__(name: str):
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(__all__) | {n for n in globals() if not n.startswith('_')})

if TYPE_CHECKING:
    from . import IAgriculturalPromotionFundsController as _IAgriculturalPromotionFundsController
    from . import IAspectsClassificationController as _IAspectsClassificationController
    from . import ICNCodesController as _ICNCodesController
    from . import ICountriesController as _ICountriesController
    from . import ICurrenciesController as _ICurrenciesController
    from . import ICurrencyRatesController as _ICurrencyRatesController
    from . import IDepartmentsController as _IDepartmentsController
    from . import IDocumentSeriesController as _IDocumentSeriesController
    from . import IDocumentTypesController as _IDocumentTypesController
    from . import IKsefController as _IKsefController
    from . import IPKWiUCodesController as _IPKWiUCodesController
    from . import IPaymentFormsController as _IPaymentFormsController
    from . import IPaymentRegistriesController as _IPaymentRegistriesController
    from . import IPricesController as _IPricesController
    from . import IRegionsController as _IRegionsController
    from . import IUnitsOfMeasurementController as _IUnitsOfMeasurementController
    from . import IVatRatesController as _IVatRatesController
    from . import IWarehousesController as _IWarehousesController
