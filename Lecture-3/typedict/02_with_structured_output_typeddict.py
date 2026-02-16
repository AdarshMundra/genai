from typing import TypedDict, Annotated, Optional, Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI





load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    summary: str
    sentiment: Literal['positive', 'negative', 'neutral']


structured_model = model.with_structured_output(Review)

review = structured_model.invoke("""The hardware is great but the software fell bad the os is not responsive and updated and comes with lots of pre installed apps which i don't need and cant remove""")

print(review)
