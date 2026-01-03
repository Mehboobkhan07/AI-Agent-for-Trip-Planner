import streamlit as st
import requests
import uuid



API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI Trip Planner", page_icon="🧳")
st.title("🧳 AI Trip Planner")


# Session ID

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())


# Chat history

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# User input

user_input = st.chat_input("Plan your trip...")

if user_input:
    # Store + show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

 
    # Call backend

    payload = {
        "session_id": st.session_state.session_id,
        "message": user_input
    }

    raw_response = requests.post(API_URL, json=payload).json()
    response = raw_response.get("response", {})

    action = response.get("action")

   
    # Handle ASK USER
   
    if action == "ask_user":
        question = response.get("question", "Please provide more details.")
        missing_fields = response.get("missing_fields", [])

        agent_reply = f"❓ **More details needed**\n\n{question}"

        if missing_fields:
            agent_reply += "\n\n**Missing information:**\n"
            for field in missing_fields:
                agent_reply += f"- {field.replace('_', ' ').title()}\n"


    # Handle GENERATE PLAN

    elif action == "generate_plan":
        itinerary = response.get("itinerary", {})

        agent_reply = "### ✈️ Your Trip Plan\n\n"

        for day, details in itinerary.items():
            agent_reply += f"#### {day}\n"

            if isinstance(details, dict):
                for key, value in details.items():
                    agent_reply += f"- **{key.replace('_', ' ').title()}**: {value}\n"
            else:
                agent_reply += f"{details}\n"

            agent_reply += "\n"

    # Fallback

    else:
        agent_reply = (
            response.get("message")
            or response.get("detail")
            or str(response)
        )

   
    # Store + show assistant reply
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": agent_reply
    })

    with st.chat_message("assistant"):
        st.markdown(agent_reply)
