from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from app.models.db_base import DBBase


class TransactionBase(BaseModel):
    account_id: str
    client_id: str
    amount: float
    status: str


class TransactionCreate(TransactionBase, DBBase):
    pass


class TransactionUpdate(TransactionBase):
    account_id: Optional[str]
    client_id: Optional[str]
    amount: Optional[float]
    status: Optional[str]


class TransactionIn(TransactionBase):
    amount: Optional[float]
    status: Optional[str]
    status: str = Field(default='open')


class Transaction(TransactionBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
