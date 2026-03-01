from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('cricket.pdf')

docs = loader.load()

print(docs)

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)


docc1 = loader.lazy_load()

print(docc1)