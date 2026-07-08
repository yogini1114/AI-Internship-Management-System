from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.submission import Submission
from backend.models.task import Task


def get_task_recommendations(intern_id: str) -> dict:

    db = SessionLocal()

    try:

        intern = (
            db.query(Intern)
            .filter(Intern.intern_id == intern_id)
            .first()
        )

        if not intern:
            return {
                "error": "Intern not found"
            }

        submissions = (
            db.query(Submission)
            .filter(Submission.intern_id == intern_id)
            .all()
        )

        weak_skills = []
        recommended_courses = []
        recommended_practice_tasks = []
        recommended_projects = []
        recommended_reading_material = []
        revision_topics = []

        low_score_tasks = []

        for sub in submissions:

            if sub.score is not None and sub.score < 60:

                task = (
                    db.query(Task)
                    .filter(Task.task_id == sub.task_id)
                    .first()
                )

                if task:

                    low_score_tasks.append(task)

        if not low_score_tasks:

            return {

                "intern_id": intern.intern_id,

                "intern_name": intern.name,

                "message": "Excellent performance. Keep learning!",

                "weak_skills": [],

                "recommended_courses": [
                    "Advanced System Design",
                    "Cloud Computing"
                ],

                "recommended_practice_tasks": [],

                "recommended_projects": [
                    "Full Stack Internship Portal"
                ],

                "recommended_reading_material": [
                    "Design Patterns",
                    "Clean Code"
                ],

                "revision_topics": []
            }

        domains = list(set([t.domain for t in low_score_tasks]))

        for domain in domains:

            weak_skills.append(domain)

            recommended_courses.append(
                f"{domain} Complete Course"
            )

            recommended_projects.append(
                f"{domain} Mini Project"
            )

            recommended_reading_material.append(
                f"{domain} Documentation"
            )

        for task in low_score_tasks:

            recommended_practice_tasks.append(
                task.title
            )

            revision_topics.append(
                task.title
            )

        return {

            "intern_id": intern.intern_id,

            "intern_name": intern.name,

            "weak_skills": weak_skills,

            "recommended_courses":
                recommended_courses,

            "recommended_practice_tasks":
                recommended_practice_tasks,

            "recommended_projects":
                recommended_projects,

            "recommended_reading_material":
                recommended_reading_material,

            "revision_topics":
                revision_topics

        }

    finally:

        db.close()