from __future__ import annotations

from typing import Any, TypedDict

class InstanceInfoJSON(TypedDict):
    Seed: str
    ServerName: str
    DatabaseName: str
    Firm: str
    User: str

class LoadedModuleInfoJSON(TypedDict):
    AssemblyName: str
    ModuleName: str
    ModuleVersion: str

class PingJSON(TypedDict):
    OpenSessionsNumber: int
    ActiveHMFInfo: list[InstanceInfoJSON]
    ActiveITGInfo: list[InstanceInfoJSON]
    LoadedModuleInfo: list[LoadedModuleInfoJSON]
