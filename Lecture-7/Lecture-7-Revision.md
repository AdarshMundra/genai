# Lecture 7 Revision

## Overview

This lecture focuses on **LangChain Expression Language (LCEL)** and the various `Runnable` primitives that allow for building complex, readable, and efficient chains.

## Key Runnables

### 1. `RunnableSequence`

- **File**: `1_runnable_sequence.py`
- **Usage**: `RunnableSequence(step1, step2, step3)`
- **Function**: Explicitly defines a sequence of steps, equivalent to `step1 | step2 | step3`.

### 2. `RunnableParallel`

- **File**: `2_runnable_parallel.py`
- **Usage**: `RunnableParallel({"key1": chain1, "key2": chain2})`
- **Function**: Executes multiple chains in parallel and returns the results as a dictionary.

### 3. `RunnablePassthrough`

- **File**: `3_runnable_passthrough.py`
- **Usage**: `{"original": RunnablePassthrough(), "processed": chain}`
- **Function**: Passes the input through unchanged. Useful when you want to keep the original input alongside the output of a chain in a parallel branch.

### 4. `RunnableLambda`

- **File**: `4_runnable_Lambda.py`
- **Usage**: `RunnableLambda(custom_function)`
- **Function**: Allows you to wrap any custom Python function into a runnable so it can be part of an LCEL chain.

### 5. `RunnableBranch`

- **File**: `5_runnable_branch.py`
- **Usage**: `RunnableBranch((condition, chain_if_true), default_chain)`
- **Function**: Implements "if-else" logic within a chain. In the example, it only summarizes the text if it's longer than 300 words; otherwise, it passes it through.
