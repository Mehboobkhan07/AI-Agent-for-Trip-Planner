from groq import Groq
from .prompts import SYSTEM_PROMPT
from .memory import TripMemory
from dotenv import load_dotenv
import os
import json

load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

# one memory per session
SESSIONS={}

## memory=TripMemory()

def get_memory(session_id: str):
    if session_id not in SESSIONS:
        SESSIONS[session_id] = TripMemory()
    return SESSIONS[session_id]

def agent_think(session_id: str, user_input: str):
    memory = get_memory(session_id)
    memory.add_message("user", user_input)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *memory.get_context()
        ],
        temperature=0.3
    )

    raw = response.choices[0].message.content

    parsed = json.loads(raw)
    memory.update_trip(parsed.get("trip_data", {}))
    memory.add_message("assistant", raw)

    return parsed