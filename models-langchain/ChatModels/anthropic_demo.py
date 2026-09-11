from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

anthropic = ChatAnthropic(model='claude-haiku-4-5-20251001')  # type: ignore
result = anthropic.invoke('Reply with Hello')

print(result.content)