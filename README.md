# Allegation Rebuttal Agent (LangGraph + Ollama + Llama 3.1)

## Setup
1. Install Ollama and download `llama3.1:8b`.
2. Create and activate a Python virtualenv.
3. `pip install -r requirements.txt`
4. Place PDFs into `data/raw_pdfs/`.
5. `python src/ingestion/ingest_pdfs.py`  # builds Chroma DB
6. `python main.py` to run CLI, or `uvicorn src.api.fastapi_app:app --reload` for API.

## Files
- `src/ingestion/` - ingestion pipeline for PDFs
- `src/vectorstore/` - wrapper for Chroma
- `src/llm/` - Ollama LLM wrapper
- `src/agents/` - LangGraph agent nodes and graph
- `src/api/` - FastAPI wrapper

