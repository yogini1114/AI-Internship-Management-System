from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.models.task import Task
from backend.api.schemas.task import (
    TaskCreate,
    TaskResponse,
)

router = APIRouter(
    prefix="/api/tasks",
    tags=["Task Management"]
)


# -----------------------------
# Create Task
# -----------------------------
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    existing = db.query(Task).filter(
        Task.task_id == task.task_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Task already exists."
        )

    new_task = Task(**task.model_dump())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# -----------------------------
# Get All Tasks
# -----------------------------
@router.get("/", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):

    return db.query(Task).all()


# -----------------------------
# Get Task By ID
# -----------------------------
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str, db: Session = Depends(get_db)):

    task = db.query(Task).filter(
        Task.task_id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    return task


# -----------------------------
# Update Task
# -----------------------------
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: str,
    updated: TaskCreate,
    db: Session = Depends(get_db),
):

    task = db.query(Task).filter(
        Task.task_id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    for key, value in updated.model_dump().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


# -----------------------------
# Delete Task
# -----------------------------
@router.delete("/{task_id}")
def delete_task(
    task_id: str,
    db: Session = Depends(get_db),
):

    task = db.query(Task).filter(
        Task.task_id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully."
    }