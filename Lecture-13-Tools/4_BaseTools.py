from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class CalculatorInput(BaseModel):
    a: int = Field(description="First number", required=True)
    b: int = Field(description="Second number", required=True)

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"

    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, a: int, b: int) -> int:
        return a * b

multiply_tool = MultiplyTool()

result = multiply_tool.invoke({'a':3, 'b':3})

print(f"result -> {result}")
print(f"tool name -> {multiply_tool.name}")
print(f"tool description -> {multiply_tool.description}")

print(f"tool args -> {multiply_tool.args}")
print(f"tool args schema -> {multiply_tool.args_schema}")


