from sqlalchemy import func

from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.attendance import Attendance
from backend.models.submission import Submission
from backend.models.github_activity import GitHubActivity
from backend.models.mentor_feedback import MentorFeedback


def get_certificate_eligibility(intern_id: str) -> dict:

    db = SessionLocal()

    try:

        intern = (
            db.query(Intern)
            .filter(Intern.intern_id == intern_id)
            .first()
        )

        if not intern:
            return {"error": "Intern not found"}

        # ----------------------------
        # Attendance Score
        # ----------------------------

        total_days = (
            db.query(Attendance)
            .filter(Attendance.intern_id == intern_id)
            .count()
        )

        present_days = (
            db.query(Attendance)
            .filter(
                Attendance.intern_id == intern_id,
                Attendance.status == "present"
            )
            .count()
        )

        attendance_score = (
            round((present_days / total_days) * 100, 2)
            if total_days
            else 0
        )

        # ----------------------------
        # Task Score
        # ----------------------------

        avg_task_score = (
            db.query(func.avg(Submission.score))
            .filter(Submission.intern_id == intern_id)
            .scalar()
        )

        task_score = round(avg_task_score or 0, 2)

        # ----------------------------
        # GitHub Score
        # ----------------------------

        github = (
            db.query(GitHubActivity)
            .filter(GitHubActivity.intern_id == intern_id)
            .first()
        )

        github_score = (
            round(github.overall_score, 2)
            if github
            else 0
        )

        # ----------------------------
        # Mentor Score
        # ----------------------------

        avg_rating = (
            db.query(func.avg(MentorFeedback.rating))
            .filter(MentorFeedback.intern_id == intern_id)
            .scalar()
        )

        mentor_score = round((avg_rating or 0) * 20, 2)

        # ----------------------------
        # Overall
        # ----------------------------

        overall_score = round(
            (
                attendance_score
                + task_score
                + github_score
                + mentor_score
            )
            / 4,
            2,
        )

        # ----------------------------
        # Eligibility
        # ----------------------------

        if overall_score >= 75:
            status = "Eligible"
        elif overall_score >= 60:
            status = "Needs Improvement"
        else:
            status = "Not Eligible"

        ai_remarks = (
            f"{intern.name} scored {overall_score}%. "
            f"Attendance: {attendance_score}%, "
            f"Task: {task_score}%, "
            f"GitHub: {github_score}%, "
            f"Mentor: {mentor_score}%."
        )

        return {
            "intern_id": intern.intern_id,
            "intern_name": intern.name,
            "attendance_score": attendance_score,
            "task_score": task_score,
            "github_score": github_score,
            "mentor_score": mentor_score,
            "overall_score": overall_score,
            "status": status,
            "ai_remarks": ai_remarks,
        }

    finally:
        db.close()