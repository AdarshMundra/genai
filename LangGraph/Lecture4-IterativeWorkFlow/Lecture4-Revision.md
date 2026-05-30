# Lecture 4 Revision (LangGraph: Iterative Workflow)

## Overview

Iterative workflows (loops) are where LangGraph shines compared to standard chains. By creating cycles in the graph, we can build **self-correcting agents** that repeatedly generate, evaluate, and refine their own output until it meets a certain standard.

## Key Concepts

### 1. Cycles in StateGraph

- You can route an edge from a node back to an earlier node in the graph.
- A conditional edge is usually placed after an "Evaluator" node to either loop back to an "Optimizer" or break out of the loop and go to `END`.

### 2. Preventing Infinite Loops

- When building loops, LLMs might get stuck forever if they can't meet the evaluation criteria.
- **Solution**: Keep an `iteration` count in the `State`. Increment it on each loop, and in your routing function, force an exit (e.g., path to `approved` or `END`) if `iteration >= max_iteration`.
- Example Router:
    ```python
    def route_evaluation(state: TweetState):
        if state['evaluation'] == 'approved' or state['iteration'] >= state['max_iteration']:
            return 'approved' # Go to END or next phase
        else:
            return 'needs_improvement' # Go to Optimizer
    ```

### 3. State History Tracking

- Using `Annotated[list[str], operator.add]`, you can track the history of generated responses and feedback across iterations. This is very useful for debugging the agent's thought process.

## Example Implementation

**Viral Tweet Generator**:

1. **Generator Node**: Takes a topic and drafts a clever tweet.
2. **Evaluator Node**: A structural output LLM acts as a strict critic. It returns an evaluation status (`approved` or `needs_improvement`) and detailed feedback.
3. **Optimizer Node (The Loop)**: If the conditional router detects `needs_improvement`, the flow goes to the optimizer. It receives the feedback and the original tweet, rewrites the tweet to be funnier, increments the iteration count, and _loops back_ to the evaluator.
