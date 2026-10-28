"""Benchmark sync/threading dla pobierania szczegółów zamówień.

Skrypt drukuje tabelę w formacie:

Tryb           Workers     OK/ERR           Czas
-------------- ------- ---------- --------------
sync                 1      100/0    1570.860 ms
sync-raw             1      100/0    1412.597 ms
threading            5      100/0     451.205 ms
threading-raw        5      100/0     439.581 ms

`*-raw` oznacza wywołanie tej samej metody interfejsu z `validate=False`, czyli
z pominięciem walidacji Pydantic i z pozostaniem przy JSON.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from time import perf_counter_ns
from typing import Any

from SymfWebAPI import ClientConfig, WebAPI, build_sync_client

COUNT = 100
DEFAULT_THREAD_WORKERS = (1, 2, 5, 10, 20)


def _required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Brak zmiennej środowiskowej {name}.")
    return value


def _config() -> ClientConfig:
    return ClientConfig(
        domain=_required_env("SYMFWEBAPI_DOMAIN"),
        application_key=_required_env("SYMFWEBAPI_APP_KEY"),
        device_name=os.getenv("SYMFWEBAPI_DEVICE_NAME", "benchmark-order-details"),
        https=os.getenv("SYMFWEBAPI_HTTPS", "false").lower() in {"1", "true", "yes"},
        sanitize_nul_chars_in_responses=os.getenv("SYMFWEBAPI_SANITIZE_NUL", "false").lower() in {"1", "true", "yes"},
    )


def _epoch(value: datetime | None) -> float:
    if value is None:
        return float("-inf")
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.timestamp()


def _last_n(orders: list[Any], count: int) -> list[Any]:
    return sorted(
        orders,
        key=lambda x: _epoch(x.IssueDate or x.SaleDate or x.MaturityDate),
        reverse=True,
    )[:count]


def _format_duration_ns(duration_ns: int) -> str:
    if duration_ns < 1_000_000:
        return f"{duration_ns / 1_000:.3f} us"
    return f"{duration_ns / 1_000_000:.3f} ms"


def _detect_physical_cores() -> int | None:
    if value := os.getenv("SYMFWEBAPI_BENCHMARK_PHYSICAL_CORES", "").strip():
        return int(value)

    if sys.platform.startswith("linux"):
        physical_pairs: set[tuple[str, str]] = set()
        core_ids: set[str] = set()
        physical_id: str | None = None
        core_id: str | None = None
        try:
            with open("/proc/cpuinfo", "r", encoding="utf-8") as handle:
                for raw_line in handle:
                    line = raw_line.strip()
                    if not line:
                        if physical_id is not None and core_id is not None:
                            physical_pairs.add((physical_id, core_id))
                        elif core_id is not None:
                            core_ids.add(core_id)
                        physical_id = None
                        core_id = None
                        continue
                    if line.startswith("physical id"):
                        physical_id = line.split(":", 1)[1].strip()
                    elif line.startswith("core id"):
                        core_id = line.split(":", 1)[1].strip()
            if physical_pairs:
                return len(physical_pairs)
            if core_ids:
                return len(core_ids)
        except OSError:
            return None

    if os.name == "nt":
        cmd = [
            "powershell",
            "-NoProfile",
            "-Command",
            "(Get-CimInstance Win32_Processor | Measure-Object -Property NumberOfCores -Sum).Sum",
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=5)
            value = result.stdout.strip()
            return int(value) if value else None
        except (OSError, subprocess.SubprocessError, ValueError):
            return None

    return None


def _default_thread_workers() -> tuple[int, ...]:
    workers: list[int] = list(DEFAULT_THREAD_WORKERS)
    physical = _detect_physical_cores()
    logical = os.cpu_count() or 1
    for candidate in (physical, logical):
        if candidate and candidate > 0 and candidate not in workers:
            workers.append(candidate)
    return tuple(workers)


def _print_results_table(rows: list[tuple[str, int, int, int, str]]) -> None:
    print("\nWyniki benchmarku (pobranie szczegółów):")
    print(f"{'Tryb':<14} {'Workers':>7} {'OK/ERR':>10} {'Czas':>14}")
    print(f"{'-' * 14} {'-' * 7} {'-' * 10} {'-' * 14}")
    for mode, workers, ok, err, elapsed in rows:
        print(f"{mode:<14} {workers:>7} {f'{ok}/{err}':>10} {elapsed:>14}")
    print("")


def _fetch_order_detail(api: Any, one: Any, *, validate: bool) -> Any:
    if one.Buffer:
        resp = WebAPI.Interface.Orders.Interfaces.IOrdersController.Get(api, number=one.DocumentNumber, buffer=one.Buffer, validate=validate)
    else:
        resp = WebAPI.Interface.Orders.Interfaces.IOrdersController.Get(api, id=one.Id, validate=validate)
    return resp.unwrap()


def run_sync(*, validate: bool) -> tuple[int, int, int]:
    with build_sync_client(_config()) as api:
        orders = WebAPI.Interface.Orders.Interfaces.IOrdersController.GetList(api).unwrap()
        if not orders:
            print("Brak zamówień do pobrania.")
            return 0, 0, 0

        selected = _last_n(orders, COUNT)
        t0 = perf_counter_ns()
        ok = 0
        err = 0
        for one in selected:
            try:
                _fetch_order_detail(api, one, validate=validate)
                ok += 1
            except Exception:
                err += 1
        return ok, err, perf_counter_ns() - t0


def run_threading(workers: int, *, validate: bool) -> tuple[int, int, int]:
    with build_sync_client(_config()) as api:
        orders = WebAPI.Interface.Orders.Interfaces.IOrdersController.GetList(api).unwrap()
        if not orders:
            print("Brak zamówień do pobrania.")
            return 0, 0, 0

        selected = _last_n(orders, COUNT)

        def fetch(one: Any) -> Any:
            return _fetch_order_detail(api, one, validate=validate)

        t0 = perf_counter_ns()
        ok = 0
        err = 0
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(fetch, one): one for one in selected}
            for future in as_completed(futures):
                try:
                    future.result()
                    ok += 1
                except Exception:
                    err += 1
        return ok, err, perf_counter_ns() - t0


def _parse_workers(value: str | None) -> tuple[int, ...]:
    if not value:
        return _default_thread_workers()
    parts = [p.strip() for p in value.split(",") if p.strip()]
    return tuple(int(p) for p in parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark pobierania szczegółów zamówień: sync/threading")
    parser.add_argument("--mode", choices=["sync", "threading", "all"], default="all")
    parser.add_argument("--workers", type=int, default=5)
    parser.add_argument("--thread-workers-list", type=str, default=None)
    args = parser.parse_args()

    rows: list[tuple[str, int, int, int, str]] = []

    if args.mode in ("sync", "all"):
        ok, err, elapsed_ns = run_sync(validate=True)
        rows.append(("sync", 1, ok, err, _format_duration_ns(elapsed_ns)))
        ok, err, elapsed_ns = run_sync(validate=False)
        rows.append(("sync-raw", 1, ok, err, _format_duration_ns(elapsed_ns)))

    if args.mode in ("threading", "all"):
        worker_values = (args.workers,) if args.mode == "threading" else _parse_workers(args.thread_workers_list)
        for workers in worker_values:
            ok, err, elapsed_ns = run_threading(workers, validate=True)
            rows.append(("threading", workers, ok, err, _format_duration_ns(elapsed_ns)))
            ok, err, elapsed_ns = run_threading(workers, validate=False)
            rows.append(("threading-raw", workers, ok, err, _format_duration_ns(elapsed_ns)))

    _print_results_table(rows)


if __name__ == "__main__":
    main()
