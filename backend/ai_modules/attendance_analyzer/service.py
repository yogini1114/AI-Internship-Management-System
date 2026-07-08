"""
AI Attendance Analyzer

Provides attendance statistics and insights.
"""

from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.models.attendance import Attendance


def get_attendance_summary(intern_id: str) -> dict:

    db: Session = SessionLocal()

    try:

        records = (
            db.query(Attendance)
            .filter(
                Attendance.intern_id == intern_id
            )
            .order_by(Attendance.date)
            .all()
        )

        if not records:

            return {
                "intern_id": intern_id,
                "overall_attendance": 0,
                "weekly_attendance": 0,
                "monthly_attendance": 0,
                "present_days": 0,
                "absent_days": 0,
                "late_days": 0,
                "consecutive_absences": 0,
                "consistency_score": 0,
                "trend": "No Data",
                "heatmap_data": [],
                "ai_summary": "No attendance records found."
            }

        total = len(records)

        present = sum(
            1
            for r in records
            if r.status.lower() == "present"
        )

        absent = sum(
            1
            for r in records
            if r.status.lower() == "absent"
        )

        late = sum(
            1
            for r in records
            if r.status.lower() == "late"
        )

        attendance_percentage = round(
            (present + late) / total * 100,
            2
        )

        # consecutive absences

        consecutive = 0
        maximum = 0

        for r in records:

            if r.status.lower() == "absent":

                consecutive += 1

                maximum = max(
                    maximum,
                    consecutive
                )

            else:

                consecutive = 0

        consistency = round(
            attendance_percentage - maximum * 2,
            2
        )

        if consistency < 0:
            consistency = 0

        if attendance_percentage >= 90:

            trend = "Excellent"

        elif attendance_percentage >= 75:

            trend = "Stable"

        else:

            trend = "Needs Improvement"

        heatmap = []

        for r in records:

            heatmap.append({

                "date": str(r.date),

                "status": r.status

            })

        return {

            "intern_id": intern_id,

            "overall_attendance": attendance_percentage,

            "weekly_attendance": attendance_percentage,

            "monthly_attendance": attendance_percentage,

            "present_days": present,

            "absent_days": absent,

            "late_days": late,

            "consecutive_absences": maximum,

            "consistency_score": consistency,

            "trend": trend,

            "heatmap_data": heatmap,

            "ai_summary": (
                f"Attendance is {attendance_percentage}% "
                f"with {late} late entries."
            )
        }

    finally:

        db.close()