import streamlit as st
import pandas as pd
from utils.api_client import get

st.set_page_config(
    page_title="Mentor Dashboard",
    page_icon="🧑‍🏫",
    layout="wide"
)

st.title("🧑‍🏫 AI Mentor Dashboard")

mentor_name = st.text_input(
    "Filter by Mentor Name (Optional)"
)

response = get(
    "/api/mentor-dashboard",
    params={"mentor_name": mentor_name} if mentor_name else None
)

if response and response.get("data"):

    stats = response["data"]

    # -----------------------------
    # KPI Cards
    # -----------------------------
    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "👨‍🎓 Total Interns",
        stats["total_interns"]
    )

    c2.metric(
        "🟢 Active",
        stats["active_interns"]
    )

    c3.metric(
        "🔴 Inactive",
        stats["inactive_interns"]
    )

    c4.metric(
        "📄 Pending",
        stats["pending_submissions"]
    )

    st.divider()

    # -----------------------------
    # Completion %
    # -----------------------------
    completion = stats["completion_statistics"][
        "average_completion_percentage"
    ]

    st.subheader("📈 Average Completion")

    st.progress(completion / 100)

    st.write(f"Average Completion : **{completion:.2f}%**")

    st.divider()

    # -----------------------------
    # Tables
    # -----------------------------
    left, right = st.columns(2)

    with left:

        st.subheader("🏆 Top Performers")

        top = pd.DataFrame(
            stats["top_performers"]
        )

        if not top.empty:
            st.dataframe(
                top,
                use_container_width=True
            )
        else:
            st.info("No Data")

    with right:

        st.subheader("⚠️ Weak Performers")

        weak = pd.DataFrame(stats["weak_performers"])
        if not weak.empty:
            weak=weak[
                weak["intern_id"]!="string"
            ]

        if not weak.empty:
            st.dataframe(
                weak,
                use_container_width=True
            )
        else:
            st.info("No Data")

    st.divider()

    # -----------------------------
    # Alerts
    # -----------------------------
    st.subheader("🚨 AI Alerts")

    for alert in stats["ai_alerts"]:
        st.warning(alert)

    st.divider()

    # -----------------------------
    # Recommendations
    # -----------------------------
    st.subheader("💡 Mentor Recommendations")

    for rec in stats["mentor_recommendations"]:
        st.success(rec)

else:

    st.error(
        "Unable to fetch Mentor Dashboard."
    )