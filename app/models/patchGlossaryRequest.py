from typing import Optional, List
from pydantic import BaseModel

class PatchGlossaryRequest(BaseModel):
    key: str
    value: str