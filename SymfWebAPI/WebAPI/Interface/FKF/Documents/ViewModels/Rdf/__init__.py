from __future__ import annotations

from pydantic import BaseModel


class RdfDocumentAttachment(BaseModel):
    FileName: str
    Description: str
    Content: str

class RdfDocumentLink(BaseModel):
    Description: str
    URL: str
