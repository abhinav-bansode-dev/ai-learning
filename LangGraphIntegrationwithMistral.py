from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph, END

# Initialize Ollama with mistral
llm = OllamaLLM(model="llama3")

# Define workflow functions
def llm_step(state):
    text = state["input"]
    result = llm.invoke(f"Summarize in one sentence: {text}")
    return {"llm_output": result}

def validate_step(state):
    output = state["llm_output"]
    return {
        "llm_output": output,
        "validation": f"Length: {len(output)} characters"
    }


# Build graph
graph = StateGraph(dict)

graph.add_node("llm", llm_step)
graph.add_node("validate", validate_step)

graph.set_entry_point("llm")
graph.add_edge("llm", "validate")
graph.add_edge("validate", END)

# Compile graph
app = graph.compile()

# Run workflow
result = app.invoke({"input": "LangChain and LangGraph help orchestrate AI workflows."})
print(result)
