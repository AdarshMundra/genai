# MCP (Model Context Protocol) Revision Notes

## Overview

The `MCP` folder contains foundational examples for creating your own **Model Context Protocol (MCP)** Servers. While LangGraph uses MCP _clients_ to connect to external tools, this repository demonstrates how to actually _build_ the server that provides those tools.

## Key Concepts

### 1. FastMCP

**FastMCP** is a lightweight, FastAPI-like framework for rapidly building MCP servers in Python. It heavily utilizes decorators to map standard Python functions directly into MCP-compatible network endpoints that LLM agents can call.

### 2. Defining Tools

To expose a Python function as an AI tool across the network, you simply define the function with strict type hints and a docstring, and wrap it with the `@mcp.tool()` decorator.

- **Type Hints**: Are strictly required because they are automatically converted into the JSON schema that the LLM agent reads to know what arguments to pass.
- **Docstrings**: Are required because they become the tool description the LLM agent uses to understand _when_ and _why_ to use the tool.

```python
from fastmcp import FastMCP
import random

mcp = FastMCP()

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers. Useful for basic arithmetic."""
    return a + b

@mcp.tool()
def generate_random_number(min: int, max: int) -> int:
    """Generates a random integer between min and max inclusive."""
    return random.randint(min, max)
```

### 3. Server Execution

To run the server and expose the tools, you execute the `mcp.run()` command.

- You specify the **`transport`** protocol (e.g., `"http"` for a web server, or `"stdio"` for local standard input/output streaming).
- By running `mcp.run(transport="http", host="0.0.0.0", port=8000)`, the MCP server spins up and actively listens for remote LangGraph/LangChain agents requesting to use its tools.

## Summary

Building an MCP Server is incredibly straightforward using `FastMCP`. By decorating strongly-typed Python functions with `@mcp.tool()`, any local python script can instantly become a remote toolset that an AI Agent can dynamically import and use.
