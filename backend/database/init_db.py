"""
Database initialization script.

Creates all tables and seeds sample data from datasets/.
"""

import csv
import os
from datetime import datetime

from backend.database.database import (
    Base,
    engine,
    SessionLocal,
)

from backend.models import (
    Intern,
    Task,
    Attendance,
    Submission,
    MentorFeedback,
    Certificate,
    GitHubActivity,
)

# --------------------------------------------
# Dataset Path
# --------------------------------------------

DATASET_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "datasets",
)

# --------------------------------------------
# Utility Functions
# --------------------------------------------


def parse_date(value):
    if not value:
        return None

    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except Exception:
        return None


def parse_datetime(value):
    if not value:
        return None

    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt)
        except Exception:
            pass

    return None


def get_reader(filename):
    path = os.path.join(DATASET_DIR, filename)

    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


# --------------------------------------------
# Database
# --------------------------------------------


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables Created")


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Database Reset Complete")


# --------------------------------------------
# Seed Interns
# --------------------------------------------


def seed_interns():

    db = SessionLocal()

    rows = get_reader("interns.csv")

    count = 0

    for row in rows:

        exists = (
            db.query(Intern)
            .filter(Intern.intern_id == row["intern_id"])
            .first()
        )

        if exists:
            continue

        intern = Intern(
            intern_id=row["intern_id"],
            name=row["name"],
            email=row["email"],
            domain=row["domain"],
            mentor_name=row["mentor_name"],
            batch=row["batch"],
            start_date=parse_date(row["start_date"]),
            end_date=parse_date(row["end_date"]),
            status=row.get("status", "Active"),
        )

        db.add(intern)
        count += 1

    db.commit()
    db.close()

    print(f"✅ Seeded {count} interns")


# --------------------------------------------
# Seed Tasks
# --------------------------------------------


def seed_tasks():

    db = SessionLocal()

    rows = get_reader("tasks.csv")

    count = 0

    for row in rows:

        exists = (
            db.query(Task)
            .filter(Task.task_id == row["task_id"])
            .first()
        )

        if exists:
            continue

        task = Task(
            task_id=row["task_id"],
            title=row["title"],
            domain=row["domain"],
            week_number=int(row["week_number"]),
            difficulty=row.get("difficulty", "Beginner"),
        )

        db.add(task)

        count += 1

    db.commit()
    db.close()

    print(f"✅ Seeded {count} tasks")
    
# --------------------------------------------
# Seed Attendance
# --------------------------------------------

def seed_attendance():

    db = SessionLocal()

    rows = get_reader("attendance.csv")

    count = 0

    for row in rows:

        exists = (
            db.query(Attendance)
            .filter(
                Attendance.intern_id == row["intern_id"],
                Attendance.date == parse_date(row["date"]),
            )
            .first()
        )

        if exists:
            continue

        attendance = Attendance(
            intern_id=row["intern_id"],
            date=parse_date(row["date"]),
            status=row["status"],
            remarks=row.get("remarks"),
        )

        db.add(attendance)

        count += 1

    db.commit()
    db.close()

    print(f"✅ Seeded {count} attendance records")


# --------------------------------------------
# Seed Submissions
# --------------------------------------------

def seed_submissions():

    db = SessionLocal()

    rows = get_reader("submissions.csv")

    count = 0

    for row in rows:

        exists = (
            db.query(Submission)
            .filter(
                Submission.submission_id == row["submission_id"]
            )
            .first()
        )

        if exists:
            continue

        submission = Submission(

            submission_id=row["submission_id"],

            intern_id=row["intern_id"],

            task_id=row["task_id"],

            # CSV me github link nahi hai
            github_link="https://github.com/sample/repository",

            submitted_at=parse_datetime(
                row["submission_date"]
            ) or datetime.utcnow(),

            status=row["status"],

            score=float(row["score"])
            if row.get("score")
            else None,
        )

        db.add(submission)

        count += 1

    db.commit()
    db.close()

    print(f"✅ Seeded {count} submissions")
    
# --------------------------------------------
# Seed GitHub Activity
# --------------------------------------------

def seed_github_activity():

    db = SessionLocal()

    rows = get_reader("github_activity.csv")

    count = 0

    for row in rows:

        exists = (
            db.query(GitHubActivity)
            .filter(
                GitHubActivity.intern_id == row["intern_id"],
                GitHubActivity.repo_name == row["repo_name"],
            )
            .first()
        )

        if exists:
            continue

        activity = GitHubActivity(

            intern_id=row["intern_id"],

            repo_name=row["repo_name"],

            repo_url=row.get(
                "repo_url",
                "https://github.com/sample/repository",
            ),

            primary_language=row.get(
                "primary_language",
                "Unknown",
            ),

            commits=int(row.get("commits", 0)),

            branches=int(row.get("branches", 0)),

            stars=int(row.get("stars", 0)),

            forks=int(row.get("forks", 0)),

            open_issues=int(row.get("open_issues", 0)),

            pull_requests=int(row.get("pull_requests", 0)),

            readme_score=float(row.get("readme_score", 0)),

            documentation_score=float(
                row.get("documentation_score", 0)
            ),

            code_quality_score=float(
                row.get("code_quality_score", 0)
            ),

            overall_score=float(
                row.get("overall_score", 0)
            ),

            last_commit_date=parse_datetime(
                row.get("last_commit_date")
            ),
        )

        db.add(activity)

        count += 1

    db.commit()

    db.close()

    print(f"✅ Seeded {count} GitHub Activity records")


# --------------------------------------------
# Seed Mentor Feedback
# --------------------------------------------

def seed_mentor_feedback():

    db = SessionLocal()

    rows = get_reader("mentor_feedback.csv")

    count = 0

    for row in rows:

        feedback = MentorFeedback(

            intern_id=row["intern_id"],

            mentor_name=row["mentor_name"],

            week_number=int(row["week_number"]),

            feedback_text=row["feedback_text"],

            rating=int(row["rating"]),

            sentiment_score=float(
                row.get("sentiment_score", 0)
            ),

            strengths=row.get("strengths"),

            weaknesses=row.get("weaknesses"),

            recommendations=row.get("recommendations"),
        )

        db.add(feedback)

        count += 1

    db.commit()

    db.close()

    print(f"✅ Seeded {count} mentor feedback")
    
# --------------------------------------------
# Seed Certificates
# --------------------------------------------

def seed_certificates():

    db = SessionLocal()

    rows = get_reader("certificates.csv")

    count = 0

    for row in rows:

        exists = (
            db.query(Certificate)
            .filter(
                Certificate.intern_id == row["intern_id"]
            )
            .first()
        )

        if exists:
            continue

        certificate = Certificate(

            intern_id=row["intern_id"],

            status=row.get(
                "status",
                "Pending"
            ),

            issue_date=parse_datetime(
                row.get("issue_date")
            ),

            overall_score=int(
                row.get("overall_score", 0)
            ),

            attendance_score=int(
                row.get("attendance_score", 0)
            ),

            github_score=int(
                row.get("github_score", 0)
            ),

            task_score=int(
                row.get("task_score", 0)
            ),

            mentor_score=int(
                row.get("mentor_score", 0)
            ),

            ai_remarks=row.get(
                "ai_remarks",
                row.get("remarks", "")
            )
        )

        db.add(certificate)

        count += 1

    db.commit()

    db.close()

    print(f"✅ Seeded {count} certificates")


# --------------------------------------------
# Main
# --------------------------------------------

if __name__ == "__main__":

    print("\n🚀 Initializing Database...\n")

    reset_database()

    seed_interns()

    seed_tasks()

    seed_attendance()

    seed_submissions()

    seed_github_activity()

    seed_mentor_feedback()

    seed_certificates()

    print("\n🎉 Database Ready Successfully!")