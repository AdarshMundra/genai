# Lecture 11 Revision

## Overview

This lecture explores **Retrievers**, which are interfaces that return documents given an unstructured query. They are more general than vector stores.

## Types of Retrievers

### 1. Wikipedia Retriever

- **Class**: `WikipediaRetriever`
- **Usage**: Directly queries Wikipedia for relevant articles based on the user's prompt. Especially useful for general knowledge grounding.

### 2. Vector Store Retriever

- **Usage**: `vectorstore.as_retriever(search_kwargs={"k": 2})`
- **Function**: The most common way to use a vector store in a RAG pipeline.

### 3. MMR (Maximal Marginal Relevance)

- **Usage**: `vectorstore.as_retriever(search_type="mmr")`
- **Function**: Balances **relevance** to the query with **diversity** among the results. It prevents getting multiple documents that say the exact same thing.

### 4. MultiQuery Retriever

- **Class**: `MultiQueryRetriever`
- **Function**: Uses an LLM to rephrase the user's query into multiple versions. It then retrieves documents for all versions and takes the union. This helps overcome limitations in vector search where a single query might miss relevant info due to phrasing.

### 5. Contextual Compression

- **Class**: `ContextualCompressionRetriever`
- **Function**: Uses a "compressor" (usually an LLM) to post-process retrieved documents. It extracts only the snippets that are actually relevant to the query, reducing noise and saving tokens.
