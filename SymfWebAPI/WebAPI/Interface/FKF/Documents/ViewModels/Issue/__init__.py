from __future__ import annotations

from pydantic import BaseModel


class DocumentRecordAccountIssue(BaseModel):
    Synthetic: int
    Analytic1: int
    Analytic2: int
    Analytic3: int
    Analytic4: int
    Analytic5: int
