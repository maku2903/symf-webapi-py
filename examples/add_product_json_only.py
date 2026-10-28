"""Przykład write-pathu validate=False dla dodawania produktu.

Uwaga:
- payload poniżej jest przykładowy i może wymagać dostosowania do Twojej instancji Symfonii,
- nie uruchamiaj tego na produkcji bez świadomej decyzji.
"""

from __future__ import annotations

import json
import os

from SymfWebAPI import ClientConfig, WebAPI, build_sync_client


def _required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Brak zmiennej środowiskowej {name}.")
    return value


def _product_payload() -> dict[str, object]:
    return {
        "Id": None,
        "Active": True,
        "Code": "P-RAW-001",
        "Name": "Produkt z raw JSON",
        "Type": 0,
        "Barcode": "",
        "PKWiU": "",
        "CNFull": "",
        "CN": "",
        "DeliveryScheme": "",
        "FiscalName": "Produkt z raw JSON",
        "AgriculturalPromotionFund": "",
        "PriceNegotiation": False,
        "PriceRounding": None,
        "PriceRecalculateType": None,
        "SettlementMethod": None,
        "PriceParameter": None,
        "VAT50Minus": False,
        "ReverseCharge": False,
        "SplitPayment": False,
        "JPK_V7ProductGroup": None,
        "StaticSet": False,
        "PriceSetMode": False,
        "CollationSetMode": False,
        "SalePriceRecalculate": False,
        "CurrencyMode": False,
        "CurrencyRateWithoutConversion": 1,
        "CurrencyRate": 1,
        "CurrencyConversion": 1,
        "CurrencyRateDate": "2026-01-01T00:00:00",
        "MinState": 0,
        "MaxState": 0,
        "Note": None,
        "Marker": 0,
        "FK": {"IdFK": "", "ParameterFK": ""},
        "Intrastat": {
            "RatioOfWeight": 0,
            "RatioOfComplementaryUM": 0,
            "ComplementaryUM": "",
            "UseComplementaryUM": False,
        },
        "UnitsOfMeasurement": {
            "RecordUM": "szt.",
            "DefaultSaleUM": "szt.",
            "DefaultPurchaseUM": "szt.",
            "SecondSaleUM": "",
            "SecondPurchaseUM": "",
            "DefaultUnitKind": 0,
        },
        "BasePrice": {"Net": 0, "Gross": 0},
        "PurchasePrice": {"Net": 0, "Gross": 0},
        "PurchasePriceInCurrency": {"Net": 0, "Gross": 0},
        "SalePrices": [],
        "CalcOther": {"Net": 0, "Gross": 0},
        "CalcExcise": {"Net": 0, "Gross": 0},
        "CalcDuty": {"Net": 0, "Gross": 0},
        "Kind": {"Id": 0, "Name": ""},
        "Catalog": {"Id": 0, "Name": "", "Path": ""},
        "VatRate": None,
        "SetElements": None,
        "Dimensions": [],
        "Barcodes": [],
        "LogisticFields": [],
        "RtfNote": None,
    }


def main() -> None:
    payload = _product_payload()

    config = ClientConfig(
        domain=_required_env("SYMFWEBAPI_DOMAIN"),
        application_key=_required_env("SYMFWEBAPI_APP_KEY"),
        device_name=os.getenv("SYMFWEBAPI_DEVICE_NAME", "json-only-write-example"),
        https=os.getenv("SYMFWEBAPI_HTTPS", "false").lower() in {"1", "true", "yes"},
        sanitize_nul_chars_in_responses=os.getenv("SYMFWEBAPI_SANITIZE_NUL", "false").lower() in {"1", "true", "yes"},
    )

    with build_sync_client(config) as api:
        created = WebAPI.Interface.Products.Interfaces.IProductsController.AddNew(
            api,
            product=payload,
            validate=False,
        ).unwrap()

    print("Utworzony rekord:")
    print(json.dumps(created, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
