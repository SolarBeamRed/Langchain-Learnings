from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
result = gemini.invoke('Reply with Hello')

print(result.content)