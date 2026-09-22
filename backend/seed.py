from random import choice, randint, uniform
from app.database import Base, engine, SessionLocal
from app.models import Transaction, Investigation, FraudRule
from app.services import calculate_risk

Base.metadata.create_all(bind=engine)
db = SessionLocal()
if db.query(Transaction).count() == 0:
    countries = ["Ethiopia","Kenya","Uganda","United Kingdom","United Arab Emirates"]
    channels = ["mobile","bank_transfer","card","international"]
    for i in range(1, 61):
        amount = round(uniform(500, 180000), 2)
        country = choice(countries)
        channel = choice(channels)
        risk = calculate_risk(amount, country, channel)
        t = Transaction(reference=f"FG-{2026:04d}-{i:05d}",
                        customer=choice(["Abebe Trading","Nile Retail","Horizon Imports","Blue Acacia","Atlas Foods"]),
                        amount=amount, channel=channel, country=country,
                        risk_score=risk,
                        status="blocked" if risk >= 85 else ("review" if risk >= 60 else "monitoring"))
        db.add(t)
    db.commit()

    txs = db.query(Transaction).filter(Transaction.risk_score >= 60).limit(12).all()
    for idx, tx in enumerate(txs):
        db.add(Investigation(transaction_id=tx.id, title=f"Review {tx.reference}",
                             owner=choice(["Marta Chen","Daniel Bekele","Sara Morgan","Unassigned"]),
                             priority="high" if tx.risk_score >= 75 else "medium",
                             status="open" if idx % 3 else "review",
                             notes="Validate transaction context and customer activity."))
    db.add_all([
        FraudRule(name="High Value Transfer", description="Flag transfers above configured amount.", threshold=100000, severity="high"),
        FraudRule(name="International Velocity", description="Flag unusual international activity.", threshold=3, severity="medium"),
        FraudRule(name="Card Anomaly", description="Flag elevated card transaction patterns.", threshold=70, severity="high"),
    ])
    db.commit()
db.close()
print("FinGuard demo data ready.")
