"""
SQLAlchemy model representing an Intern.
"""

from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship

from backend.database.database import Base


class Intern(Base):
    __tablename__ = "interns"

    intern_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    domain = Column(String, nullable=False)
    mentor_name = Column(String, nullable=False)
    batch = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String, default="active")

    # Relationships
    submissions = relationship(
        "Submission",
        back_populates="intern",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Intern {self.intern_id} - {self.name}>"