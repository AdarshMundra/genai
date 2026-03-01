# Lecture 10 Revision

## Overview

This lecture covers **Vector Stores**, specifically **ChromaDB**, which are specialized databases designed to store and search high-dimensional vector embeddings.

## Key Concepts

### 1. Initializing Chroma

- **Package**: `langchain_community.vectorstores` (Note: Moving to `langchain_chroma`).
- **Setup**:
    ```python
    vector_store = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory='my_chroma_db',
        collection_name='sample'
    )
    ```

### 2. Operations

- **Adding Documents**: `vector_store.add_documents(docs)`
- **Retrieving**: `vector_store.get(include=['embeddings','documents', 'metadatas'])`
- **Updating**: `vector_store.update_document(document_id, document)`
- **Deleting**: `vector_store.delete(ids=[id_list])`

### 3. Searching

- **Similarity Search**: `vector_store.similarity_search(query, k=2)` returns the most similar documents.
- **Search with Scores**: `vector_store.similarity_search_with_score(query)` returns documents along with their distance/similarity score.
- **Metadata Filtering**: You can narrow down searches using filters:
    ```python
    vector_store.similarity_search(query, filter={"team": "Mumbai Indians"})
    ```

## Summary

Vector stores allow us to perform **semantic search** rather than keyword search, enabling the model to find information based on meaning even if exact words don't match.
