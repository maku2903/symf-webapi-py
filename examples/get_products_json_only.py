from __future__ import annotations

import os

from SymfWebAPI import ClientConfig, WebAPI, build_sync_client


def _required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Brak zmiennej środowiskowej {name}.")
    return value


def main() -> None:
    config = ClientConfig(
        domain=_required_env("SYMFWEBAPI_DOMAIN"),
        application_key=_required_env("SYMFWEBAPI_APP_KEY"),
        device_name=os.getenv("SYMFWEBAPI_DEVICE_NAME", "json-only-example"),
        https=os.getenv("SYMFWEBAPI_HTTPS", "false").lower() in {"1", "true", "yes"},
        sanitize_nul_chars_in_responses=os.getenv("SYMFWEBAPI_SANITIZE_NUL", "false").lower() in {"1", "true", "yes"},
    )

    with build_sync_client(config) as api:
        products = WebAPI.Interface.Products.Interfaces.IProductsController.Get(
            api,
            salePrices=False,
            validate=False,
        ).unwrap()

    print(f"Liczba rekordow: {len(products) if isinstance(products, list) else 'nie-lista'}")
    if isinstance(products, list) and products:
        first = products[0]
        print("Pierwszy rekord:")
        print(f"  Id: {first.get('Id')}")
        print(f"  Code: {first.get('Code')}")
        print(f"  Name: {first.get('Name')}")
        print(f"  VatRate: {first.get('VatRate')}")


if __name__ == "__main__":
    main()
