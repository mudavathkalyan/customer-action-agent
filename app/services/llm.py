import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from app.models.ticket import TicketData

load_dotenv()

llm = ChatOpenAI(
    model="model1",
    base_url="http://localhost:4000/v1",
    api_key=os.getenv("LITELLM_MASTER_KEY"),
    temperature=0,
)

structured_llm = llm.with_structured_output(TicketData)