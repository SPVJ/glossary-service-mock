from pydantic import BaseModel

class Glossary(BaseModel):
    id: str
    key: str
    value: str
    createdAt: str
    updatedAt: str