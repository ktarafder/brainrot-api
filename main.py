from fastapi import FastAPI, APIRouter
import random
from words import BRAINROT

app = FastAPI()
router = APIRouter(prefix="/api")

@app.get("/")
async def root():
    return {"message": "Skibidi bop yes yes! Welcome to the moggiest Brainrot API of all time."}

@router.get("/brainrot")
async def get_all_brainrot():
    return {
        "terms": list(BRAINROT.keys()),
        "message": f"Here's the full Brainrot dictionary with {len(BRAINROT)} terms! Stay gooning and skibidi."
    }

@router.get("/brainrot/random")
async def get_random_brainrot():
    term = random.choice(list(BRAINROT.keys()))
    return {
        "term": term,
        "definition": BRAINROT[term]["definition"],
        "example": BRAINROT[term]["example"],
        "message": f"Random moggy Brainrot term incoming: {term}!"
    }

for term, details in BRAINROT.items():
    @router.get(f"/{term}")
    async def specific_term(term=term, definition=details["definition"], example=details["example"]):
        return {
            "term": term,
            "definition": definition,
            "example": example,
            "message": f"Here's the 411 on '{term}'. Now go mog the competition."
        }

app.include_router(router)