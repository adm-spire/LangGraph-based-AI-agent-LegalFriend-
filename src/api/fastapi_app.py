from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.graph import app as lg_app

class RebuttalRequest(BaseModel):
    allegation: str

class RebuttalResponse(BaseModel):
    allegation: str
    draft: str | None = None
    final: str | None = None
    evidence: list[str] | None = None

api = FastAPI(title="Allegation Rebuttal Agent")

@api.post("/rebuttal", response_model=RebuttalResponse)
def generate_rebuttal(req: RebuttalRequest):
    state = {"allegation": req.allegation}
    result = lg_app.invoke(state)
    return RebuttalResponse(
        allegation=req.allegation,
        draft=result.get("draft"),
        final=result.get("final"),
        evidence=result.get("evidence", [])
    )
