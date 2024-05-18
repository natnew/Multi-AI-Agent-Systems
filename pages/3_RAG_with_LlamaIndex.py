from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/natnew/Multi-AI-Agent-Systems/blob/main/Chatbot.py)"
    
uploaded_files = st.file_uploader("Upload documents", type=["txt", "pdf"], accept_multiple_files=True)

st.title("📄 Agentic RAG with Llamaindex")
st.caption("🚀 A Streamlit app performing RAG over uploaded documents using OpenAI and Llamaindex")

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Process uploaded documents
if uploaded_files:
    documents = []
    for uploaded_file in uploaded_files:
        content = uploaded_file.read().decode("utf-8")
        documents.append(content)
        
    llama_index = LlamaIndex()
    llama_index.index_documents(documents)
else:
    st.info("Please upload documents to continue.")
    st.stop()

# Handle user prompt
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Perform retrieval-augmented generation
    retrieved_docs = llama_index.retrieve(prompt)
    context = "\n".join(retrieved_docs)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages + [{"role": "system", "content": context}]
    )
    
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
