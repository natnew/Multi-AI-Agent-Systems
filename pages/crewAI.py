import streamlit as st

with st.sidebar:
    OpenAI_api_key = st.text_input("OpenAI API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/natnew/Multi-AI-Agent-Systems/blob/main/pages/crewAI.py)"
   

st.title("📝 Multi AI Agent Systems with crewAI")

uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))
question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)


if uploaded_file and question and not OpenAI_api_key:
    st.info("Please add your OpenAI API key to continue.")



