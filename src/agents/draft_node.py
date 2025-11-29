from src.llm.ollama_llm import generate
from typing import List

PROMPT_TEMPLATE = """
You are an assistant that must write a factual, concise rebuttal using only the provided evidence.
Do not invent facts. Anchor all claims to the evidence and cite the evidence pieces by number.

Allegation:
{allegation}

Evidence (numbered):
{evidence_list}

Write a clear rebuttal. Keep it professional and factual.
"""

def draft_node(state: dict) -> dict:
    allegation = state.get("allegation", "")
    evidence: List[str] = state.get("evidence", [])

    if not evidence:
        # No evidence found — be explicit.
        state["draft"] = (
            "No supporting evidence found in the document collection. "
            "Unable to produce an evidence-supported rebuttal."
        )
        return state

    numbered = "\n".join([f"[{i+1}] {e}" for i, e in enumerate(evidence)])
    prompt = PROMPT_TEMPLATE.format(allegation=allegation, evidence_list=numbered)
    response = generate(prompt, max_tokens=800, temperature=0.0)
    state["draft"] = response
    return state
