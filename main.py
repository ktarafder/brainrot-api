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

@router.get("/don-pollo")
async def don_pollo():
    return {
        "name": "Don Pollo",
        "title": "The Unspoken Sigma Chicken Overlord of Ohio",
        "backstory": (
            "Don Pollo, born in the depths of an Ohio chicken coop, rose from humble beginnings to mog the entire poultry industry. "
            "Known for his rawdogging approach to leadership, Don Pollo single-wingedly defeated Grimace in a skibidi cook-off and has since become "
            "a symbol of chaotic moggery. They say he mews while clucking, perfecting his jawline even while ruling the coop."
        ),
        "achievements": [
            "Beat Grimace in a skibidi-level cook-off",
            "Invented the 'GYATT wing'—a chicken wing so moggy it makes Baby Gronk jealous",
            "Pulled Livee Dunn out of retirement with his unparalleled rizz",
            "Declared Top G of poultry by Kai Cenat himself"
        ],
        "vibe": "Absolute sigma grindset, rawdogging life with no cap and bussin' feathers.",
        "quotes": [
            "Cluck twice, mog once.",
            "Even betas can fly when they follow the coop's Top G.",
            "Rawdogging the skibidi grindset every day, cluck yeah!"
        ],
        "message": "Don Pollo isn't just a name. It's a lifestyle. Mog your way to the top with skibidi vibes and stay based."
    }

@app.get("/rizzlord")
async def rizzlord():
    return {
    "rizzlord": {
    "definition": "The ultimate master of charisma and flirting, mogging everyone with unshakable confidence and skibidi-level charm.",
    "example": "Bro walked into the party, said two words, and left with everyone’s attention—absolute rizzlord energy.",
    "backstory": (
        "The title of 'Rizzlord' is reserved for those who have maxed out their rizz stats. Legends say the first Rizzlord once rizzy'd up "
        "Livee Dunn in Ohio while simultaneously teaching Baby Gronk how to mog on the football field. The Rizzlord operates on a sigma grindset, "
        "effortlessly commanding attention with a single look or word."
    ),
    "criteria": [
        "Unstoppable confidence in any situation.",
        "Effortless ability to riz up anyone, anytime, anywhere.",
        "Leaves no beta un-mogged in their wake."
    ],
    "message": "If you're not a Rizzlord, what are you even doing? Skibidi vibes only, no cap."
        }
    }   

app.include_router(router)