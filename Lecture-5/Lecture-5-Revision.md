# Lecture 5 Revision

## Overview

This lecture covers different ways of chaining components in LangChain using the pipe (`|`) operator.

## Files Summary

### `1_simple_chain.py`

- **Description**: The most basic chain structure.
- **Structure**: `prompt | model | output_parser`
- **Functionality**: Takes a topic, formats it into a prompt, gets a response from the model, and parses it as a string.

### `2_sequential_chain.py`

- **Description**: Connecting multiple chains where the output of one is the input to the next.
- **Structure**: `prompt1 | model | parser | prompt2 | model | parser`
- **Functionality**: Generates a detailed report on a topic, then takes that report and generates a 5-pointer summary.

### `3_parallel_chain.py`

- **Description**: Running multiple chains simultaneously on the same input.
- **Key Class**: `RunnableParallel`
- **Functionality**:
    1. Takes a text about SVMs.
    2. Runs two tasks in parallel: generating short notes and generating a quiz.
    3. Merges the results into a single document using a third prompt.

### `4_conditional_chain.py`

- **Description**: Branching the chain logic based on intermediate results.
- **Key Classes**: `RunnableBranch`, `PydanticOutputParser`.
- **Functionality**:
    1. Classifies the sentiment of user feedback (Positive/Negative) using Pydantic.
    2. Based on the sentiment, routes the feedback to either a "Positive Response" prompt or a "Negative Response" prompt.
