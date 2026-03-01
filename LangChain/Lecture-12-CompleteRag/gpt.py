import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

# Load environment variables
load_dotenv()

# Initialize components
model = ChatOpenAI()
embeddings = OpenAIEmbeddings()
parser = StrOutputParser()
youtube_transcript = YouTubeTranscriptApi()

st.title("📺 YouTube Video Knowledge Base")

# -----------------------------
# SECTION 1: FETCH TRANSCRIPT
# -----------------------------

video_id = st.text_input("Enter YouTube Video ID")

if st.button("Get Transcript"):

    if not video_id:
        st.warning("Please enter a video ID.")
    else:
        try:
            transcript_list = youtube_transcript.fetch(
                video_id,
                languages=["en", "hi"]
            )

            transcript = " ".join(chunk.text for chunk in transcript_list)
            st.success("Transcript fetched successfully!")

            # Split transcript
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.create_documents([transcript])

            # Create vector store
            vectorstore = FAISS.from_documents(chunks, embeddings)

            # Store retriever in session state
            st.session_state.retriever = vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 4}
            )

            st.success("Transcript processed and stored!")

        except TranscriptsDisabled:
            st.error("Transcripts are disabled for this video.")
        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------------
# SECTION 2: ASK QUESTIONS
# -----------------------------

st.header("Ask a Question")
question = st.text_input("Enter your question")

if st.button("Ask"):

    if "retriever" not in st.session_state:
        st.warning("Please fetch the transcript first.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        try:

            prompt = PromptTemplate(
                template="""
                You are a helpful assistant.
                Answer ONLY using the provided transcript context.
                If the answer is not in the context, say "I don't know."

                Context:
                {context}

                Question:
                {question}
                """,
                input_variables=["context", "question"]
            )

            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            # Build chain
            parallel_chain = RunnableParallel({
                "context": st.session_state.retriever | RunnableLambda(format_docs),
                "question": RunnablePassthrough()
            })

            main_chain = parallel_chain | prompt | model | parser

            result = main_chain.invoke(question)

            st.write("### Answer:")
            st.write(result)

        except Exception as e:
            st.error(f"Error: {e}")