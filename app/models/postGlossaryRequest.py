from typing import Optional, List
from pydantic import BaseModel

class PostGlossaryRequest(BaseModel):
    key: str
    value: str
