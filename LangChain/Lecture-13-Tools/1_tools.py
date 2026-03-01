
from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke('top news in india today')

# print(results)
print(f"Tool Name: {search_tool.name}")
print(f"Tool Description: {search_tool.description}")
print(f"Tool Args: {search_tool.args}")


# Shell Tool
shell_tool = ShellTool()
results = shell_tool.invoke('dir')
print(results)

print(f"Tool Name: {shell_tool.name}")
print(f"Tool Description: {shell_tool.description}")
print(f"Tool Args: {shell_tool.args}")

