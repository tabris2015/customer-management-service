from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from app.models.db_base import TimestampDBBase
from app.models.account import Account


class ClientBase(BaseModel):
    """Base Model for Client object, it has the base fields"""
    name: str
    company: Optional[str]
    accounts: List[Account] = []


class ClientCreate(ClientBase, TimestampDBBase):
    """Client model for database"""
    pass


class ClientUpdate(ClientBase):
    name: Optional[str]
    accounts: Optional[List[Account]]
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ClientIn(ClientBase):
    pass


class Client(ClientBase):
    id: str
    created_at: datetime
    updated_at: datetime
    accounts: List[Account]

    class Config:
        orm_mode = True
