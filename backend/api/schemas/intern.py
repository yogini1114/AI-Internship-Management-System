from pydantic import BaseModel
from datetime import date


class InternBase(BaseModel):
    intern_id: str
    name: str
    email: str
    domain: str
    mentor_name: str
    batch: str
    start_date: date
    end_date: date
    status: str


class InternCreate(InternBase):
    pass


class InternResponse(InternBase):
    class Config:
        from_attributes = True