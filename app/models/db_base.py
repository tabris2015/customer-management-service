from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class TimestampDBBase(BaseModel):
    """Base model with timestamps for database"""
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DBBase(TimestampDBBase):
    """Default Database fields"""
    id: UUID = Field(default_factory=uuid4)




