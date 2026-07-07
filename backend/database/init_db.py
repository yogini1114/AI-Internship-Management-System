"""
Database initialization script.

Run this once to create all tables defined in backend/models/.
Optionally loads the sample CSV datasets from /datasets into the
database so the API has data to serve during development.

Usage:
    python -m backend.database.init_db

TODO (Interns):
- Extend this script to also seed MentorFeedback, Certificate and
  GitHubActivity tables from their respective CSV files.
- Add a `--reset` flag to drop and recreate all tables.
"""

import csv
import os

from backend.database.database import Base, engine, SessionLocal
from backend.models import intern, task, attendance, submission, mentor_feedback, certificate, github_activity, analytics  # noqa: F401

DATASETS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "datasets")


def create_tables():
    """Create all tables in the database if they do not already exist."""
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")


def seed_interns():
    """
    Load datasets/interns.csv into the Intern table.

    TODO (Interns):
    - Add error handling for malformed rows.
    - Avoid duplicate inserts if the script is run multiple times.
    """
    from backend.models.intern import Intern

    csv_path = os.path.join(DATASETS_DIR, "interns.csv")
    if not os.path.exists(csv_path):
        print(f"⚠️  {csv_path} not found, skipping intern seeding.")
        return

    db = SessionLocal()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            exists = db.query(Intern).filter_by(intern_id=row["intern_id"]).first()
            if exists:
                continue
            intern_obj = Intern(
                intern_id=row["intern_id"],
                name=row["name"],
                email=row["email"],
                domain=row["domain"],
                mentor_name=row["mentor_name"],
                batch=row["batch"],
                start_date=row["start_date"],
                end_date=row["end_date"],
                status=row["status"],
            )
            db.add(intern_obj)
    db.commit()
    db.close()
    print("✅ Interns seeded successfully.")


if __name__ == "__main__":
    create_tables()
    seed_interns()
    # TODO (Interns): call additional seed_* functions for other tables here.
