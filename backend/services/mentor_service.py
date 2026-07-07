"""
Backend service layer for the Mentor Dashboard feature.
"""

from ai_modules.mentor_dashboard import service as mentor_ai


def get_mentor_dashboard(mentor_name: str = None) -> dict:
    """Return mentor dashboard statistics + AI insights (dummy data for now)."""
    # TODO (Interns): Replace with mentor_ai.get_dashboard_stats() etc.
    return {
        "total_interns": 40,
        "active_interns": 34,
        "inactive_interns": 6,
        "weekly_submissions": 112,
        "pending_submissions": 18,
        "completion_statistics": {"average_completion_percentage": 68.5},
        "top_performers": [
            {"intern_id": "INT-0001", "name": "Placeholder Intern A", "score": 96.5},
        ],
        "weak_performers": [
            {"intern_id": "INT-0007", "name": "Placeholder Intern B", "score": 41.2},
        ],
        "ai_alerts": [
            "TODO: e.g. '12 interns are falling behind due to missing weekly submissions.'",
        ],
        "mentor_recommendations": [
            "TODO: e.g. 'Schedule a check-in with inactive interns in Batch A.'",
        ],
    }
