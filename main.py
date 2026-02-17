from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI(title="Ai Notes Summarizer with Fast Apis")

class user_input(BaseModel):
    text : str


def generate_summarize(input_text):

    prompt = f"""You are an expert summarizer.
    Summarize the following text in 5 clear bullet points:
    {input_text}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"gemma:2b",
            "prompt":prompt,
            "stream":False,
            "temperature":0.4 
        }
    )

    return response.json()['rresponses']

@app.get("/summarize")
def summarize_note(notes:user_input):
    