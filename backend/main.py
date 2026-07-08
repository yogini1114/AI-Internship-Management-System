"""
SkillNova AI-Powered Internship Management & Mentor Intelligence System
Backend entry point.

Run with:
    uvicorn backend.main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config.settings import settings

# Existing Routes
from backend.api.routes import (
    progress_tracker,
    mentor_dashboard,
    attendance,
    task_recommendation,
    github_analysis,
    certificate_analysis,
    analytics_dashboard,
)

# New CRUD Route
from backend.api.routes import intern
from backend.api.routes import task
from backend.api.routes import submission
from backend.api.routes import attendance_crud
from backend.api.routes import analytics_dashboard


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "AI-powered backend services for the SkillNova Internship Platform."
    ),
)

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Existing Routers
# -----------------------------
app.include_router(progress_tracker.router)
app.include_router(mentor_dashboard.router)
app.include_router(attendance.router)
app.include_router(task_recommendation.router)
app.include_router(github_analysis.router)
app.include_router(certificate_analysis.router)
app.include_router(analytics_dashboard.router)


# -----------------------------
# CRUD Routers
# -----------------------------
app.include_router(intern.router)
app.include_router(task.router)
app.include_router(submission.router)
app.include_router(attendance_crud.router)


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/", tags=["Health"])
def root():
    return {
        "message": f"{settings.APP_NAME} is running.",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "status": "ok",
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}