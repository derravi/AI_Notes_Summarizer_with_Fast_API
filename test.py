from fastapi import FastAPI
import requests
from Schema.Pydantic_model import user_input

app = FastAPI(title="Demo_projects.")

def demo(input_text):

    prompt = f""" You are an expert summurizer. Summurize the following text in a 5 clear bullet point. 
    {input_text}
    """

    reply = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"gemma:2b",
            "prompt":prompt_input,
            "stream": False,
            "temperature":0.3
        }
    )

    return reply.json()['reply']

@app.post("/geting_answer")
def answer(notes:user_input):
    summury = demo(notes.text)

    return {
        "Original_Length": len(notes.text),
        "AI genereated Answer": summury
    }