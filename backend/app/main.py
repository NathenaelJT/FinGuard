from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import dashboard, transactions, investigations, rules

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FinGuard API", version="1.0.0",
              description="Financial operations and risk management API.")

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"],
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(dashboard.router, prefix="/api")
app.include_router(transactions.router, prefix="/api")
app.include_router(investigations.router, prefix="/api")
app.include_router(rules.router, prefix="/api")
@app.get("/")
def root():
    return {
        "application": "FinGuard",
        "description": "Financial Operations & Risk Management Platform",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
        "health": "/health",
    }
@app.get("/health")
def health():
    return {"status": "ok", "service": "finguard-api"}

