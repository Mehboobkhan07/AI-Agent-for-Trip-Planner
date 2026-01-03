# AI Trip Planner – LLM Agent 

An AI-powered Trip Planner that generates personalized travel itineraries using an LLM-based agent.  
The system is built with a **FastAPI backend**, **LLM agent reasoning**, and a **Streamlit frontend UI**.


## What This Project Does

This project acts as an **AI Travel Planning Agent** that:
- Understands natural language travel requests
- Extracts structured intent (destination, days, budget, interests)
- Uses LLM reasoning to plan a complete trip
- Returns a human-readable itinerary
- Maintains session-based conversation flow

Example prompt:
> “Plan a 3-day trip from Delhi to Shimla with a budget of ₹12,000”



---

## 🛠️ Tech Stack

### Backend
- **FastAPI** – REST API
- **Groq LLM API** – High-speed LLM inference
- **LangChain** – Agent logic & prompt orchestration
- **Pydantic** – Request/response validation
- **python-dotenv** – Environment variable management
- **Uvicorn** – ASGI server

### Frontend
- **Streamlit** – Interactive UI
- **Requests** – Backend API communication

### Deployment
- **Render** – Backend deployment
- **GitHub** – Version control

---

## 🤖 AI Agent Design

- Uses an **LLM Agent pattern**
- Maintains conversation using `session_id`
- Handles missing information gracefully
- Produces structured + readable outputs
- Designed for extensibility (hotels, maps, bookings)

---

## 📡 API Endpoint

### POST `/chat`

**Request**
```json
{
  "session_id": "uuid",
  "message": "Plan a 3 day trip to Jaipur"
}


