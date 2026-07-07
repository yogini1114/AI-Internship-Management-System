"""
Backend service layer for the Internship Analytics Dashboard feature.
"""

from ai_modules.analytics_dashboard import service as analytics_ai


def get_platform_analytics() -> dict:
    """Return platform-wide analytics (dummy data for now)."""
    # TODO (Interns): Replace with analytics_ai.* function calls.
    return {
        "total_interns": 40,
        "active_interns": 34,
        "internship_completion_percentage": 68.5,
        "certificates_generated": 12,
        "certificates_pending": 9,
        "weekly_submissions": 112,
        "attendance_statistics": {"average_attendance_percentage": 81.2},
        "domain_wise_distribution": [
            {"domain": "Backend Development", "count": 14},
            {"domain": "AI/ML", "count": 12},
            {"domain": "Frontend Development", "count": 9},
            {"domain": "Data Science", "count": 5},
        ],
        "mentor_workload": [
            {"mentor_name": "Placeholder Mentor A", "intern_count": 20},
            {"mentor_name": "Placeholder Mentor B", "intern_count": 20},
        ],
        "overall_health_score": 74.0,
        "ai_insights": {
            "weekly_summary": "TODO: AI-generated weekly summary goes here.",
            "batch_performance_report": "TODO: AI-generated batch report goes here.",
            "department_statistics": "TODO: AI-generated department stats go here.",
            "mentor_recommendations": ["TODO: AI-generated recommendation goes here."],
        },
    }
