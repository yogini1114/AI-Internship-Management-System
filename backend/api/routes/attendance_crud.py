from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.database import get_db

from backend.models.attendance import Attendance
from backend.models.intern import Intern

from backend.api.schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
    AttendanceResponse,
)

router = APIRouter(
    prefix="/api/attendance-crud",
    tags=["Attendance Management"],
)


# ---------------------------------
# Create Attendance
# ---------------------------------
@router.post("/", response_model=AttendanceResponse)
def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):

    # Check Intern Exists
    intern = db.query(Intern).filter(
        Intern.intern_id == attendance.intern_id
    ).first()

    if not intern:
        raise HTTPException(
            status_code=404,
            detail="Intern not found."
        )

    # Prevent duplicate attendance
    existing = db.query(Attendance).filter(
        Attendance.intern_id == attendance.intern_id,
        Attendance.date == attendance.date
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this date."
        )

    new_attendance = Attendance(
        **attendance.model_dump()
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance


# ---------------------------------
# Get All Attendance
# ---------------------------------
@router.get("/", response_model=list[AttendanceResponse])
def get_all_attendance(
    db: Session = Depends(get_db)
):

    return db.query(Attendance).all()


# ---------------------------------
# Get Attendance By ID
# ---------------------------------
@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):

    attendance = db.query(Attendance).filter(
        Attendance.attendance_id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found."
        )

    return attendance


# ---------------------------------
# Update Attendance
# ---------------------------------
@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(
    attendance_id: int,
    updated: AttendanceUpdate,
    db: Session = Depends(get_db)
):

    attendance = db.query(Attendance).filter(
        Attendance.attendance_id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found."
        )

    update_data = updated.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(attendance, key, value)

    db.commit()
    db.refresh(attendance)

    return attendance


# ---------------------------------
# Delete Attendance
# ---------------------------------
@router.delete("/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):

    attendance = db.query(Attendance).filter(
        Attendance.attendance_id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found."
        )

    db.delete(attendance)
    db.commit()

    return {
        "message": "Attendance deleted successfully."
    }