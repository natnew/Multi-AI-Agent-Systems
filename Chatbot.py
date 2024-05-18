from openai import OpenAI
import streamlit as st
import sys
from pathlib import Path

# Add the pages directory to the sys.path
pages_dir = Path(__file__).parent / 'pages'
sys.path.append(str(pages_dir))

import sidebar  # Import the sidebar module

def main():
    openai_api_key = sidebar.add_sidebar()  # Load sidebar content

    st.title("💬 Chatbot")
    st.caption("🚀 A Streamlit chatbot powered by OpenAI")
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

if __name__ == "__main__":
    main()

