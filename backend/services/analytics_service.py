from sqlalchemy import func

from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.attendance import Attendance
from backend.models.submission import Submission
from backend.models.github_activity import GitHubActivity
from backend.models.certificate import Certificate


def get_platform_analytics() -> dict:

    db = SessionLocal()

    try:

        total_interns = db.query(Intern).count()

        active_interns = (
            db.query(Intern)
            .filter(func.lower(Intern.status) == "active")
            .count()
        )

        inactive_interns = total_interns - active_interns

        certificates_generated = (
            db.query(Certificate)
            .filter(Certificate.status == "Eligible")
            .count()
        )

        certificates_pending = (
            db.query(Certificate)
            .filter(Certificate.status != "Eligible")
            .count()
        )

        weekly_submissions = db.query(Submission).count()

        attendance_records = db.query(Attendance).all()

        if attendance_records:

            present = sum(
                1
                for a in attendance_records
                if a.status.lower() == "present"
            )

            average_attendance = round(
                (present / len(attendance_records)) * 100,
                2,
            )

        else:
            average_attendance = 0

        domain_distribution = []

        domains = (
            db.query(
                Intern.domain,
                func.count(Intern.intern_id)
            )
            .group_by(Intern.domain)
            .all()
        )

        for domain, count in domains:

            domain_distribution.append(
                {
                    "domain": domain,
                    "count": count
                }
            )

        mentor_workload = []

        mentors = (
            db.query(
                Intern.mentor_name,
                func.count(Intern.intern_id)
            )
            .group_by(Intern.mentor_name)
            .all()
        )

        for mentor, count in mentors:

            mentor_workload.append(
                {
                    "mentor_name": mentor,
                    "intern_count": count
                }
            )

        github_scores = db.query(GitHubActivity.overall_score).all()

        if github_scores:

            avg_github = round(
                sum(x[0] for x in github_scores) /
                len(github_scores),
                2,
            )

        else:
            avg_github = 0

        overall_health = round(
            (
                average_attendance +
                avg_github
            ) / 2,
            2,
        )

        completion_percentage = round(
            (certificates_generated / total_interns) * 100,
            2,
        ) if total_interns else 0

        return {

            "total_interns": total_interns,

            "active_interns": active_interns,

            "inactive_interns": inactive_interns,

            "internship_completion_percentage":
                completion_percentage,

            "certificates_generated":
                certificates_generated,

            "certificates_pending":
                certificates_pending,

            "weekly_submissions":
                weekly_submissions,

            "attendance_statistics": {

                "average_attendance_percentage":
                    average_attendance

            },

            "domain_wise_distribution":
                domain_distribution,

            "mentor_workload":
                mentor_workload,

            "overall_health_score":
                overall_health,

            "ai_insights": {

                "weekly_summary":
                    f"{weekly_submissions} submissions received.",

                "batch_performance_report":
                    f"{completion_percentage}% interns completed internship.",

                "department_statistics":
                    f"{len(domain_distribution)} active domains.",

                "mentor_recommendations": [

                    "Monitor inactive interns.",

                    "Conduct weekly mentor meetings.",

                    "Recognize top performers."

                ]
            }

        }

    finally:

        db.close()