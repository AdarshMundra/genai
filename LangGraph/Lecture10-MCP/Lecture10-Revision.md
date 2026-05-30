# Lecture 10 Revision (LangGraph: MCP Implementation)

## Overview

This lecture explores how to integrate the **Model Context Protocol (MCP)** into a LangGraph Agent. MCP allows your agent to dynamically fetch and use tools provided by external, remote, or local "MCP Servers" without hardcoding them in your main application.

## Key Concepts

### 1. MultiServerMCPClient

- LangChain provides the `langchain_mcp_adapters.client.MultiServerMCPClient` to connect to multiple MCP servers simultaneously.
- Connections can be done via local commands (e.g., executing a local python script via `stdio`) or over the network (e.g., `streamable_http` or `sse`).
- Example setup:
    ```python
    client = MultiServerMCPClient({
        "math_server": {
            "transport": "stdio",
            "command": "python3",
            "args": ["path/to/server.py"]
        },
        "remote_server": {
            "transport": "streamable_http",
            "url": "https://remote-mcp.app/mcp"
        }
    })
    ```

### 2. Async Execution Flow

- MCP operations are inherently asynchronous. Because of this, the entire graph setup transitions to an async architecture.
- **Async LLM Invocation**: Instead of `invoke`, the node uses `await llm_with_tools.ainvoke(messages)`.
- **Async SqliteSaver**: The standard synchronous sqlite checkpointer is replaced by `AsyncSqliteSaver` using the `aiosqlite` library.

### 3. Loading MCP Tools

- By awaiting `client.get_tools()`, you receive a list of LangChain-compatible `BaseTool` objects from the MCP servers.
- These fetched MCP tools are simply appended to checking custom local tools array (`search_tool`, etc.) and bound to the LLM:
    ```python
    mcp_tools = await client.get_tools()
    tools = [search_tool] + mcp_tools
    llm_with_tools = llm.bind_tools(tools)
    ```

## Example Implementation

**Advanced API Agent**:

- Instead of hardcoding all analytical logic or database queries, the agent dials into external MCP servers to fetch its tools during initialization.
- Uses threading to run a dedicated backend asyncio event loop safely alongside the synchronous logic where necessary.
