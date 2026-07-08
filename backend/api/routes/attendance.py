"""
API routes for Attendance Analyzer.
"""

from fastapi import APIRouter

from backend.api.schemas.common import APIResponse
from backend.services import attendance_service

router = APIRouter(
    prefix="/api/attendance",
    tags=["Attendance Analyzer"]
)


@router.get("/{intern_id}", response_model=APIResponse)
def get_attendance(intern_id: str):

    data = attendance_service.get_intern_attendance(
        intern_id
    )

    return APIResponse(
        message="Attendance fetched successfully.",
        data=data
    )