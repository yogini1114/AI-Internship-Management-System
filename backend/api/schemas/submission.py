from pydantic import BaseModel, ConfigDict
from datetime import datetime


class SubmissionBase(BaseModel):
    intern_id: str
    task_id: str
    github_link: str
    submitted_at: datetime
    status: str
    score: float | None = None


class SubmissionCreate(SubmissionBase):
    submission_id: str


class SubmissionUpdate(BaseModel):
    github_link: str | None = None
    submitted_at: datetime | None = None
    status: str | None = None
    score: float | None = None


class SubmissionResponse(SubmissionBase):
    submission_id: str

    model_config = ConfigDict(from_attributes=True)