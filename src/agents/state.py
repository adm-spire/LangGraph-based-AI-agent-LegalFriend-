from typing import TypedDict, List, Optional

class RebuttalState(TypedDict):
    allegation: str
    evidence: List[str]
    draft: Optional[str]
    final: Optional[str]
