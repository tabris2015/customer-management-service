from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from app.models.db_base import DBBase


class TodoBase(BaseModel):
    """Base Model for Todo object, it has the base fields"""
    text: str
    priority: int


class TodoCreate(TodoBase, DBBase):
    """Todo model for database"""
    pass


class TodoUpdate(TodoBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TodoIn(TodoBase):
    pass


class Todo(TodoBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
