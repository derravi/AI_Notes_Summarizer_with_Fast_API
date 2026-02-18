from fastapi import FastAPI
import requests
from Schema.Pydantic_model import user_input

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

@app.post("/summarize")
def summarize_note(notes: user_input):
    summary = generate_summarize(notes.text)

    return {
        "Original_Length": len(notes.text),
        "summary": summary
    }

