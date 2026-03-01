# Lecture 8 Revision

## Overview

This lecture covers **Document Loaders**, which are used to bring data from various sources (text files, PDFs, websites, etc.) into the LangChain ecosystem as standard `Document` objects.

## Key Loaders

### 1. `TextLoader`

- **File**: `1_TextLoader.py`
- **Usage**: `loader = TextLoader('file.txt', encoding='utf-8')`
- **Function**: Loads content from a plain text file. Each file results in one `Document` object with `page_content` and `metadata`.

### 2. `PyPDFLoader`

- **File**: `2_PDF_LOADER.py`
- **Usage**: `loader = PyPDFLoader('file.pdf')`
- **Function**: Extracts text from PDF files. It often creates one `Document` per page of the PDF. Supports both `.load()` and `.lazy_load()`.

### 3. `DirectoryLoader`

- **File**: `3_Directory_loader.py`
- **Usage**: `loader = DirectoryLoader('path', glob='*.txt')`
- **Function**: Scans a directory and loads all files matching a specific pattern.

### 4. `WebBaseLoader`

- **File**: `4_WEB_BASED_loader.py`
- **Usage**: `loader = WebBaseLoader('https://example.com')`
- **Function**: Scrapes content from a URL and converts it into a `Document`.

### 5. `CSVLoader`

- **File**: `5_CSV_LOADER.py`
- **Usage**: `loader = CSVLoader('file.csv')`
- **Function**: Loads data from CSV files, creating one `Document` per row.
