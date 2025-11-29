import os
from pathlib import Path
from tqdm import tqdm

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import Chroma

from src.config.settings import CHROMA_PERSIST_DIR, CHUNK_SIZE, CHUNK_OVERLAP

DATA_DIR = Path("data/raw_pdfs")

def load_pdfs(directory: Path):
    docs = []
    for p in directory.glob("*.pdf"):
        loader = PyPDFLoader(str(p))
        loaded = loader.load()
        docs.extend(loaded)
    return docs

def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(docs)

def embed_and_persist(chunks):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PERSIST_DIR
    )
    db.persist()
    return db

def main():
    if not DATA_DIR.exists():
        print(f"Data directory {DATA_DIR} does not exist. Create it and add PDFs.")
        return

    print("Loading PDFs...")
    docs = load_pdfs(DATA_DIR)
    if not docs:
        print("No PDFs found in data/raw_pdfs/")
        return

    print(f"Loaded {len(docs)} documents. Chunking...")
    chunks = chunk_documents(docs)
    print(f"Generated {len(chunks)} chunks. Creating embeddings and persisting to Chroma...")
    db = embed_and_persist(chunks)
    print("Ingestion finished. Vector DB persisted to", CHROMA_PERSIST_DIR)

if __name__ == "__main__":
    main()
