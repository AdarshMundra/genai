from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatOpenAI()


prompt = PromptTemplate(
    template = "Genrate 5 intersting facts about {topic}\n",
    input_variables=["topic"]
)

output_parser = StrOutputParser()

chain = prompt | model | output_parser

result = chain.invoke({"topic": "Cricket"})

print(result)

chain.get_graph().print_ascii()
