
import pytest
from fastapi.testclient import TestClient
from main import app
from fastapi.responses import JSONResponse


#@pytest.fixture
#def client():
#    return TestClient(app)

#client = TestClient(app)
client = TestClient(app,raise_server_exceptions=False)

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

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message":"Text Processing API"
    }

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status":"ok"}

def test_unhandled_exception():

    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    test_app= FastAPI()

    @test_app.exception_handler(Exception)
    async def global_exception_handler(request,exc):
        return JSONResponse(
            status_code= 500,
            content= {
                "error":{
                      "code":"INTERNAL_SERVER_ERROR",
                      "message":"An unexpected error occurred"
             }
            }
        )
    @test_app.get("/test-error")
    def test_error():
        raise RuntimeError("This is a secret internal error")

    test_client = TestClient(
        test_app,
        raise_server_exceptions= False
    )

    response = test_client.get("/test-error")

    assert response.status_code== 500

    assert response.json() == {
        "error":{
            "code":"INTERNAL_SERVER_ERROR",
            "message":"An unexpected error occurred"
        }
    }
    assert "This is a secret internal error" not in response.text