import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/incident/analyze"

st.set_page_config(
    page_title="IT Incident Copilot",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ IT Incident Copilot")
st.caption("AI-powered IT incident investigation using RAG")

st.warning(
    "Development environment: Runbooks and historical "
    "tickets are synthetic. Runbooks are unapproved drafts."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("Knowledge Base")
    st.metric("Runbooks", 22)
    st.metric("Historical Tickets", 1000)

    st.divider()

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if question := st.chat_input("Describe your IT incident..."):

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing incident and retrieving evidence..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=180
                )

                response.raise_for_status()
                answer = response.json()["answer"]

            except requests.exceptions.RequestException:
                answer = (
                    "Unable to analyze the incident. "
                    "Please check that the FastAPI backend "
                    "is running and try again."
                )

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })