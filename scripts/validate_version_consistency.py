#!/usr/bin/env python3
"""Check that the SDK manifest and release metadata agree."""
from __future__ import annotations

import json
import tomllib
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    release = json.loads((root / "version.json").read_text(encoding="utf-8"))
    expected = ".".join(str(release[key]) for key in (
        "sdk_major", "iteration", "webapi_major", "webapi_minor"
    ))
    actual = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]
    if expected != actual:
        raise SystemExit("SDK manifest and release metadata have different versions")
    print(f"SDK version: {actual}")


if __name__ == "__main__":
    main()
