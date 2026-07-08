"""
SQLAlchemy model representing internship certificate status.
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from backend.database.database import Base


class Certificate(Base):

    __tablename__ = "certificates"

    certificate_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    intern_id = Column(
        String,
        ForeignKey("interns.intern_id"),
        nullable=False,
        index=True
    )

    status = Column(
        String,
        default="Pending"
    )
    # Eligible / Not Eligible / Pending

    issue_date = Column(
        DateTime,
        nullable=True
    )

    overall_score = Column(
        Integer,
        default=0
    )

    attendance_score = Column(
        Integer,
        default=0
    )

    github_score = Column(
        Integer,
        default=0
    )

    task_score = Column(
        Integer,
        default=0
    )

    mentor_score = Column(
        Integer,
        default=0
    )

    ai_remarks = Column(
        Text,
        nullable=True
    )

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # -------------------------
    # Relationship
    # -------------------------

    intern = relationship(
        "Intern",
        back_populates="certificates"
    )

    def __repr__(self):
        return (
            f"<Certificate {self.certificate_id} | "
            f"{self.intern_id}>"
        )