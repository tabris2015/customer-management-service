from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from app.models.db_base import DBBase


class CustomerBase(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    # add accounts


class CustomerCreate(CustomerBase, DBBase):
    pass


class CustomerUpdate(CustomerBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class CustomerIn(CustomerBase):
    pass


class Customer(CustomerBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
