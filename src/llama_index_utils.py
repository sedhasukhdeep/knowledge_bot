import os
from llama_index.core.indices.vector_store.base import VectorStoreIndex
from llama_index.core.readers.file.base import SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from src.config import OPENAI_API_KEY


def query_index(index, question):
    """Query the index using a QueryEngine"""
    query_engine = index.as_query_engine()  # create query engine
    response = query_engine.query(question)
    return response.response


def build_index(data_dir="data"):
    """Load PDFs and create an index"""
    documents = SimpleDirectoryReader(data_dir).load_data()
    
    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0)

    index = VectorStoreIndex.from_documents(
        documents, llm=llm
    )
    return index

