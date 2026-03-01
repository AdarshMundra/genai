# Lecture 12 Revision

## Overview

This lecture demonstrates a **complete RAG (Retrieval-Augmented Generation) pipeline** integrated into a web application using Streamlit. The project is a "YouTube Video Knowledge Base" that allows users to ask questions about any English/Hindi YouTube video.

## Key Components & Workflow

### 1. Data Ingestion

- **Tool**: `YouTubeTranscriptApi`
- **Process**: Fetches the transcript of a video using its Video ID. It supports multiple languages (e.g., `en`, `hi`).

### 2. Document Processing

- **Splitter**: `RecursiveCharacterTextSplitter`
- **Settings**: `chunk_size=1000`, `chunk_overlap=200`.
- **Function**: Converts the long transcript string into smaller, overlapping chunks to preserve context.

### 3. Vector Storage

- **Store**: `FAISS` (In-memory)
- **Embeddings**: `OpenAIEmbeddings`
- **Session State**: The retriever is stored in `st.session_state.retriever` so it persists across Streamlit reruns.

### 4. Retrieval & Augmentation

- **Prompt**: A specific prompt template that instructs the LLM to answer **ONLY** using the provided context and say "I don't know" if the information is missing.
- **Chain Architecture**:
    ```python
    parallel_chain = RunnableParallel({
        "context": retriever | format_docs_function,
        "question": RunnablePassthrough()
    })
    main_chain = parallel_chain | prompt | model | parser
    ```

### 5. UI (Streamlit)

- `st.text_input` for Video ID and Question.
- `st.button` to trigger transcript fetching or question answering.
- `st.success`/`st.error` for user feedback.

## Summary

This project ties together everything learned about Loaders, Splitters, Embeddings, Vector Stores, and LCEL to build a functional, user-facing AI application.
