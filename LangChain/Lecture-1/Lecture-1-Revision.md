# Lecture 1 Revision

## 1. LLMs

### `1_llm_demo.py`
- **Description**: Demonstrates how to instantiate and use a basic non-chat LLM using `LangChain`.
- **Key Classes**: `OpenAI` from `langchain_openai`.
- **Functionality**: Loads environment variables, initializes the model (`gpt-3.5-turbo-instruct`), and invokes it with a simple question.

## 2. Chat Models

### `1_chatmodel_openai.py`
- **Description**: Setup for OpenAI's Chat Model.
- **Key Classes**: `ChatOpenAI` from `langchain_openai`.
- **Functionality**: Uses `gpt-3.5-turbo` to answer a query.

### `2_chatmodel_anthropic.py`
- **Description**: Setup for Anthropic's Claude Model.
- **Key Classes**: `ChatAnthropic` from `langchain_anthropic`.
- **Functionality**: Uses `claude-3-haiku-20240307` to answer a query.

### `3_chatmodel_google.py`
- **Description**: Setup for Google's Gemini Model.
- **Key Classes**: `ChatGoogleGenerativeAI` from `langchain_google_genai`.
- **Functionality**: Uses `gemini-2.0-flash-exp` to answer a query.

### `4_chatmodel_hf_api.py`
- **Description**: Using Hugging Face Inference API.
- **Key Classes**: `HuggingFaceEndpoint`, `ChatHuggingFace` from `langchain_huggingface`.
- **Functionality**: Connects to a remote model (`TinyLlama`) via API key.

### `5_chatmodel_hf_local.py`
- **Description**: Running Hugging Face models locally.
- **Key Classes**: `HuggingFacePipeline`, `ChatHuggingFace` from `langchain_huggingface`.
- **Functionality**: Downloads and runs a model locally using a pipeline. Sets a custom cache directory (`HF_HOME`).

## 3. Embedding Models

### `1_embedding_openai_query.py`
- **Description**: Generating embeddings for a single query string.
- **Key Classes**: `OpenAIEmbeddings` from `langchain_openai`.
- **Functionality**: Uses `text-embedding-3-large` to embed a simple text query.

### `2_embedding_openai_docs.py`
- **Description**: Generating embeddings for a list of documents.
- **Key Classes**: `OpenAIEmbeddings`.
- **Functionality**: Embeds a list of strings (documents) into vectors.

### `3_embedding_hf_local.py`
- **Description**: Using local Hugging Face embeddings.
- **Key Classes**: `HuggingFaceEmbeddings` from `langchain_huggingface`.
- **Functionality**: Uses `sentence-transformers/all-MiniLM-L6-v2` to embed documents locally.

### `4_document_similarity.py`
- **Description**: implementing semantic search/similarity.
- **Key Classes**: `OpenAIEmbeddings`, `cosine_similarity` from `sklearn`.
- **Functionality**: 
    1. Embeds a list of documents about cricketers.
    2. Embeds a user query ("tell me about bumrah").
    3. Calculates cosine similarity between the query and documents.
    4. Returns the most similar document.
