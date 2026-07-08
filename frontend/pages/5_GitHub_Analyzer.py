"""Streamlit page: GitHub Repository Analyzer."""

import streamlit as st
from utils.api_client import post

st.set_page_config(
    page_title="GitHub Analyzer",
    page_icon="🐙",
    layout="wide"
)

st.title("🐙 AI GitHub & Code Review Assistant")

repo_url = st.text_input(
    "Enter GitHub Repository URL",
    value="https://github.com/langchain-ai/langchain"
)

if st.button("Analyze Repository"):

    response = post(
        "/api/github-analysis",
        json_body={
            "repo_url": repo_url
        }
    )

    if response and response.get("data"):

        result = response["data"]

        if "error" in result:
            st.error(result["error"])
            st.stop()

        analysis = result.get("analysis", {})

        st.subheader("📊 Repository Information")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("⭐ Stars", result.get("stars", 0))
        col2.metric("🍴 Forks", result.get("forks", 0))
        col3.metric("👀 Watchers", result.get("watchers", 0))
        col4.metric("🐍 Language", result.get("language", "N/A"))

        st.divider()

        st.subheader("📈 AI Scores")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Overall",
            analysis.get("overall_score", 0)
        )

        col2.metric(
            "Documentation",
            analysis.get("documentation_score", 0)
        )

        col3.metric(
            "Code Quality",
            analysis.get("code_quality_score", 0)
        )

        col4.metric(
            "Git Practices",
            analysis.get("git_practices_score", 0)
        )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:
            st.subheader("✅ Strengths")

            strengths = analysis.get("strengths", [])

            if strengths:
                for s in strengths:
                    st.success(s)
            else:
                st.info("No strengths available.")

        with c2:
            st.subheader("⚠️ Weaknesses")

            weaknesses = analysis.get("weaknesses", [])

            if weaknesses:
                for w in weaknesses:
                    st.warning(w)
            else:
                st.success("No major weaknesses found.")

        st.divider()

        st.subheader("🤖 AI Suggestions")

        suggestions = analysis.get("suggestions", [])

        if suggestions:
            for suggestion in suggestions:
                st.info(suggestion)
        else:
            st.success("Repository looks good!")

        st.divider()

        st.subheader("📦 Repository Details")

        st.write("**Repository:**", result.get("repo_name"))
        st.write("**Default Branch:**", result.get("default_branch"))
        st.write("**Open Issues:**", result.get("open_issues"))

        with st.expander("View Complete API Response"):
            st.json(result)

    else:
        st.error("❌ Could not analyze repository.")