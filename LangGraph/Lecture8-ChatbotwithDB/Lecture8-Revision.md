# Lecture 8 Revision (LangGraph: Chatbot with Database Persistence)

## Overview

This lecture upgrades the chatbot's memory system from transient memory (`InMemorySaver`) to permanent on-disk storage using **SQLite** (`SqliteSaver`). This allows conversation threads to survive server restarts.

## Key Concepts

### 1. Database Persistence (`SqliteSaver`)

- `InMemorySaver` stores data in RAM. If the Python process dies, all chat histories are lost.
- **`SqliteSaver`** uses an SQLite database `chatbot.db` to permanently write checkpoints to disk.

### 2. Integrating SqliteSaver

Integrating an SQLite checkpointer requires establishing a synchronous SQLite connection:

```python
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

# Connect to database file (creates it if it doesn't exist)
conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)

# Initialize SqliteSaver with the connection
checkpointer = SqliteSaver(conn=conn)

# Compile graph
chatbot = graph.compile(checkpointer=checkpointer)
```

### 3. Retrieving All Stored Threads

Since the threads are now persistent, users should be able to see their previous chats when they reload the application.

- `checkpointer.list(None)` yields a generator of all stored checkpoints in the database.
- By parsing the `configurable['thread_id']` from each checkpoint's config, you can extract a list of all unique thread IDs to display in the UI sidebar.

```python
def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)
```

## Example Implementation

**Persistent Streamlit Chat Application**:

- Identical UI to Lecture 7, but powered by a SQLite database (`chatbot.db`).
- The `st.session_state["chat_threads"]` is initialized by querying the database (`retrieve_all_threads()`), ensuring that shutting down the Streamlit server does not wipe out user conversations.
