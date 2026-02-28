from fastapi import FastAPI
import requests
from Schema.Pydantic_model import user_input
from Data_Base.database import engine, SessionLocal, Base
from Data_Base.models import Summury
from datetime import datetime

app = FastAPI(title="AI Notes Summarizer with FastAPI")

Base.metadata.create_all(bind=engine)

def format_datetime(dt: datetime):
    return dt.strftime("%d-%m-%Y %I:%M %p")

#SUMMARIZATION FUNCTION
def generate_summarize(input_text):

    prompt = f"""
    You are an expert summarizer.
    Summarize the following text in 2 clear bullet points:

    {input_text}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False,
            "temperature": 0.4
        }
    )

    return response.json()['response']


#DEFAULT ROUTE
@app.get("/")
def default():
    return {"message": "AI Summarizer Running 🚀"}


#SUMMARIZE ENDPOINT
@app.post("/summarize")
def summarize_note(notes: user_input):

    db = SessionLocal()

    summary = generate_summarize(notes.text)

    new_summury = Summury(
        original_text=notes.text,
        summary_text=summary
    )

    db.add(new_summury)
    db.commit()
    db.refresh(new_summury)
    db.close()

    return {
        "id": new_summury.id,
        "summary": summary,
        "created_at": format_datetime(new_summury.created_at)
    }


#HISTORY ENDPOINT
@app.get("/history")
def history_endpoint():

    db = SessionLocal()

    data = db.query(Summury).all()

    db.close()

    return [
        {
            "id": item.id,
            "original_text": item.original_text,
            "summary_text": item.summary_text,
            "created_at": format_datetime(item.created_at)
        }
        for item in data
    ]