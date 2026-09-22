from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import Transaction, Investigation, FraudRule

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/overview")
def overview(db: Session = Depends(get_db)):
    total = db.query(func.count(Transaction.id)).scalar() or 0
    high = db.query(func.count(Transaction.id)).filter(Transaction.risk_score >= 70).scalar() or 0
    volume = db.query(func.sum(Transaction.amount)).scalar() or 0
    open_cases = db.query(func.count(Investigation.id)).filter(Investigation.status.in_(["open","review"])).scalar() or 0
    rules = db.query(func.count(FraudRule.id)).filter(FraudRule.enabled == True).scalar() or 0
    return {"total_transactions": total, "high_risk": high, "volume": round(volume,2),
            "open_cases": open_cases, "active_rules": rules}
