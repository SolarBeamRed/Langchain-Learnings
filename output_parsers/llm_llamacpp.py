from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm_model = ChatOpenAI(
    model='local qwen',
    base_url='http://127.0.0.1:8080/v1',
    max_completion_tokens=2800
)