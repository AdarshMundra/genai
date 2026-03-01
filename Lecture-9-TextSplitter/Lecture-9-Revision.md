# Lecture 9 Revision

## Overview

This lecture covers **Text Splitters**, which are essential for breaking down large documents into smaller "chunks" that fit within the context window of LLMs and are suitable for vector search.

## Key Splitters

### 1. `CharacterTextSplitter`

- **File**: `1_length_based_text_splitter.py`
- **Function**: Splits based on a single character (default is whitespace) into fixed-size chunks. Use `chunk_size` and `chunk_overlap`.

### 2. `RecursiveCharacterTextSplitter`

- **File**: `2_Text_Structure_Based.py`
- **Function**: The recommended general-purpose splitter. It tries to split on a list of characters (newline, space, etc.) recursively to keep related text together while staying within the `chunk_size`.

### 3. Language-Specific Splitting

- **Files**: `3_Document_structurebased.py` (Python), `4_markDown_splitter.py` (Markdown)
- **Function**: Specialized versions of `RecursiveCharacterTextSplitter` that understand the syntax of specific languages (like Python function definitions or Markdown headers) to ensure logical splits.

### 4. `SemanticChunker`

- **File**: `5_Semantic_meaning.py`
- **Function**: Splits text based on **semantic similarity** rather than character count. It uses embeddings to find points where the topic changes and inserts a break there. It requires an embedding model (e.g., `OpenAIEmbeddings`).
