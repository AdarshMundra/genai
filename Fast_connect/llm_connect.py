from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

app = FastAPI(title="LangChain Summary API")

# Initialize model
model = ChatOpenAI()

# Prompt 1: Detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Prompt 2: Summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text.\n{text}",
    input_variables=["text"]
)

# Output parser
parser = StrOutputParser()

# Chain
chain = template1 | model | parser | template2 | model | parser


# Request schema
class TopicRequest(BaseModel):
    topic: str


# Response schema
class SummaryResponse(BaseModel):
    summary: str


@app.post("/generate-summary", response_model=SummaryResponse)
async def generate_summary(request: TopicRequest):
    try:
        result = chain.invoke({"topic": request.topic})
        return SummaryResponse(summary=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "LangChain FastAPI is running"}



