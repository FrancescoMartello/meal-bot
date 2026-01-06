from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MealInput(BaseModel):
    target_kcal: float
    macro_style: str
    disliked: str

@app.get("/")
def root():
    return {"status": "ok", "message": "meal-bot is running. Go to /docs"}

@app.post("/generate_meal")
def generate_meal(data: MealInput):
    return {"text": "BOT collegato correttamente – risposta di test"}
