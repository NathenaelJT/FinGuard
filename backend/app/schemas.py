from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TransactionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    reference: str
    customer: str
    amount: float
    currency: str
    channel: str
    country: str
    risk_score: float
    status: str
    created_at: datetime

class InvestigationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    transaction_id: int
    title: str
    owner: str
    priority: str
    status: str
    notes: str
    created_at: datetime

class RuleCreate(BaseModel):
    name: str
    description: str
    threshold: float
    severity: str = "medium"
    enabled: bool = True

class RuleOut(RuleCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int

class StatusUpdate(BaseModel):
    status: str
