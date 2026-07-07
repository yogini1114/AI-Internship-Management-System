from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.database import get_db

from backend.models.submission import Submission
from backend.models.intern import Intern
from backend.models.task import Task

from backend.api.schemas.submission import (
    SubmissionCreate,
    SubmissionResponse,
)

router = APIRouter(
    prefix="/api/submissions",
    tags=["Submission Management"]
)


# -----------------------------
# Create Submission
# -----------------------------
@router.post("/", response_model=SubmissionResponse)
def create_submission(
    submission: SubmissionCreate,
    db: Session = Depends(get_db)
):

    # Duplicate Submission ID
    existing = db.query(Submission).filter(
        Submission.submission_id == submission.submission_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Submission ID already exists."
        )

    # Intern Exists?
    intern = db.query(Intern).filter(
        Intern.intern_id == submission.intern_id
    ).first()

    if not intern:
        raise HTTPException(
            status_code=404,
            detail="Intern not found."
        )

    # Task Exists?
    task = db.query(Task).filter(
        Task.task_id == submission.task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    new_submission = Submission(
        **submission.model_dump()
    )

    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    return new_submission


# -----------------------------
# Get All Submissions
# -----------------------------
@router.get("/", response_model=list[SubmissionResponse])
def get_all_submissions(
    db: Session = Depends(get_db)
):

    return db.query(Submission).all()


# -----------------------------
# Get Single Submission
# -----------------------------
@router.get("/{submission_id}", response_model=SubmissionResponse)
def get_submission(
    submission_id: str,
    db: Session = Depends(get_db)
):

    submission = db.query(Submission).filter(
        Submission.submission_id == submission_id
    ).first()

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Submission not found."
        )

    return submission


# -----------------------------
# Update Submission
# -----------------------------
@router.put("/{submission_id}", response_model=SubmissionResponse)
def update_submission(
    submission_id: str,
    updated: SubmissionCreate,
    db: Session = Depends(get_db)
):

    submission = db.query(Submission).filter(
        Submission.submission_id == submission_id
    ).first()

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Submission not found."
        )

    for key, value in updated.model_dump().items():
        setattr(submission, key, value)

    db.commit()
    db.refresh(submission)

    return submission


# -----------------------------
# Delete Submission
# -----------------------------
@router.delete("/{submission_id}")
def delete_submission(
    submission_id: str,
    db: Session = Depends(get_db)
):

    submission = db.query(Submission).filter(
        Submission.submission_id == submission_id
    ).first()

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Submission not found."
        )

    db.delete(submission)
    db.commit()

    return {
        "message": "Submission deleted successfully."
    }