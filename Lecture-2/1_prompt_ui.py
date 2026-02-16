from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo")
    
st.header("Summarize any document")

user_input = st.text_input("Enter your document")

if st.button("Summarize"):
    st.write(user_input)
    result=model.invoke(user_input)
    st.write(result.content)


