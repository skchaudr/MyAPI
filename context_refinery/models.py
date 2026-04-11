from pydantic import BaseModel
from typing import Union
from datetime import datetime

class CanonicalDocument(BaseModel):
    id: str
    source_type: str
    content: str
    metadata: dict
    tags: list[str]
    created_at: Union[str, datetime]
