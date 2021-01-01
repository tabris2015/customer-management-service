from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from app.models.db_base import DBBase


class TransactionBase(BaseModel):
    account_id: str
    amount: float
    status: str


class TransactionCreate(TransactionBase, DBBase):
    pass


class TransactionUpdate(TransactionBase):
    pass


class TransactionIn(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
