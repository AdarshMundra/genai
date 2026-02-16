from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.3,max_tokens=10)

result = llm.invoke("What is the capital of India")


print(result.content)