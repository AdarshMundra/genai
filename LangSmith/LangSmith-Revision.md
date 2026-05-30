# LangSmith Revision Notes

## Overview

The `LangSmith` folder demonstrates how to integrate tracing, observability, and evaluation into LangChain and LangGraph workflows. LangSmith makes it easy to track LLM inputs/outputs, latency, token usage, and complex agent/graph executions.

## Key Concepts

### 1. Simple Chains & Pipelines

The scripts start by demonstrating basic LangChain pipelines (e.g., prompt → model → parser).

- **`1_simple_llm_call.py`**: A basic `prompt | model | parser` chain.
- **`2_sequential_chain.py`**: A chain where the output of one model directly feeds into another prompt template `prompt1 | model | parser | prompt2 | model | parser`.
- By simply having LangSmith environment variables configured (e.g., `LANGCHAIN_TRACING_V2=true`, `LANGCHAIN_API_KEY`), these standard LangChain runnables are **automatically traced** without any extra code.

### 2. Manual Tracing with `@traceable`

When writing custom Python functions (like loading a PDF, splitting text, or querying a vector store), LangSmith doesn't trace them automatically unless told to do so.

- The **`@traceable`** decorator (from `langsmith`) allows you to wrap any Python function to track its execution.
- You can categorize traces using `name` and `tags` kwargs.

```python
from langsmith import traceable

@traceable(name="load_pdf", tags=["data-ingestion"])
def load_pdf(path: str):
    return PyPDFLoader(path).load()
```

- A wrapped function passing its output to another wrapped function automatically nests the traces in the LangSmith UI.

### 3. Tracing LangGraph Applications

In `5_langgraph.py`, LangGraph and LangSmith are combined to trace a modular essay grading system.

- The `StateGraph` performs a **Fan-out → Join** workflow: it runs `evaluate_language`, `evaluate_analysis`, and `evaluate_thought` in parallel, merging their scores using `operator.add` in the state.
- Each of these node functions is decorated with `@traceable(name="...", metadata={"dimension": "..."})` to inject custom metadata into the trace.
- **Root Run Name**: When invoking a compiled LangGraph workflow, you can assign a custom root name, tags, and metadata to the entire run by passing a `config` dictionary to `.invoke()`:

```python
result = workflow.invoke(
    {"essay": essay2},
    config={
        "run_name": "evaluate_upsc_essay",
        "tags": ["essay", "langgraph", "evaluation"],
        "metadata": {"essay_length": len(essay2)}
    }
)
```

### 4. Agent Tracing

`4_agent.py` demonstrates standard ReAct agent creation using `create_react_agent` and `AgentExecutor`. Agent executions are automatically nested nicely within LangSmith, allowing you to see the exact intermediate steps (e.g., when the agent decides to use `search_tool` vs `get_weather_data`) inside the LangSmith dashboard.

## Summary

The primary lesson is that while LangChain handles automatic tracing, you must use `@traceable` and `config` dictionaries to gain deep visibility into the granular custom python logic and complex graph node behaviors.
