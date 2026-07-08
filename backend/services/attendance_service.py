"""
Attendance Service
"""

from backend.ai_modules.attendance_analyzer import service as attendance_ai


def get_intern_attendance(intern_id: str):

    return attendance_ai.get_attendance_summary(
        intern_id
    )