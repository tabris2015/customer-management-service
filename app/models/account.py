from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.db_base import DBBase, TimestampDBBase


class AccountBase(BaseModel):
    id: str
    client_id: str
    description: str
    balance: float


class AccountCreate(AccountBase, TimestampDBBase):
    balance: float = Field(default=0.0)


class AccountUpdate(AccountBase):
    id: Optional[str]
    client_id: Optional[str]
    description: Optional[str]
    balance: float
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AccountIn(AccountBase):
    balance: Optional[float]


class Account(AccountBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
