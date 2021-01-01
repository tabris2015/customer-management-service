from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class DBBase(BaseModel):
    """Default Database fields"""
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)