from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(model='gpt-5.6-luna')
result = openai.invoke('Reply with hello')

print(result)