from langchain_community.tools import tool

@tool
def add(a:int,b:int) -> int:
    """Add two numbers"""
    return a+b

@tool
def sub(a:int,b:int) -> int:
    """Subtract two numbers"""
    return a-b

@tool
def mul(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b

@tool
def div(a:int,b:int) -> int:
    """Divide two numbers"""
    return a/b

class MathToolkit:
    def __init__(self):
        print("Math Toolkit Initialized")
        pass
    
    def get_tools(self):
        return [add, sub, mul, div]

math_toolkit = MathToolkit()

tools = math_toolkit.get_tools()

for tool in tools:
    print(tool.name, "=>", tool.description)


# Using the tools

# print(tools.add(1,2))
# print(math_toolkit.sub(1,2))
# print(math_toolkit.mul(1,2))
# print(math_toolkit.div(1,2))

# print(math_toolkit.invoke({"name":"add","args":{"a":1,"b":2}}))
