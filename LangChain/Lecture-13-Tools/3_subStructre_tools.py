from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class CalculatorInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")

def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b

calculator_tool = StructuredTool.from_function(
    func=multiply,
    name="calculator",
    description="Multiply two numbers",
    args_schema=CalculatorInput
)

result = calculator_tool.invoke({'a':2,'b':3})
print(result)

print(f"tool name: {calculator_tool.name}")
print(f"tool description: {calculator_tool.description}")
print(f"tool args: {calculator_tool.args}")

print(calculator_tool.args_schema.model_json_schema())
