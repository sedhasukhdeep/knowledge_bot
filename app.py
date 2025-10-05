from src.llama_index_utils import build_index, query_index # <-- absolute import
import streamlit as st
import os

st.title("📄 Chat with Your Docs")

uploaded_files = st.file_uploader(
    "Upload PDFs", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    # Save uploaded PDFs to data/
    for file in uploaded_files:
        with open(f"data/{file.name}", "wb") as f:
            f.write(file.getbuffer())
    st.success("Files uploaded successfully!")

    # Build index
    with st.spinner("Indexing PDFs..."):
        index = build_index()
    st.success("Indexing complete!")

    # Query
    question = st.text_input("Ask a question about your documents:")
    if question:
        answer = query_index(index, question)
        st.write("**Answer:**", answer)
