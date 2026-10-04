from langchain_openai import ChatOpenAI, OpenAIEmbeddings

llm = ChatOpenAI(
    model='local qwen 3.5',
    base_url='http://127.0.0.1:8080/v1',
    api_key='not needed'
)

embedder = OpenAIEmbeddings(
    model='local qwen3 embedding',
    base_url='http://127.0.0.1:8081/v1',
    api_key='not needed'
)