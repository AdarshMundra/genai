from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()


prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the joke {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)


parallel_chain = RunnableParallel({"joke": RunnablePassthrough(),
 "explanation": RunnableSequence(prompt2, model, parser)})


final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({"topic": "dogs"}))

final_chain.get_graph().print_ascii()
