from typing import Any
from src.vectorstore.store import get_vectorstore
from src.config.settings import TOP_K

_vectorstore = None

def _get_db():
    global _vectorstore
    if _vectorstore is None:
        _vectorstore = get_vectorstore()
    return _vectorstore

def retrieve_node(state: dict) -> dict:
    """
    Expects state["allegation"] to be present.
    Populates state["evidence"] with a list of page_content strings.
    """
    query = state.get("allegation", "")
    if not query:
        state["evidence"] = []
        return state

    db = _get_db()
    docs = db.similarity_search(query, k=TOP_K)
    state["evidence"] = [d.page_content for d in docs]
    return state
