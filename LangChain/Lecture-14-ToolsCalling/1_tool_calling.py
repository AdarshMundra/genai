from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests





load_dotenv()


# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b


model = ChatOpenAI()

model_with_tools = model.bind_tools([multiply])


print(model_with_tools.invoke('Hi how are you'))

query = HumanMessage('can you multiply 3 with 100')
message = [query]
response = model_with_tools.invoke(message)

print(response)

message.append(response)

tool_result = multiply.invoke(response.tool_calls[0])

print(tool_result)

message.append(tool_result)

# final_response = model_with_tools.invoke(query)

# print(final_response)
# llm_with_tools.invoke(messages).content


print(model_with_tools.invoke(message).content)