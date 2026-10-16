
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_process_text_sucess():
    response = client.post(
        "/process",
        json = {"text":"Large Language models are useful"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "text":"Large Language models are useful",
        "word_count":5,
    }

def test_empty():
    response = client.post(
        "/process",
        json = {"text":"   "}
    )

    assert response.status_code == 422
    
def test_wrong_input():
    response = client.post(
        "/process",
        json = {"text":123}
    )

    assert response.status_code == 422
    assert "detail" in response.json()

    
def test_missing_field():
    response = client.post(
        "/process",
        json = {}
    )

    assert response.status_code == 422
    assert "detail" in response.json()
