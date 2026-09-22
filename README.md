# FinGuard — Financial Operations & Risk Management Platform

FinGuard is a production-oriented portfolio application for monitoring financial transactions,
triaging suspicious activity, managing fraud rules, and tracking investigations.

## Stack
- Backend: Python 3.12+, FastAPI, SQLAlchemy 2, Pydantic
- Frontend: Next.js App Router, TypeScript, React
- Database: SQLite for local development; PostgreSQL-ready configuration
- Auth-ready API boundary, audit events, risk scoring, rule management
- Docker Compose for local deployment

## Features
- Executive risk dashboard
- Searchable/filterable transaction queue
- Deterministic transaction risk scoring
- Investigation workflow with status changes
- Fraud-rule management
- Audit trail
- Health endpoint
- Seed data for a realistic demo
- API tests

## Run locally

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000

### Docker
```bash
docker compose up --build
```

Frontend: http://localhost:3000
API: http://localhost:8000

## Architecture
The backend follows FastAPI's multi-router application pattern, while the frontend uses
Next.js App Router route segments and shared components.

> Portfolio note: This is an original FinGuard implementation inspired by common production
architecture patterns. It is not a copy of another repository.
