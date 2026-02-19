from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableSequence, RunnableParallel

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()


def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Explain the joke {topic}',
    input_variables=['topic']
)



joke_gen_chain = RunnableSequence(prompt1, model, parser)


parallel_chain = RunnableParallel({"joke": RunnablePassthrough(),
 "word_count": RunnableLambda(word_count),
 "explanation": RunnableSequence(prompt2, model, parser)})


final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)


final_chain.get_graph().print_ascii()

final_chain.get_graph().print_ascii()
