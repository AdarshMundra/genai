from langchain_community.tools import tool

@tool
def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b


result = multiply.invoke({'a':2,'b':3})
print(result)

print(f"tool name: {multiply.name}")
print(f"tool description: {multiply.description}")
print(f"tool args: {multiply.args}")

print(multiply.args_schema.model_json_schema())