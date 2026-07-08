from datetime import date as Date
from typing import Optional

from pydantic import BaseModel, ConfigDict

class AttendanceBase(BaseModel):
    intern_id: str
    date: Date
    status: str
    remarks: Optional[str] = None


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    date: Optional[Date] = None
    status: Optional[str] = None
    remarks: Optional[str] = None


class AttendanceResponse(AttendanceBase):
    attendance_id: int

    model_config = ConfigDict(from_attributes=True)