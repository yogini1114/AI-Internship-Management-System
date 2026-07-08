"""
Backend service layer for the Progress Tracker feature.

Fetches real progress data from the database.
"""

from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.task import Task
from backend.models.submission import Submission


def get_intern_progress(intern_id: str) -> dict:
    """
    Return overall progress of a single intern.
    """

    db: Session = SessionLocal()

    try:

        intern = (
            db.query(Intern)
            .filter(Intern.intern_id == intern_id)
            .first()
        )

        if intern is None:
            return {
                "error": "Intern not found"
            }

        # ------------------------------------
        # Total tasks assigned for intern domain
        # ------------------------------------

        total_tasks = (
            db.query(Task)
            .filter(Task.domain == intern.domain)
            .count()
        )

        # ------------------------------------
        # Completed submissions
        # ------------------------------------

        completed_tasks = (
            db.query(Submission)
            .filter(
                Submission.intern_id == intern_id,
                Submission.status.in_(["on_time", "late"])
            )
            .count()
        )

        # ------------------------------------
        # Pending submissions
        # ------------------------------------

        pending_tasks = max(
            total_tasks - completed_tasks,
            0
        )

        # ------------------------------------
        # Late submissions
        # ------------------------------------

        late_submissions = (
            db.query(Submission)
            .filter(
                Submission.intern_id == intern_id,
                Submission.status == "late"
            )
            .count()
        )

        # ------------------------------------
        # Completion %
        # ------------------------------------

        if total_tasks == 0:
            completion_percentage = 0.0
        else:
            completion_percentage = round(
                (completed_tasks / total_tasks) * 100,
                2
            )

        # ------------------------------------
        # Slow Progress Flag
        # ------------------------------------

        is_slow_progress = completion_percentage < 50

        # ------------------------------------
        # AI Summary (placeholder)
        # ------------------------------------

        ai_summary = (
            f"{intern.name} has completed "
            f"{completed_tasks} out of "
            f"{total_tasks} tasks."
        )

        # ------------------------------------
        # Suggested Next Tasks
        # ------------------------------------

        suggestions = []

        if pending_tasks > 0:
            suggestions.append("Complete pending internship tasks.")

        if late_submissions > 0:
            suggestions.append("Avoid late submissions.")

        if completion_percentage >= 80:
            suggestions.append("Start advanced project.")

        if len(suggestions) == 0:
            suggestions.append("Maintain your current progress.")

        return {

            "intern_id": intern.intern_id,

            "intern_name": intern.name,

            "domain": intern.domain,

            "total_tasks": total_tasks,

            "completed_tasks": completed_tasks,

            "pending_tasks": pending_tasks,

            "late_submissions": late_submissions,

            "completion_percentage": completion_percentage,

            "is_slow_progress": is_slow_progress,

            "ai_summary": ai_summary,

            "suggested_next_tasks": suggestions,
        }

    finally:
        db.close()


def get_inactive_interns() -> list:
    """
    Return inactive interns.
    """

    db: Session = SessionLocal()

    try:

        inactive = (
            db.query(Intern)
            .filter(Intern.status != "Active")
            .all()
        )

        return [
            {
                "intern_id": intern.intern_id,
                "name": intern.name,
                "status": intern.status,
            }
            for intern in inactive
        ]

    finally:
        db.close()