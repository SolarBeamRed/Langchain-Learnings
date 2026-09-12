import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-1.5B-Instruct:featherless-ai',
    task='text-generation'
) # type: ignore 

model = ChatHuggingFace(llm=llm)
result = model.invoke('Just a test prompt. Reply with a single random word')

print(result.content)