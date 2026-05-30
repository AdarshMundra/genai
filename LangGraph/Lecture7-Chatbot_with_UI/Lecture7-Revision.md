# Lecture 7 Revision (LangGraph: Chatbot with Streamlit UI)

## Overview

This lecture bridges the gap between a backend LangGraph chatbot and a functional frontend user interface using **Streamlit**. It demonstrates how to wrap a LangGraph state machine with memory into a visually appealing web application.

## Key Concepts

### 1. LangGraph Backend Setup

- The backend remains a `StateGraph` compiled with an `InMemorySaver`.
- Uses `add_messages` to track conversation history.
- The compiled `chatbot` object is imported by the frontend script to handle the logic.

### 2. Managing Threads in Streamlit

Since the web application needs to handle multiple parallel sessions or chats, it relies on Streamlit's `st.session_state`:

- **`thread_id`**: A unique ID (generated via `uuid.uuid4()`) is stored in `st.session_state` to represent the current active chat.
- **`chat_threads`**: A list kept in session state to show past conversations in the sidebar.
- Every chat message is passed to the LangGraph backend along with the active `thread_id` so the `InMemorySaver` knows which memory to retrieve.

### 3. Streaming Assistant Responses

To provide a natural, typing-effect response, the backend's `.stream()` method is utilized:

- Using `stream_mode="messages"`, LangGraph yields message chunks as the LLM generates them.
- Only the `AIMessage` chunks are intercepted and yielded to Streamlit's `st.write_stream()` to display the text smoothly.

```python
def ai_only_stream():
    for message_chunk, metadata in chatbot.stream(
        {"messages": [HumanMessage(content=user_input)]},
        config=CONFIG,
        stream_mode="messages"
    ):
        if isinstance(message_chunk, AIMessage):
            yield message_chunk.content

ai_message = st.write_stream(ai_only_stream())
```

### 4. Conversation History UI

- Historic messages are manually fetched from the chatbot's state using `chatbot.get_state(config)` and rendered when switching between threads.

## Example Implementation

**Streamlit Chat Application**:

- A sidebar that holds "New Chat" and historical conversation thread buttons.
- A main chat interface displaying user prompts and streaming AI responses.
- Handles switching between ongoing threads via LangGraph's checkpointer.
