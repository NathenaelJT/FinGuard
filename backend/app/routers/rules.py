from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import FraudRule
from ..schemas import RuleCreate, RuleOut

router = APIRouter(prefix="/rules", tags=["Fraud Rules"])

@router.get("", response_model=list[RuleOut])
def list_rules(db: Session = Depends(get_db)):
    return db.query(FraudRule).order_by(FraudRule.id.desc()).all()

@router.post("", response_model=RuleOut, status_code=201)
def create_rule(payload: RuleCreate, db: Session = Depends(get_db)):
    rule = FraudRule(**payload.model_dump())
    db.add(rule); db.commit(); db.refresh(rule)
    return rule

@router.patch("/{rule_id}/toggle", response_model=RuleOut)
def toggle_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.get(FraudRule, rule_id)
    if not rule: raise HTTPException(404, "Rule not found")
    rule.enabled = not rule.enabled
    db.commit(); db.refresh(rule)
    return rule
