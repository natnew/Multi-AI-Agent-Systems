import streamlit as st

def add_sidebar():
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        st.markdown("[View the source code](https://github.com/natnew/Multi-AI-Agent-Systems/blob/main/Chatbot.py)")
    return openai_api_key
