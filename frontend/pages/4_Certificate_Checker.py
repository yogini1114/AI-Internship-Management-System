"""Streamlit page: Certificate Eligibility Checker."""

import streamlit as st
from utils.api_client import get

st.set_page_config(
    page_title="Certificate Checker",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Certificate Eligibility Checker")

intern_id = st.text_input(
    "Enter Intern ID",
    value="INT-0001"
)

if st.button("Check Eligibility"):

    response = get(f"/api/certificate/{intern_id}")

    if response and response.get("data"):

        result = response["data"]

        status = result.get("status", "Unknown")

        st.subheader("🏆 Certificate Status")

        if status == "Eligible":
            st.success(f"✅ {status}")

        elif status == "Not Eligible":
            st.error(f"❌ {status}")

        else:
            st.warning(f"⚠️ {status}")

        st.divider()

        # ------------------------------------
        # Metrics
        # ------------------------------------

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(
                "Overall Score",
                result.get("overall_score", 0)
            )

        with col2:
            st.metric(
                "Attendance",
                result.get("attendance_score", 0)
            )

        with col3:
            st.metric(
                "GitHub",
                result.get("github_score", 0)
            )

        with col4:
            st.metric(
                "Task Score",
                result.get("task_score", 0)
            )

        with col5:
            st.metric(
                "Mentor Score",
                result.get("mentor_score", 0)
            )

        st.divider()

        # ------------------------------------
        # AI Remarks
        # ------------------------------------

        st.subheader("🤖 AI Remarks")

        remarks = result.get("ai_remarks", "")

        if remarks:
            st.info(remarks)
        else:
            st.info("No AI remarks available.")

    else:
        st.error("Could not load certificate data from the backend.")
