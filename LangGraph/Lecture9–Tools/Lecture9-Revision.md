# Lecture 9 Revision (LangGraph: Agents with Tools)

## Overview

Building upon the persistent chatbot, this lecture transforms the standard chatbot into an **Agent** by giving it access to external **Tools**. The agent can decide when to use a tool (like a web search, API call, or calculator) to fulfill a user's request, executing everything in a loop until the final answer is generated.

## Key Concepts

### 1. Defining and Binding Tools

Tools are defined using LangChain's `@tool` decorator or built-in community tools.

- They are then bound to the LLM so the LLM is aware of their schemas and can request to execute them.

```python
search_tool = DuckDuckGoSearchRun()
@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict: ...

tools = [search_tool, get_stock_price, calculator]
llm_with_tools = llm.bind_tools(tools)
```

### 2. The ToolNode

LangGraph provides a prebuilt `ToolNode` that acts as the executor.

- You pass the list of tools to `ToolNode()`.
- When the LLM requests a tool call, the graph moves to `ToolNode`, which automatically runs the correct Python function and returns the result as a `ToolMessage`.

```python
from langgraph.prebuilt import ToolNode
tool_node = ToolNode(tools)
graph.add_node("tools", tool_node)
```

### 3. Conditional Routing with `tools_condition`

LangGraph also provides a pre-built routing condition called `tools_condition`.

- This function checks the last message. If the LLM requested a tool, it routes to `"tools"`. If the LLM outputted standard text, it routes to `END`.

```python
from langgraph.prebuilt import tools_condition

graph.add_conditional_edges("chat_node", tools_condition)
graph.add_edge('tools', 'chat_node') # loop back after tool execution
```

### 4. Streaming Tools in Streamlit

To make the UI feel reactive, the frontend intercepts `ToolMessage` events during streaming.

- Instead of just streaming text, it captures when a `ToolMessage` is generated and displays an `st.status` box (e.g., "🔧 Using `calculator`...").

## Example Implementation

**Stock & Math Bot**:

- A Streamlit UI agent equipped with `DuckDuckGoSearch`, a custom `get_stock_price` using AlphaVantage API, and a custom arithmetic `calculator`.
- The user can ask "What is the price of AAPL?" and the LLM will route to `tools`, execute the API, retrieve the JSON, route back to the LLM, and provide natural language output. All while saving state to SQLite.
