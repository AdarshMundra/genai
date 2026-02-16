from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

st.header("Summarize any document")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = """
Summarize the following research paper in a {length} explanation.

Research Paper: {paper}

Explanation Style: {style}

Summary:
"""

prompt = PromptTemplate(template=template, input_variables=["paper", "style", "length"])


if st.button("Summarize"):
    # st.write(user_input)
    result = model.invoke(prompt.format(paper=paper_input, style=style_input, length=length_input))
    st.write(result.content)


