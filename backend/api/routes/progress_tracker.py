"""
API routes for Module 1 — AI Internship Progress Tracker.
"""

from fastapi import APIRouter

from backend.api.schemas.common import APIResponse
from backend.services import progress_service

router = APIRouter(
    prefix="/api/progress",
    tags=["Progress Tracker"]
)


@router.get("/{intern_id}", response_model=APIResponse)
def get_progress(intern_id: str):

    data = progress_service.get_intern_progress(intern_id)

    return APIResponse(
        message="Progress fetched successfully.",
        data=data
    )


@router.get("/inactive/list", response_model=APIResponse)
def get_inactive_interns():

    data = progress_service.get_inactive_interns()

    return APIResponse(
        message="Inactive interns fetched successfully.",
        data=data
    )