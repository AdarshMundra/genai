import os
import shutil
from dotenv import load_dotenv

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

# =========================
# CONFIG
# =========================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found")

UPLOAD_DIR = "uploads"
VECTOR_DB = "vectorstore"

os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="FastAPI RAG")

# =========================
# OPENAI EMBEDDINGS
# =========================

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# =========================
# REQUEST MODEL
# =========================

class QueryRequest(BaseModel):
    question: str

# =========================
# DOCUMENT INGESTION
# =========================

def ingest_pdf(pdf_path: str):

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(VECTOR_DB)

    return len(chunks)

# =========================
# LOAD VECTOR STORE
# =========================

def load_vectorstore():

    if not os.path.exists(VECTOR_DB):
        raise HTTPException(
            status_code=404,
            detail="Upload a document first"
        )

    return FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )

# =========================
# RAG CHAIN
# =========================

def get_rag_chain():

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using only the provided context.

        Context:
        {context}

        Question:
        {input}

        If the answer is not found in the context,
        say "I could not find that information in the document."
        """
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    rag_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return rag_chain

# =========================
# API
# =========================

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files supported"
        )

    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = ingest_pdf(filepath)

    return {
        "message": "Document indexed successfully",
        "chunks": chunks
    }

@app.post("/query")
async def query_document(request: QueryRequest):

    chain = get_rag_chain()

    result = chain.invoke({
        "input": request.question
    })

    return {
        "question": request.question,
        "answer": result["answer"]
    }

# =========================
# LOCAL RUN
# =========================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )