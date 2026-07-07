"""
AI Internship Progress Tracker - Service Layer

Responsible for turning raw task/submission/attendance data into
progress insights for a single intern or a whole batch.

TODO (Interns):
1. Implement `get_completion_percentage()` using real Task/Submission data.
2. Implement `predict_slow_progress()` - use a simple heuristic first
   (e.g. completion_rate < 50% and week_number > 2), then upgrade to
   a trained classifier (Scikit-learn) if time allows.
3. Implement `detect_inactive_interns()` - e.g. no submissions in last 7 days.
4. Implement `generate_progress_summary()` - call an LLM (Gemini/Groq via
   LangChain) to turn the raw stats into a natural-language paragraph.
5. Implement `suggest_next_tasks()` - recommend the next logical task(s)
   based on completed tasks and domain.
"""

from typing import Dict, List


def get_completion_percentage(intern_id: str) -> float:
    """
    Calculate what percentage of assigned tasks an intern has completed.

    TODO: Query Submission + Task tables and compute:
          completed_tasks / total_assigned_tasks * 100
    """
    # Placeholder dummy value
    return 0.0


def get_progress_summary(intern_id: str) -> Dict:
    """
    Return a structured progress summary for one intern.

    TODO: Replace the dummy dict below with real aggregated data:
          - total tasks, completed tasks, pending tasks, late submissions
          - overall completion percentage
          - daily/weekly progress trend
    """
    return {
        "intern_id": intern_id,
        "total_tasks": 0,
        "completed_tasks": 0,
        "pending_tasks": 0,
        "late_submissions": 0,
        "completion_percentage": 0.0,
        "note": "TODO: replace with real computed values",
    }


def predict_slow_progress(intern_id: str) -> bool:
    """
    Predict whether an intern is progressing slower than expected.

    TODO: Start with a rule-based heuristic, then optionally train a
          Scikit-learn classifier (e.g. Logistic Regression) using
          historical completion-rate data as features.
    """
    return False


def detect_inactive_interns() -> List[str]:
    """
    Return a list of intern_ids who have had no activity
    (no submissions, no attendance) in the last N days.

    TODO: Implement the actual "no activity" query against the database.
    """
    return []


def generate_ai_progress_narrative(intern_id: str) -> str:
    """
    Use an LLM to turn structured progress stats into a natural-language
    summary, e.g. "Intern X has completed 8/10 tasks and is on track."

    TODO: Wire this up to Gemini API / Groq via LangChain.
    """
    return "TODO: AI-generated progress narrative goes here."


def suggest_next_tasks(intern_id: str) -> List[str]:
    """
    Suggest the next task(s) an intern should attempt.

    TODO: Base this on completed tasks + domain + difficulty progression.
    """
    return []
