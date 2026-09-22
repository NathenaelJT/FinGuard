from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_dashboard():
    r = client.get("/api/dashboard/overview")
    assert r.status_code == 200
    assert "high_risk" in r.json()

def test_transactions():
    r = client.get("/api/transactions")
    assert r.status_code == 200
