# Lecture 5 Revision (LangGraph: Basic Chatbot)

## Overview

This lecture covers building a basic conversational agent (chatbot) using LangGraph. The main focus is on maintaining a conversation history so the LLM remembers previous interactions.

## Key Concepts

### 1. State representing Messages

Instead of a custom dictionary of distinct variables, a chatbot's state is primarily a list of messages.

- **`add_messages` Reducer**: The `messages` key in the state uses the `add_messages` function (from `langgraph.graph.message`) to manage conversation history. It ensures that new messages are appended to the existing list rather than overwriting it entirely.

```python
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from typing import TypedDict, Annotated

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
```

### 2. Checkpointer (MemorySaver)

- Without memory, an LLM forgets the conversation as soon as the execution finishes.
- **`MemorySaver`** (or `InMemorySaver`) is a checkpointer that saves the graph's state _during_ and _after_ execution.
- By compiling the graph with a checkpointer, LangGraph remembers the state associated with a unique `thread_id`.

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
workflow = graph.compile(checkpointer=checkpointer)
```

### 3. Thread IDs (Config)

To recall the memory for a particular user or conversation, you pass a `config` dictionary with a `thread_id` during invocation:

```python
config = {'configurable': {"thread_id": "user_session_1"}}
workflow.invoke({"messages": [HumanMessage(content="Hello")]}, config=config)
```

## Example Implementation

**Simple CLI Chatbot**:

- A simple loop asks for user input.
- Input is wrapped in a `HumanMessage` and sent to the workflow using `.invoke()`.
- The workflow correctly recalls past interactions, enabling follow-up questions because the checkpointer stores the message history matching the `thread_id`.
