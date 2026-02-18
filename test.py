from fastapi import FastAPI
import requests
from Schema.Pydantic_model import user_input

app = FastAPI(title="Demo_projects.")

def demo_testing(input_data):

    prmopt = f""" Hello my name is Der Ravi can u please explain about the {input_data}. """

    req = requests.post(
        ""
    )