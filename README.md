# SymfWebAPI

[![CI](https://github.com/maku2903/symf-webapi-py/actions/workflows/public-ci-release.yml/badge.svg)](https://github.com/maku2903/symf-webapi-py/actions/workflows/public-ci-release.yml)
[![PyPI version](https://img.shields.io/pypi/v/SymfWebAPI.svg)](https://pypi.org/project/SymfWebAPI/)
[![Python versions](https://img.shields.io/pypi/pyversions/SymfWebAPI.svg)](https://pypi.org/project/SymfWebAPI/)
[![License](https://img.shields.io/pypi/l/SymfWebAPI.svg)](https://github.com/maku2903/symf-webapi-py/blob/main/LICENSE)

Pythonowa biblioteka kliencka do Symfonia WebAPI w architekturze sync-first: z typowanymi modelami, dostępnymi kontrolerami, wsparciem dla threading i opcjonalnym trybem JSON-only.

## Instalacja

```bash
pip install SymfWebAPI
```

## Szybki start

```python
from SymfWebAPI import ClientConfig, WebAPI, build_sync_client

config = ClientConfig(
    domain="host:9000",
    application_key="00000000-0000-0000-0000-000000000000",
    device_name="integration-client",
)

with build_sync_client(config) as api:
    resp = WebAPI.Interface.Products.Interfaces.IProductsController.Get(
        api,
        salePrices=False,
    )
    products = resp.unwrap()
    print(len(products))
```

## Tryb JSON-only

Biblioteka wspiera oficjalny tryb pracy bez mapowania do modeli Pydantic.

Masz dwie ścieżki:
- niskopoziomową: `api.request_json(...)` albo `envelope.json()`,
- dostępne metody kontrolerów z flagą `validate=False`.

To jest przydatne, gdy:
- integrujesz się z niestabilnymi lub nieidealnymi danymi produkcyjnymi,
- chcesz szybko zdiagnozować payload z WebAPI,
- robisz migracje i chcesz odczytać tylko kilka pól bez kosztu walidacji Pydantic,
- benchmarkujesz lub przetwarzasz duże listy rekordów.

Przy `validate=False` dostępne metody nadal zachowują podpowiedzi IDE dla kształtu JSON przez stuby `.pyi`.

Tryb `validate=False` działa spójnie po obu stronach:
- response side: omija walidację odpowiedzi i zwraca surowy JSON,
- request side: dla endpointów z body pozwala wysłać surowy `dict` / `list` / JSON-serializable payload bez modelu Pydantic.

Przy `validate=True` endpointy z modelowym body nadal oczekują modelu Pydantic.

Najwygodniejsza ścieżka w aktualnej bibliotece to wywołanie dostępnej metody kontrolera z `validate=False`.

Przykład z dostępną metodą kontrolera:

```python
from SymfWebAPI import ClientConfig, WebAPI, build_sync_client

config = ClientConfig(
    domain="host:9000",
    application_key="00000000-0000-0000-0000-000000000000",
    device_name="json-only-client",
)

with build_sync_client(config) as api:
    resp = WebAPI.Interface.Products.Interfaces.IProductsController.GetPagedDocument(
        api,
        page=1,
        size=10,
        orderBy=WebAPI.Interface.Enums.enumOrderByType.Asc,
        validate=False,
    )
    page = resp.unwrap()
    print(page["Data"][0]["Code"])
```

Przykład niskopoziomowy:

```python
with build_sync_client(config) as api:
    products = api.request_json(
        "GET",
        "/api/Products",
        params={"salePrices": False},
    )
    print(len(products))
```

Przykład write-pathu bez Pydantic:

```python
with build_sync_client(config) as api:
    created = WebAPI.Interface.Products.Interfaces.IProductsController.AddNew(
        api,
        product={
            "Code": "P-RAW-001",
            "Name": "Produkt z raw JSON",
            "Active": True,
        },
        validate=False,
    ).unwrap()
    print(created["Code"])
```

Przykład gotowego skryptu:
- `examples/get_products_json_only.py`
- `examples/add_product_json_only.py` (zabezpieczony przed przypadkowym write)

## Dokumentacja

- Omówienie biblioteki: `docs/overview.md`
- Przykłady: `examples/`

## Benchmark bez sekretów

Przykład benchmarku znajduje się w:
- `examples/benchmark_order_details.py`

Przykład pracy bez modeli Pydantic:
- `examples/get_products_json_only.py`
- `examples/add_product_json_only.py` (write-path `validate=False`, domyślnie zablokowany)

Konfiguracja przez zmienne środowiskowe:
- `SYMFWEBAPI_DOMAIN`
- `SYMFWEBAPI_APP_KEY`
- `SYMFWEBAPI_DEVICE_NAME` (opcjonalnie)
- `SYMFWEBAPI_HTTPS` (opcjonalnie, np. `true`/`false`)
- `SYMFWEBAPI_SANITIZE_NUL` (opcjonalnie, usuwa `NUL` / `\u0000` z odpowiedzi)
- `SYMFWEBAPI_BENCHMARK_PHYSICAL_CORES` (opcjonalnie, ręcznie ustawia liczbę fizycznych rdzeni dla benchmarku)

Benchmark działa w trybach:
- `sync`
- `sync-raw`
- `threading`
- `threading-raw`

Przy braku `--thread-workers-list` skrypt automatycznie dorzuca test dla liczby fizycznych rdzeni i liczby logicznych wątków, jeśli da się je rozróżnić.

## Wersjonowanie

Wersja paczki ma format `X.I.WM.Wm`, np. `2.0.26.10`:
- `X` - major SDK,
- `I` - iteracja SDK dla tej samej wersji WebAPI.
- `WM.Wm` - docelowa wersja Symfonia WebAPI.

## Wersjonowanie

Wersja `2.1.26.20` używa formatu `X.I.WM.Wm`: `X` oznacza główną wersję SDK,
`I` kolejną iterację klienta, a `WM.Wm` docelową wersję WebAPI.

## Licencja BSD

BSD-3-Clause.
