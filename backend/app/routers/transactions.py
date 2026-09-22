from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..database import get_db
from ..models import Transaction
from ..schemas import TransactionOut

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("", response_model=list[TransactionOut])
def list_transactions(
    search: str = Query("", max_length=100),
    status: str = Query("", max_length=32),
    min_risk: float | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(Transaction)
    if search:
        pattern = f"%{search}%"
        q = q.filter(or_(Transaction.reference.ilike(pattern),
                         Transaction.customer.ilike(pattern),
                         Transaction.country.ilike(pattern)))
    if status:
        q = q.filter(Transaction.status == status)
    if min_risk is not None:
        q = q.filter(Transaction.risk_score >= min_risk)
    return q.order_by(Transaction.created_at.desc()).limit(200).all()

@router.get("/{transaction_id}", response_model=TransactionOut)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return db.get(Transaction, transaction_id)
