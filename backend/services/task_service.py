"""
Backend service layer for the Task Recommendation feature.
"""

from ai_modules.task_recommender import service as task_ai


def get_task_recommendations(intern_id: str) -> dict:
    """Return personalized task/resource recommendations (dummy data for now)."""
    # TODO (Interns): Replace with task_ai.* function calls.
    return {
        "intern_id": intern_id,
        "weak_skills": ["TODO: weak skill 1"],
        "recommended_courses": ["TODO: course 1"],
        "recommended_practice_tasks": ["TODO: practice task 1"],
        "recommended_projects": ["TODO: project 1"],
        "recommended_reading_material": ["TODO: reading material 1"],
        "revision_topics": ["TODO: revision topic 1"],
    }
