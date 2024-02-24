import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input: str):
    return "I don't know!"

# App config
st.set_page_config(page_title="Chat with websites", page_icon=":speech_balloon:", layout="centered", initial_sidebar_state="expanded")
st.title("Chat with websites")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a chat bot! How can I help you?"),
    ]

# Sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL") #st.radio("Select a website", ["Wikipedia", "Google", "Facebook", "Twitter", "YouTube"])

# User input
chat_history = st.session_state.chat_history
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    response = get_response(user_query)
    chat_history.append(HumanMessage(content=user_query))
    chat_history.append(AIMessage(content=response))

# Conversation
for message in chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(f"**You**: {message.content}")
    elif isinstance(message, AIMessage):
        with st.chat_message("Bot"):
            st.write(f"**Bot**: {message.content}")
    
