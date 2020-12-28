from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from app.models.db_base import DBBase


class AccountBase(BaseModel):
    description: str


class AccountCreate(AccountBase, DBBase):
    pass


class AccountUpdate(AccountBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AccountIn(AccountBase):
    pass


class Account(AccountBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
