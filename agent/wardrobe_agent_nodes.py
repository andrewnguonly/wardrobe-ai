from langchain_ollama import ChatOllama

from agent.wardrobe_agent_state import AgentState


SYSTEM_PROMPT = """Be a helpful assistant"""

def call_model(state: AgentState):
    messages = state["messages"]
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages
    model = ChatOllama(model="llama3.2")
    response = model.invoke(messages)
    return {"messages": [response]}
