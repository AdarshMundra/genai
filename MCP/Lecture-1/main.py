from fastmcp import FastMCP
import random
import json

mcp = FastMCP()

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

@mcp.tool()
def generate_random_number(min: int, max: int) -> int:
    """Generates a random number between min and max."""
    return random.randint(min, max)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)