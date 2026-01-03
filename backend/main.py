from fastapi import FastAPI
from backend.schemas.trip import ChatRequest, ChatResponse

from backend.agent.planner import agent_think

app = FastAPI(title="AI Trip Planner Agent")

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = agent_think(req.session_id, req.message)
    return {"response": result}
