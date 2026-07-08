import streamlit as st
from utils.api_client import get

st.set_page_config(page_title="Intern Profile", page_icon="👤")

st.title("👤 Intern Profile")

intern_id = st.text_input(
    "Enter Intern ID",
    value="INT-0001"
)

if st.button("Load Profile"):

    progress = get(f"/api/progress/{intern_id}")
    attendance = get(f"/api/attendance/{intern_id}")
    task = get(f"/api/task-recommendations/{intern_id}")

    if progress and attendance:

        p = progress["data"]
        a = attendance["data"]

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Progress",
            f"{p['completion_percentage']}%"
        )

        col2.metric(
            "Attendance",
            f"{a['overall_attendance']}%"
        )

        col3.metric(
            "Consistency",
            f"{a['consistency_score']}"
        )

        st.divider()

        st.subheader("Attendance Trend")

        st.progress(
            a["overall_attendance"] / 100
        )

        st.write("Trend :", a["trend"])

        st.divider()

        st.subheader("Recommended Skills")

        if task:

            t = task["data"]

            st.write("Weak Skills")

            for skill in t["weak_skills"]:
                st.error(skill)

            st.write("Courses")

            for course in t["recommended_courses"]:
                st.success(course)

            st.write("Projects")

            for project in t["recommended_projects"]:
                st.info(project)

            st.write("Practice Tasks")

            for practice in t["recommended_practice_tasks"]:
                st.warning(practice)

    else:
        st.error("Intern not found.")