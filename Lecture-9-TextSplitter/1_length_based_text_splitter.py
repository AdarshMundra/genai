from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data.pdf")

docs = loader.load()

# print(docs)

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

text_splitter = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=10)


result = text_splitter.split_documents(docs)

print(result[1].page_content)
