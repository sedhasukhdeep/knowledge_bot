# Chat with Your Docs

A simple AI-powered application to **upload PDF documents and chat with them** using natural language. Built with **LlamaIndex** for indexing and retrieval, **OpenAI GPT** for answering questions, and **Streamlit** for a web UI.

---

## Features

- Upload PDF files through a web interface
- Index your documents using LlamaIndex
- Ask natural language questions about your PDFs
- Get concise answers with context from the documents
- Supports multiple files and dynamic queries

---

## Tech Stack

| Layer                  | Tool / Library                    |
|------------------------|----------------------------------|
| LLM                    | OpenAI GPT via `llama_index`     |
| Document Indexing      | LlamaIndex                        |
| Querying / Retrieval   | LlamaIndex `VectorStoreIndex` + QueryEngine |
| App / UI               | Streamlit                         |
| Config / Secrets       | `.env` / `config.py`             |

---

## Project Structure

knowledge_bot/
├── src/
│ ├── init.py
│ ├── llama_index_utils.py # functions to build index & query
│ └── config.py # store your OPENAI_API_KEY
├── app.py # Streamlit app entry point
├── venv/ # Python virtual environment
├── data/ # folder to store uploaded PDFs
├── requirements.txt # dependencies
└── README.md

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <this repo>
cd knowledge_bot
2. Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows
3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
4. Set OpenAI API Key
Create src/config.py:
OPENAI_API_KEY="your-openai-api-key-here"
Alternatively, use a .env file and python-dotenv to load your key.
5. Run Streamlit App
streamlit run app.py
Open the browser at: http://localhost:8501
Upload your PDFs and start asking questions!


Future Improvements
Add persistent vector database support (e.g., Chroma, Pinecone)
Support multiple LLM backends (Ollama, GPT-4, local LLMs)
Multi-document conversational memory
Wrap with LangGraph for multi-step AI agents