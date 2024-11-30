from fastapi import FastAPI
from words import BRAINROT
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Brainrot API. Get ready for chaos!"}

@app.get("/brainrot")
async def get_brainrot():
    return BRAINROT

@app.get("/brainrot/random")
async def get_random_brainrot():
    random_word = random.choice(BRAINROT)
    return {"random_brainrot_term": random_word}

@app.get("/skibidi")
async def get_skibidi():
    return {
           "definition": "Can either mean cool or dumb, depending on the context.",
           "example": "That's so skibidi!",
           "usage": [
               "When something is impressive: 'That trick was so skibidi!'",
               "When something is silly: 'Why did you do that? That's so skibidi!'"
           ],   
           }

