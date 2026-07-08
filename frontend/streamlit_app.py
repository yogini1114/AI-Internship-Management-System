import streamlit as st
from utils.api_client import get

st.set_page_config(
    page_title="AI Internship System",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------
# Hero Section
# ---------------------------------------------------

st.title("🎓 AI Internship Management System")
st.caption("AI Powered Internship Monitoring & Analytics Platform")

st.markdown("""
Welcome to the **AI Internship Management System**.

This platform helps mentors and interns monitor internship progress using AI-powered insights.

### 🚀 What you can do
- 👤 Track Intern Progress
- 📈 Monitor Attendance
- 🧑‍🏫 View Mentor Dashboard
- 📊 Analytics Dashboard
- 🎓 Certificate Eligibility
- 🐙 GitHub Repository Analysis
""")

st.divider()

# ---------------------------------------------------
# Backend Status
# ---------------------------------------------------

st.subheader("🟢 Backend Status")

health = get("/health")

if health:
    st.success("Backend Connected Successfully")
else:
    st.error("Backend Offline")

st.divider()

# ---------------------------------------------------
# Platform Overview
# ---------------------------------------------------

st.subheader("📊 Platform Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("👨‍🎓 Interns", "35")

with c2:
    st.metric("📁 Projects", "35")

with c3:
    st.metric("🧑‍🏫 Mentors", "8")

with c4:
    st.metric("🤖 AI Modules", "5")

st.divider()

# ---------------------------------------------------
# AI Modules
# ---------------------------------------------------

st.subheader("🚀 AI Modules")

left, right = st.columns(2)

with left:

    st.info("""
### 👤 Intern Profile

- Progress Tracking
- Attendance Analysis
- Task Recommendation
- Performance Monitoring
""")

    st.success("""
### 📊 Analytics Dashboard

- Overall Health Score
- Domain-wise Distribution
- Mentor Workload
- AI Insights
""")

    st.warning("""
### 🎓 Certificate Checker

- Certificate Eligibility
- Overall Score
- Attendance Score
- Mentor Score
""")

with right:

    st.info("""
### 🧑‍🏫 Mentor Dashboard

- Top Performers
- Weak Performers
- Pending Tasks
- AI Alerts
""")

    st.success("""
### 🐙 GitHub Analyzer

- Repository Analysis
- Documentation Score
- Code Quality
- AI Suggestions
""")

st.divider()

# ---------------------------------------------------
# Workflow
# ---------------------------------------------------

st.subheader("⚙ System Workflow")

st.code(
"""
Intern
   │
   ▼
Task Submission
   │
   ▼
Attendance + GitHub + Mentor Feedback
   │
   ▼
AI Analysis Engine
   │
   ▼
Analytics Dashboard
   │
   ▼
Certificate Eligibility
""",
language="text"
)

st.divider()

# ---------------------------------------------------
# Tech Stack
# ---------------------------------------------------

st.subheader("🛠 Tech Stack")

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.success("⚡ FastAPI")

with t2:
    st.success("🎨 Streamlit")

with t3:
    st.success("🗄 SQLAlchemy")

with t4:
    st.success("🤖 Groq LLM")

st.divider()

# ---------------------------------------------------
# Features
# ---------------------------------------------------

st.subheader("✨ Project Highlights")

f1, f2 = st.columns(2)

with f1:

    st.markdown("""
### ✅ AI Features

- GitHub Repository Review
- Mentor Dashboard
- Attendance Analytics
- Progress Tracking
- Certificate Eligibility
""")

with f2:

    st.markdown("""
### 💡 Why this?

- Centralized Internship Management
- AI Assisted Insights
- Real-time Analytics
- Performance Evaluation
- Modern Dashboard
""")

st.divider()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.markdown("---")

st.sidebar.markdown(
"""


### AI Internship Management System

🚀 AI Powered Dashboard

Made with ❤️ using

- ⚡ FastAPI
- 🎨 Streamlit
- 🗄 SQLAlchemy
- 🤖 Groq LLM
"""
)