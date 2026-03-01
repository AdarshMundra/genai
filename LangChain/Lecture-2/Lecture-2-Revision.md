# Lecture 2 Revision

## Overview
This lecture focuses on **Prompt Engineering** and building **User Interfaces** using `Streamlit`. It covers creating prompt templates, managing chat history, and loading prompts from files.

## Files Summary

### `1_prompt_ui.py`
- **Description**: A basic Streamlit application.
- **Functionality**:
    - Takes a text input from the user ("Enter your document").
    - Uses `ChatOpenAI` (gpt-3.5-turbo) to summarize the input.
    - Displays the result.

### `2_prompt_ui_dropdown.py`
- **Description**: An advanced Streamlit app with structured inputs.
- **Functionality**:
    - Provides dropdowns for "Research Paper Name", "Explanation Style", and "Explanation Length".
    - Uses a `PromptTemplate` to format these inputs into a prompt.
    - Invokes the model with the formatted prompt.

### `3_prompt_ui_dropdown.py`
- **Description**: Similar to the previous script but demonstrates **loading prompts from files**.
- **Functionality**:
    - Loads a prompt template from `template.json` using `load_prompt`.
    - constructs a chain `chain = template | model`.
    - Invokes the chain with user inputs.

### `4_chatbot.py`
- **Description**: A console-based chatbot.
- **Key Concepts**: `SystemMessage`, `HumanMessage`, `AIMessage`.
- **Functionality**:
    - Maintains a `chat_history` list.
    - Appends user input and model response to the history in a loop.
    - Allows a continuous conversation.

### `5_chat_prompt_template.py`
- **Description**: Usage of `ChatPromptTemplate`.
- **Functionality**:
    - Creates a template with a system message and a human message.
    - Uses variables (`{domain}`, `{topic}`) to generate a prompt.

### `6_message_placceholder.py`
- **Description**: usage of `MessagesPlaceholder`.
- **Functionality**:
    - Useful for injecting a list of messages (like chat history) into a prompt template.
    - Reads `chat_history.txt` and inserts it into the prompt.

### `prompt_generator.py`
- **Description**: creating and saving a Prompt Template.
- **Functionality**:
    - Defines a comprehensive `PromptTemplate` with input variables.
    - Saves this template to `template.json` for reuse (used in `3_prompt_ui_dropdown.py`).
