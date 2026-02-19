from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader('data', glob='*.txt')

docs = loader.load()

print(docs)

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)