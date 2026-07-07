from pydantic import BaseModel, ConfigDict
from datetime import date


class AttendanceBase(BaseModel):
    intern_id: str
    date: date
    status: str
    remarks: str | None = None


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    status: str | None = None
    remarks: str | None = None


class AttendanceResponse(AttendanceBase):
    attendance_id: int

    model_config = ConfigDict(
        from_attributes=True
    )