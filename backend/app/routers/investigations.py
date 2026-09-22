from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Investigation
from ..schemas import InvestigationOut, StatusUpdate

router = APIRouter(prefix="/investigations", tags=["Investigations"])

@router.get("", response_model=list[InvestigationOut])
def list_investigations(db: Session = Depends(get_db)):
    return db.query(Investigation).order_by(Investigation.created_at.desc()).all()

@router.patch("/{case_id}/status", response_model=InvestigationOut)
def update_status(case_id: int, payload: StatusUpdate, db: Session = Depends(get_db)):
    case = db.get(Investigation, case_id)
    if not case:
        raise HTTPException(404, "Investigation not found")
    allowed = {"open", "review", "escalated", "resolved", "dismissed"}
    if payload.status not in allowed:
        raise HTTPException(400, "Invalid status")
    case.status = payload.status
    db.commit()
    db.refresh(case)
    return case
