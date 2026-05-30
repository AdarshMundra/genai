# Lecture 12 Revision (LangGraph: Human-in-the-Loop)

## Overview

This lecture covers **Human-in-the-Loop (HITL)** interaction. For high-stakes operations (like spending money, sending an email, deleting database records), we do not want an autonomous agent acting alone. HITL allows the graph's execution to intentionally pause and wait for a human supervisor's approval before proceeding.

## Key Concepts

### 1. The `interrupt` Command

- LangGraph provides the `interrupt` function from `langgraph.types`.
- When invoked inside a node or a tool, it suspends execution and returns control entirely back to the developer (or the user interface), surfacing whatever payload was passed into the `interrupt()` call.

```python
from langgraph.types import interrupt

@tool
def purchase_stock(symbol: str, quantity: int) -> dict:
    # 1. Execution pauses here!
    decision = interrupt(f"Approve buying {quantity} shares of {symbol}? (yes/no)")

    # 2. Execution resumes here after human responds
    if decision == "yes":
        return {"status": "Purchased!"}
    else:
        return {"status": "Declined!"}
```

### 2. Handling the Interrupt in Invocation

- When `chatbot.invoke(state, config)` hits an interrupt, it returns early.
- You can inspect the result dictionary. If it contains `__interrupt__`, it means the execution is paused.
- You can extract the prompt payload, ask the user, and then **resume** the graph context.

### 3. Resuming the Graph (`Command`)

- To continue the execution, you use the `Command(resume=value)` object from `langgraph.types`.
- By passing `Command(resume=user_decision)` into `chatbot.invoke()`, LangGraph wakes up exactly where it left off, assigning the `user_decision` string to the variable that was waiting on the `interrupt` call.

```python
from langgraph.types import Command

result = chatbot.invoke(state, config)
interrupts = result.get("__interrupt__", [])

if interrupts:
    human_decision = input(interrupts[0].value)  # Ask the human
    # Resume the suspended node
    result = chatbot.invoke(Command(resume=human_decision), config)
```

## Example Implementation

**Stock Purchasing Agent**:

- The agent has a normal `get_stock_price` tool and a critical `purchase_stock` tool.
- If the user types "Buy 10 shares of AAPL", the agent routes to the `purchase_stock` tool.
- The tool fires an `interrupt`, stopping the graph and prompting the CLI: "Approve buying 10 shares of AAPL? (yes/no)".
- The system waits. Once the human replies "yes", the agent resumes, confirms the purchase, and responds back to the user naturally.
