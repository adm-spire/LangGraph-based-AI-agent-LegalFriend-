from langgraph.graph import StateGraph, END
from src.agents.state import RebuttalState
from src.agents.retrieve_node import retrieve_node
from src.agents.draft_node import draft_node
from src.agents.verify_node import verify_node

# Build the graph
graph = StateGraph(RebuttalState)

graph.add_node("retrieve", retrieve_node)
graph.add_node("draft_rebuttal", draft_node)
graph.add_node("verify_rebuttal", verify_node)

graph.set_entry_point("retrieve")

graph.add_edge("retrieve", "draft_rebuttal")
graph.add_edge("draft_rebuttal", "verify_rebuttal")
graph.add_edge("verify_rebuttal", END)

app = graph.compile()
