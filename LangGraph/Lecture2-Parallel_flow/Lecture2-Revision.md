# Lecture 2 Revision (LangGraph: Parallel Flow)

## Overview

This lecture explores how to run operations simultaneously using **Parallel Flow** in LangGraph. When multiple edges originate from the same node (or `START`), LangGraph automatically executes those destination nodes in parallel.

## Key Concepts

### 1. Parallel Execution

- If you have multiple independent tasks that rely on the same input state, you can map them all directly from the source node.
- This is highly efficient for tasks like running multiple evaluations or calculators at the same time.
- Example:
    ```python
    graph.add_edge(START, "StrikeRateCalculator")
    graph.add_edge(START, "BallPerBoundaryCalculator")
    graph.add_edge(START, "BoundaryPercentageCalculator")
    ```

### 2. Joining Parallel Branches

- After parallel nodes finish, their results are typically merged into a single join node (e.g., a "Summary" node).
- Example:
    ```python
    graph.add_edge("StrikeRateCalculator", "Summary")
    graph.add_edge("BallPerBoundaryCalculator", "Summary")
    graph.add_edge("BoundaryPercentageCalculator", "Summary")
    ```

### 3. Reducers (`Annotated` State)

- When multiple parallel nodes update the _same key_ in the state dictionary simultaneously, it causes conflicts unless you tell LangGraph how to handle it.
- **Solution**: Use `typing.Annotated` with a reducer function (like `operator.add`). This tells LangGraph to append/add the values together instead of overwriting them.
- Example (from Essay Review):
    ```python
    from typing import Annotated
    import operator

    class UPSCState(TypedDict):
        # individual_scores will collect scores from parallel nodes as a list
        individual_scores: Annotated[list[int], operator.add]
    ```

## Example Implementations

1. **Cricket Batsman Record**: Given basic stats, calculates Strike Rate, Balls Per Boundary, and Boundary Percentage in parallel, then creates a final summary.
2. **Essay Reviewer**: An essay is evaluated on Language, Analysis, and Clarity simultaneously by an LLM with Structured Output. The scores are aggregated into a list, and a final node computes the average and summarizes the feedback.
