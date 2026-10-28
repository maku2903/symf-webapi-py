# Omówienie biblioteki SymfWebAPI

`SymfWebAPI` to klient do Symfonia WebAPI udostępniający interfejsy API.

## Co zawiera biblioteka

- `SymfWebAPI.config.ClientConfig`
  Konfiguracja połączenia (`domain`, `application_key`, `device_name`, `https`).

- `SymfWebAPI.runtime.build_sync_client`
  Fabryka gotowego klienta synchronicznego.

- `SymfWebAPI.session.SessionManager`
  Zarządzanie cyklem życia sesji (otwarcie, odświeżenie, zamknięcie).

- `SymfWebAPI.transport.httpx_sync`
  Domyślny transport HTTP oparty o `httpx`.

- `SymfWebAPI.WebAPI.Interface.*`
  Dostępne kontrolery i modele endpointów.

## Jak wygląda wywołanie endpointu

1. Konfigurujesz klienta przez `ClientConfig`.
2. Tworzysz klienta `build_sync_client(...)`.
3. Wywołujesz dostępną metodę z `WebAPI.Interface...`.
4. Otrzymujesz `ResponseEnvelope[T]` i wyciągasz model przez `unwrap()`.

Biblioteka wspiera też tryb JSON-only:

1. Wywołujesz `api.request_json(...)` i dostajesz od razu `dict` / `list`.
2. Albo używasz `api.request(...)`, a potem `envelope.json()`.
3. Albo korzystasz z dostępnych metod kontrolerów z flagą `validate=False`.

Przykład:
- `WebAPI.Interface.Products.Interfaces.IProductsController.GetPagedDocument(..., validate=False)`

W praktyce najwygodniejsza jest trzecia ścieżka, bo zachowuje kontrakt dostępnych kontrolerów i daje podpowiedzi IDE przez stuby `.pyi`.

To jest przydatne przy migracjach, benchmarkach i diagnostyce danych, które nie przechodzą mapowania do modeli albo gdy chcesz odczytać tylko kilka pól bez kosztu walidacji Pydantic.

`validate=False` działa też po stronie request body:
- przy `validate=True` modelowe endpointy oczekują obiektu Pydantic,
- przy `validate=False` możesz wysłać surowy `dict` / `list` / JSON-serializable payload.

## Obsługa błędów

- Błędy HTTP: `SymfWebAPI.errors.WebAPIHttpError`
- Błędy transportu: `SymfWebAPI.errors.TransportError`
- Problemy sesji: `SymfWebAPI.errors.SessionError` / `SessionExpiredError`

## Sync i threading

- `build_sync_client` jest głównym publicznym entrypointem runtime.
- Biblioteka wspiera współdzielenie klienta między wątkami.
- Równoległość po stronie klienta opiera się na threading, nie na async.

## Przykłady

Sprawdź katalog `examples/`, w tym benchmark:
- `examples/benchmark_order_details.py`
- `examples/get_products_json_only.py`
- `examples/add_product_json_only.py`

Benchmark w aktualnym snapshotcie działa w trybach:
- `sync`
- `sync-raw`
- `threading`
- `threading-raw`

Domyślnie testuje także liczbę fizycznych rdzeni i liczbę logicznych wątków, jeśli środowisko pozwala je wykryć lub jeśli podasz `SYMFWEBAPI_BENCHMARK_PHYSICAL_CORES`.
