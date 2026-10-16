from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from text_processing import count_words


app = FastAPI()

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
    return {"message":"My first AI engineering API"}


@app.post("/process")
def process_text(request: TextRequest):
#    word_count = len(request.text.split())
    word_count = count_words(request.text)

    return{
        "text":request.text,
        "word_count": word_count,
    }
