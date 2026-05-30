# Lecture 11 Revision (LangGraph: RAG Agent)

## Overview

This lecture combines **Retrieval-Augmented Generation (RAG)** with a LangGraph Agent. Rather than just asking the LLM direct questions, the agent is equipped with a `rag_tool` that it can call to search through embedded PDF documents specifically uploaded for the current chat thread.

## Key Concepts

### 1. Thread-Specific Vector Stores

- A global dictionary (`_THREAD_RETRIEVERS`) maps a `thread_id` to its unique FAISS vector store retriever.
- When a user uploads a PDF, the file is temporarily saved, parsed via `PyPDFLoader`, split via `RecursiveCharacterTextSplitter`, embedded using `OpenAIEmbeddings`, and saved into a new `FAISS` store.
- The `FAISS` retriever is then assigned to the user's `thread_id`.

### 2. The RAG Tool

- To act as an agent, instead of forcefully injecting context into every prompt, a dedicated `@tool` is created.
- The LLM decides when to call `rag_tool(query, thread_id)`.
- The tool looks up `_THREAD_RETRIEVERS[thread_id]`, performs a similarity search, and returns the raw context chunks.

```python
@tool
def rag_tool(query: str, thread_id: str) -> dict:
    retriever = _get_retriever(thread_id)
    if not retriever:
        return {"error": "Upload PDF first."}

    docs = retriever.invoke(query)
    return {"context": [d.page_content for d in docs]}
```

### 3. Agent System Prompt

- The LLM is guided by a `SystemMessage` injected during compilation explicitly telling it:
    > "For questions about the PDF, use the `rag_tool` with this specific `thread_id`. If there's no document, ask the user to provide one."
- This gives the LLM the self-awareness to gracefully request file uploads and only search when document data is necessary.

## Example Implementation

**Document Q&A Assistant**:

- A Streamlit frontend where users drop a PDF file.
- The backend `ingest_pdf()` function processes the file in the background.
- During chatting, the agent seamlessly invokes the `rag_tool` whenever it recognizes the user is querying information contained in the PDF, while continuing to use its normal conversational memory for generic queries.
