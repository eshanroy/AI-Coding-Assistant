from langgraph.graph import StateGraph
from agents.planner import planner
from agents.coder import coder
from agents.debugger import debugger

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("plan", planner)
    graph.add_node("code", coder)
    graph.add_node("debug", debugger)

    graph.set_entry_point("plan")

    graph.add_edge("plan", "code")
    graph.add_edge("code", "debug")

    graph.add_conditional_edges(
        "debug",
        lambda state: "end" if state["success"] else "code"
    )

    return graph.compile()
