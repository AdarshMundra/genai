# Lecture 13 Revision

## Overview

This lecture covers **Tools**, which allow LLMs to interact with the real world (search the web, run code, use a calculator, etc.).

## 1. Pre-built Tools

- **Package**: `langchain_community.tools`
- **Examples**:
    - `DuckDuckGoSearchRun`: For web searching.
    - `ShellTool`: For executing shell commands.
- **Attributes**: Every tool has a `name`, `description`, and `args` (arguments schema).

## 2. Defining Custom Tools

### The `@tool` Decorator

- The simplest way to create a tool. The function's docstring becomes the tool's description.

```python
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b
```

### `StructuredTool`

- Useful when you want more control, such as defining a specific Pydantic schema for inputs using `args_schema`.

### `BaseTool` (Class-based)

- Inherit from `BaseTool` to create complex tools with custom logic in the `_run` method. This is the most flexible approach.

## 3. Toolkits

- A `Toolkit` is a collection of related tools grouped together (e.g., a `MathToolkit` containing add, sub, mul, div tools).

## Summary

Tools are the "hands" of an LLM. By providing tools with clear names and descriptions, we enable the model to decide when and how to use external functionality to answer a prompt.
