"""
Backend service layer for the Progress Tracker feature.

Bridges the API routes and the ai_modules/progress_tracker AI logic.
Currently returns dummy/placeholder data so the API is runnable
before the AI logic is implemented.
"""

from ai_modules.progress_tracker import service as progress_ai


def get_intern_progress(intern_id: str) -> dict:
    """Return progress data for a single intern (dummy data for now)."""
    # TODO (Interns): Replace with real DB-backed logic via progress_ai.*
    dummy = {
        "intern_id": intern_id,
        "total_tasks": 10,
        "completed_tasks": 6,
        "pending_tasks": 3,
        "late_submissions": 1,
        "completion_percentage": 60.0,
        "is_slow_progress": False,
        "ai_summary": "TODO: Implement AI progress summary generation.",
        "suggested_next_tasks": ["TODO: task suggestion 1", "TODO: task suggestion 2"],
    }
    return dummy


def get_inactive_interns() -> list:
    """Return the list of currently inactive interns (dummy data for now)."""
    # TODO (Interns): Wire this to progress_ai.detect_inactive_interns()
    return ["INT-0007", "INT-0021"]
