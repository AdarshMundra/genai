# Lecture 15 Revision

## Overview

This lecture covers **Agents**, which are the most advanced way to use LLMs. Unlike a fixed chain, an Agent uses the LLM as a "reasoning engine" to determine the sequence of steps and tool usage dynamically.

## Key Concepts

### 1. ReAct Logic (Reason + Act)

- The agent goes through a thinking process:
    1. **Thought**: What do I need to do?
    2. **Action**: Which tool should I use?
    3. **Observation**: What did the tool return?
- This loop repeats until the agent has enough information to provide a **Final Answer**.

### 2. Building an Agent

- **Prompts**: Agents require specific instructions to follow the ReAct logic. These are often pulled from the LangChain Hub (e.g., `hub.pull("hwchase17/react")`).
- **Constructor**: `create_react_agent(llm, tools, prompt)`
- **Executor**: `AgentExecutor(agent, tools, verbose=True)`
    - The `AgentExecutor` is the runtime that actually manages the loop, calls the tools, and feeds observations back to the agent.

### 3. Practical Example

- **Task**: "Find the capital of Madhya Pradesh and its current weather."
- **Execution**:
    1. Agent searches for the capital -> Observation: "Bhopal".
    2. Agent uses a `get_weather_data` tool for Bhopal -> Observation: "Clear, 40°C".
    3. Agent provides the combined final answer.

## Summary

Agents transform LLMs from passive text generators into active problem solvers capable of executing complex, multi-step tasks by autonomously navigating available tools.
