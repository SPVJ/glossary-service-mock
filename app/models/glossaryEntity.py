from fsCommonLib.databases.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class GlossaryEntity(Base):
    __tablename__ = "glossary"

    id = Column(String, primary_key=True, nullable=False)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

