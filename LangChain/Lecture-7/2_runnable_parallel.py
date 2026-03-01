from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()


prompt1 = PromptTemplate.from_template("What is the capital of {country}")
prompt2 = PromptTemplate.from_template("What is the currency of {country}")

parallel_chain = RunnableParallel({"capital": RunnableSequence(prompt1, model, parser), "currency": RunnableSequence(prompt2, model, parser)})

print(parallel_chain.invoke({"country": "France"}))

parallel_chain.get_graph().print_ascii()