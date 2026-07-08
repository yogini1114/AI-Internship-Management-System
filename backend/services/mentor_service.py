from sqlalchemy import func

from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.submission import Submission
from backend.models.github_activity import GitHubActivity
from backend.models.mentor_feedback import MentorFeedback


def get_mentor_dashboard(mentor_name: str = None):

    db = SessionLocal()

    try:

        interns_query = db.query(Intern)

        if mentor_name:
            interns_query = interns_query.filter(
                Intern.mentor_name == mentor_name
            )

        interns = interns_query.all()

        total_interns = len(interns)

        active_interns = len(
            [i for i in interns if i.status.lower() == "active"]
        )

        inactive_interns = total_interns - active_interns

        dashboard = []

        for intern in interns:

            task_avg = (
                db.query(func.avg(Submission.score))
                .filter(
                    Submission.intern_id == intern.intern_id
                )
                .scalar()
            ) or 0

            github = (
                db.query(GitHubActivity)
                .filter(
                    GitHubActivity.intern_id == intern.intern_id
                )
                .first()
            )

            github_score = (
                github.overall_score
                if github
                else 0
            )

            mentor_avg = (
                db.query(func.avg(MentorFeedback.rating))
                .filter(
                    MentorFeedback.intern_id == intern.intern_id
                )
                .scalar()
            ) or 0

            mentor_score = mentor_avg * 20

            overall = round(
                (
                    task_avg +
                    github_score +
                    mentor_score
                ) / 3,
                2,
            )

            dashboard.append(
                {
                    "intern_id": intern.intern_id,
                    "name": intern.name,
                    "overall_score": overall,
                }
            )

        dashboard.sort(
            key=lambda x: x["overall_score"],
            reverse=True,
        )

        top_performers = dashboard[:5]

        weak_performers = dashboard[-5:]

        avg_completion = round(
            sum(
                x["overall_score"]
                for x in dashboard
            ) / total_interns,
            2,
        ) if total_interns else 0

        pending = (
            db.query(Submission)
            .filter(
                Submission.status == "pending"
            )
            .count()
        )

        weekly = db.query(Submission).count()

        alerts = []

        if pending > 10:
            alerts.append(
                f"{pending} submissions are still pending."
            )

        if inactive_interns > 0:
            alerts.append(
                f"{inactive_interns} interns are inactive."
            )

        recommendations = [
            "Schedule mentoring sessions for weak performers.",
            "Recognize top performers.",
            "Review pending submissions weekly.",
        ]

        return {
            "total_interns": total_interns,
            "active_interns": active_interns,
            "inactive_interns": inactive_interns,
            "weekly_submissions": weekly,
            "pending_submissions": pending,
            "completion_statistics": {
                "average_completion_percentage": avg_completion
            },
            "top_performers": top_performers,
            "weak_performers": weak_performers,
            "ai_alerts": alerts,
            "mentor_recommendations": recommendations,
        }

    finally:
        db.close()