from src.llm.ollama_llm import generate

VERIFY_PROMPT = """
You are a fact-check assistant. Given a draft rebuttal and the evidence list used to create it,
ensure every factual claim in the rebuttal is supported by the evidence. If something is not
supported, mark it and either (a) remove it, or (b) rewrite it to only contain supported facts.

Draft Rebuttal:
{draft}

Evidence (numbered):
{evidence_list}

Return a cleaned and verified final rebuttal. If you cannot verify, be conservative and flag unsupported sentences.
"""

def verify_node(state: dict) -> dict:
    draft = state.get("draft", "")
    evidence = state.get("evidence", [])

    if not draft:
        state["final"] = "No draft available to verify."
        return state

    numbered = "\n".join([f"[{i+1}] {e}" for i, e in enumerate(evidence)]) if evidence else "No evidence provided."

    prompt = VERIFY_PROMPT.format(draft=draft, evidence_list=numbered)
    response = generate(prompt, max_tokens=800, temperature=0.0)
    state["final"] = response
    return state
