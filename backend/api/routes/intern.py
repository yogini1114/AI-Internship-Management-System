from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.models.intern import Intern
from backend.api.schemas.intern import (
    InternCreate,
    InternResponse,
)

router = APIRouter(
    prefix="/api/interns",
    tags=["Intern Management"]
)


# -----------------------------
# Create Intern
# -----------------------------
@router.post("/", response_model=InternResponse)
def create_intern(intern: InternCreate, db: Session = Depends(get_db)):

    existing = db.query(Intern).filter(
        Intern.intern_id == intern.intern_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Intern ID already exists."
        )

    new_intern = Intern(**intern.model_dump())

    db.add(new_intern)
    db.commit()
    db.refresh(new_intern)

    return new_intern


# -----------------------------
# Get All Interns
# -----------------------------
@router.get("/", response_model=list[InternResponse])
def get_all_interns(db: Session = Depends(get_db)):

    return db.query(Intern).all()


# -----------------------------
# Get Single Intern
# -----------------------------
@router.get("/{intern_id}", response_model=InternResponse)
def get_intern(intern_id: str, db: Session = Depends(get_db)):

    intern = db.query(Intern).filter(
        Intern.intern_id == intern_id
    ).first()

    if not intern:
        raise HTTPException(
            status_code=404,
            detail="Intern not found."
        )

    return intern


# -----------------------------
# Update Intern
# -----------------------------
@router.put("/{intern_id}", response_model=InternResponse)
def update_intern(
    intern_id: str,
    updated: InternCreate,
    db: Session = Depends(get_db),
):

    intern = db.query(Intern).filter(
        Intern.intern_id == intern_id
    ).first()

    if not intern:
        raise HTTPException(
            status_code=404,
            detail="Intern not found."
        )

    for key, value in updated.model_dump().items():
        setattr(intern, key, value)

    db.commit()
    db.refresh(intern)

    return intern


# -----------------------------
# Delete Intern
# -----------------------------
@router.delete("/{intern_id}")
def delete_intern(
    intern_id: str,
    db: Session = Depends(get_db),
):

    intern = db.query(Intern).filter(
        Intern.intern_id == intern_id
    ).first()

    if not intern:
        raise HTTPException(
            status_code=404,
            detail="Intern not found."
        )

    db.delete(intern)
    db.commit()

    return {
        "message": "Intern deleted successfully."
    }