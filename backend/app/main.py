import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.services.ai_service import ask_gemini

# Step 1: Load the secrets from .env
load_dotenv()

app = FastAPI()

# Step 2: Access a secret
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

@app.get("/")
def read_root():
    return {
        "status": "TicketTulong Backend Online",
        "api_key_loaded": bool(GEMINI_KEY) # Tells you True if it found the key
    }

@app.get("/test-ai")
def test_ai(user_input: str = "Hello Gemini, TicketTulong is online!"):
    ai_response = ask_gemini(user_input)
    return {"reply": ai_response}