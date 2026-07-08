import streamlit as st
import pandas as pd
from utils.api_client import get

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Internship Analytics Dashboard")

with st.spinner("Loading Analytics..."):
    response = get("/api/analytics")

if response and response.get("data"):

    stats = response["data"]

    # ----------------------------------------------------
    # KPI Cards
    # ----------------------------------------------------

    st.subheader("📌 Platform Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "👨‍🎓 Total Interns",
        stats.get("total_interns", 0)
    )

    c2.metric(
        "🟢 Active Interns",
        stats.get("active_interns", 0)
    )

    c3.metric(
        "🎓 Completion %",
        f"{stats.get('internship_completion_percentage',0)}%"
    )

    c4.metric(
        "💚 Health Score",
        stats.get("overall_health_score", 0)
    )

    st.divider()

    # ----------------------------------------------------
    # Attendance
    # ----------------------------------------------------

    st.subheader("🗓 Attendance")

    attendance = stats.get(
        "attendance_statistics",
        {}
    )

    attendance_percent = attendance.get(
        "average_attendance_percentage",
        0
    )

    st.metric(
        "Average Attendance",
        f"{attendance_percent}%"
    )

    st.progress(
        attendance_percent / 100
    )

    st.divider()

    # ----------------------------------------------------
    # Domain Distribution
    # ----------------------------------------------------

    st.subheader("🌐 Domain-wise Distribution")

    domain_data = stats.get(
        "domain_wise_distribution",
        []
    )

    if domain_data:

        df = pd.DataFrame(domain_data)

        if "domain" in df.columns:

            df = df[
                (df["domain"] != "string") &
                (df["domain"] != "") &
                (df["domain"].notna())
            ]

        if not df.empty:

            st.bar_chart(
                df.set_index("domain")
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No domain data available."
            )

    else:

        st.info(
            "No domain distribution available."
        )

    st.divider()

    # ----------------------------------------------------
    # Mentor Workload
    # ----------------------------------------------------

    st.subheader("👨‍🏫 Mentor Workload")

    mentor_data = stats.get(
        "mentor_workload",
        []
    )

    if mentor_data:

        df = pd.DataFrame(
            mentor_data
        )

        if "mentor_name" in df.columns:

            df = df[
                (df["mentor_name"] != "string") &
                (df["mentor_name"] != "") &
                (df["mentor_name"].notna())
            ]

        if not df.empty:

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No mentor workload data."
            )

    else:

        st.info(
            "No mentor workload data."
        )

    st.divider()

    # ----------------------------------------------------
    # Certificates
    # ----------------------------------------------------

    st.subheader("🏆 Certificates")

    c1, c2 = st.columns(2)

    c1.metric(
        "Generated",
        stats.get(
            "certificates_generated",
            0
        )
    )

    c2.metric(
        "Pending",
        stats.get(
            "certificates_pending",
            0
        )
    )

    st.divider()

    # ----------------------------------------------------
    # AI Insights
    # ----------------------------------------------------

    st.subheader("🤖 AI Insights")

    insights = stats.get(
        "ai_insights",
        {}
    )

    weekly = insights.get(
        "weekly_summary",
        ""
    )

    batch = insights.get(
        "batch_performance_report",
        ""
    )

    department = insights.get(
        "department_statistics",
        ""
    )

    recommendations = insights.get(
        "mentor_recommendations",
        []
    )

    if weekly and weekly != "string":
        st.info(
            f"📅 {weekly}"
        )

    if batch and batch != "string":
        st.success(
            f"📈 {batch}"
        )

    if department and department != "string":
        st.warning(
            f"🏢 {department}"
        )

    if recommendations:

        st.markdown(
            "### 💡 Recommendations"
        )

        for rec in recommendations:

            if rec != "string":
                st.write(f"✅ {rec}")

else:

    st.error(
        "❌ Unable to connect to Analytics API."
    )