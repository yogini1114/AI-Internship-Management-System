"""
Backend service layer for the Certificate Eligibility Analyzer feature.
"""

from ai_modules.certificate_analyzer import service as certificate_ai


def get_certificate_eligibility(intern_id: str) -> dict:
    """Return certificate eligibility decision (dummy data for now)."""
    # TODO (Interns): Replace with certificate_ai.evaluate_certificate_eligibility()
    return {
        "intern_id": intern_id,
        "status": "Needs Improvement",
        "explanation": (
            "TODO: Replace with a real AI-generated explanation based on "
            "attendance, task completion, submissions, mentor feedback, "
            "and GitHub activity."
        ),
    }
