# Lecture 13 Revision (LangGraph: Subgraphs)

## Overview

This lecture discusses **Subgraphs**, a critical pattern for modular application design. Instead of building one massive, tangled, monolithic graph, you can build specialized smaller graphs (Subgraphs) that handle specific isolated workflows, and invoke them seamlessly from a broader Parent Graph.

## Key Concepts

### 1. The Subgraph

A Subgraph is just a standard `StateGraph` compilation, perfectly self-contained. It has its own dedicated `TypedDict` State, its own nodes, and its own routing logic.

```python
class SubState(TypedDict):
    input_text: str
    translated_text: str

# standard compilation
subgraph = subgraph_builder.compile()
```

### 2. The Parent Graph

The Primary or Parent Graph manages the high-level application flow. It has a completely different state definition geared towards the broader task.

```python
class ParentState(TypedDict):
    question: str
    answer_eng: str
    answer_hin: str
```

### 3. Invoking the Subgraph from a Parent Node

The simplest way to connect them is to just manually invoke the compiled subgraph inside a parent node function. The parent node maps the parent's data to the subgraph's input, runs the subgraph synchronously, and then extracts the subgraph's output to update the parent's state.

```python
def translate_answer(state: ParentState):
    # Pass Data to Subgraph Interface
    sub_payload = {'input_text': state['answer_eng']}

    # Execute the isolated subgraph workflow
    result = subgraph.invoke(sub_payload)

    # Map Subgraph output perfectly back to parent state
    return {'answer_hin': result['translated_text']}
```

## Benefits of Subgraphs

- **Modularity:** Let specialized teams work on specific sub-agents (e.g., a "Research API Graph" and a "Summary Document Graph").
- **State Encapsulation:** Prevents state-bloat. The Translator node doesn't need to know about the user's original "question", it only needs the "input_text" it's translating.
- **Reusability:** A robust tool-calling subgraph can be called by dozens of different parent administrative nodes across different enterprise applications.

## Example Implementation

**Bilingual QA Bot**:

- **Parent Process**: A parent node fields the original user query and generates an English answer via LLM.
- **Subgraph Process**: The parent then passes the completed English text to an independent Subgraph. The Subgraph applies a strict prompt template strictly intended for perfect Hindi translation. The final Hindi response is then returned to the main process for the user.
