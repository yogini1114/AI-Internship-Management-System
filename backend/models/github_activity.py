"""
SQLAlchemy model representing an intern's GitHub repository activity.
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from backend.database.database import Base


class GitHubActivity(Base):

    __tablename__ = "github_activity"

    activity_id = Column(
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

    repo_name = Column(
        String,
        nullable=False
    )

    repo_url = Column(
        String,
        nullable=False
    )

    primary_language = Column(
        String,
        nullable=True
    )

    commits = Column(
        Integer,
        default=0
    )

    branches = Column(
        Integer,
        default=0
    )

    stars = Column(
        Integer,
        default=0
    )

    forks = Column(
        Integer,
        default=0
    )

    open_issues = Column(
        Integer,
        default=0
    )

    pull_requests = Column(
        Integer,
        default=0
    )

    readme_score = Column(
        Float,
        default=0
    )

    documentation_score = Column(
        Float,
        default=0
    )

    code_quality_score = Column(
        Float,
        default=0
    )

    overall_score = Column(
        Float,
        default=0
    )

    last_commit_date = Column(
        DateTime,
        nullable=True
    )

    last_analysis = Column(
        DateTime,
        default=datetime.utcnow
    )

    # -------------------------
    # Relationship
    # -------------------------

    intern = relationship(
        "Intern",
        back_populates="github_activity"
    )

    def __repr__(self):
        return (
            f"<GitHubActivity {self.repo_name} | "
            f"{self.intern_id}>"
        )