from dotenv import load_dotenv

from langchain_openai import ChatOpenAI


load_dotenv()

llm_model = ChatOpenAI(
    model='qwen_model',
    base_url='http://127.0.0.1:8080/v1',
    max_completion_tokens=3000
)  


# print(llm_model.invoke('Hi').content)
