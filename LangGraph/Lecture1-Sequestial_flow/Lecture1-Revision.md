# Lecture 1 Revision (LangGraph: Sequential Flow)

## Overview

This lecture introduces **LangGraph**, an extension of LangChain used for building stateful, multi-actor applications with LLMs. Unlike simple linear chains in LangChain (LCEL), LangGraph allows for complex, cyclic graphs. This lecture focuses on the simplest form: **Sequential Flow**.

## Key Concepts

### 1. State (`TypedDict`)

- Every graph must have a defined `State`. This is a shared data structure that gets passed from node to node.
- Typically defined using Python's `TypedDict`.
- Example:
    ```python
    class BMIState(TypedDict):
        weight_kg: float
        height_m: float
        bmi: float
        category: str
    ```

### 2. Nodes

- Nodes are simply Python functions. They take the current `state` as input, perform some operation (like math or calling an LLM), and return a dictionary containing the updates to the state.
- Example:
    ```python
    def calculate_BMI(state: BMIState) -> BMIState:
        # compute BMI and return the updated dictionary
        return {'bmi': state['weight_kg'] / (state['height_m']**2)}
    ```

### 3. Edges and Graph Compilation

- **Edges** define the flow of execution from one node to another.
- Special nodes `START` and `END` represent the beginning and termination of the workflow.
- **Compilation**: Once nodes and edges are added, the graph is compiled into a runnable application.
- Example:
    ```python
    graph = StateGraph(BMIState)
    graph.add_node('calculate_BMI', calculate_BMI)
    graph.add_node('label_bmi', label_bmi)

    graph.add_edge(START, 'calculate_BMI')
    graph.add_edge('calculate_BMI', 'label_bmi')
    graph.add_edge('label_bmi', END)

    workflow = graph.compile()
    final_state = workflow.invoke(initial_state)
    ```

## Example Implementations

1. **BMI Calculator**: A pure logical sequence without LLMs.
2. **Simple LLM QA**: A single node that invokes an LLM to generate an answer.
3. **Blog Generator**: A multi-step LLM sequence where one node generates an outline from a topic, and the next node writes the blog using that outline.
