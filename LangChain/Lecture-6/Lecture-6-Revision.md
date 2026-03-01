# Lecture 6 Revision

## Overview

This lecture is a deep dive into the internal workings of LangChain by building a "Nakli" (fake) version of LangChain from scratch. It uses Python's Abstract Base Classes (`ABC`) to define how components interact.

## Key Concepts

### 1. The `Runnable` Interface

- Every component (LLM, Prompt, Parser) in LangChain inherits from a base `Runnable` class.
- They all implement an `.invoke()` method which ensures they can be chained together consistently.

### 2. Custom Components (Nakli versions)

- **NakliLLM**: A fake model that returns random pre-defined responses.
- **NakliPromptTemplate**: A fake template that uses Python's `.format()` method.
- **NakliStrOutputParser**: A fake parser that extracts the response string.

### 3. Chaining (RunnableConnector)

- Demonstrates how the pipe (`|`) operator works internally by creating a `RunnableConnector` that iterates through a list of runnables, passing the output of one as the input to the next.

## Summary

By rebuilding the core components, this lecture explains why LangChain uses the `|` operator and how different components (which might have different logic) can talk to each other through the shared `invoke` interface.
