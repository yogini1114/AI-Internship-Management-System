from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from backend.database.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    intern_id = Column(
        String,
        ForeignKey("interns.intern_id"),
        nullable=False
    )

    date = Column(
        Date,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    remarks = Column(
        String,
        nullable=True
    )

    intern = relationship(
        "Intern",
        back_populates="attendance"
    )

    def __repr__(self):
        return f"<Attendance {self.attendance_id}>"