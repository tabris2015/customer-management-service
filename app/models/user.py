from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from app.models.db_base import TimestampDBBase
from app.models.account import Account


class UserBase(BaseModel):
    """Base Model for User object, it has the base fields"""
    email: EmailStr
    name: Optional[str]
    role: str = 'agent'
    active: Optional[bool]
    agent_id: Optional[str]


class UserCreate(UserBase, TimestampDBBase):
    """User model for database"""
    id: Optional[str]


class UserUpdate(UserBase):
    email: Optional[EmailStr]
    name: Optional[str]
    role: Optional[str]
    active: Optional[bool]
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserUpdateIn(UserBase):
    id: str
    email: Optional[EmailStr]
    name: Optional[str]
    password: Optional[str]


class UserIn(UserBase):
    password: str


class User(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
