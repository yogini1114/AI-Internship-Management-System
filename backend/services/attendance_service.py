"""
Backend service layer for the Attendance & Performance Analyzer feature.
"""

from ai_modules.attendance_analyzer import service as attendance_ai


def get_intern_attendance(intern_id: str) -> dict:
    """Return attendance analytics for a single intern (dummy data for now)."""
    # TODO (Interns): Replace with attendance_ai.* function calls.
    return {
        "intern_id": intern_id,
        "attendance_percentage_overall": 82.0,
        "attendance_percentage_weekly": 80.0,
        "attendance_percentage_monthly": 85.0,
        "late_count": 2,
        "consecutive_absences": 0,
        "consistency_score": 75.0,
        "trend": "stable",
        "heatmap_data": [],
    }
