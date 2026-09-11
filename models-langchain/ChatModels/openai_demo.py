from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatOpenAI(model='gpt-5.6-luna')
result = chatmodel.invoke('Reply with hello')

print(result.content)