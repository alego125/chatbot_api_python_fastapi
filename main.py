from fastapi import FastAPI
from dotenv import load_dotenv
import openai
import os
from models.model import Model

app = FastAPI()

load_dotenv()

openai.api_key = os.getenv('SECRET_KEY')

@app.post('/chat')
def generate_response(prompt: Model):
    engine_model_gpt3 = "text-davinci-003"

    response = openai.Completion.create(
        engine=engine_model_gpt3,
        prompt=prompt.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3
    )

    return response.choices[0].text

