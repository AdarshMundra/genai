from langgraph.graph import StateGraph, START, END
from typing import TypedDict

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()


class State(TypedDict):
    Question: str
    Answer: str
    

def llm_qa(state: State) -> State:

    # extract the question from state
    question = state['Question']

    # form a prompt
    prompt = f'Answer the following question {question}'

    # ask that question to the LLM
    answer = model.invoke(prompt).content

    # update the answer in the state
    state['Answer'] = answer

    return state

if __name__ == "__main__":
    # create a state graph
    workflow = StateGraph(State)

    # add the node
    workflow.add_node("llm_qa", llm_qa)

    # add the edges
    workflow.add_edge(START, "llm_qa")
    workflow.add_edge("llm_qa", END)

    # compile the graph
    app = workflow.compile()

    # invoke the graph
    print(app.invoke({"Question": "What is the capital of France?"}))