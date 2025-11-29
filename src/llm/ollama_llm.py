from langchain_community.llms import Ollama
from src.config import settings

# Load LLM
llm = Ollama(model=settings.LLM_MODEL)

def generate(prompt: str, max_tokens: int = 512, temperature: float = 0.0):
    """
    Returns the LLM response text for a prompt.
    """

    try:
        # Proper call for LangChain community Ollama LLM
        resp = llm.invoke(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )

        # resp will be an LLMResult or string depending on version
        if isinstance(resp, dict) and "text" in resp:
            return resp["text"]

        return str(resp)

    except Exception as e:
        raise ValueError(
            f"Ollama LLM error: {e}. Ensure Ollama is running and '{settings.LLM_MODEL}' is installed."
        )

