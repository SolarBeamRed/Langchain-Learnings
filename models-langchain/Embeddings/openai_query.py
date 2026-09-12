from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=256)
result = embedding.embed_query('Counter Strike tournaments are fun to watch')

print(str(result))