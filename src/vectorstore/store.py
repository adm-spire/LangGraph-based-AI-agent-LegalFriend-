from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from src.config.settings import CHROMA_PERSIST_DIR

def get_vectorstore():
    """
    Returns a Chroma vector store instance persisted to CHROMA_PERSIST_DIR.
    """
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma(
        persist_directory=CHROMA_PERSIST_DIR,
        embedding_function=embeddings
    )
    return db
