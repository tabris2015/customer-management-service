from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.models.db_base import TimestampDBBase


class ClientBase(BaseModel):
    """Base Model for Client object, it has the base fields"""
    name: str
    company: Optional[str]


class ClientCreate(ClientBase, TimestampDBBase):
    """Client model for database"""
    pass


class ClientUpdate(ClientBase):
    name: Optional[str]


class ClientIn(ClientBase):
    pass


class Client(ClientBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
