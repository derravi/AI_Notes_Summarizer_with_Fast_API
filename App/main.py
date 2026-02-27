from fastapi import FastAPI
import requests
from Schema.Pydantic_model import user_input
from Data_Base.database import engine,SessionLocal,Base
from Data_Base.models import Summury

app = FastAPI(title="AI Notes Summarizer with FastAPI")

def generate_summarize(input_text):

    prompt = f"""
    You are an expert summarizer.
    Summarize the following text in 5 clear bullet points:

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


# if __name__ == "__main__":
#     user_input = input("Enter teh Text:\n")

#     summury = generate_summarize(user_input)
#     print("======Summury======")
#     print(summury)
 
@app.post("/summarize")
def summarize_note(notes: user_input):

    db = SessionLocal()

    summary = generate_summarize(notes.text)

    new_summury = Summury(
        original_text = notes.text,
        summary_text = summary  
    )

    db.add(new_summury)
    db.commit()
    db.refresh(new_summury)
    db.close()

    return {
        "id": new_summury.id,
        "summary": summary
    }

@app.get("/history")
def history_endpoint():

    db = SessionLocal()
    db = db.query(Summury).all()
    db.close()

    return db

