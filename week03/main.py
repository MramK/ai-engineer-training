import os
import logging
import time


from fastapi import FastAPI, Request
from pydantic import BaseModel, Field, field_validator
from fastapi.responses import JSONResponse
from text_processing import count_words


app = FastAPI()

SERVICE_NAME = os.getenv("SERVICE_NAME","Text Processing API")



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger(__name__)

class TextRequest(BaseModel):   
    #text: str
    text: str = Field(min_length = 1)

    @field_validator("text")
    @classmethod

    def validate_text(cls, value:str) -> str:
        if not value.strip():
            raise ValueError("Field can not be empty space")
        return value





@app.get("/")
def home():
    return {"message":SERVICE_NAME}


@app.get("/health")
def health_check():
    return {"status":"ok"}


@app.post("/process")
def process_text(request: TextRequest):
#    word_count = len(request.text.split())
    start_time = time.perf_counter()

    word_count = count_words(request.text)

    duration = time.perf_counter() - start_time

    logger.info(
        "Text processed successfully | word_count=%d | duration_ms=%.2f",
        word_count,
        duration * 1000
    )

    return{
        "text":request.text,
        "word_count": word_count,
    }

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./development.db"
)

@app.get("/config")
def get_config():
    return {"database_configured": bool(DATABASE_URL)}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    logger.exception("Unhandled error on %s %s",
                      request.method,
                      request.url.path)

    return JSONResponse(
        status_code=500,
        content={"error":{"code":"INTERNAL_SERVER_ERROR", "message":"An unexpected error occurred"}},
    )

#@app.get("/test-error")
#def test_error():
#    raise RuntimeError("This is a secret internal error")

