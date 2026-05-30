# Lecture 3 Revision (LangGraph: Conditional Workflow)

## Overview

This lecture introduces decision-making in graphs using **Conditional Edges**. This allows the workflow to dynamically branch into different paths based on the current state or the output of an LLM.

## Key Concepts

### conditional_edges

- A conditional edge uses a routing function to decide which node should be executed next.
- The routing function examines the `state` and returns the string name of the destination node.
- **Typing with Literal**: It is good practice to type-hint the return value of the routing function using `Literal` so that it matches exactly the node names available.

### Implementation Pattern

1. **Define the Routing Function**:

    ```python
    def check_condition(state: QuadState) -> Literal["real_roots", "repeated_roots", "no_real_roots"]:
        if state['discriminant'] > 0:
            return "real_roots"
        elif state['discriminant'] == 0:
            return "repeated_roots"
        else:
            return "no_real_roots"
    ```

2. **Add the Conditional Edge**:
   Instead of `graph.add_edge("Source", "Destination")`, you use:
    ```python
    graph.add_conditional_edges("SourceNode", routing_function)
    ```

## Example Implementations

1. **Quadratic Equation Solver**: Calculates the discriminant, then uses a conditional edge to branch off to different nodes to calculate real roots, repeating roots, or declare no real roots.
2. **Customer Support Triage**:
    - Uses `with_structured_output` to perform sentiment analysis ("positive" or "negative") on a customer review.
    - A conditional edge checks the sentiment.
    - **Positive Path**: Responds with a thank-you message.
    - **Negative Path**: Runs an advanced diagnosis to extract issue type, tone, and urgency, then routes to a specialized negative response node.
