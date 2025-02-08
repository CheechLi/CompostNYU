import streamlit as st
from transformers import pipeline

# Load a conversational model
chatbot = pipeline("conversational", model="EleutherAI/gpt-neo-1.3B")

st.title("🤖 Chatbot using Streamlit and Transformers")

# Initialize session state for conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", "")
if st.button("Send") and user_input:
    # Append user input to history
    st.session_state.chat_history.append({"role": "user", "text": user_input})
    
    # Get chatbot response
    from transformers import Conversational
    conv = Conversational(user_input)
    response = chatbot(conv)
    bot_reply = response.generated_responses[-1]
    
    # Append chatbot response to history
    st.session_state.chat_history.append({"role": "bot", "text": bot_reply})

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.text_area("You:", message["text"], key=message["text"] + "_user", height=50)
    else:
        st.text_area("Bot:", message["text"], key=message["text"] + "_bot", height=50)
