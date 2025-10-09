from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)



def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "AI Resume Analyzer" in resp.json().get("message")
