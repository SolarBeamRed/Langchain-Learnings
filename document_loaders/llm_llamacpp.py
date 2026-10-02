from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model='local qwen 3.4',
    base_url='http://127.0.0.1:8080/v1',
    api_key='not_needed' # type: ignore
)

# print(llm.invoke('Hi').content)