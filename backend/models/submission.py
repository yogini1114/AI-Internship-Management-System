"""
SQLAlchemy model representing an intern's task submission.
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Float,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship

from backend.database.database import Base


class Submission(Base):

    __tablename__ = "submissions"

    submission_id = Column(
        String,
        primary_key=True,
        index=True
    )

    intern_id = Column(
        String,
        ForeignKey("interns.intern_id"),
        nullable=False
    )

    task_id = Column(
        String,
        ForeignKey("tasks.task_id"),
        nullable=False
    )

    github_link = Column(
        String,
        nullable=False
    )

    submitted_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )   # pending / on_time / late

    score = Column(
        Float,
        nullable=True
    )

    # -------------------------
    # Relationships
    # -------------------------

    intern = relationship(
        "Intern",
        back_populates="submissions"
    )

    task = relationship(
        "Task",
        back_populates="submissions"
    )

    def __repr__(self):
        return (
            f"<Submission {self.submission_id} | "
            f"{self.intern_id}>"
        )