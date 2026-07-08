"""
SQLAlchemy model representing mentor feedback for interns.
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from backend.database.database import Base


class MentorFeedback(Base):

    __tablename__ = "mentor_feedback"

    feedback_id = Column(
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

    mentor_name = Column(
        String,
        nullable=False
    )

    week_number = Column(
        Integer,
        nullable=False
    )

    feedback_text = Column(
        Text,
        nullable=False
    )

    rating = Column(
        Integer,
        nullable=False
    )

    sentiment_score = Column(
        Float,
        default=0.0
    )

    strengths = Column(
        Text,
        nullable=True
    )

    weaknesses = Column(
        Text,
        nullable=True
    )

    recommendations = Column(
        Text,
        nullable=True
    )

    feedback_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    # ----------------------------
    # Relationship
    # ----------------------------

    intern = relationship(
        "Intern",
        back_populates="mentor_feedback"
    )

    def __repr__(self):
        return (
            f"<MentorFeedback {self.feedback_id} | "
            f"{self.intern_id}>"
        )