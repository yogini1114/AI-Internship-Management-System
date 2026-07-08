"""
SQLAlchemy model representing an internship Task.
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from backend.database.database import Base


class Task(Base):

    __tablename__ = "tasks"

    task_id = Column(
        String,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    domain = Column(
        String,
        nullable=False
    )

    week_number = Column(
        Integer,
        nullable=False
    )

    difficulty = Column(
        String,
        default="Beginner"
    )

    # -------------------------
    # Relationships
    # -------------------------

    submissions = relationship(
        "Submission",
        back_populates="task",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"<Task {self.task_id} | "
            f"{self.title}>"
        )
        