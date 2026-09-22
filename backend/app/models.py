from datetime import datetime
from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    reference: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    customer: Mapped[str] = mapped_column(String(120))
    amount: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String(8), default="ETB")
    channel: Mapped[str] = mapped_column(String(32))
    country: Mapped[str] = mapped_column(String(64))
    risk_score: Mapped[float] = mapped_column(Float, default=0)
    status: Mapped[str] = mapped_column(String(32), default="monitoring")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Investigation(Base):
    __tablename__ = "investigations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    transaction_id: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(200))
    owner: Mapped[str] = mapped_column(String(120), default="Unassigned")
    priority: Mapped[str] = mapped_column(String(20), default="medium")
    status: Mapped[str] = mapped_column(String(32), default="open")
    notes: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class FraudRule(Base):
    __tablename__ = "fraud_rules"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(160))
    description: Mapped[str] = mapped_column(Text)
    threshold: Mapped[float] = mapped_column(Float)
    severity: Mapped[str] = mapped_column(String(20), default="medium")
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)

class AuditEvent(Base):
    __tablename__ = "audit_events"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    action: Mapped[str] = mapped_column(String(120))
    actor: Mapped[str] = mapped_column(String(120))
    entity: Mapped[str] = mapped_column(String(120))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
