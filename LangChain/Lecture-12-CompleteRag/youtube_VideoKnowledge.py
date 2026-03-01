import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled



load_dotenv()
parser = StrOutputParser()
model = ChatOpenAI()
youtube_transcript = YouTubeTranscriptApi()
embeddings = OpenAIEmbeddings()

st.header("Youtube Video Knowledge Base")

id = st.text_input("Enter Youtube Video ID")

if st.button("Get Transcript"):
    try:
        transcript_list = youtube_transcript.fetch(id,languages=['en','hi'])
        transcript = " ".join(chunk.text for chunk in transcript_list)
        st.write("Transcript Done")
    except TranscriptsDisabled:
        st.write("Transcripts are disabled for this video")
    except Exception as e:
        st.write(e)
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])
    vectorstore = FAISS.from_documents(chunks, embeddings)
    st.session_state.retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    
    st.write("Transcript fetched and stored successfully")
st.header("Ask a Question")
question = st.text_input("Enter your question")
if st.button("Ask"):
    try:
        prompt = PromptTemplate(
            template="""
            You are a helpful assistant.
            Answer ONLY from the provided transcript context.
            If the context is insufficient, just say you don't know.

            {context}
            Question: {question}
            """,
            input_variables = ['context', 'question']
        )
        print(prompt)
        def format_docs(retrieved_docs):
            context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
            return context_text
        if "retriever" not in st.session_state:
            st.write("Please fetch transcript first.")                
            # st.warning("Please fetch transcript first.")
        else:
            # retriever = st.session_state.retriever
            parallel_chain = RunnableParallel({
            'context': st.session_state.retriever | RunnableLambda(format_docs),
            'question': RunnablePassthrough()
            })
            main_chain = parallel_chain | prompt | model | parser

            result = main_chain.invoke(question)

            st.write("### Answer:")
            st.write(result)
    except Exception as e:
        st.write(e)
# else:
    #     st.write("Ask a question")

