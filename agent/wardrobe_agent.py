from langgraph.graph import StateGraph, END

from agent.wardrobe_agent_nodes import call_model
from agent.wardrobe_agent_state import AgentState


workflow = StateGraph(AgentState)
workflow.add_node("call_model", call_model)
workflow.add_edge("call_model", END)

workflow.set_entry_point("call_model")
wardrobe_agent_graph = workflow.compile()
